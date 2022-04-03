from shared_data import SharedData
from raylib import *
from raylib.colors import *
import random
from pages.title_page import TitlePage
from pages.game_end_page import GameEndPage
from pages.round_start_page import RoundStartPage
from pages.scored_page import ScoredPage
from casting.player import Player
from casting.ball import Ball
from directing.director import MovePlayers

class Game():
    
    def __init__(self):
        self._data = SharedData()
        self._last_scored = ""
        self.new_round()
        self._player_mover = MovePlayers()

    def new_round(self):
        """sets up ball for a new round of play"""

        self.ball = Ball()
        self.ball.set_color(GREEN)
        self.ball.set_position(int(self._data.MAX_X / 2), int(self._data.MAX_Y / 2))
        self.ball.set_velocity((random.randint(7, 15) * random.choice([1,-1])), (random.randint(7, 15) * random.choice([1,-1])))
    
    def start(self):

        # The code below initializes game elements (ball, players, pages)
        SetTargetFPS(60)
        InitWindow(self._data.MAX_X, self._data.MAX_Y, self._data.CAPTION.encode())
        self.player1 = Player()
        self.player1.set_position(0, int(self._data.MAX_Y / 2))
        self.player1.set_color(BLUE)
        self.player2 = Player()
        self.player2.set_position(self._data.MAX_X - 20, int(self._data.MAX_Y / 2))
        self.player2.set_color(BLUE)
        self.current_page = "title_page"
        title_page = TitlePage()
        game_end_page = GameEndPage()
        round_start_page = RoundStartPage()
        scored_page = ScoredPage()
        self.new_round()

        # main logic loop
        while not WindowShouldClose():
            HideCursor()
            if (self.current_page == "title_page"):
                title_page.draw()
                if IsKeyPressed(KEY_ENTER):
                    self.current_page = "round_start_page"

            # TODO: clean up round start page
            elif (self.current_page == "round_start_page"):
                round_start_page.draw(self.player1, self.player2, self.ball)
                self._player_mover.move_players(self.player1, self.player2)
                self.ball.move_actor()
                self.ball.check_collisions(self.player1, self.player2)
                (self.current_page, self._last_scored, self.player1, self.player2) = self.ball.check_score(self.player1, self.player2, self.current_page, self._last_scored)

            # TODO: clean up scored page
            elif (self.current_page == "scored_page"):
                self.new_round()
                scored_page.draw(self._last_scored, self.player1, self.player2)
                if IsKeyPressed(KEY_ENTER):
                    self.player1.set_position(0, int(self._data.MAX_Y / 2))
                    self.player2.set_position(self._data.MAX_X - 20, int(self._data.MAX_Y / 2))
                    self.current_page = "round_start_page"

            # TODO: create and implement game end page
            elif (self.current_page == "game_end_page"):
                pass