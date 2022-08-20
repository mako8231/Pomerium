from ast import Str
from dis import disco
from fileinput import close
from typing import get_args
import discord
import json
#cmd imports 
from pkg import command 
from pkg import ping
from pkg.player import * 
from pkg.admin_cmd import * 
import os
import pkg.save as save 

CONFIG_PATH = "config.json"
BOT_PREFIX = "~"

class Client(discord.Client):
    def __init__(self, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        self.cmd = command.Commands()
        self.players = {}
        #stats 

        self.cmd.add_cmd("ping", ping.ping)
        self.cmd.add_cmd("player", player)
        self.cmd.add_cmd("mudar_hp", mudar_hp)
        self.cmd.add_cmd("por_item", por_item)
        self.cmd.add_cmd("status", status)
        self.cmd.add_cmd("mudar_em", mudar_em)
        self.cmd.add_cmd("echo", echo)
        self.cmd.add_cmd("add_equip", add_equip)
        self.cmd.add_cmd("level_up", level_up)
        self.cmd.add_cmd("distribuir", distribuir)

    def load_players(self):
        for id in os.listdir("./player/"):
            pl = save.load_player(id)
            self.players[pl.id_discord] = pl
            
        print(self.players) 
    
    async def on_ready(self):
        print("Logado como: {0}".format(self.user))
    
    async def on_message(self, message):
        if (not(message.author.bot) and message.author.id != self.user.id) and (message.content[0] == BOT_PREFIX):         
            print("Mensagem enviada: {0.author}: {0.content}".format(message))
            args = self.get_args(message.content.replace(BOT_PREFIX, ""))
            await self.cmd.call_cmd(args[0], self, message=message, args=args, players=self.players)
    
    def get_args(self, message_str : str):
        args = message_str.split(" ")
        return args 



players = {}


def load_config():
    stream = open(CONFIG_PATH)
    data = json.load(stream)
    stream.close()
    return data

config_dict = load_config()

client = Client()
client.load_players()
const.ADMINS = config_dict["admins"]
client.run(config_dict["token"])