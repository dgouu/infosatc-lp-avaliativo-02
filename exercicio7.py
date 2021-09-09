#criação das 4 listas
filmes = ["carros","jurassic park","v de vingança","velozes e furiosos"]
jogos = ["minecraft","lol","csgo"]
livros = ["diario de um banana","as cronicas de narnia","diario de anne frank"]
esportes = ["volei <3","basquete","futebol"]
#criando a lista das listas
listas = ["filmes","jogos","livros","esportes"]
#mostrando um item da lista dos livros
print(livros[2])
#removendo um item da lista dos esportes
esportes.remove("futebol")
#adicionando uma lista de disciplinas na lista das listas 
listas.append("disciplinas")
print(listas)