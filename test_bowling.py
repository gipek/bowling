import pytest
from bowling import Game

@pytest.fixture
def game():
    return Game()

def roll_many(game, n, pins):
    for i in xrange(n):
        game.roll(pins)

def test_gutter_game(game):
    roll_many(game, 20, 0)

    assert game.get_score() == 0

def test_all_ones(game):
    roll_many(game, 20, 1)

    assert game.get_score() == 20

def test_one_spare(game):
    game.roll(5)
    game.roll(5)
    game.roll(3)
    roll_many(game, 17, 0)

    assert game.get_score() == 16

def test_false_spare(game):
    # If the scores that total to 10 are not in the same frame, it is not a spare.
    game.roll(0)
    game.roll(5)
    game.roll(5)
    game.roll(3)
    roll_many(game, 16, 0)

    assert game.get_score() == 13

def test_one_strike(game):
    game.roll(10)
    game.roll(3)
    game.roll(4)
    roll_many(game, 16, 0)

    assert game.get_score() == 24

def test_gutter_and_ten_means_spare(game):
    game.roll(0)
    game.roll(10)
    game.roll(3)
    game.roll(4)
    roll_many(game, 16, 0)

    assert game.get_score() == 20

def test_strike_followed_by_spare(game):
    game.roll(10)
    game.roll(3)
    game.roll(7)
    game.roll(4)
    game.roll(4)
    roll_many(game, 14, 0)

    assert game.get_score() == 42

def test_strike_followed_by_strike(game):
    game.roll(10)
    game.roll(10)
    game.roll(3)
    game.roll(4)
    roll_many(game, 14, 0)

    assert game.get_score() == 47

def test_spare_followed_by_strike(game):
    game.roll(3)
    game.roll(7)
    game.roll(10)
    game.roll(3)
    game.roll(4)
    roll_many(game, 14, 0)

    assert game.get_score() == 44

def test_last_frame_normal_case(game):
    roll_many(game, 18, 0)
    game.roll(3)
    game.roll(4)

    assert game.get_score() == 7

def test_last_frame_spare(game):
    roll_many(game, 18, 0)
    game.roll(3)
    game.roll(7)
    game.roll(9)

    assert game.get_score() == 19

@pytest.mark.skipif(True, reason='not implemented')
def test_last_frame_strike(game):
    roll_many(game, 18, 0)
    game.roll(10)
    game.roll(3)
    game.roll(4)

    assert game.get_score() == 17

@pytest.mark.skipif(True, reason='not implemented')
def test_last_frame_strike_followed_by_spare(game):
    roll_many(game, 18, 0)
    game.roll(10)
    game.roll(3)
    game.roll(7)

    assert game.get_score() == 20

@pytest.mark.skipif(True, reason='not implemented')
def test_perfect_game(game):
    roll_many(game, 12, 10)

    assert game.get_score() == 300
