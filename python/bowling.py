class Game:
    score = 0

    def __init__(self):
        self.rolls = []

    def roll(self, n):
        self.rolls.append(n)

    def get_score(self):
        if self.score != 0:
            self.score = 0

        mid_frame = False
        is_strike = False
        for i in xrange(len(self.rolls)):
            if self.rolls[i] == 10 or mid_frame:
                if is_strike:
                    if mid_frame:
                        self.score += self.rolls[i] + self.rolls[i-1]
                    else:
                        if i != len(self.rolls) - 1:
                            self.score += self.rolls[i] + self.rolls[i+1]
                    is_strike = False

                if self.rolls[i] == 10 and not mid_frame:
                    self.score += self.rolls[i]
                    is_strike = True
                else:
                    if (self.rolls[i-1] + self.rolls[i] == 10) and mid_frame:
                        if i != len(self.rolls) - 1:
                            self.score += self.rolls[i + 1]
                    self.score += self.rolls[i] + self.rolls[i-1]
                    if mid_frame:
                        mid_frame = False
            else:
                mid_frame = True

        return self.score
