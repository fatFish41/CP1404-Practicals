"""
ADD YOUR OWN COMMENTS HERE.
"""

class Place:

    def __init__(self, name="", country="", priority=0, is_required=""):
        self.name = name
        self.country = country
        self.priority = priority
        self.is_required = is_required

    def __str__(self):
        if self.is_required == "n":
            is_required = "visited"
            return ("You need to visit {} )".format(self.name,self.country, self.priority))
        else:
            is_required = "v"
            return ("You visited {}. Great travelling!)".format(self.name,self.country, self.priority))

    def mark_visited(self):
        self.is_required = 'v'
        return self.is_required

    def mark_unvisited(self):
        self.is_required = 'n'
