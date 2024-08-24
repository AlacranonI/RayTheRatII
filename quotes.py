from choice_types.people import People
from discord import Intents, Client, Message

def get_quote(client: Client, user_in: str) -> str:
    user_in_split = user_in.split(' ')

    quote_filter = user_in_split[0].lower()
    
    if quote_filter in People.__members__.values():
        return fetch_selected_quote(client, quote_filter)
    else:
        return 'You selected an invalid option!'
    
def fetch_selected_quote(client: Client, filter: str) -> str:

    raise NotImplementedError('This function is not yet implemented!')

