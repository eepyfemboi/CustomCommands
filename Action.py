from typing import *

import discord
from discord.ext import commands

from CustomCommands.formatter import formatter

class Action:
    def __init__(self):
        ...

class SendMessageToChannel(Action):
    def __init__(self, channel_id: int, message: str, vars: Dict[str, str]):
        pass
