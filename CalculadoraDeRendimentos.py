from os import system, name
import datetime
system('cls' if name == 'nt' else 'clear') #Linha que limpa a tela.
escolha = tempoi = tempof = int()
valor = float()

def menu(escolha): #Mostra um menu inicial e fornece as opções ao usuário
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Bem Vindo(a) á calculadora de investimentos em Renda Fixa.')
    print('Em qual fundo você irá investir hoje?\n[1]TESOURO SELIC\n[2]CDB PRÉ FIXADO\n[3]CDB PÓS-FIXADO\n[4]CDB HÍBRIDO')
    escolha = verificadorescolha(escolha) #Manda o valor recebido para a função verificadora.
    return(escolha)

def verificadorescolha(escolha): #Verifica se o valor Inserido na função menu é válido
    while (escolha >= 5) or (escolha < 1):
        escolha = int(input('Escolha um item: '))
        if (escolha >= 5) or (escolha < 1):
            print('O valor inserido não é válido.')
    return(escolha)

def verificadordedatainicial(datai):
    while True: #Verifica se o valor inserido veio no formato correto e se a data já não passou para a data inicial.
        try:
            datai = datetime.datetime.strptime(input('Digite a data que será efetuada o investimento. FORMATO [dd/mm/aaaa]: ').strip(), '%d/%m/%Y')
            while datetime.datetime.now() > datai: #Transforma a data string para objeto datetime
                if datetime.datetime.now() > datai: #Verifica se a data está no passado
                    print('A data inserida já passou')
                    datai = datetime.datetime.strptime(input('Digite a data que será efetuada o investimento. FORMATO [dd/mm/aaaa]: ').strip(), '%d/%m/%Y')
            return(datai)
        except ValueError: #Retorna erro caso a data seja inválida
            print('A data inserida não é válida')

def verificadordedatafinal(dataf, datai):
     while True: #Verifica se o valor inserido veio no formato correto e se a data já não passou para a data final.
        try:
            dataf = datetime.datetime.strptime(input('Muito bem! Agora digite a data aproximada a qual você quer sacar esse valor. FORMATO [dd/mm/aaaa]: ').strip(), '%d/%m/%Y')
            while (datetime.datetime.now() > dataf) or (dataf == datai):
                while datetime.datetime.now() > dataf: #Transforma a data String recebida para objeto DateTime
                    if datetime.datetime.now() > dataf: #Verifica se a data está no passado
                        print('A data inserida já passou')
                        dataf = datetime.datetime.strptime(input('Muito bem! Agora digite a data aproximada a qual você quer sacar esse valor. FORMATO [dd/mm/aaaa]: ').strip(), '%d/%m/%Y')
                while dataf == datai:
                    if dataf == datai: #Verifica se a data de início e de término do investimento são iguais.
                        print('As duas datas não podem ser iguais.')
                        dataf = datetime.datetime.strptime(input('Insira novamente a data aproximada do fim do investimento: ').strip(), '%d/%m/%Y')
            return(dataf)
        except ValueError: #Retorna erro caso a data seja inválida.
            print('A data inserida não é válida')  

def selic (valor, tempoi, tempof): #Trabalha o investimento no tesouro Selic.
    from time import sleep
    intervalo = 0
    system('cls' if name == 'nt' else 'clear')
    if datetime.datetime.now() > datetime.datetime(2023, 5, 2):  #Verifica se a próxima reunião do COPOM já ocorreu.
        print('Este software não está datado de acordo com a última reunião do COPOM e a taxa selic pode ter sofrido alterações.')
        print(datetime.datetime.now()) #Imprime na tela a data atual.
    print('Bem Vindo(a) á calculadora de investimentos do TESOURO SELIC.')
    sleep(1)
    print('A taxa selic está em 13.75% de acordo com a última atualização desse programa.')
    sleep(1)
    valor = input('Insira aqui o valor inicial (Primeiro Mês) que deseja investir. R$ ') #Recebe o valor de entrada do investimento
    valor = valor.replace(',', '.') #Substitui uma posível vírgula digitada pelo usuário por um ponto
    valor = float(valor)
    system('cls' if name == 'nt' else 'clear')
    print('Muito bem! Agora vamos definir o tempo de investimento')
    tempoi = verificadordedatainicial(tempoi)#Ativa a função de verificação do formato de data inicial.
    tempof = verificadordedatafinal(tempof, tempoi) #Ativa a função de verificação do formato de data final.
    intervalo = diasuteis(tempoi, tempof)  #Ativa a função dias úteis.
    system('cls' if name == 'nt' else 'clear')
    print(f'O seu dinheiro estará investido em um intevalo de {intervalo} dias úteis. [exceto feriados.]')
    sleep(1)
    rendimento = valor * ((1 + 0.1375/252) ** intervalo - 1) #Calcula o rendimento.
    print(f'O seu rendimento líquido será de R${round(rendimento, 2)} e o montante final será de R${round(valor+rendimento, 2)}')

def cdbprefixado (valor, tempoi, tempof): #Trabalha o investimento no tesouro Selic.
    from time import sleep
    intervalo = 0
    system('cls' if name == 'nt' else 'clear')
    print('Bem Vindo(a) á calculadora de investimentos do CDB Pré-Fixado.')
    sleep(1)
    taxa = input('Insira aqui a taxa de rendimento em % ao ano: ')
    lista = list()
    for i in range(0, len(taxa)): #Retira da taxa qualquer possível entrada que não seja numérica
        if taxa[i].isnumeric() or taxa[i] == '.' or taxa[i] == ',':
            if taxa[i] == ',': #Substitui uma possível , digitada na taxa por um .
                lista.append('.')
            else:
                lista.append(taxa[i])
    taxa = float(''.join(lista)) #Recebe a taxa em um valor float.
    valor = input('Insira aqui o valor inicial (Primeiro Mês) que deseja investir. R$ ') #Recebe o valor de entrada do investimento
    valor = valor.replace(',', '.') #Substitui uma posível vírgula digitada pelo usuário por um ponto
    valor = float(valor)
    system('cls' if name == 'nt' else 'clear')
    print('Muito bem! Agora vamos definir o tempo de investimento')
    tempoi = verificadordedatainicial(tempoi)#Ativa a função de verificação do formato de data inicial.
    tempof = verificadordedatafinal(tempof, tempoi) #Ativa a função de verificação do formato de data final.
    intervalo = diasuteis(tempoi, tempof)  #Ativa a função dias úteis.
    system('cls' if name == 'nt' else 'clear')
    print(f'O seu dinheiro estará investido em um intevalo de {intervalo} dias úteis. [exceto feriados.]')
    sleep(1)
    rendimento = valor * ((1 + (taxa/100)/252) ** intervalo - 1) #Calcula o rendimento.
    print(f'O seu rendimento líquido será de R${round(rendimento, 2)} e o montante final será de R${round(valor+rendimento, 2)}')
    

def diasuteis(datai, dataf): #Função que vai selecionar apenas os dias úteis(Dias de Rendimento) no intervalo escolhido.
    import pandas as pd
    from pandas.tseries.offsets import CustomBusinessDay   
    calendario = CustomBusinessDay(weekmask='Mon Tue Wed Thu Fri') #Seleciona apenas os dias úteis da semana
    diasuteis = len(pd.date_range(start=datai, end=dataf, freq=calendario)) #Analisa o calendário com os dias pré definidos
    return(diasuteis) #Retorna o número de dias úteis.

escolha = menu(escolha)
if escolha == 1:
    selic(valor, tempoi, tempof)
elif escolha == 2:
    cdbprefixado(valor, tempoi, tempof)

