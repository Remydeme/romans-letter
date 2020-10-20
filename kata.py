import random


def Score(list_of_scores):
    total_score = 0
    list_size = len(list_of_scores)

    for turn, score in enumerate(list_of_scores):
        if "/" in score:
            total_score += 10
            if turn - 1 >= 0 and ("/" in list_of_scores[turn - 1]):
                total_score += int(score[0])
            if turn - 1 >= 0 and ("X" in list_of_scores[turn - 1]):
                total_score += 10
        elif score == "X":
            total_score += 10
            if turn - 1 >= 0 and ("/" in list_of_scores[turn - 1]):
                total_score += 10
            if turn - 1 >= 0 and ("X" in list_of_scores[turn - 1]):
                total_score += 10
        else:
            if score[1] != "-":
                total_score += int(score[1])
                if turn - 1 >= 0 and ("X" in list_of_scores[turn - 1]):
                    total_score += int(score[1])

            if score[0] != "-":
                total_score += int(score[0])
                if turn - 1 >= 0 and ("/" in list_of_scores[turn - 1]):
                    total_score += int(score[0])
                if turn - 1 >= 0 and ("X" in list_of_scores[turn - 1]):
                    total_score += int(score[0])
    return total_score


class Player:

    def __init__(self, name):
        self.name = name
        self._launch_counter = 0
        self._previous_score = 0
        self.score_dico = {0: "-", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "X"}

    def play(self):
        self._previous_score = 0
        score = ""
        for _ in range(0, 2):
            if self._launch_counter == 0:
                index = random.randint(0, 10)
                if index == 10:
                    score = self.score_dico[index]
                    break
                else:
                    score = self.score_dico[index]
                self._launch_counter += 1
                self._previous_score = index
            else:
                index = random.randint(0, 10 - self._previous_score)
                if self._previous_score + index == 10:
                    score += "/"
                else:
                    score += self.score_dico[index]
                self._launch_counter = 0
        return score

    def have_made_a_strike(self):
        return self._previous_score == "X"


class Game:

    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.scores_one = []
        self.scores_two = []

    def play(self):
        player_turn = 0
        while player_turn < 20:
            if player_turn % 2 == 0:
                score = self.player_one.play()
                self.scores_one.append(score)
            else:
                score = self.player_two.play()
                self.scores_two.append(score)
            player_turn += 1

    def who_is_winner(self):
        player_one_score = Score(list_of_scores=self.scores_one)
        player_two_score = Score(list_of_scores=self.scores_two)
        if player_one_score > player_two_score:
            # print(f"Player {self.player_one.name} won with {player_one_score} points")
            return 1
        elif player_one_score < player_two_score:
            # print(f"Player {self.player_two.name} won with {player_two_score} points")
            return 2
        else:
            print(f" Equal game ")
            return 0

    def pretty_printer(self):
        print("_____________ Player 1 _________________")
        print(self.scores_one)
        print("_____________ Player 2 _________________")
        print(self.scores_two)


if __name__ == "__main__":
    p1 = Player(name="dede")
    p2 = Player(name="dodo")
    game = Game(player_one=p1, player_two=p2)
    game.play()
    game.pretty_printer()
    game.who_is_winner()
