def conta_letras(frase,contar = "vogais"):
    frase= frase.lower()
    frase= frase.strip()
    contar = contar.lower()
    vogais = 0
    consoantes = 0
    espaco = 0 
    for i in frase:
        x = i
        if x ==" ":
            espaco =espaco+1
        if x == "a"or x == "e" or x == "i" or x == "o" or x == "u":
            vogais = vogais +1
        else:
            consoantes = consoantes + 1
    if contar == "vogais": 
        return (vogais)
    else:
        return(consoantes - espaco)
