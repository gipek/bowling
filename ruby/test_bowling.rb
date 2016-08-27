require_relative './bowling.rb'
require 'test/unit'

class TestGame < Test::Unit::TestCase
  def setup
    @game = Game.new
  end

  def _roll_many(n, pins)
    (0..n).each do |i|
      @game.roll(pins)
    end
  end

  def test_gutter
    _roll_many(20, 0)
    assert_equal(@game.get_score(), 0)
  end

  def test_all_ones
    _roll_many(20, 1)
    assert_equal(@game.get_score(), 20)
  end

  def test_one_spare
    @game.roll(5)
    @game.roll(5)
    @game.roll(3)
    _roll_many(17, 0)

    assert_equal(@game.get_score(), 16)
  end

  def test_false_spare
    # If the scores that total to 10 are not in the same frame, it is not a spare.
    @game.roll(0)
    @game.roll(5)
    @game.roll(5)
    @game.roll(3)
    _roll_many(16, 0)
    assert_equal(@game.get_score(), 13)
  end

  def test_one_strike
    @game.roll(10)
    @game.roll(3)
    @game.roll(4)
    _roll_many(16, 0)

    assert_equal(@game.get_score(), 24)
  end

  def test_gutter_and_ten_means_spare
    @game.roll(0)
    @game.roll(10)
    @game.roll(3)
    @game.roll(4)
    _roll_many(16, 0)

    assert_equal(@game.get_score(), 20)
  end

  def test_strike_followed_by_spare
    @game.roll(10)
    @game.roll(3)
    @game.roll(7)
    @game.roll(4)
    @game.roll(4)
    _roll_many(14, 0)

    assert_equal(@game.get_score(), 42)
  end

  def test_strike_followed_by_strike
    @game.roll(10)
    @game.roll(10)
    @game.roll(3)
    @game.roll(4)
    _roll_many(14, 0)

    assert_equal(@game.get_score(), 47)
  end

  def test_spare_followed_by_strike
    @game.roll(3)
    @game.roll(7)
    @game.roll(10)
    @game.roll(3)
    @game.roll(4)
    _roll_many(14, 0)

    assert_equal(@game.get_score(), 44)
  end

  def test_last_frame_normal_case
    _roll_many(17, 0)
    @game.roll(3)
    @game.roll(4)

    assert_equal(@game.get_score(), 7)
  end

  def test_last_frame_spare
    _roll_many(18, 0)
    @game.roll(3)
    @game.roll(7)
    @game.roll(9)

    assert_equal(@game.get_score(), 19)
  end

  # The following tests are failing...
  #
  def test_last_frame_strike
    _roll_many(18, 0)
    @game.roll(10)
    @game.roll(3)
    @game.roll(4)

    assert_equal(@game.get_score(), 17)
  end

  def test_last_frame_strike_followed_by_spare
    _roll_many(18, 0)
    @game.roll(10)
    @game.roll(3)
    @game.roll(7)

    assert_equal(@game.get_score(), 20)
  end

  def test_perfect_game
    _roll_many(12, 10)

    assert_equal(@game.get_score(), 300)
  end

end
