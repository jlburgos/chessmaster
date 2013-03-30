#!/usr/bin/python

##################################################
# Imports

import pgn_parser as pgn

##################################################
# Tester


def print_test(filename):
  pgn_text = open(filename).read()
  pgn_game = pgn.PGNGame()

  print pgn.loads(pgn_text) # Returns a list of PGNGame
  print '\n'
  print pgn.dumps(pgn_game) # Returns a string with a pgn game
  print '\n'
  print pgn_game.moves
  print '\n'

##################################################
# Main

print_test('example.pgn')
