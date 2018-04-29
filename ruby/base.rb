# frozen_string_literal: true
class ProblemBase

  def filename
    "p#{@problem}.txt"
  end

  def data
    @data ||= File.open(filename).read
  end

end
