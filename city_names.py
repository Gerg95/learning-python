def get_city_country(city_name, city_country):
	city_details = city_name + ", " + city_country
	return city_details.title()


while True:
	print("\nWhat is the name of the city, and where is it?:")
	print("(enter 'q' at any time to quit)")

	c_name = input("City: ")
	if c_name == 'q':
		break

	country_name = input("Country: ")
	if country_name == 'q':
		break

	formatted_city = get_city_country(c_name, country_name)
	print("\n" + formatted_city)