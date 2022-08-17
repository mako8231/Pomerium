
import math 
modificadores = [-1, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
#classe abstrata do tipo personagem, a ficha se baseará nessa classe 
class Personagem:
    def __init__(self, nome, inteligencia, forca, intimidacao, carisma, percep, const, destreza, furtividade, devocao):
        #stats primários 
        self.nome = nome 
        self.inteligencia = inteligencia
        self.forca = forca 
        self.intimidacao = intimidacao
        self.carisma = carisma 
        self.percep = percep 
        self.const = const 
        self.destreza = destreza
        self.furtividade = furtividade
        self.devocao = devocao

        #stats secundários 
        self.atk_forca = 10 + (self.forca * 2)
        self.atk_dex = 10 + (self.destreza * 2)
        self.em = 60 + (self.devocao * 2)
        self.max_hp = 100 + (self.const * 10)
        self.hp = self.max_hp
        self.locomocao = 2 + math.ceil(self.destreza)
        
    def __str__(self):
        out = "Nome: "+str(self.nome)+"\n"
        out += "STATS\n"
        out += "INTELIGÊNCIA: "+str(self.inteligencia)+"("+str(modificadores[self.inteligencia])+")"+"\n"
        out += "FORÇA: "+str(self.forca)+"("+str(modificadores[self.forca])+")"+"\n"
        out += "INTIMIDAÇÃO: "+str(self.intimidacao)+"("+str(modificadores[self.intimidacao])+")"+"\n"
        out += "CARISMA: "+str(self.carisma)+"("+str(modificadores[self.carisma])+")"+"\n"
        out += "PERCEP: "+str(self.percep)+"("+str(modificadores[self.percep])+")"+"\n"
        out += "CONSTITUIÇÃO: "+str(self.const)+"("+str(modificadores[self.const])+")"+"\n"
        out += "DESTREZA: "+str(self.destreza)+"("+str(modificadores[self.destreza])+")"+"\n"
        out += "FURTIVIDADE: "+str(self.furtividade)+"("+str(modificadores[self.furtividade])+")"+"\n"
        out += "DEVOÇÃO: "+str(self.devocao)+"("+str(modificadores[self.devocao])+")"+"\n"

        out += "\n"

        out += "ATK BASE (FORÇA): "+str(self.atk_forca)+"\n"
        out += "ATK BASE (DESTREZA): "+str(self.atk_dex)+"\n"
        out += "HP: "+str(self.max_hp)+"/"+str(self.hp)+"\n"
        out += "EM: "+str(self.em)+"\n"
        out += "LOCOMOÇÃO: "+str(self.locomocao)+"\n"
        
        return out 

class Jogador(Personagem):
    def __init__(self, nome, inteligencia, forca, intimidacao, carisma, percep, const, destreza, furtividade, devocao, id_discord : str, id_stealth : str):
        super().__init__(nome, inteligencia, forca, intimidacao, carisma, percep, const, destreza, furtividade, devocao)
        self.id_discord = id_discord
        self.id_stealth = id_stealth
        self.inventario = []
    def __str__(self):
        out = super().__str__()
        out += "\n"
        out += "ID DISCORD: "+self.id_discord + "\n"
        out += "ID do canal de Stealth: " + self.id_stealth + "\n"
        return out 