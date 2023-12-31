import unittest
from gothonweb.planisphere import *


class TestRoom(unittest.TestCase):
    def test_room(self):
        gold = Room("GoldRoom",
                    """This room has gold in it you can grab. There's a
                    door to the north.""")
        self.assertEqual(gold.name, "GoldRoom")
        self.assertEqual(gold.paths, {})

class TestRoomPaths(unittest.TestCase):
    def test_room_paths(self):
        center = Room("Center", "Test room in the center.")
        north = Room("North", "Test room in the north.")
        south = Room("South", "Test room in the south.")

        center.add_paths({'north': north, 'south': south})
        self.assertEqual(center.go('north'), north)
        self.assertEqual(center.go('south'), south)

class TestMap(unittest.TestCase):
    def test_map(self):
        start = Room("Start", "You can go west and down a hole.")
        west = Room("Trees", "There are trees here, you can go east.")
        down = Room("Dungeon", "It's dark down here, you can go up.")

        start.add_paths({'west': west, 'down': down})
        west.add_paths({'east': start})
        down.add_paths({'up': start})

        self.assertEqual(start.go('west'), west)
        self.assertEqual(start.go('west').go('east'), start)
        self.assertEqual(start.go('down').go('up'), start)

class TestGothonGameMap(unittest.TestCase):
    def test_gothon_game_map(self):
        start_room = load_room(START)
        self.assertEqual(start_room.go('shoot!'), generic_death)
        self.assertEqual(start_room.go('dodge!'), generic_death)

        room = start_room.go('tell a joke')
        self.assertEqual(room, laser_weapon_armory)


if __name__ == "__main__":
    unittest.main()


# ________________________
#barebones unittest:

#import unittest

#class LearnTest(unittest.TestCase):

#    def test_func_1(self):
#        pass

#if __name__ == "__main__":
#    unittest.main()