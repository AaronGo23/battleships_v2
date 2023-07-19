import unittest
from battleship import *




class TestGame(unittest.TestCase):
    #Ce test crée deux instances de la classe `game` et appelle la méthode
    #`check_display_strikes` de `game1` en passant `game2` en paramètre.
    #Ensuite, il vérifie que la propriété `display_strikes` de `game1` a bien été modifiée à `True`.
    def test_check_display_strikes(self):
        game1 = game(1)
        game2 = game(2)
        game1.check_display_strikes(game2)
        self.assertEqual(game1.display_strikes, True)

    #Ce test crée deux instances de la classe `game` et modifie la propriété `hits` de `game2`.
    #Ensuite, il appelle la méthode `get_hits` de `game1` en passant `game2` en paramètre.
    #Enfin, il vérifie que la propriété `opponent_hits` de `game1` est bien égale à la liste des hits de `game2`.
    def test_get_hits(self):
        game1 = game(1)
        game2 = game(2)
        game2.hits = [[0,0], [1,0]]
        game1.get_hits(game2)
        self.assertEqual(game1.opponent_hits, [[0,0], [1,0]])

    