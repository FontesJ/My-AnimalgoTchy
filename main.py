import functions as fn

saude = 100
risco = 50
fome = 0
vacina = 0
social = 50
moedas = 200
estoque = {"alimentos":{"agua":5, "lanche":2, "frango":0}, "cuidados": {"mascara":10, "alquingel":0}}

atividade = fn.menu(moedas)
#1.Alimentar
# 2.Armário
# 3.loja
# 4.Médico
# 5.Dormir
# 6.Passear
# 7. Status

if atividade == "1":
    fome, estoque = fn.alimentar(fome, estoque, moedas)

elif atividade == "2":
    fn.armario(estoque)

elif atividade == "3":
    moedas, estoque = fn.comprar(moedas, estoque)

elif atividade == "4":
    saude, moedas = fn.irAoMedico(saude, moedas)

elif atividade == "5":
     saude, fome, social = fn.dormir(saude, fome, social, moedas)

elif atividade == "6":
    print("Passear")

elif atividade == "7":
    fn.status(saude, fome, social, risco, vacina, moedas)