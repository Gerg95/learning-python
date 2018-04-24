def my_profile(first,last,**my_info):
	profile = {}
	profile['first'] = first
	profile['last'] = last
	for key,value in my_info.items():
		profile[key] = value
	print(my_profile)
	return my_profile

my_profile('Greg','Evans', Location = 'London', Occupation = 'Intern', needs = 'food')
