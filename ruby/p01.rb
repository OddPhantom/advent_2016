# frozen_string_literal: true
require_relative 'base'
require 'pry-byebug'

class Person
  attr_reader :orientation, :position
  def initialize()
    @orientation = Direction.new(0, 1)
    @position = Location.new(0, 0)
  end

  def follow_instruction(instruction)
    turn(instruction.turn_direction)
    move(instruction.count)
  end

  def move(count)
    @position = Location.new(position.x + orientation.x * count,
                             position.y + orientation.y * count)
  end

  def turn(direction)
    send(direction)
  end

  private

  def l
    @orientation = Direction.new(-1 * orientation.y,  orientation.x)
  end

  def r
    @orientation = Direction.new(orientation.y, -1 * orientation.x)
  end
end

Direction= Struct.new(:x, :y) do
  def to_s
    "(#{x}, #{y})"
  end
end

Location = Struct.new(:x, :y) do
  def away
    x.abs + y.abs
  end
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
end

class Problem01 < ProblemBase

  def initialize
    @problem = '01'
    @person = Person.new
  end

  def run
    data.split(",").map { |step| Instruction.new(step) }.each do |instruction|
      @person.follow_instruction(instruction)
    end
    puts  "#{@person.position.away} blocks away at #{@person.position.to_s}"
  end
end

p = Problem01.new

p.run
