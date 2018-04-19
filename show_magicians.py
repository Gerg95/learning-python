def show_magicians(name):
	print("These are the magicians:")
	for name in magicians:
	
		print(name.title())


def make_great(name):
	for name in magicians:
		name = name + " the Great"

magicians = ['gandalf', 'harry potter', 'dumbledore']

show_magicians(magicians)

make_great(magicians)

print(magicians)
