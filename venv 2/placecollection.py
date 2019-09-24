
from place import Place  # import Song class
from operator import attrgetter  # import Attribute Getter


class PlacesList:
    def __init__(self):
        self.list_places = []  # Create a list of places

    def load_places(self, file):

        # To load the places from csv file and append to list_places

        in_file = open("places.csv", "r")  # load places from csv
        lines = in_file.readlines()
        for line in lines:
            place_item = line.split(',')
            place_item[3] = place_item[3].strip('\n')
            loaded_place = Place(place_item[0], place_item[1], place_item[2], place_item[3])

            self.list_places.append(loaded_place)

        in_file.close()  # close the file

    def sort(self, key):
        if key == "visit":
            key = "is_required"
            self.list_places = sorted(self.list_places, key=attrgetter(key, "priority"), reverse=True)
        else:
            self.list_places = sorted(self.list_places, key=attrgetter(key, "priority"))

    def add_to_list(self, name, country, priority, is_required):
        # add the place to the place list
        newPlace = Place(name, country, priority, 'v')
        self.list_places.append(newPlace)

    def save_places(self):
        csv_string = ""
        for each in self.list_places:
            csv_string += "{},{},{},{}\n".format(each.name, each.country, each.priority, each.is_required)
        out_file = open("places.csv", 'w')
        out_file.seek(0)
        out_file.truncate()
        out_file.write(csv_string)
        out_file.close()  # close the file
