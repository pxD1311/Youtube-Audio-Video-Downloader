from terminal_app import TerminalApp

links = []

tapp = TerminalApp();

while True:
    tapp.display_options()
    user_input = int(input("Enter your choice :"));
    match user_input:
        case 1:
            tapp.insert_link(links)
        case 2:
            video_confirmation = input("Enter (V)ideo , (A)udio :")
            if video_confirmation not in ['y', 'Y', 'Yes', 'YES', 'yes', 'YeS', 'yEs', 'YEs', 'yES', 'yeS']:
                video_confirmation = True
            else:
                video_confirmation = False
            tapp.download_all_links(video_confirmation)
        case 3:
            video_confirmation = input("Enter (V)ideo , (A)udio :")
            if video_confirmation not in ['y', 'Y', 'Yes', 'YES', 'yes', 'YeS', 'yEs', 'YEs', 'yES', 'yeS']:
                video_confirmation = True
            else:
                video_confirmation = False
            link = input("Enter link :")
            tapp.download(link, video_confirmation)
        case _:
            print(f"Invalid Input : {user_input}, Please try again.");