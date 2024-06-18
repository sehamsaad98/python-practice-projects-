#import modules important for the game
import curses
import random

#initialize the screen
screen = curses.initscr()

#hide the mouse cursor
curses.curs_set(0)

#get max screen height and width
screen_height, screen_width = screen.getmaxyx()
window = curses.newwin(screen_height, screen_width, 0, 0)

#allow window to receive input from the keyboard
window.keypad(True)
window.timeout(100)

#set the x , y coordinates of the initial position of snake's head
snake_x = screen_width // 4
snake_y = screen_width // 2

#define the initial position of the snake body
snake = [[snake_y, snake_x], [snake_y, snake_x - 1], [snake_y, snake_x - 2]]

#create the food in the middle of the window
food = [screen_height // 2, screen_width // 2]

#add the food by using pi character from the curses module
window.addch(food[0], food[1], curses.ACS_PI)

#set initial the movement direction to the right
key = curses.KEY_RIGHT

#set the game loop that loops forever until the game ends
while True:

  #set the next key that will be pressed by user
  next_key = window.getch()
  key = key if next_key == -1 else next_key

  if (snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width]
      or snake[0] in snake[1:]):
    quit()

  #set the new position of the snake head based on the direction
  new_head = [snake[0][0], snake[0][1]]

  if key == curses.KEY_DOWN:
    new_head[0] += 1
  if key == curses.KEY_UP:
    new_head[0] -= 1
  if key == curses.KEY_RIGHT:
    new_head[1] += 1
  if key == curses.KEY_LEFT:
    new_head[1] -= 1

  #insert the new head to the first position of snake list
  snake.insert(0, new_head)

  #check if snake ate the food
  if snake[0] == food:
    food = None

    while food is None:
      new_food = [
          random.randint(1, screen_height - 1),
          random.randint(1, screen_width - 1)
      ]
      food = new_food if new_food not in snake else None
    window.addch(food[0], food[1], curses.ACS_PI)

  # remove the tail if the snake didn't eat the food
  else:
    tail = snake.pop()
    window.addch(tail[0], tail[1], ' ')

  window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
