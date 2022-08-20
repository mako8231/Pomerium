from ast import arg
import pkg.const as const

async def add_equip(client, message, args, players):
    #add_equip nome id_jogador descrição
    if len(args) < 4:
        await message.channel.send(const.SEM_ARGUMENTOS)
        await message.channel.send("`add_equip nome id_jogador descrição`")
        return 
    msg = const.arg2text(args=args, start=3)
    players[args[2]].adicionar_equipamento(args[1], msg)
    message.channel.send("Equipamento adicionado com sucesso.")
    pass

async def level_up(client, message, args, players):
    #level_up valor 
    if len(args) < 2:
        await message.channel.send(const.SEM_ARGUMENTOS)
        await message.channel.send("`level_up valor`")
        return 
    for id in players: 
        players[id].aumentar_stack(int(args[1]))
    await message.channel.send("Todos os jogadores subiram de nível")
    pass