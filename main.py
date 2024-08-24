from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from choice_types.features import Features
from responses import get_response
from quotes import get_quote
from images import get_image
from delegator import choose_feature

# Loading our environment variables
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_BOT_TOKEN')

# Reads the IDs of the elements from the respective files
def read_ids(file_path: str) -> list[int]:
    file_path = os.path.join(os.path.dirname(__file__), 'element_ids', file_path)
    with open(file_path, 'r') as f:
        return [int(line.strip().split('#')[0]) for line in f.readlines()]

# Reading the IDs of the admins and testers
ADMIN_IDS: Final[list[int]] = read_ids('admins.txt')
TESTER_IDS: Final[list[int]] = read_ids('testers.txt')

# Reading the IDs of relevant channels
QUOTES_CHANNEL_ID: Final[int] = read_ids('quotes_channel.txt')[0]
IMAGES_CHANNEL_ID: Final[int] = read_ids('images_channel.txt')[0]
CHAT_CHANNEL_ID: Final[int] = read_ids('chat_channel.txt')[0]
TEST_CHANNEL_ID: Final[int] = read_ids('test_channel.txt')[0]
                                  
# Instantiating the bot
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# Preparing message functionality
async def process_message(message: Message, user_message: str) -> None:
    # If the user's message is empty, we can't do anything
    if not user_message:
        print('(Message was empty because intents weren\'t enabled probably lol)')
        return

    user_message_split = user_message.split(' ')

    # Only the first character of the user's choice is relevant
    choice = user_message_split[0].lower()[1:]

    # Combines the rest of the user's message to continue processing
    user_message = ' '.join(user_message_split[1:])

    functions = {
        Features.INVALID: 'I may be omnipotent, but you some how found a way to confuse me. Look at my bio and define your function CLEARLY next time, mortal.',
        Features.QUOTER: get_quote(client, user_message),
        Features.IMAGER: get_image(client, user_message),
        Features.RESPONDER: get_response(client, user_message)
    }

    # Fail safe
    if choice not in functions.keys():
        choice = Features.INVALID

    response: str = functions[choice]

    try:
        # Sending response
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

    # If the message doesn't start with the command, we skip it
    if(not message.content.lower().startswith('!ray')):
        print('Skipped...')
        return

    # If the message is from the bot itself, a tester, or not in the test channel, we skip it
    if(message.author == client.user or
       message.author.id not in TESTER_IDS or
       message.channel.id != TEST_CHANNEL_ID or #TODO Change on production
       message.channel.id != CHAT_CHANNEL_ID):
        print('Skipped...')
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await process_message(message, user_message)

def main() -> None: 
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()