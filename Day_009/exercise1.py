strage = input ("Enter your age: ")
age = int(strage)
remainder= 18-age
if age > 18:
    print ('Congratulations, You can drive')
else: 
    print ('Sorry, you are not old enough to drive, please wait for', remainder, 'years to drive')


your_age= input ('please enter your age: ')
intage = int(your_age)
if intage>29:
    difference = intage - 29
    print ('you are older than me with', difference, 'Years')
else:
    difference= 29-intage
    print ('I am older than you with', difference, 'years')
