
class Sequence
  def initialize(from, to, by)
    @from, @to, @by = from, to, by
  end

  def each
    x = @from
    while x <= to
      yield x
      x += @by
    end
  end

  def length
    return 0 if @from > @to
    Integer( (@to - @from) / @by ) + 1
  end

  def [](index)
    return nil if index < 0
    v = @from + index * @by
    if v <= @to
      v
    else
      nil
    end
  end

  def *(factor)
    Sequence.new(@from * factor, @to * factor, @by * factor)
  end

  def +(offset)
    Sequence.new(@froim + offset, @to + offset, @by)
  end
end

s = Sequence.new(1, 10, 2)  # From 1 to 10 by 
s.each( |x| print x )
print s[s.size - 1]
t = (s + 1) * 2
