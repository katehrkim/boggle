import random
import string
class BoggleBoard:
  
  def __init__(self):
    self.board = [['_','_','_','_'],['_','_','_','_'],['_','_','_','_'],['_','_','_','_']]
    
  def shake(self):
    for i, list in enumerate(self.board):
      for j, elem in enumerate(list):
        random_letter = random.choice(string.ascii_uppercase)
        if random_letter == 'Q':
          random_letter = 'Qu'
        self.board[i][j] = random_letter

test = BoggleBoard()
print(test.board)
test.shake()
print(test.board)
