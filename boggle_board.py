import random
import string
class BoggleBoard:
  
  def __init__(self):
    self.board = [
      ['_','_','_','_'],
      ['_','_','_','_'],
      ['_','_','_','_'],
      ['_','_','_','_']]
    self.dice = [
      'AAEEGN',
      'ELRTTY',
      'AOOTTW',
      'ABBJOO',
      'EHRTVW',
      'CIMOTU',
      'DISTTY',
      'EIOSST',
      'DELRVY',
      'ACHOPS',
      'HIMNQU',
      'EEINSU',
      'EEGHNW',
      'AFFKPS',
      'HLNNRZ',
      'DEILRX'
    ]
    
  def shake(self):
    random.shuffle(self.dice)
    for i, list in enumerate(self.board):
      for j, elem in enumerate(list):
        # random_letter = random.choice(string.ascii_uppercase)
        random_index = random.randint(0,5)
        random_letter = self.dice[i][random_index]
        if random_letter == 'Q':
          random_letter = 'Qu'
        self.board[i][j] = random_letter

test = BoggleBoard()
print(test.board)
test.shake()
print(test.board)
