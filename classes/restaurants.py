class Restaurant():
	"""Modelling a restaurant"""

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 23456

	def describe_restaurant(self):
		print("\nThe name of the restaurant is " + self.restaurant_name.title() + ".")
		print("It specialises in " + self.cuisine_type.title() + ".")
		print("This restaurant has served " + str(self.number_served) + " customers.")

	def open_restaurant(self):
		print(self.restaurant_name.title() + " is now open!")

	def set_restaurant_served(self, served):
		self.number_served = served

	def increment_number_served(self, people):
		self.number_served += people

class IceCreamStand(Restaurant):
	"""Represents aspects of restaurant specific to Ice Cream Stand"""
	
	def __init__(self, restaurant_name, cuisine_type='ice cream'):
		super().__init__(restaurant_name, cuisine_type)
		self.flavours = []


	def display_flavours(self):
		"""prints the flavours available"""
		print("/nThese are the flvours available:")
		for flavour in self.flavours:
			print("- " + flavour.title())



my_restaurant_1 = IceCreamStand("Gelateria")
my_restaurant_1.flavours = ['vanilla','pistachio','chocolate']

my_restaurant_1.describe_restaurant()
my_restaurant_1.display_flavours()
