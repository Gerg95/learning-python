def make_sandwich(*fillings):
	print("Making a sandwich with the following fillings:")
	for filling in fillings:
		print("-" + filling)

make_sandwich('onion','cheese','ham','salad')
make_sandwich('cheddar')