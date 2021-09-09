n1 = input("Digite aqui um nome: ")
n2 = input("Digite aqui um nome: ")
n3 = input("Digite aqui um nome: ")
listanomes = [n1,n2,n3]
ib = input("Digiite algum nome que voce deseja saber se está ou não na lista: ")
if ib in listanomes:
    print("Sim, está na lista")
else:
    print("Não, não está na lista ;-;")