class Restaurant():
	"""Modelling a restaurant"""

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print("The name of the restaurant is " + self.restaurant_name.title() + ".")
		print("It specialises in " + self.cuisine_type.title() + ".")

	def open_restaurant(self):
		print(self.restaurant_name.title() + " is now open!")


my_restaurant_1 = Restaurant("homeslice", "pizza")
my_restaurant_2 = Restaurant("Franco Manca","sourdough pizza")
my_restaurant_3 = Restaurant("Corner Kitchen", "neapolitan pizza")
my_restaurant_1.describe_restaurant()
my_restaurant_1.open_restaurant()
my_restaurant_2.describe_restaurant()
my_restaurant_2.open_restaurant()
my_restaurant_3.describe_restaurant()
my_restaurant_3.open_restaurant()