# tic tac toe
# 1 2 3
# 4 5 6
# 7 8 9
# create board
# display --> board
# global variables 
# --- funnction-----
# play_game()
# display_board()
# handle_turn()
# check_won()
# change_turn()

#--------global variables------

board = [ '-','-','-',
          '-','-','-',
          '-','-','-', 
          ]

# is there any winner
winner = None 

# is game is still on
game_still_going = True

# current player 
current_player = 'x'

#--------main function--------
def play_game():

# to  display the board
  display_board()
 
  while game_still_going:
# handle the turn
    handle_turn(current_player)

# check if any one has won the game
    check_if_won()

    change_player()
  
  if winner == 'x' or winner == 'o':
    print(winner + ' s has won')
  else:
    print(' it was and tie')

def display_board():

  print( board[0] + ' | ' + board[1] + ' | ' + board[2]+ '  1 2 3' )
  print( board[3] + ' | ' + board[4] + ' | ' + board[5]+ '  4 5 6' )
  print( board[6] + ' | ' + board[7] + ' | ' + board[8]+ '  7 8 9' )


def handle_turn(player):
  global current_player 

  print(player + ' s turn' )
  position = input('type the number between 1--9 ')

  valid = False
  if not valid:

    while position not in ['1','2','3','4','5','6','7','8','9']:
      position = input('type the number between 1--9 try again')
    
  position = int(position) - 1

  if board[position] == '-':
    valid = True
  else:
   print('find another place')

  board[position] = current_player
  
  display_board()


def check_if_won():
  check_if_there_is_winner()
  check_there_is_tie()
  


def check_if_there_is_winner():
  global winner

  row_winner = check_row()
  column_winner = check_column()
  diagnol_winner = check_diagnol()

  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagnol_winner:
    winner = diagnol_winner
  else:
    return None

def check_row():
  global game_still_going 

  # if there is any match 
  row1 = board[0] == board[1] == board[2] != '-'
  row2 = board[3] == board[4] == board[5] != '-'
  row3 = board[6] == board[7] == board[8] != '-'

  if row1 or row2 or row3:
    game_still_going = False
  
  if row1:
    return board[0]
  elif row2:
    return board[3]
  elif row3:
    return board[6]


def check_column():
  global game_still_going 

  # if there is any match 
  column1 = board[0] == board[3] == board[6] != '-'
  column2 = board[1] == board[4] == board[7] != '-'
  column3 = board[2] == board[5] == board[8] != '-'

  if column1 or column2 or column3:
    game_still_going = False
  
  if column1:
    return board[0]
  elif column2:
    return board[1]
  elif column3:
    return board[2]



def check_diagnol():
  global game_still_going 

  # if there is any match 
  diagnol1 = board[0] == board[4] == board[8] != '-'
  diagnol2 = board[2] == board[4] == board[6] != '-'
  

  if diagnol1 or diagnol2 :
    game_still_going = False
  
  if diagnol1:
    return board[0]
  elif diagnol2:
    return board[2]
 
 

def check_there_is_tie():
  global game_still_going

  if '-' not in board:
    game_still_going = False
  else:
    return None
    

def change_player():
  global current_player

  if current_player == 'x':
    current_player  = 'o'
  elif current_player == 'o':
    current_player = 'x'


play_game()
