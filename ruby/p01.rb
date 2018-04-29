# frozen_string_literal: true
require_relative 'base'
require 'pry-byebug'

Location = Struct.new(:x, :y) do
  def away
    x.abs + y.abs
  end
  def to_s
    "(#{x}, #{y})"
  end
end

Direction= Struct.new(:x, :y) do
  def to_s
    "(#{x}, #{y})"
  end
end

class Instruction
  attr_reader :turn_direction, :count

  def initialize(instruction)
    instruction.strip!
    @turn_direction = instruction[0].downcase
    @count = instruction[1..-1].to_i
  end

  def turn(o)
    send(turn_direction, o)
  end

  def move(o, location)
    Location.new(location.x + o.x * count,
                 location.y + o.y * count)
  end

  private

  def l(o)
    Direction.new(-1 * o.y,  o.x)
  end

  def r(o)
    Direction.new(o.y, -1 * o.x)
  end
end

class Problem01 < ProblemBase

  def initialize
    @problem = '01'
    @o = Direction.new(0, 1)
    @locations = [] << Location.new(0, 0)
  end

  def run
    data.split(",").map { |step| Instruction.new(step) }.each do |instruction|
      @o = instruction.turn(@o)
      @locations <<  instruction.move(@o, @locations.last)
    end
    puts  "#{@locations.last.away} blocks away at #{@locations.last.to_s}"
  end
end

p = Problem01.new

p.run
