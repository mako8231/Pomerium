import pkg.char as char  
import json 

def save_player(json_dict, player_id):
    with open("./player/"+player_id+".json", "w") as out:
        out.write(json_dict)

def load_player(id):
    jogador = None 
    with open("./player/"+id, "r") as out:
        data = json.load(out)
        jogador = char.Jogador(data["nome"], data["inteligencia"], data["forca"], data["intimidacao"], data["carisma"], data["percep"], data["const"], data["destreza"], data["furtividade"], data["devocao"], data["id_discord"], data["id_stealth"])
        jogador.hp = data["hp"]
        jogador.em = data["em"]
        jogador.inventario = data["inventario"]
        jogador.stack_pts = data["stack_pts"]
    return jogador 