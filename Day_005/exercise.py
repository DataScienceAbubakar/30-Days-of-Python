empty_list = list ()
five_items = ['house', 'room', 'parlour', 'plot', 'land']
print (len (five_items))
mixed_data_types = ['Abubakar', 'Sabiu', '29', '1.86m', 'Married', 'BUK']
print (mixed_data_types)
it_companies = ['Facebook','Google', 'IBM', 'Oracle', 'Apple', 'Microsoft']
print (it_companies)
print ('list of companies in the list: ',len(it_companies))
first_company = it_companies [0]
last_company = it_companies [5]
print ('first company is: ', first_company)
print ('last company is: ', last_company)
middle_company = it_companies [3]
print ('middle company is: ', middle_company)
it_companies [1]= 'Space X'
print (it_companies)
it_companies.append ('Lucid')
print (it_companies)
it_companies.insert (2,'BMW')
it_companies [3]= 'Mercedes'
print (it_companies)
print (it_companies.index('BMW'))
it_companies.sort()
print (it_companies)
it_companies.sort (reverse= true)
print (it_companies)

