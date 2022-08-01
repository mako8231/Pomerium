import json

from pkg.personagem import Jogador, Personagem 

def carregarConfig(caminho):
    #abrindo o arquivo
    stream = open(caminho)
    #carregar os dados 
    obj = json.load(stream)
    #fechar o arquivo
    stream.close()
    return obj

def carregarJogador(caminho):
    #abrindo o arquivo
    stream = open(caminho)
    #carregar os dados
    obj = json.load(stream)
    #fechar o arquivo 
    stream.close()
    player = Jogador(obj["inteligencia"], obj["forca"], obj["intimidacao"], obj["carisma"], obj["constituicao"], obj["destreza"], obj["furtividade"], obj["devocao"], obj["nome"], obj["id_jogador"], obj["id_stealth"])
    player.setHP(obj["hp_atual"])
    player.setEM(obj["em_atual"])
    return player

def criarFicha(player):
    stream = open("fichas/jogadores/"+str(player.id_jogador)+".json", "w")
    file = json.dumps(player, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    stream.write(file)