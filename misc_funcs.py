def video_confirmation():
    user_input = ''
    while user_input not in ('v', 'V', 'a', 'A'):
        user_input = input("Enter (V)ideo , (A)udio :")
    if user_input not in ('y', 'Y', 'Yes', 'YES', 'yes', 'YeS', 'yEs', 'YEs', 'yES', 'yeS'):
        return True
    else:
        return False