fruits = ('banana', 'mango', 'orange', 'guava', 'pea')
vegetables = ('lentils', 'salad' 'carrot', 'cabbage')
animal_products = ('beef', 'chicken', 'fish')
print (fruits, vegetables, animal_products)
food_stuff_tp = fruits+vegetables+animal_products
food_stuff2 = list (food_stuff_tp)
print (food_stuff2)
food_stuff2.append ('waakye')
print (food_stuff2)
del food_stuff2 [6]
print (food_stuff2)
del food_stuff2
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print ('Estonia' in nordic_countries)
print ('Iceland' in nordic_countries)