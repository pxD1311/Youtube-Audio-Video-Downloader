from terminal_app import TerminalApp
from misc_funcs import video_confirmation

links = []

tapp = TerminalApp();

while True:
    tapp.display_options()
    user_input = int(input("Enter your choice :"));
    match user_input:
        case 1:#insert links into the list
            tapp.insert_link(links)
        case 2:#download all links in list
            tapp.download_all_links(video_confirmation())
        case 3:#download a single video
            link = input("Enter link :")
            tapp.download(link, video_confirmation())
        case 4:
            pass
        case 5:
            print("Thanks for using the application.")
            quit()
        case _:#default case
            print(f"Invalid Input : {user_input}, Please try again.");