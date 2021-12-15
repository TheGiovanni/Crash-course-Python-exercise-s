"""Modify your for loop to print a sentence using the name of the pizza"""

pizzas = ['Pepperoni', 'Hawaiana', 'Pastor', 'Salami', 'Margarita']
pizzas.append('salchironi')
print("my favorite pizzas are: ")
for i in pizzas:
    print(i.title())

friends_pizzas = pizzas [4:6]
friends_pizzas.append('cochinita') #si, si existe
print ("My friends favorite pizzas are: ")
for i in friends_pizzas:
    print(i)
    

