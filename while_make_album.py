def make_album(artist_name,album_title, track_number=''):
	"""Return a dictionary of albums"""
	if track_number:
		album = {'Artist Name' : artist_name, 'Album Title' : album_title,
		'Number of Tracks' : track_number}
	else:
		album = {'Artist Name' : artist_name, 'Album Title' : album_title}
	return album

while True:
	print("\nPlease enter album details")
	print("(enter 'q' at any time to quit)")

	artist = input("Artist name: ")
	if artist == 'q':
		break

	album_name = input("Album name: ")
	if album_name == 'q':
		break

	tracks = input("Number of tracks: ")
	if tracks == 'q':
		break

	album_details = make_album(artist, album_name, tracks)
	print(album_details)