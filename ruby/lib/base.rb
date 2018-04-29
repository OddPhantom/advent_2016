# frozen_string_literal: true
class ProblemBase
  attr_reader :filename

  def initialize(filename)
    @filename = filename
  end

  def data
    @data ||= File.open(filename).read
  end
end
