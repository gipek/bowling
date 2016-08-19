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

#### Uncle Bob version
# class Game:
#     def __init__(self):
#         self.rolls = []

#     def roll(self, pins):
#         self.rolls.append(pins)

#     def get_score(self):
#         score = 0
#         frame_index = 0
#         for frame in xrange(10):
#             if self.is_strike(frame_index):
#                 score += 10 + self.strike_bonus(frame_index)
#                 frame_index += 1
#             elif self.is_spare(frame_index):
#                 score += 10 + self.spare_bonus(frame_index)
#                 frame_index += 2
#             else:
#                 score += self.sum_of_balls_in_frame(frame_index)
#                 frame_index += 2

#         return score

#     def is_strike(self, frame_index):
#         return self.rolls[frame_index] == 10

#     def sum_of_balls_in_frame(self, frame_index):
#         return self.rolls[frame_index] + self.rolls[frame_index + 1]

#     def spare_bonus(self, frame_index):
#         return self.rolls[frame_index + 2]

#     def strike_bonus(self, frame_index):
#         return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

#     def is_spare(self, frame_index):
#         return self.rolls[frame_index] + self.rolls[frame_index + 1] == 10
