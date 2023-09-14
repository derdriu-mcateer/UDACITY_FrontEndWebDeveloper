#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.my_move = moves
        self.their_move = random.choice(moves)

    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.my_move = my_move


class RockPlayer:
    def move(self):
        return moves[0]

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        human = input("\n Your move - Rock, Paper or Scissors? > ")
        while human.lower() not in moves:
            human = input("Sorry please try again >")
        return human.lower()


class ReflectPlayer(Player):
    def move(self):
        if self.their_move not in moves:
            return (random.choice(moves))
        else:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == "rock":
            return 'paper'
        elif self.my_move == "paper":
            return 'scissors'
        else:
            return 'rock'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f" Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if beats(move1, move2):
            self.p1_score += 1
            result = " YAY YOU WIN"
        elif move1 == move2:
            result = " TIE"
        else:
            self.p2_score += 1
            result = " YOU LOSE"

        print(f"{result}"
              f"\n Player 1 Score ( {self.p1_score} ),",
              f"Player 2 Score ( {self.p2_score} )")

    def play_game(self):
        self.p1_score = 0
        self.p2_score = 0

        print("You're playing Rock, Paper, Scissors - Game start!")

        for round in range(3):
            print(f"\nRound {round+1} of 3 :")
            self.play_round()

        print(f"\n THE FINAL SCORE [ {self.p1_score} ] to [ {self.p2_score} ]")
        if self.p1_score > self.p2_score:
            print(" GREAT JOB YOU WIN")
        elif self.p1_score < self.p2_score:
            print(" SORRY YOU LOSE - BETTER LUCK NEXT TIME")
        else:
            print(" THAT'S A TIE - GOOD GAME")


if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice([CyclePlayer(),
                RandomPlayer(), ReflectPlayer(), RockPlayer()]))
    game.play_game()
