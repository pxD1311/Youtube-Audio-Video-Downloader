from config import VERSION

class TerminalApp:
    def __init__(self) -> None:
        self.version = VERSION
        self.link = ""
        self.links = []

    def run(self):
        self.__display_init_info()
        self.__mainloop()
        self.__display_exit_info()

    def __mainloop(self) -> None:
        while True:
            self.__display_options()
            match (input(">>>")):
                case '1':
                    match (input("Options:\naudio - a or A\nvideo - v or V\n>>>")):
                        case 'a'|'A':
                            self.__download_audio()
                        case 'v'|'V':
                            self.__download_video()
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
                    break
                case '_':
                    print("Invalid Input : please try again.")

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

    def __download_audio(self,):
        pass

    def __download_video(self,):
        pass

    def __change_download_directory(self, path):
        pass