import random
import operator

def format(value):
  if value == 0:  return " "
  if value == 1:  return "X"
  if value == 2:  return "O"
  return


def printBoard(state):
  print(" ", format(state[0]), " | ", format(state[1]), " | ", format(state[2]));
  print("-----+-----+-----");
  print(" ", format(state[3]), " | ", format(state[4]), " | ", format(state[5]));
  print("-----+-----+-----");
  print(" ", format(state[6]), " | ", format(state[7]), " | ", format(state[8]));

# given a state, simulate a game, return 0 for draw, 1 for X win, 2 for O win
def simulate(state):
    
  # tempList is a list of 'state' indexes that are 0s
    tempList = [];
    for i in range(len(state)):
        if state[i] == 0:
            tempList.append(i);
    #print("S-tempList: ", tempList);

  # pick a random index and set it to X/O depending on how many 0s there are
    while len(tempList) > 0:
        aaa = random.choice(tempList);
        #print("S-picked ", aaa);


        if (len(tempList) > 0) and (len(tempList) % 2 == 0):
            state[aaa] = 2;
        else:
            state[aaa] = 1;
         
        tempList.remove(aaa);
        #print("S-state ", state);
        if testGameOver(state) == 1:
            #print("1 wins");
            return 1
        elif testGameOver(state) == 2:
            #print("2 wins");
            return 2
        elif testGameOver(state) == 3:
            #print("draw");
            return 3

# given a state, collect data and return the optimal move
def decideMove(state):
    
    # tempList is a list of legal moves
    tempList = [];
    for i in range(len(state)):
        if state[i] == 0:
            tempList.append(i);
    #print("tempList: ", tempList);

    # winList is a list of wins for each move, indexes relative to tempList
    winList = [];
    for k in range(len(tempList)):
        winList.append(0);
    #print("winList:  ", winList);
    #print("");

    # for each legal move
    for j in range(len(tempList)):
        
        #print("choosing position ", tempList[j], " to simulate");
        dummyState = state.copy();

        # simulate X amount of random playouts
        for a in range(5000):
            
            dummyState = state.copy();

            pos = tempList[j];
            
            #print("state: ", state);
            #print("dummyState: ", dummyState);
            #print("");

            dummyState[pos] = 2;
            #print("dummyState going into simulate", dummyState);
            result = simulate(dummyState);
            if result == 2 or result == 3:
                winList[j] += 1;
        
        #print("winList:  ", winList);

    max_index, max_value = max(enumerate(winList), key=operator.itemgetter(1))
    
    return tempList[max_index]

# given a state, returns 1 for X win, 2 for O win, 3 for draw, "not done" for incomplete board
def testGameOver(state):
  status = "not done";

  if (state[0] == state[1] == state[2]) and (state[0] != 0): return state[0];
  elif (state[3] == state[4] == state[5]) and (state[4] != 0): return state[4];
  elif (state[6] == state[7] == state[8]) and (state[6] != 0): return state[6];
  elif (state[0] == state[3] == state[6]) and (state[0] != 0): return state[0];
  elif (state[1] == state[4] == state[7]) and (state[1] != 0): return state[1];
  elif (state[2] == state[5] == state[8]) and (state[2] != 0): return state[2];
  elif (state[0] == state[4] == state[8]) and (state[0] != 0): return state[0];
  elif (state[2] == state[4] == state[6]) and (state[2] != 0): return state[2];
  elif (state[0] != 0) and (state[1] != 0) and (state[2] != 0) and (state[3] != 0) and (state[4] != 0) and (state[5] != 0) and (state[6] != 0) and (state[7] != 0) and (state[8] != 0): return 3;
  return status


def play_a_new_game():
  
  print("");
  print("This is TicTacToe.");
  print("To place your X, enter the number corresponding to the position as shown.");
  print("");

  print("  0  |  1  |  2  ");
  print("-----+-----+-----");
  print("  3  |  4  |  5  ");
  print("-----+-----+-----");
  print("  6  |  7  |  8  ");

  print("");
  print("You go first, you are X, computer is O.");
  print("");
  
  state = [0, 0, 0, 0, 0, 0, 0, 0, 0];
  run = 1;
  printBoard(state);
  

  while run == 1:

    
    # accept user input
    pos = int(input());
    state[pos] = 1;
    printBoard(state)
    print("");

    # check for game over
    if testGameOver(state) == 1:
      run = 0;
      print("");
      print("You win. Congratulations.");
      return
    elif testGameOver(state) == 2:
      run = 0;
      print("");
      print("You lose. Git Gud.");
    elif testGameOver(state) == 3:
      run = 0;
      print("");
      print("Draw.");
      return
    
    # decide what move to execute
    abc = decideMove(state);
    state[abc] = 2;
    printBoard(state)
    print("");

    # check for game over
    if testGameOver(state) == 1:
      run = 0;
      print("");
      print("You win. Congratulations.");
      return
    elif testGameOver(state) == 2:
      run = 0;
      print("");
      print("You lose. Git Gud.");
    elif testGameOver(state) == 3:
      run = 0;
      print("");
      print("Draw.");
      return
  
  return


if __name__ == '__main__':
  play_a_new_game()
