# frozen_string_literal: true
require_relative 'base'
require 'set'

class Person
  attr_reader :orientation, :position, :walking, :arrived, :visited
  def initialize(walking)
    @orientation = Direction.new(0, 1)
    @position = Location.new(0, 0)
    @visited = Set.new
    @walking = walking
    @arrived = false
  end

  def follow_instruction(instruction)
    turn(instruction.turn_direction)
    if walking
      walk(instruction.count)
    else
      move(instruction.count)
    end
  end

  def move(count)
    (1..count).each do |_|
      @position = Location.new(position.x + orientation.x,
                               position.y + orientation.y)
      if walking?
        if @visited.include? @position.to_s
          @arrived = true
          return
        else
          @visited << @position.to_s
        end
      end
    end
  end


  def turn(direction)
    send(direction)
  end

  def arrived?
    !!@arrived
  end

  def walking?
    !!@walking
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

  def initialize(filename)
    super(filename)
    @problem = '01'
  end

  def run_phase_1
    run(false)
  end

  def run_phase_2
    run(true)
  end

  def run(walking)
    person = Person.new(walking)

    data.split(",").map { |step| Instruction.new(step) }.each do |instruction|
      person.follow_instruction(instruction)
      break if person.arrived?
    end
    "#{person.position.away} blocks away at #{person.position.to_s}"
  end
end

def get_problem_solver(filename)
  Problem01.new(filename)
end
