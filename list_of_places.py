"""print seven places in the world and order them"""
places = ['Italia', 'Colombia', 'México', 'Argentina', 'Chile', 'Grecia', 'España']
print (places)

place = places
print(sorted(place))  #ordenado alfabeticamente

place.sort(reverse=True)
print(place) #ordenado en reversa del alfabeto

places.sort()
print(places)

#usa len para ver cuantos invitados iran a cenar
guest = ['pepe', 'Juana', 'Tita']
guest = ['pepe', 'Juana', 'Tita']
guest.append('Mike')
guest.insert(1,'Luis')
print(guest)
print (f"Estas cordialmente invitado {guest [0].capitalize()}")
print (f"Estas cordialmente invitado {guest [1]}")
print (f"Estas cordialmente invitado {guest [2]}")
print (f"Estas cordialmente invitado {guest [3]}")
print (f"Estas cordialmente invitado {guest [4]}")
print (f"hay {len(guest)} invitados")
