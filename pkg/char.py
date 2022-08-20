import json
import math
from tkinter import E
import pkg.save as save  

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
        self.max_em = 60 + (self.devocao * 2)
        self.em = self.max_em
        self.max_hp = 100 + (self.const * 10)
        self.hp = self.max_hp
        self.locomocao = 2 + math.ceil(self.destreza)
        
    def __str__(self):
        out = "Nome: "+str(self.nome)+"\n"
        out += "STATS\n"
        out += "INTELIGÊNCIA:   "+str(self.inteligencia)+"("+str(modificadores[self.inteligencia])+")"+"\n"
        out += "FORÇA:          "+str(self.forca)+"("+str(modificadores[self.forca])+")"+"\n"
        out += "INTIMIDAÇÃO:    "+str(self.intimidacao)+"("+str(modificadores[self.intimidacao])+")"+"\n"
        out += "CARISMA:        "+str(self.carisma)+"("+str(modificadores[self.carisma])+")"+"\n"
        out += "PERCEP:         "+str(self.percep)+"("+str(modificadores[self.percep])+")"+"\n"
        out += "CONSTITUIÇÃO:   "+str(self.const)+"("+str(modificadores[self.const])+")"+"\n"
        out += "DESTREZA:       "+str(self.destreza)+"("+str(modificadores[self.destreza])+")"+"\n"
        out += "FURTIVIDADE:    "+str(self.furtividade)+"("+str(modificadores[self.furtividade])+")"+"\n"
        out += "DEVOÇÃO:        "+str(self.devocao)+"("+str(modificadores[self.devocao])+")"+"\n"

        out += "\n"

        out += "ATK BASE (FORÇA):"+str(self.atk_forca)+"\n"
        out += "ATK BASE (DESTREZA):"+str(self.atk_dex)+"\n"
        out += "HP:"+str(self.max_hp)+"/"+str(self.hp)+"\n"
        out += "EM:"+str(self.max_em)+"/"+str(self.em)+"\n"
        out += "LOCOMOÇÃO:"+str(self.locomocao)+"\n"
        
        return out 
    
    #stats base
    def mudar_inteligencia(self, valor):
        out = ""
        if self.inteligencia < 10:
            out = str(valor) +" Pontos para inteligência" + "\n"
            self.inteligencia += valor 
            return out
        else:
            return "Esse atributo maximizou." 
    
    def mudar_forca(self, valor):
        if self.forca < 10:
            out = str(valor) +" Pontos para força" + "\n"
            self.forca += valor 
            return out 
        else: 
            return "Esse atributo maximizou."
    
    def mudar_intimidacao(self, valor):
        if self.intimidacao < 10:
            out = str(valor) +" Pontos para intimidação" + "\n"
            self.intimidacao += valor 
            return out 
        else:
            return "Esse atributo maximizou."
    
    def mudar_carisma(self, valor):
        if self.carisma < 10:
            out = str(valor) +" Pontos para carisma" + "\n"
            self.carisma += valor 
            return out 
        else: 
            return "Esse atributo maximizou."

    
    def mudar_percep(self, valor):
        if self.percep < 10:
            out = str(valor) +" Pontos para percep" + "\n"
            self.percep += valor 
            return out
        else:
            return "Esse atributo maximizou."

    
    def mudar_const(self, valor):
        if self.const < 10:
            out = str(valor) +" Pontos para constituição" + "\n"
            self.const += valor 
            return out
        else:
            return "Esse atributo maximizou."
    
    def mudar_dex(self, valor):
        if self.destreza < 10:
            out = str(valor) +" Pontos para destreza" + "\n"
            self.destreza += valor 
            return out
        else:
            return "Esse atributo maximizou."
    
    def mudar_furtividade(self, valor):
        if self.furtividade < 10:
            out = str(valor) +" Pontos para furtividade" + "\n"
            self.furtividade += valor 
            return out
        else:
            return "Esse atributo maximizou."
 
    
    def mudar_devocao(self, valor):
        if self.devocao < 10:
            out = str(valor) +" Pontos para devoção" + "\n"
            self.devocao += valor 
            return out 
        else:
            return "Esse atributo maximizou."

    def mudar_hp(self, valor):
        out = ""
        self.hp += valor 
        out += "`HP:"+str(self.hp)+"/"+str(self.max_hp)+"`\n";
        return out 
    
    def mudar_em(self, valor):
        out = ""
        self.em += valor 
        out += "`EM:"+str(self.em)+"/"+str(self.max_em)+"`\n";
        return out 
    
    #recalcular os stats 
    def atualizar_stats(self):
        #stats secundários 
        self.atk_forca = 10 + (self.forca * 2)
        self.atk_dex = 10 + (self.destreza * 2)
        self.max_em = 60 + (self.devocao * 2)
        self.max_hp = 100 + (self.const * 10)
        self.locomocao = 2 + math.ceil(self.destreza)
        
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class Jogador(Personagem):
    def __init__(self, nome, inteligencia, forca, intimidacao, carisma, percep, const, destreza, furtividade, devocao, id_discord : str, id_stealth : str):
        super().__init__(nome, inteligencia, forca, intimidacao, carisma, percep, const, destreza, furtividade, devocao)
        self.id_discord = id_discord
        self.id_stealth = id_stealth
        self.stack_pts = 0
        self.inventario = []
        self.equipamento = []
    
    def adicionar_equipamento(self, nome_equi, desc):
        self.equipamento.append({nome_equi: desc})
        save.save_player(self.toJSON(), self.id_discord)

    def adicionar_item(self, nome_item):
        self.inventario.append(nome_item)
        save.save_player(self.toJSON(), self.id_discord)

    def aumentar_stack(self, valor):
        self.stack_pts += valor 
        save.save_player(self.toJSON(), self.id_discord)
    
    def mudar_em(self, valor):
        out = super().mudar_em(valor)
        save.save_player(self.toJSON(), self.id_discord)
        return out 

    def mudar_hp(self, valor):
        out = super().mudar_hp(valor)
        save.save_player(self.toJSON(), self.id_discord)
        return out 
    

