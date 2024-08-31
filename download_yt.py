from pytube import YouTube
from config import DEVELOPER_MODE

class DownloadYT:
    def __init__(self, v_path : str, a_path : str) -> None:
        self.audio_path = a_path
        self.video_path = v_path

    def __download(self, object, is_audio = False) -> bool|None:
        """
            downloads the audio/video from youtube 
            returns True for successful downloading, False for failure and None if file is already present
        """
        try:
            file_name = object.streams[0].default_filename
            if is_audio:
                object.download(self.video_path)
            elif not is_audio:
                object.download(self.audio_path)
            else:
                if DEVELOPER_MODE:
                    print(f"File {file_name} already present")
                return None
            return True
        except Exception as e:
            if DEVELOPER_MODE == True:
                print(f"Error : {e}")
            return False

    def download_video(self, link : str, resolution : str) ->bool|None:
        """
            uses internal __download method to download a given yt video
        """
        yt_obj = YouTube(link)
        if resolution:
            video = yt_obj.streams.filter(res=resolution).first()
        else :
            video = yt_obj.streams.get_highest_resolution()
        return self.__download(video)

    def download_audio(self, link : str, audio_quality : str) ->bool|None:
        """
        uses internal __download method to download a given yt video
        """
        yt_obj = YouTube(link)
        if audio_quality:
            audio = yt_obj.streams.filter(only_audio=True, abr=audio_quality).first()
        else:
            audio = yt_obj.streams.filter(only_audio=True).first()
        return self.__download(audio, True)
