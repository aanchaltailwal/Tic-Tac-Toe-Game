def printBoard(xState, zState):
    print(f"0 | 1 | 2 ")
    print(f"--|---|---")
    print(f"3 | 4 | 5 ")
    print(f"--|---|---")
    print(f"6 | 7 | 8 ")
    

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0]
    yState = [0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for x and 0 for 0
    print("Welcome to Tic Tac Toe")
    while(True):
        printBoard(xState, zState)
        if(turn == 1):
            print("X's Chance")
            value = int(input("Please enter a value"))
            xState[value] = 1
        else:
            print("X's Chance")
            value = input("Please enter a value")
            zState[value] = 1
        break
