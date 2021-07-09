#Source: https://www.learnpython.org/en/List_Comprehensions
#List Comprenhensions permite crear una nueva lista utilizando una linea mas fácil de enteder.

#Example of program
# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# word_lengths = []
# for word in words:
#       if word != "the":
#           word_lengths.append(len(word))
# print(words)
# print(word_lengths)

#El mismo programa podríamos reducirlo a:
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)
#Funciona encadenanto cosas :O

#Otro ejemplo:
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [number for number in numbers if number > 0]
print(newlist)
#El primer "number" es el resultado final, ahí podemos aplicar algún postprocesado.
# seguido de for que se declara como un loop for normal.
# if es un condicional que se pone al final.