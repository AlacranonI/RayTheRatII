from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from types import FunctionType
from responses import get_response
from quotes import get_quote
from images import get_image
from delegator import choose_feature

# Loading our token
load_dotenv(dotenv_path='.env.client')
TOKEN: Final[str] = os.getenv('DISCORD_BOT_TOKEN')

load_dotenv(dotenv_path='.env.guild')
ADMIN_IDS: Final[list[int]] = os.getenv('ADMIN_IDS').split(',')
TESTER_IDS: Final[list[int]] = os.getenv('TESTER_IDS').split(',')

QUOTES_CHANNEL_ID: Final[int] = int(os.getenv('QUOTES_CHANNEL_ID'))
IMAGES_CHANNEL_ID: Final[int] = int(os.getenv('IMAGES_CHANNEL_ID'))

# Instantiating the bot
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# Preparing message functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents weren\'t enabled probably lol)')
        return

#    if is_private := user_message[0] == 'r':
#        user_message = user_message[1:]

    choice: FunctionType = choose_feature(user_message[1:])

    functions = {
        FunctionType.INVALID: 'I may be omnipotent, but you some how found a way to confuse me. Define your function CLEARLY next time, mortal.',
        FunctionType.QUOTER: get_quote(user_message),
        FunctionType.IMAGER: get_image(user_message),
        FunctionType.RESPONDER: get_response(user_message)
    }

    response: str = functions[choice]

    try:
        await message.channel.send(response)
    except Exception as e:
        print(e)

# Starting the bot up
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# Listening for messages
@client.event
async def on_message(message: Message) -> None:
    if(message.author == client.user or
       message.author.id != 1223150746728530002 or
       message.channel.id != 1276621797541806136):
        print('Response conditions not met. Ignoring...')
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

def main() -> None: 
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()