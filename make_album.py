def make_album(artist_name,album_title, track_number = ''):
	"""Return a dictionary of albums"""
	if track_number:
		album = {'Artist Name' : artist_name, 'Album Title' : album_title,
		'Number of Tracks' : track_number}
	else:
		album = {'Artist Name' : artist_name, 'Album Title' : album_title}
	return album

album_1 = make_album('Jurassic 5', 'Power in Numbers', 12)
print(album_1)

album_2 = make_album('Bruce Springsteen', 'Born to Run')
print(album_2)

album_3 = make_album('Photek', 'Modus Operandi')
print(album_3)