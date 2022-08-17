from ast import Str
from dis import disco
from fileinput import close
from typing import get_args
import discord
import json
#cmd imports 
from pkg import command 
from pkg import ping 

CONFIG_PATH = "config.json"
BOT_PREFIX = "~"

class Client(discord.Client):
    def __init__(self, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        self.cmd = command.Commands()
        self.cmd.add_cmd("ping", ping.ping)
    
    async def on_ready(self):
        print("Logado como: {0}".format(self.user))
    
    async def on_message(self, message):
        if (not(message.author.bot) and message.author.id != self.user.id) and (message.content[0] == BOT_PREFIX):         
            print("Mensagem enviada: {0.author}: {0.content}".format(message))
            args = self.get_args(message.content.replace(BOT_PREFIX, ""))
            await self.cmd.call_cmd(args[0], self, message=message, args=args)
    
    def get_args(self, message_str : str):
        args = message_str.split(" ")
        return args 



def load_config():
    stream = open(CONFIG_PATH)
    data = json.load(stream)
    stream.close()
    return data

config_dict = load_config()

client = Client()
client.run(config_dict["token"])