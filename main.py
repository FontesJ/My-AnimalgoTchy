import functions as fn

saude = 100
risco = 50
fome = 0
vacina = 0
social = 50
moedas = 200
estoque = {"alimentos":{"agua":5, "lanche":2, "frango":0}, "cuidados": {"mascara":10, "alquingel":0}}

atividade = fn.menu()aaaaa
#1.Alimentar
# 2.Armário
# 3.loja
# 4.Médico
# 5.Dormir
# 6.Passear
if atividade == "1":
    fn.alimentar(fome, estoque)
elif atividade == "2":
    fn.armario(estoque)
elif atividade == "3":
    fn.comprar(moedas, estoque)
elif atividade == "4":
    fn.irAoMedico(saude, moedas)