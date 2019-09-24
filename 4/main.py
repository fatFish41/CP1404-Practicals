"""
Name:
Date:
Brief Project Description:
GitHub URL:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from places_list import PlacesList


class TravelTracker(App):

    def __init__(self):
        super().__init__()
        self.places_list = PlacesList()
        self.sort_label = Label(text="Sort by:")
        self.spinner = Spinner(text="Place", values=("Place", "Country", "Priority", "Visited"))
        self.add_label = Label(text="Add New Place:")
        self.name_label = Label(text="Name: ")
        self.name_input = TextInput(write_tab=False, multiline=False)
        self.country_label = Label(text="Country: ")
        self.country_input = TextInput(write_tab=False, multiline=False)
        self.priority_label = Label(text="Priority: ")
        self.priority_input = TextInput(write_tab=False, multiline=False)
        self.add_button = Button(text="Add place")
        self.top_label = Label(id="count_place_label")
        self.clear_button = Button(text="Clear Fields")

    def build(self):
        self.title = "TravelTracker 2.0 by Tu Weilun"
        self.root = Builder.load_file('app.kv')
        self.places_list.load_places()
        self.build_widgets_left_col()
        self.build_widgets_right_col()
        return self.root

    def build_widgets_left_col(self):
        self.root.ids.right_layout.add_widget(self.sort_label)
        self.root.ids.right_layout.add_widget(self.spinner)
        self.root.ids.right_layout.add_widget(self.add_label)
        self.root.ids.right_layout.add_widget(self.name_label)
        self.root.ids.right_layout.add_widget(self.name_input)
        self.root.ids.right_layout.add_widget(self.country_label)
        self.root.ids.right_layout.add_widget(self.country_input)
        self.root.ids.right_layout.add_widget(self.priority_label)
        self.root.ids.right_layout.add_widget(self.priority_input)
        self.root.ids.right_layout.add_widget(self.add_button)
        self.root.ids.right_layout.add_widget(self.clear_button)
        self.root.ids.top_layout.add_widget(self.top_label)

        self.add_button.bind(on_release=self.handle_add_place)
        self.clear_button.bind(on_release=self.clear_fields)
        self.spinner.bind(text=self.places_sort)

    def places_sort(self, *args):
        self.places_list.sort(self.spinner.text)
        self.root.ids.right_layout.clear_widgets()
        self.build_widgets_right_col()

    def handle_add_place(self, *args):
        if str(self.name_input.text).strip() == '' or str(self.country_input.text).strip() == '' or str(
                self.priority_input.text).strip() == '':
            self.root.ids.bottom_layout.text = "Input fields cannot be blank"
        else:
            try:
                if int(self.priority_input.text) < 0:
                    self.root.ids.bottom_layout.text = "Please enter a valid number!"
                else:
                    self.places_list.add_place(self.name_input.text, self.country_input.text, int(self.priority_input.text))
                    self.places_list.sort(self.spinner.text)
                    self.clear_fields()
                    self.root.ids.right_layout.clear_widgets()
                    self.build_widgets_right_col()
            except ValueError:
                self.root.ids.bottom_layout.text = "Please enter a number in the priority field."

    def clear_fields(self, *args):
        self.name_input.text = ""
        self.country_input.text = ""
        self.priority_input.text = ""
        self.root.ids.bottom_layout.text = ""

    def build_widgets_right_col(self):
        self.top_label.text = "To visit: {} places, {} places visited.".format(
            str(self.places_list.get_unvisited_places_count()), self.places_list.get_visited_places_count())
        for place in self.places_list.places_list:
            if place[0].status == "v":
                song_display_button = Button(
                    text="'{}' in  {} ({}) (visited)".format(place[0].place, place[0].country, place[0].priority),
                    id=place[0].place)
                song_display_button.background_color = [88, 89, 88, 0.3]
            else:
                song_display_button = Button(
                    text="'{}' by  {} ({})".format(place[0].place, place[0].country, place[0].priority), id=place[0].place)
                song_display_button.background_color = [88, 88, 0, 0.3]
            song_display_button.bind(on_release=self.do_on_click)
            self.root.ids.right_layout.add_widget(song_display_button)

    def do_on_click(self, button):
        if self.places_list.get_place(button.id).status == 'n':
            self.places_list.get_place(button.id).status = 'v'
            self.root.ids.bottom_layout.text = "You need to visit {}".format(
                str(self.places_list.get_place(button.id).place))

        else:
            self.places_list.get_place(button.id).status = 'n'
            self.root.ids.bottom_layout.text = "You visited {}".format(
                str(self.places_list.get_place(button.id).place))
        self.places_sort()
        self.root.ids.right_layout.clear_widgets()
        self.build_widgets_right_col()


if __name__ == '__main__':
    app = TravelTracker()
    app.run()