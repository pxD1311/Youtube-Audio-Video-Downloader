from downloader import DowloadYT

class TerminalApp:
    def __init__(self) -> None:
        downloader = DowloadYT()
        self.link_list = []

    def display_options(self):
        print("Welcome to Youtube audio/video downloader!")
        print("What would you like to do?")
        print("(1) Enter a link inside the list.")
        print("(2) Download all audios/videos in the list.")
        print("(3) Enter a link and download a single audio/video.")
        print("(4) Change download path.")
        print("(5) Exit.")

    def insert_link(self, link_list : list):
        link_list.append(input("Enter link :"))
        return link_list

    def download_all_links(self, audio = False):
        if self.link_list != []:
            if (not audio):
                self.downloader.download_videos(self.link_list)
            else:
                self.downloader.download_audios(self.link_list)

    @staticmethod
    def download_link(self, link,  audio = False):
        if (not audio):
            self.downloader.download_video(link)
        else:
            self.downloader.download_audio(link )
