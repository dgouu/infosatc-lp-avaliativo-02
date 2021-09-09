#criação das 4 listas
filmes = ["carros","jurassic park",]
jogos = ["minecraft","lol"]
livros = ["diario de um banana","as cronicas de narnia",]
esportes = ["volei <3","basquete"]
#adicionando mais 2 itens em cada lista
filmes.append("V de vingança")
filmes.append("velozes e furiosos")
jogos.insert(1,"csgo")
jogos.append("roblox")
livros.insert(1,"diario de anne frank")
livros.append("destrua esse diario")
esportes.append("futebol")
esportes.append("tenis")
#criando a lista das listas
listas = [filmes,jogos,livros,esportes]
print(listas)
#mostrando um item da lista dos livros
print(livros[2])
#removendo um item da lista dos esportes
esportes.remove("futebol")
#adicionando uma lista de disciplinas na lista das listas 
listas.append("[portugues")
listas.append("matematica")
listas.append("fisica]")
print(listas)