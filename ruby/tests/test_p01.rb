require_relative "../lib/p01.rb"
require "minitest"
require 'minitest/autorun'

class TestProblem01 < MiniTest::Test

  def test_turning
    p = Person.new(false)

    north = Direction.new(0, 1)
    south = Direction.new(0, -1)
    east = Direction.new(1, 0)
    west = Direction.new(-1, 0)

    assert_equal north, p.orientation
    p.turn('l')
    assert_equal west, p.orientation
    p.turn('l')
    assert_equal south, p.orientation
    p.turn('l')
    assert_equal east, p.orientation

    p.turn('r')
    assert_equal south, p.orientation
    p.turn('r')
    assert_equal west, p.orientation
    p.turn('r')
    assert_equal north, p.orientation
  end

  def test_moving
    p = Person.new(false)
    assert_equal  Location.new(0, 0), p.position
    p.move(10)
    assert_equal Location.new(0, 10), p.position
    p.turn('l')
    p.turn('l')
    p.move(10)
    assert_equal Location.new(0, 0), p.position
  end

  def test_walking
    p = Person.new(true)
    assert_equal Location.new(0, 0), p.position
    p.move(10)
    assert_equal Location.new(0, 10), p.position
    p.turn('l')
    p.turn('l')
    p.move(10)
    assert_equal Location.new(0, 9), p.position
    assert p.arrived
  end

  def test_visited
    p = Person.new(true)
    assert_equal Location.new(0, 0), p.position
    p.move(10)
    assert_equal 10, p.visited.count

  end
end
