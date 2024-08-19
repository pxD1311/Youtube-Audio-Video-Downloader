from downloader import DowloadYT

def display_options():
    print("Welcome to Youtube audio/video downloader!")
    print("What would you like to do?")
    print("(1) Enter a link inside the list.")
    print("(2) Download all audios/videos in the list.")
    print("(3) Enter a link and download a single audio/video.")
    print("(4) Change download path.")
    print("(5) Exit.")

def insert_link(link_list : list):
    link_list.append(input("Enter link :"))
    return link_list