#stats base
    def mudar_inteligencia(self, valor):
        if valor <= self.stack_pts:
            out = super().mudar_inteligencia(valor)
            self.stack_pts -= valor 
            self.atualizar_stats()
            save.save_player(self.toJSON(), self.id_discord)
            return out
        return "Pontos acumulados insuficiente."
    
    def mudar_forca(self, valor):
        print(self.stack_pts)
        if valor <= self.stack_pts:
            out = super().mudar_forca(valor)
            self.stack_pts -= valor 
            self.atualizar_stats()
            save.save_player(self.toJSON(), self.id_discord)
            return out
        return "Pontos acumulados insuficiente."
    
    def mudar_intimidacao(self, valor):
        if valor <= self.stack_pts:
            out = super().mudar_intimidacao(valor)
            self.stack_pts -= valor 
            self.atualizar_stats()
            save.save_player(self.toJSON(), self.id_discord)
            return out
        return "Pontos acumulados insuficiente."
    
    def mudar_carisma(self, valor):
        if valor <= self.stack_pts:
            out = super().mudar_carisma(valor)
            self.stack_pts -= valor 
            self.atualizar_stats()
            save.save_player(self.toJSON(), self.id_discord)
            return out
        return "Pontos acumulados insuficiente."

    
    def mudar_percep(self, valor):
        if valor <= self.stack_pts:
            out = super().mudar_percep(valor)
            self.stack_pts -= valor 
            self.atualizar_stats()
            save.save_player(self.toJSON(), self.id_discord)
            return out
        return "Pontos acumulados insuficiente."

    
    def mudar_const(self, valor):
        if valor <= self.stack_pts:
            out = super().mudar_const(valor)
            self.stack_pts -= valor 
            self.atualizar_stats()
            save.save_player(self.toJSON(), self.id_discord)
            return out
        return "Pontos acumulados insuficiente."
    
    def mudar_dex(self, valor):
        if valor <= self.stack_pts:
            out = super().mudar_dex(valor)
            self.stack_pts -= valor 
            self.atualizar_stats()
            save.save_player(self.toJSON(), self.id_discord)
            return out
        return "Pontos acumulados insuficiente."
    
    def mudar_furtividade(self, valor):
        if valor <= self.stack_pts:
            out = super().mudar_furtividade(valor)
            self.stack_pts -= valor 
            self.atualizar_stats()
            save.save_player(self.toJSON(), self.id_discord)
            return out
        return "Pontos acumulados insuficiente."
 
    
    def mudar_devocao(self, valor):
        if valor <= self.stack_pts:
            out = super().mudar_devocao(valor)
            self.stack_pts -= valor 
            self.atualizar_stats()
            save.save_player(self.toJSON(), self.id_discord)
            return out
        return "Pontos acumulados insuficiente."


    def __str__(self):
        out = super().__str__()
        out += "\n"
        out += "Itens: " + "\n"
        for item in self.inventario:
            out += item + "\n"
        
        return out 
    