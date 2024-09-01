from download_yt import DownloadYT
from input_validation import validate_youtube_url
from config import VERSION, DEFAULT_AUDIO_PATH, DEFAULT_VIDEO_PATH

class TerminalApp:
    def __init__(self) -> None:
        self.version = VERSION
        self.link = ""
        self.links = []
        self.downloader = DownloadYT(DEFAULT_VIDEO_PATH, DEFAULT_AUDIO_PATH)

    def run(self):
        self.__display_init_info()
        self.__mainloop()
        self.__display_exit_info()

    def __mainloop(self) -> None:
        run_again = True
        while run_again:
            self.__display_options()
            run_again = self.__process()

    def __process(self) -> bool:
        match (input(">>>")):
            case '1':
                match (input("Options:\naudio - a or A\nvideo - v or V\n>>>")):
                    case 'a'|'A':
                        self.__input_link()
                        if self.downloader.download_audio(self.link):
                            print("Audio has been downloaded successfully.")
                        else:
                            print("Failed to download audio.")
                    case 'v'|'V':
                        self.__input_link()
                        if self.downloader.download_video(self.link):
                            print("Video has been downloaded successfully.")
                        else:
                            print("Failed to download video.")
                    case '_':
                        print("Invalid Input : please try again.")

            case '2':
                match (input("Options:\n(a) or (A)- audio\n(v) or (V) - video\n>>>")):
                    case 'a'|'A':
                        pass
                    case 'v'|'V':
                        pass
                    case '_':
                        print("Invalid Input : please try again.")

            case '3':
                new_dir_path = input("Enter the path you want to use to download files :")
                self.__change_download_directory(new_dir_path)
            case '4':
                return False
            case '_':
                print("Invalid Input : please try again.")
        return True

    def __display_init_info(self) -> None:
        print( "*********************************")
        print(f"Yt-video-audio-Downloader V-{self.version}")
        print( "*********************************")

    def __display_exit_info(self) -> None:
        print( "*********************************")
        print( "   Thanks for using the app.")
        print(f"         Version - {self.version}")
        print( "*********************************")

    def __display_options(self) -> None:
        print("(1) - Download single file.")
        print("(2) - Download multiple files.")
        print("(3) - Change Download directory.")
        print("(4) - Exit.")

    def __input_link(self):
        while True:
            link = input("Enter link\n>>>")
            if validate_youtube_url(link):
                self.link = link
                break;    
            print("ERROR : Invalid LINK entered, try again.")

    def __change_download_directory(self, path):
        pass