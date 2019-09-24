# """
# (incomplete) Tests for SongList class
# """
# from placecollection import PlacesList
# from place import Place
#
# # test empty places_List
# places_list = PlacesList
# print(places_list)
# assert len(places_list.list_places) == 0
#
# # test loading places
# places_list.load_places('places.csv')
# print(places_list)
# assert len(places_list.list_places) > 0  # assuming CSV file is not empty
#
# # TODO: add tests below to show the various required methods work as expected
# # test sorting places
# print("Sorting by Country")
# places_list.sort('Country')
# print("Sorting by name")
# places_list.sort('Place')
# print("Sorting by priority")
# places_list.sort('Priority')
# # test adding a new place
#
# # test get_place()
#
# # test getting the number of required and visited songs (separately)
#
# # test saving places (check CSV file manually to see results)