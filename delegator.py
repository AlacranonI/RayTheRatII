from discord import Message
from choice_types.features import Features
from choice_types.people import People

def choose_feature(user_choice: str) -> Features:
    if user_choice == 'q':
        return Features.QUOTER
    elif user_choice == 'i':
        return Features.IMAGER
    elif user_choice == 'r':
        return Features.RESPONDER
    else:
        return Features.INVALID
    
# def choose_quote_type(user_choice: str) -> QuoteChoice:
#     if user_choice == 'q':
#         return Features.QUOTER
#     elif user_choice == 'i':
#         return Features.IMAGER
#     elif user_choice == 'r':
#         return Features.RESPONDER
#     else:
#         return Features.INVALID