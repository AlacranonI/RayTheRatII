import json
from typing import List, Dict
from discord import Client, Message

async def fetch_and_save_messages(client: Client, channel_id: int, limit: int) -> None:
    channel = client.get_channel(channel_id)
    messages = await channel.history(limit=limit).flatten()

def read_saved_messages() -> None:
    raise NotImplementedError('This function is not yet implemented!')