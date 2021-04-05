def menu():
    print("Olá. o que gostaria de fazer?\n\n")
    print("1.Alimentar\n2.Armário\n3.loja\n4.Médico\n5.Dormir\n6.Passear\n\n")
    atividade = input("Resposta: ")

    if int(atividade) > 6 and atividade < 1:
        print("Entrada inválida")

    return atividade

def dormir(saude, fome, social):
    print("zzZZzZZZzzZzZZ")
    print("O dia amanheceu...\n\n")

    saude += 10
    fome += 30
    social -= 15

def alimentar(fome, estoque):

    estoque_alimentos = estoque["alimentos"]

    agua = [estoque["agua"], 5]
    lanche = [estoque["lanche"], 25]
    frango = [estoque["frango"], 45]

    x = input("1.Água(-5 fome)\n2.Lanche(-25 fome)\n3.Frango(-45 fome)\n\nQual a sua escolha?")

    if x == "1":
        if agua[0] != 0:
            a = agua[1]
        else:
            print("sem estoque!")
    elif x == "2":
        if lanche[0] != 0:
            a = lanche[1]
        else:
            print("sem estoque!")
    elif x == "3":
        if frango[0] != 0:
            a = frango[1]
        else:
            print("sem estoque!")
    else:
        print("Valor inválido")

    fome -= a

    return fome

def comprar(moedas, estoque):

    mascara = 10
    alquingel = 15
    agua = 5
    lanche = 25
    frango = 50

    modalidade = input("o que quer comprar?\n\n1.Alimentos\n2.Cuidados\n\n")

    if modalidade == "1":

        x = input("1.Água 5$\n2.Lanche $25\n3.Frango $50\n\nQual a sua escolha?")

        if x == "1":
            try:
                estoque["agua"] += 1
            except:
                estoque["agua"] = 1
            try:
                moedas -= agua
            except:
                print("moedas insuficientes!\n\n")

        elif x == "2":
            try:
                estoque["lanche"] += 1
            except:
                estoque["lanche"] = 1
            try:
                moedas -= lanche
            except:
                print("moedas insuficientes!\n\n")

        elif x == "3":
            try:
                estoque["frango"] += 1
            except:
                estoque["frango"] = 1
            try:
                moedas -= frango
            except:
                print("moedas insuficientes!\n\n")
        else:
            print("Entrada inválida!\n\n")

    elif modalidade == "2":

        x = input("1.Mascara 10$\n2.Alcool $15\n\nQual a sua escolha?")

        if x == "1":
            try:
                estoque["mascara"] += 1
            except:
                estoque["mascara"] = 1
            try:
                moedas -= mascara
            except:
                print("moedas insuficientes!\n\n")

        elif x == "2":
            try:
                estoque["Alcool em gel"] += 1
            except:
                estoque["Alcool em gel"] = 1
            try:
                moedas -= alquingel
            except:
                print("moedas insuficientes!\n\n")

        else:
            print("Entrada inválida!\n\n")

    return moedas, estoque

def dormir(saude):
    saude += 15

def irAoMedico(saude, moedas):

    if saude < 10:
        saude='gravíssimo'
    elif saude < 20:
        saude = 'grave'
    elif saude < 40:
        saude = 'sério'
    elif saude < 60:
        saude = 'moderado'
    elif saude < 80:
        saude = 'saudavel'
    elif saude < 100:
        saude = 'super saudavel'

    medico = input("1.Consulta\n2.Teste $30\n\nO que deseja fazer?")

    if medico == '1':
        print("Doutor: sua condição é "+saude+"!\n")

        if saude < 30:
            print("Sua condição é crítica! precisará ficar internado! :(")

        if saude < 60:
            print("você precisa de remédios. Recomendo também um TESTE.")

        else:
            print("Você está indo bem, mas precisa se cuidar.")

    elif medico == '2':
        print("O resultado do teste sai em uma hora!")
        moedas -=30

    return moedas, saude
    aaaaaaaaaaaaaaaaaaaaaaa
def armario(estoque):

    print(estoque)

