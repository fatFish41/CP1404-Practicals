"""
# Name: TuWeilun
# Date: 24/10/2019
# Brief Project Description:
# GitHub URL:
# """

from kivy.app import App
from kivy.lang import Builder
from placecollection import PlacesList
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from place import Place
from kivy.uix.button import Button

# I create the main program in this file, using the class TravelTracker

class TravelTracker(App):

    text = StringProperty()  # Define first status text
    text2 = StringProperty()  # Define second status text
    current_sort = StringProperty()  # Define current sorting of places_list
    sort_choices = ListProperty()  # Define sorting options of places_list

    def __init__(self, **kwargs):
        super(TravelTracker, self).__init__(**kwargs)
        self.places_list = PlacesList()
        self.sort_choices = ["name", "country", "visit"]
        self.current_sort = self.sort_choices[0]
        self.places_list.load_places("file")

    def build(self):

        # this is to build the Kivy GUI
        self.visit___ = "TravelTracker 2.0 by Tu Weilun"
        self.title = self.visit___
        self.root = Builder.load_file('app.kv')  # Connect to Kivy
        self.create_widgets()  # Create the widgets
        return self.root

    def change_sort(self, sorting_choice):

        self.text = "places have been sorted by: {}".format(sorting_choice)
        self.places_list.sort(sorting_choice)
        self.root.ids.entriesBox.clear_widgets()
        self.create_widgets()
        sort_index = self.sort_choices.index(sorting_choice)
        self.current_sort = self.sort_choices[sort_index]

    def Input_clear(self):

        self.root.ids.place_name.text = ''  # Clear  name input
        self.root.ids.place_country.text = ''  # Clear country input
        self.root.ids.place_priority.text = ''  # Clear priority input

    def create_widgets(self):
        """
        Create widgets that lists the places from the csv file
        """
        self.root.ids.entriesBox.clear_widgets()
        num_place = len(self.places_list.list_places)
        visited_place = 0
        for place in self.places_list.list_places:

            name = place.name
            country = place.country
            priority = place.priority
            visited = place.is_required
            display_text = self.generateDisplayText(name, country, priority,
                                                    visited)
            # display what should be added to the widget

            if visited == "n":

                visited_place += 1
                button_color = self.getColor(visited)
            else:
                button_color = self.getColor(visited)


            temp_button = Button(text=display_text, id=place.name,
                                 background_color=button_color)  # Mark the places which is visited
            temp_button.bind(on_release=self.press_entry)

            self.root.ids.entriesBox.add_widget(temp_button)  # Apply to the Kivy
        self.text = "To visit: {} places, {} places visited.".format(num_place - visited_place, visited_place)


    def generateDisplayText(self, name, country, priority, visited):
        if visited == "n":
            display_text = "{} in {} priority {} (visited)".format(name, country, priority)
        else:
            display_text = "{} in {} priority {} (unvisited)".format(name, country, priority)

        return display_text
      #return the display_text
    def getColor(self, visited):
        if visited == "n":
            button_color = [0, 0.7, 1, 1]
        else:
            button_color = [0, 0.9, 0.3, 1]
        return button_color

      # return the button_color
    def press_entry(self, button):
        buttonText = button.text
        selectedPlace = Place()
        for place in self.places_list.list_places:
            # Loop the places in the placecollection

            placeDisplayText = self.generateDisplayText(place.name, place.country, place.priority, place.is_required)
            # Display the text as formatted in generateDisplayText
            if buttonText == placeDisplayText:
                selectedPlace = place
                print(place.is_required)
                if place.is_required == 'n':
                    selectedPlace.mark_visited()  # Mark the place visited
                elif place.is_required == 'v':
                    selectedPlace.mark_unvisited()
                break


        self.root.ids.entriesBox.clear_widgets()  # Apply to Kivy GUI
        self.create_widgets()

        self.text2 = "You have visited {}".format(selectedPlace.name)  # Display what changed in text 2


    def add_places(self):

        if self.root.ids.place_name.text == "" or self.root.ids.place_country.text == "" or self.root.ids.place_priority.text == "":
            self.root.ids.status2.text = "All fields must be completed"
            return
        try:
            # Define place items inputted
            place_name = str(self.root.ids.place_name.text)
            place_country = str(self.root.ids.place_country.text)
            place_priority = int(self.root.ids.place_priority.text)
            is_required = "v"

            # Add the place inputted to the places_list
            self.places_list.add_to_list(place_name, place_country, place_priority, is_required)
            temp_button = Button(
                text=self.generateDisplayText(place_name, place_country, place_priority, is_required))
            temp_button.bind(on_release=self.press_entry)

            # Format the new place items
            temp_button.background_color = self.getColor(is_required)
            self.root.ids.entriesBox.add_widget(temp_button)
            self.create_widgets()

            # Empty the inputs after adding the place
            self.root.ids.place_name.text = ""
            self.root.ids.place_country.text = ""
            self.root.ids.place_priority.text = ""

        except ValueError:  # Display error when year input is not a number
            self.text2 = "Please enter a valid priority"

    def on_stop(self):  # To stop the GUI and save changes
        self.places_list.save_places()


TravelTracker().run()
#To run the gui system