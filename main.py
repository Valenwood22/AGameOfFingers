import random

class A_Game_Of_Fingers:
    def __init__(self):
        self.board = {'p1':[1,1], 'p2':[1,1]}
        self.run()



    def run(self):
        while True:
            self.printBoard()
            v = input("Enter a new Value: ")
            while self.check(v, 'p1', 'p2'):
                print("Invalid Value")
                v = input("Enter a new Value: ")
            self.updateBoard(v, 'p1', 'p2')
            if self.checkForWin('p2'):
                print("Player 1 Wins")
                break

            self.printBoard()
            v = self.getP2Turn()
            print(f"Opponent played {v}")
            self.updateBoard(v, 'p2', 'p1')
            if self.checkForWin('p1'):
                print("Player 1 Wins")
                break



    def getP2Turn(self):
        ans = ""
        if self.board['p2'][0] == 'X':
            ans += 'R'
        elif self.board['p2'][1] == 'X':
            ans += 'L'
        else:
            if random.randint(0,1) == 0: ans += 'L'
            else: ans += 'R'

        if self.board['p1'][0] == 'X':
            ans += 'R'
        elif self.board['p1'][1] == 'X':
            ans += 'L'
        else:
            if random.randint(0,1) == 0: ans += 'L'
            else: ans += 'R'

        return ans



    def updateBoard(self, v, send, rec):

        if v == 'S':
            if self.board[send][0] == 'X':
                temp = self.board[send][1]
                self.board[send] = [temp//2, temp//2]
            else:
                temp = self.board[send][0]
                self.board[send] = [temp//2, temp//2]

        elif v[0] == 'L' and v[1] == 'L':
            self.board[rec][0] += self.board[send][0]
            if self.board[rec][0] > 5: self.board[rec][0] = 'X'

        elif v[0] == 'L' and v[1] == 'R':
            self.board[rec][1] += self.board[send][0]
            if self.board[rec][1] > 5: self.board[rec][1] = 'X'

        elif v[0] == 'R' and v[1] == 'L':
            self.board[rec][0] += self.board[send][1]
            if self.board[rec][0] > 5: self.board[rec][0] = 'X'

        elif v[0] == 'R' and v[1] == 'R':
            self.board[rec][1] += self.board[send][1]
            if self.board[rec][1] > 5: self.board[rec][1] = 'X'



    def printBoard(self):
        print(f"Your hand {self.board['p1']} their hand {self.board['p2']}" )



    def check(self, v, send, rec):
        def illeagalX(board, send, rec, s1, s2):
            if s1 == 'L': s1 = 0
            else: s1 = 1
            if s2 == 'L': s2 = 0
            else: s2 = 1

            if board[send][s1] == 'X':
                return True
            elif board[rec][s2] == 'X':
                return True
            else:
                return False

        def validSplit(board):
            if board[send][0] == 'X' and (board[send][1] == 2 or board[send][1] == 4):
                return False
            elif board[send][1] == 'X' and (board[send][0] == 2 or board[send][0] == 4):
                return False
            else:
                return True

        if v == 'S':
            return validSplit(self.board)
        elif len(v) != 2:
            return True
        elif v[0] != 'R' and v[0] != 'L':
            return True
        elif v[1] != 'R' and v[1] != 'L':
            return True
        elif illeagalX(self.board, send, rec, v[0], v[1]):
            return True
        else:
            return False



    def checkForWin(self, p):
        return self.board[p][0] == 'X' and self.board[p][1] == 'X'



if __name__ == '__main__':
    # Run
    g = A_Game_Of_Fingers()

