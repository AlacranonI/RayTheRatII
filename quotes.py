from choice_types.people import People

def get_quote(user_selection: str) -> int:
    if user_selection == People.RANDOM:
        
        return 
    elif user_selection == 'i':
        return 'You selected the image grabber!'
    elif user_selection == 'r':
        return 'You selected the response generator!'
    else:
        return 'You selected an invalid option!'