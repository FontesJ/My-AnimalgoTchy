def menu(moedas):
    print("\n\nOlá. o que gostaria de fazer? (Moedas: " + str(moedas) + ")\n")
    print("1.Alimentar\n2.Armário\n3.loja\n4.Médico\n5.Dormir\n6.Passear\n7.Status\n")
    atividade = input("Resposta: ")

    if int(atividade) > 7 and atividade < 1:
        print("Entrada inválida")

    return atividade


def dormir(saude, fome, social, moedas):
    print("zzZZzZZZzzZzZZ")
    print("O dia amanheceu...\n\n")

    saude += 10
    fome += 30
    social -= 15

    menu(moedas)

    return saude, fome, social


def alimentar(fome, estoque, moedas):
    estoque_alimentos = estoque["alimentos"]

    agua = [estoque_alimentos["agua"], 5]
    lanche = [estoque_alimentos["lanche"], 25]
    frango = [estoque_alimentos["frango"], 45]

    x = input("1.Água(-5 fome)\n2.Lanche(-25 fome)\n3.Frango(-45 fome)\n\nQual a sua escolha?")

    if x == "1":
        if agua[0] != 0:
            a = agua[1]
            agua[0] -= 1
        else:
            print("sem estoque!")
    elif x == "2":
        if lanche[0] != 0:
            a = lanche[1]
            lanche[0] -= 1
        else:
            print("sem estoque!")
    elif x == "3":
        if frango[0] != 0:
            a = frango[1]
            frango[0] -= 1
        else:
            print("sem estoque!")
    else:
        print("Valor inválido")

    fome -= a

    print("fome -" + str(a))

    menu(moedas)

    return fome, estoque


def comprar(moedas, estoque):
    mascara = 10
    alquingel = 15
    agua = 5
    lanche = 25
    frango = 50

    modalidade = input("o que quer comprar? (Moedas: " + str(moedas) + ")\n\n1.Alimentos\n2.Cuidados\n\n")

    if modalidade == "1":

        x = input("1.Água 5$\n2.Lanche $25\n3.Frango $50\n\nQual a sua escolha?")

        if x == "1":
            if moedas < agua:
                print("moedas insuficientes!\n\n")
            else:
                try:
                    estoque["agua"] += 1
                except:
                    estoque["agua"] = 1
                moedas -= agua
                compra = "Água"

        elif x == "2":
            if moedas < lanche:
                print("moedas insuficientes!\n\n")
            else:
                try:
                    estoque["lanche"] += 1
                except:
                    estoque["lanche"] = 1
                moedas -= lanche
                compra = "Lanche"

        elif x == "3":
            if moedas < frango:
                print("moedas insuficientes!\n\n")
            else:
                try:
                    estoque["frango"] += 1
                except:
                    estoque["frango"] = 1
                moedas -= frango
                compra: "Frango"
        else:
            print("Entrada inválida!\n\n")

    elif modalidade == "2":

        x = input("1.Mascara 10$\n2.Alcool $15\n\nQual a sua escolha?")

        if x == "1":
            if moedas < mascara:
                print("moedas insuficientes!\n\n")
            else:
                try:
                    estoque["mascara"] += 1
                except:
                    estoque["mascara"] = 1
                moedas -= mascara
                compra = "Máscara"

        elif x == "2":
            if moedas < alquingel:
                print("moedas insuficientes!\n\n")
            else:
                try:
                    estoque["Alcool em gel"] += 1
                except:
                    estoque["Alcool em gel"] = 1
                moedas -= alquingel
                compra = "Álcool em gel"

        else:
            print("Entrada inválida!\n\n")

        print("você comprou: "+compra)

    menu(moedas)

    return moedas, estoque


def irAoMedico(saude, moedas):

    estado_saude = ""

    if saude < 10:
        estado_saude = 'gravíssimo'
    elif saude < 20:
        estado_saude = 'grave'
    elif saude < 40:
        estado_saude = 'sério'
    elif saude < 60:
        estado_saude = 'moderado'
    elif saude < 80:
        estado_saude = 'saudavel'
    elif saude < 100:
        estado_saude = 'super saudavel'

    medico = input("1.Consulta\n2.Teste $30\n\nO que deseja fazer?")

    if medico == '1':
        print("\nDoutor: sua condição é " + estado_saude + "!\n")

        if saude < 30:
            print("Sua condição é crítica! precisará ficar internado! :(")

        if saude < 60:
            print("você precisa de remédios. Recomendo também um TESTE.")

        else:
            print("Você está indo bem, mas precisa sempre se cuidar.")

    elif medico == '2':
        print("O resultado do teste sai em uma hora!")
        moedas -= 30

    menu(moedas)

    return saude, moedas


def armario(estoque):
    print(estoque)


def status(saude, fome, social, risco, vacina, moedas):
    print("\nSaúde: " + str(saude))
    print("Fome: " + str(fome))
    print("Amigos: " + str(social))
    print("Risco de Contaminação: " + str(risco))
    print("Avanço da Vacina: " + str(vacina) + "\n\n")

    menu(moedas)
