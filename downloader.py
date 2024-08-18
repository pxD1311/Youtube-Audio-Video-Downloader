import os
from pytube import YouTube
from rich.progress import track

class DowloadYT:
    def __init__(self, path : str = "", folder_name : str = "Downloads") -> None:
        if os.path.exists(path):
            if os.getcwd() != path:
                os.chdir(path)
                self.path = os.path.join(path,folder_name)
        else:
            print(f"Invalid Path : Therefore using {os.getcwd()}")
            self.path = os.path.join(os.getcwd(),folder_name)

        self.audio_path = os.path.join(self.path, "audio")
        self.video_path = os.path.join(self.path, "video")

        os.makedirs(self.audio_path, exist_ok=True)
        os.makedirs(self.video_path, exist_ok=True)

        self.__print_single = True

    def __clean_print__(method):
        def wrapper(self, *args, **kwargs):
            if self.__print_single:
                print("Starting Download.")
                method(self, *args, **kwargs)
                print("Downloaded Successfully")
            else:
                method(self, *args, **kwargs)
        return wrapper

    @__clean_print__
    def __download__(self, object, path) -> None:
        try:
            object.download(path)
        except Exception as e:
            print("An error has occurred:\n", e)

    def __check_files__(self, object_name: str, object_type : str):
        if object_type == "audio":
            file_names = [file_path for file_path in os.listdir(self.audio_path)]
        elif object_type == "video":
            file_names = [file_path for file_path in os.listdir(self.video_path)]
        else:
            raise ValueError("Invaid type of object : object_type must be either audio or video")
        return object_name in file_names

    def download_video(self, link : str, resolution:str = None) -> None:
        youtubeObject = YouTube(link)
        video_title = youtubeObject.streams[0].default_filename
        if self.__check_files__(video_title, "video"):
            print("Requirement already satisfied : Video file already exists in the path provided.")
        else:
            print(f"Downloading requested video : {video_title}")
            if resolution:
                video = youtubeObject.streams.filter(res=resolution).first()
            else :
                video = youtubeObject.streams.get_highest_resolution()
            self.__download__(video, self.video_path)

    def download_videos(self, links : tuple, resolution : str = None)-> None:
        self.__print_single = False
        print("\nDownloading Requested Videos :")
        for link in track(links, description= "Progress :"):
            self.download_video(link, resolution)
        self.__print_single = True

    def download_audio(self, link : str, audio_quality: str = None)-> None:
        youtubeObject = YouTube(link)
        audio_title = youtubeObject.streams.filter(only_audio=True).first().default_filename
        if self.__check_files__(audio_title, "audio"):
            print("Requirement already satisfied : Audio file already exists in the path provided.")
        else:
            print(f"Downloading requested audio : {audio_title}")
            audio = youtubeObject.streams.filter(only_audio=True).first()
            if audio_quality:
                audio = youtubeObject.streams.filter(only_audio=True, abr=audio_quality).first()
            else:
                audio = youtubeObject.streams.filter(only_audio=True).first()
            self.__download__(audio, self.audio_path)

    def download_audios(self, links : tuple, audio_quality : str = None)-> None:
        self.__print_single = False
        print("\nDownloading Requested Audios :")
        for link in track(links, description= "Progress :"):
            self.download_audio(link, audio_quality)
        self.__print_single = True




