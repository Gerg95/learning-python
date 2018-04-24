def make_cars(manufacturer_info, model_name, **car_info):
	car = {}
	car['manufacturer_info'] = manufacturer_info
	car['model_name'] = model_name
	for key, value in car_info.items():
		car[key] = value
	print(car)
	return car

