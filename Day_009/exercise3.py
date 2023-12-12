scores  = int(input('Enter your scores: '))
if scores > 80:
    print ('your grade is A')
elif scores > 70:
    print ('your grade is B')
elif scores > 60:
    print ('your grade is C')
elif scores > 50:
    print ('your grade is D')
elif scores > 40:
    print ('your grade is E')
else:
    print ('You score F, Please study harder')


season = input('Enter Month: ')
if season == 'september' or 'October' or 'november':
    print ('Season is Autumn')
elif season == 'December' or 'January' or 'February':
    print ('Season is Winter')
elif season == 'March' or 'April' or 'May':
    print ('Season is Spring')
elif season == 'August' or 'June' or 'July':
    print ('Season is Summer')
else:
    print('Month not recognized, please check input')


fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input ('Enter fruit name: ')
if new_fruit in fruits:
    print ('Fruits already exist')
else: 
    fruits.append (new_fruit)
    print ('fruit has been added, the new list is:', fruits)

    person={
    'first_name': 'Abubakar',
    'last_name': 'Sabiu',
    'age': 29,
    'country': 'Nigeria',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'bayajidda road',
        'zipcode': '700241'
    }
    }
yeah = print ( 'skills' in person)
if yeah == True:
    print ('user has skill, the middle skill he has is', ['skills'] [2])
else: 
    print ('user has no skill')