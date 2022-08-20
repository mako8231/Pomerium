from ast import arg
import sys
import pkg.const as const
import pkg.char as char

from .save import save_player 
async def player(client, message, args, players):
    if len(args) < 13:
        await message.channel.send(const.SEM_ARGUMENTOS)
        await message.channel.send("`player inteligencia forca intimidacao carisma percep constituição destreza furtividade devocao id_discord id_stealth`")
        return 
    if not(str(message.author.id) in const.ADMINS):
        await message.channel.send("Sem permissões.")
        return 
    player = char.Jogador(str(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]), int(args[6]), int(args[7]), int(args[8]), int(args[9]), int(args[10]), str(args[11]), str(args[12]))
    save_player(player.toJSON(), args[11])
    stealth_channel = message.guild.get_channel(int(args[12]))
    str_char = "Personagem de <@"+args[11]+">"+"\n" 
    str_char += "```" + player.__str__() + "```\n"
    await stealth_channel.send(str_char)

#métodos para os próprios players alterarem 
async def mudar_hp(client, message, args, players):
    #mudar_hp valor 
    if len(args) < 2:
        await message.channel.send(const.SEM_ARGUMENTOS)
        await message.channel.send("`mudar_hp valor`")
        return 
        
    if str(message.author.id) in players:  
        player = players[str(message.author.id)]
        
        stealth_channel = message.guild.get_channel(int(player.id_stealth))
        await stealth_channel.send("<@"+str(message.author.id)+">"+player.mudar_hp(int(args[1])))
        
    else:
        await message.channel.send("Você não é um jogador.")
    pass

async def mudar_em(client, message, args, players):
    #mudar_hp valor 
    if len(args) < 2:
        await message.channel.send(const.SEM_ARGUMENTOS)
        await message.channel.send("`mudar_em valor`")
        return 
        
    if str(message.author.id) in players:  
        player = players[str(message.author.id)]
        
        stealth_channel = message.guild.get_channel(int(player.id_stealth))
        await stealth_channel.send("<@"+str(message.author.id)+">"+player.mudar_em(int(args[1])))
        
    else:
        await message.channel.send("Você não é um jogador.")
    pass

async def por_item(client, message, args, players):
    #por_item nome_item 
    if len(args) < 2:
        await message.channel.send(const.SEM_ARGUMENTOS)
        await message.channel.send("`por_item nome_do_item`")
        return 
    if str(message.author.id) in players:
        player = players[str(message.author.id)]
        player.adicionar_item(const.arg2text(args=args, start=1))
        stealth_channel = message.guild.get_channel(int(player.id_stealth))
        await stealth_channel.send("<@"+str(message.author.id)+">"+"Item adicionado com sucesso\n")
    else:
        await message.channel.send("Você não é um jogador.")

async def status(client, message, args, players):
    if str(message.author.id) in players:
        player = players[str(message.author.id)]
        stealth_channel = message.guild.get_channel(int(player.id_stealth))
        await stealth_channel.send("<@"+str(message.author.id)+">\n"+"```"+player.__str__()+"```")

async def distribuir(client, message, args, players):
    #distribuir nome_attr valor 
    if len(args) < 3:
        await message.channel.send(const.SEM_ARGUMENTOS)
        await message.channel.send("`distribuir nome_attr valor`")
        await message.channel.send("atributos: inteligência, força, intimidação, carisma, percepção, constituição, destreza, furtividade, devoção.")
        return
    player = players[str(message.author.id)]
    out = ""
    if args[1] == "força":
        out = player.mudar_forca(int(args[2]))
    elif args[1] == "inteligência":
        out = player.mudar_inteligencia(int(args[2]))
    elif args[1] == "intimidação":
        out = player.mudar_intimidacao(int(args[2]))
    elif args[1] == "carisma":
        out = player.mudar_carisma(int(args[2]))
    elif args[1] == "percepção":
        out = player.mudar_percep(int(args[2]))
    elif args[1] == "constituição":
        out = player.mudar_const(int(args[2]))
    elif args[1] == "destreza":
        out = player.mudar_dex(int(args[2]))
    elif args[1] == "furtividade":
        out = player.mudar_furtividade(int(args[2]))
    elif args[1] == "devoção":
        out = player.mudar_devocao(int(args[2]))
    else: 
        out = "Atributo inexistente, use estes: inteligência, força, intimidação, carisma, percepção, constituição, destreza, furtividade, devoção."
    stealth_channel = message.guild.get_channel(int(player.id_stealth))
    await stealth_channel.send("<@"+str(message.author.id)+">\n"+out)
    


async def echo(client, message, args, players):
    #echo canal mensagem
    if len(args) < 3:
        await message.channel.send(const.SEM_ARGUMENTOS)
        await message.channel.send("`echo canal mensagem`")
        return 
    print(const.ADMINS)
    if not(str(message.author.id) in const.ADMINS):
        await message.channel.send("Sem permissões.")
        return 
    canal = message.guild.get_channel(int(args[1]))
    await canal.send(const.arg2text(args=args, start=2))
