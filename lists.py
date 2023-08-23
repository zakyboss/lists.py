fruits=["Oranges","Bananas","Mangoes","Pineapple","Guava","Blueberries","Strawberries"]
#To access a single item from list we use indexing
#e.g to Access Guavas we Use starting index which is the one behind it against index of one in front
#i.e [0:]
print(fruits[4:5])
# To print a number of Items we Use indexing Also for example
cars=["Toyota","Benz","Ferari","Bugatti","Tesla"]
#To get from Ferarri to end we use index before ferari and index of last
print(cars[2:6])
# Or you could just mention the First Index to mention where you want to start and leave the against index empty
#i.e [3:]
print(cars[2:])
#To get An Item one could also decide to use the -negative value incase the list itself is long
#for Example
Foods=["Pizza","Chips","Chicken","Lemonfle","Ribs","Black forest"]
#in this Scenario To get Black forest one could just use -1, and so on
print(Foods[-3:])