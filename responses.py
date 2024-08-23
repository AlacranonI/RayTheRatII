from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Speak, and speak well, mortal.'
    elif 'die' in lowered:
        return 'If only I could mortal.\n\n\nJust kidding, immortality is rad.'
    else:
        return 'Apologies mortal. I am still getting accustomed to this vessel. I cannot respond appropriately at the moment.'