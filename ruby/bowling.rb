class Game

  def initialize
    @rolls = []
  end

  def roll(n)
    @rolls << n
  end

  def get_score()
    if @score != 0
      @score = 0
    end

    mid_frame = false
    is_strike = false

    @rolls.each_index do |i|
      roll = @rolls[i]

      if roll == 10 or mid_frame
        if is_strike
          if mid_frame
            @score += roll + @rolls[i-1]
          else
            if i < @rolls.count - 1
              @score += roll + @rolls[i+1]
            end
          end
          is_strike = false
        end

        if roll == 10 and not mid_frame
            @score += roll
            is_strike = true
        else
          if roll + @rolls[i-1] == 10 and mid_frame and i < @rolls.count - 1
            @score += @rolls[i+1]
          end

          @score += roll + @rolls[i-1]
        end
        mid_frame = false
      else
        mid_frame = true
      end

    end

    return @score
  end
end
