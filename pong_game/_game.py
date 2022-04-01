from shared_data import SharedData
from raylib import *
from raylib.colors import *
import random
import math

class Game():
    
    def __init__(self):
        self._data = SharedData()
    
    def start(self):
        print(f"\nStarting {self._data.CAPTION} v{self._data.get_game_version()}...\n")
        print(f"Current date is: {self._data.date_utils.get_current_date()}.\n")
        print(f"Current local time is: {self._data.date_utils.get_current_time()}.\n")

        # Initialization
        SetTargetFPS(60)
        InitWindow(self._data.MAX_X, self._data.MAX_Y, b'PONG!')


        current_page = "title_page"
        # The code below initializes all game elements (ball, paddle, goal). It is temporarily located in this file, but will be moved to children and called from here.
        
        #temporary creation of players (delete and replace with initialization of two instances of player class positioned as defined below)

        player1_score = 0
        player2_score = 0
        player1_paddle_x = 0
        player1_paddle_y = int(self._data.MAX_Y / 2)
        player2_paddle_x = self._data.MAX_X - 20
        player2_paddle_y = int(self._data.MAX_Y / 2)

        #temporary creation of ball (delete and replace with initialization of ball class)
        ball_x = int(self._data.MAX_X / 2)
        ball_y = int(self._data.MAX_Y / 2)
        ball_x_vel = (random.randint(7, 15) * random.choice([1,-1]))
        ball_y_vel = (random.randint(7, 15) * random.choice([1,-1]))

        # main logic loop
        while not WindowShouldClose():

            # TODO: create movement controller for paddles and ball and move relevant code from below to that file

            # TODO: create screen updater to move elements and move relevant code from below to that file

            # TODO: pretty up game title page
            if (current_page == "title_page"):
                BeginDrawing()
                ClearBackground(BLACK)
                DrawText(b'Welcome to PONG!', int(self._data.MAX_X / 2) - 500, int(self._data.MAX_Y / 2), 100, WHITE)
                DrawText(b'Press ENTER to begin', int(self._data.MAX_X / 2) - 450, int(self._data.MAX_Y / 1.4), 30, WHITE)
                if IsKeyPressed(KEY_ENTER):
                    current_page = "round_start_page"
                EndDrawing()

            # TODO: clean up round start page
            
            elif (current_page == "round_start_page"):
                BeginDrawing()
                ClearBackground(DARKGRAY)

                # TODO: Move this code to the window service file and change the player1, player2 variables to be stored in player_bar class
                DrawRectangle(player1_paddle_x,player1_paddle_y,20,100,BLUE)
                DrawRectangle(player2_paddle_x,player2_paddle_y,20,100,BLUE)
                #DrawRectangle(player1_paddle,BLUE)
                #DrawRectangle(player2_paddle,BLUE)
                DrawCircle(ball_x, ball_y, 30, GREEN)
                EndDrawing()

                #This section of code controls the paddles and should be moved to the keyboard_service file
                if IsKeyDown(KEY_W) and (player1_paddle_y>0):
                    player1_paddle_y -= 15
                    print ("Going Up")
                if IsKeyDown(KEY_S) and (player1_paddle_y<self._data.MAX_Y - 100):
                    player1_paddle_y += 15
                    print ("Going Down")
                if IsKeyDown(KEY_UP) and (player2_paddle_y>0):
                    player2_paddle_y -= 15
                    print ("Going Up")
                if IsKeyDown(KEY_DOWN) and (player2_paddle_y<self._data.MAX_Y - 100):
                    player2_paddle_y += 15
                    print ("Going Down")

                #This section of code moves the ball each frame and should be moved to the window_service file
                ball_x += ball_x_vel
                ball_y += ball_y_vel


                #This section of code checks for and handles collisions with the paddle
                if (math.sqrt((ball_x ** 2) + ((ball_y - player1_paddle_y - 50) ** 2))) < 80:
                    print("Hit player1 paddle")
                    ball_x_vel = abs(ball_x_vel)
                if (math.sqrt(((ball_x - self._data.MAX_X) ** 2) + ((ball_y - player2_paddle_y - 50) ** 2))) < 80:
                    print("Hit player2 paddle")
                    ball_x_vel = - abs(ball_x_vel)

                #This section of code checks for and handles when points are scored
                if ball_x < 35:
                    print ("Player 2 Scored!")
                    player2_score += 1
                    current_page = "scored_page"
                if ball_x > (self._data.MAX_X - 35):
                    print ("Player 1 Scored!")
                    player1_score += 1
                    current_page = "scored_page"
                
                #This section of code checks for and handles collisions with walls
                if (ball_y < 30 or ball_y > self._data.MAX_Y - 30):
                    ball_y_vel *= -1

            # TODO: clean up life lost page
            elif (current_page == "scored_page"):
                BeginDrawing()
                ClearBackground(BLACK)
                DrawText(b'Player 1 Score: ' + (str(player1_score).encode()),20,20,60,WHITE)
                DrawText(b'Player 2 Score: ' + (str(player2_score).encode()),self._data.MAX_X-800,20,60,WHITE)
                DrawText(b'Nice Shot!', int(self._data.MAX_X / 2) - 500, int(self._data.MAX_Y / 2), 100, WHITE)
                DrawText(b'Press ENTER to start next round', int(self._data.MAX_X / 2) - 450, int(self._data.MAX_Y / 1.4), 30, WHITE)
                if IsKeyPressed(KEY_ENTER):
                    #replace this with a call to reinitialize the ball
                    ball_x = int(self._data.MAX_X / 2)
                    ball_y = int(self._data.MAX_Y / 2)
                    ball_x_vel = (random.randint(7, 15) * random.choice([1,-1]))
                    ball_y_vel = (random.choice([1,-1]) * 10)

                    current_page = "round_start_page"
                EndDrawing()

            # TODO: create and implement game end page
            elif (current_page == "game_end_page"):
                pass
