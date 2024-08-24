

def get_image(user_selection: str) -> str:
    raise NotImplementedError('This function is not yet implemented!')
    if user_selection == 'q':
        return 'You selected the quote grabber!'
    elif user_selection == 'i':
        return 'You selected the image grabber!'
    elif user_selection == 'r':
        return 'You selected the response generator!'
    else:
        return 'You selected an invalid option!'