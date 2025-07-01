frase='Ricardo E LindoPrOgRao'
conta = "vogais"
def conta_letras(frase,conta = "vogais"):
    frase= frase.lower()
    conta = conta.lower()
    vogais = 0 
    for i in frase:
        x= i
        if x == "a"or x == "e" or x == "i" or x == "o" or x == "u":
            vogais = vogais +1
    for i in conta:
        x= i
        if x == "a"or x == "e" or x == "i" or x == "o" or x == "u":
            vogais = vogais +1


    return(vogais)
