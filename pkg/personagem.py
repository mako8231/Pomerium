class Personagem:
    def __init__(self, inteligencia, forca, intimidacao, carisma, constituicao, destreza, furtividade, devocao, nome):
        #atributos
        self.nome = nome
        self.inteligencia = inteligencia
        self.forca = forca
        self.intimidacao = intimidacao
        self.carisma = carisma
        self.constituicao = constituicao
        self.destreza = destreza
        self.furtividade = furtividade
        self.devocao = devocao

        self.attStatus()
        self.hp_atual = self.hp
        self.em_atual = self.em

    def setInt(self, val, op: bool):
        self.inteligencia += val * (-1 * int(op))
        self.attStatus()
        pass
    
    def setFor(self, val, op: bool):
        self.forca += val * (-1 * int(op))
        self.attStatus()
        pass
    
    def setIntimida(self, val, op: bool):
        self.intimidacao += val * (-1 * int(op))
        self.attStatus()
        pass
    
    def setCarism(self, val, op: bool):
        self.carisma += val * (-1 * int(op))
        self.attStatus()
        pass
    
    def setConst(self, val, op: bool):
        self.constituicao += val * (-1 * int(op))
        self.attStatus()
        pass
    
    def setDest(self, val, op: bool):
        self.destreza += val * (-1 * int(op))
        self.attStatus()
        pass
    
    def setFurti(self, val, op: bool):
        self.furtividade += val * (-1 * int(op))
        self.attStatus()
        pass
    
    def setDev(self, val, op: bool):
        self.devocao += val * (-1 * int(op))
        self.attStatus()
        pass
    
    def setHP(self, val:int):
        self.hp_atual = val
    
    def setEM(self, val:int):
        self.em_atual = val


    def changeHP(self, val:int):
        self.hp_atual += val
    
    def changeEM(self, val:int):
        self.em_atual += val

    def __str__(self):
        return "Inteligência: "+str(self.inteligencia)+"\n"+"Força: "+str(self.forca)+"\n"+"Intimidação: "+str(self.intimidacao)+"\n"+"Carisma: "+str(self.carisma)+"\n"+"Constituição: "+str(self.constituicao)+"\n"+"Destreza: "+str(self.destreza)+"\n"+"Furtividade: "+str(self.furtividade)+"\n"+"Devoção: "+str(self.devocao)+"\n"+"======="+"\n"+"HP: "+str(self.hp_atual)+"/"+str(self.hp)+"\n"+"EM: "+str(self.em_atual)+"/"+str(self.em)+"\n"+"Defesa: "+str(self.defesa)+"\n"+"Ataque: "+str(self.atk)+"\n"
    
    def attStatus(self):
        self.hp = self.constituicao * 20
        self.em = (self.inteligencia + self.devocao) * 5
        self.defesa = (self.forca + self.constituicao)
        self.atk = (self.forca + self.destreza)
        
pass   


class Jogador(Personagem):
    def __init__(self, inteligencia, forca, intimidacao, carisma, constituicao, destreza, furtividade, devocao, nome, id_jogador, id_stealth):
        #chamar a classe pai
        Personagem.__init__(self, inteligencia, forca, intimidacao, carisma, constituicao, destreza, furtividade, devocao, nome)
        #simples array de strings
        self.inventario = []
        #dono do personagem
        self.id_jogador = id_jogador
        self.id_stealth = id_stealth
        self.tam_inv = 0
    pass

    def addInv(self, item: str):
        self.inventario.append({"nome" : item, "indice" : self.tam_inv+1})
    
    def inv(self) -> str:
        texto : str 
        for item in self.inventario:
            texto += item["nome"] + "\n"
        return texto 
    