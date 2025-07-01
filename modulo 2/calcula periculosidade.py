
def calculo_mes():
    mes_ini = input("Digite o mês de inicio no formato MM " )
    ano_ini = input("Digite o ano de inicio no formato AAAA " )
    mes_fin = input("Digite o mês de término no formato MM " )
    ano_fin = input("Digite o ano de término no formato AAAA " )
    condição = True
    if int(mes_ini)>12:
        print("Verifique o mês informado!")
        condição= False
    if int(ano_ini) >2020 or int(ano_fin) <2014:
        print("Verifique o ano informado!")
        condição = False
    while condição:
        calculomes= 12 - int(mes_ini)
        calculoano= ((int(ano_fin) - int(ano_ini)-1) *12)
        condição = False
    calculo_mes = calculomes + calculoano +int(mes_fin)
    return calculo_mes
def main():
    valor = input("Digite o Valor do salário mensal: ")
    periculosidade = (float(valor)/100)*30
    tempo = calculo_mes()
    valor_devido = tempo* periculosidade
    print("O valor devido ao funcionário é R$",valor_devido)
    
def ferias():
    valor = input("Digite o Valor do salário mensal: ")
    ferias = float(valor)/3
    a_receber = float(valor)+ ferias
    return a_receber

    
    
