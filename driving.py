country = input('which country you from: ')
age = input('please enter your age: ')
age = int(age)
if country == 'Tawian':
    if age >= 18:
    	print('you can take a driver\'s license')
    else:
    	print('you cannot take a driver\'s lcense')
elif country == 'America':
	if age >= 16:
		print('you can take a driver\'s license')
	else:
		print('you cannot take a driver\'s lcense')
else:
		print('you only can enter  Tawian/America')
