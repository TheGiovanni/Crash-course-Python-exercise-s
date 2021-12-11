"""Use a list to print a mesage to each person, inviting them a dinner"""

guest = ['pepe', 'Juana', 'Tita']

print (f"Estas cordialmente invitado {guest [0].capitalize()}")
print (f"Estas cordialmente invitado {guest [1]}")
print (f"Estas cordialmente invitado {guest [2]}")

#cambiar a un invitado accesando a la lista
guest = ['pepe', 'Juana', 'Tita']
guest [0]= "Mike" #en esta linea se cambia al invitado 
print (f"Estas cordialmente invitado {guest [0].capitalize()}")
print (f"Estas cordialmente invitado {guest [1]}")
print (f"Estas cordialmente invitado {guest [2]}")

#ahora se agragará a mas invitados 
guest = ['pepe', 'Juana', 'Tita']
guest.append('Mike')
guest.insert(1,'Luis')
print(guest)
print (f"Estas cordialmente invitado {guest [0].capitalize()}")
print (f"Estas cordialmente invitado {guest [1]}")
print (f"Estas cordialmente invitado {guest [2]}")
print (f"Estas cordialmente invitado {guest [3]}")
print (f"Estas cordialmente invitado {guest [4]}")

"""eliminar a dos invitados e imprimirles un mensaje a cada uno"""
guest = ['pepe', 'Juana', 'Tita', 'mike', 'luis']
desinvitado = guest.pop()
print (f"Lo siento {desinvitado.title()} pero ya no hay lugar para ti")
desinvitado_2 = guest.pop(3)
print (f"Lo siento {desinvitado_2.title()} pero ya no hay lugar para ti")



#page 42 & 43