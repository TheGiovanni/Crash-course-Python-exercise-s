tacos = ['pastor', 'cochinita', 'suadero', 'asada', 'bisteck', 'encebollado', 'choriqueso', 'arrachera','de sal'] #sorry, im hungry
#print The first three items in my list are:
print("The first three tacos in my list are:")
for taco in tacos [:3]:
    print (taco.title())
#print Three items from the middle in my list are:
print("Three tacos from the middle in my list are:")
for taco in tacos [3:6]:
    print (taco.title())
#print The last items from my list are:
print("The last tacos from my list are:")
for taco in tacos [6:9]:
    print (taco.title())
