from cgitb import text


SEM_ARGUMENTOS = "Argumentos insuficientes"
ADMINS = {}

def arg2text(args, start):
    text = ""
    i = start 
    while(i<len(args)):
        text += args[i] + " "
        i+=1
    return text