"""
Basic Kivy test code
If this works, it will produce a GUI window with "hello world" in the middle
and you know you have set everything up correctly.
It also prints the Python version in the run output (may be mixed in with Kivy output)
The Python version should be 3.x (not 2.x).
"""

"""(Incomplete) Tests for Song class."""
from place import Place

def run_tests():
   """test empty song (defaults)"""
   place = Place()
   print(place)
   assert place.name == ""
   assert place.country == ""
   assert place.priority == 0

# test initial place
   place2 = Place("Roma", "Italy", 12, True)
   print(place2)
   assert place2.visited
# TODO: write tests to show this initialisation works

# test mark_visited()
   place2.mark_visited()
   print(place2)
   assert place2.visited

run_tests()
# TODO: write tests to show the mark_learned() method works