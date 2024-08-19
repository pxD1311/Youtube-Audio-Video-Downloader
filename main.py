from terminal_funcs import display_options, insert_link

links = []

while True:
    display_options()
    user_input = int(input("Enter your choice :"));
    match user_input:
        case 1:
            insert_link(links)
        case _:
            print(f"Invalid Input : {user_input}, Please try again.");