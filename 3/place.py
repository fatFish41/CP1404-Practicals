"""
ADD YOUR OWN COMMENTS HERE.
"""
class Place:
    def __init__(self, place, country, priority, status):
        self.place = place
        self.country = country
        self.priority = priority
        self.status = status

    def mark_song(self, status):
        self.status = status

    def __str__(self):
        return "{} in {}, priority {}, {}".format(self.place, self.country, self.priority, self.status)