#for i in range (1, 21):          #lista de los primeros 20 numeros 
#    print (i)              

#odds = list(range(1,20,2))        #lista de los impares del 1 al 20
#for odd in odds:
#    print(odd) 

# squares_1= []                 #lista de multiplos de 3 hasta el 30
# for value in range (3, 30, 3):         
#    squares_1.append(value)
# print(squares_1)

# squares = []                  #cubo de los numeros del 1 al 10
# for value in range (0, 10):
#     square = value **3
#     squares.append(square)
# for square in squares:
#     print(square)

squares = [value**2 for value in range (1,11)] #list comprenhension de cuadrados del 1 al 10
print(squares)

#page 60