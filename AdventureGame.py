import random
import os

class Player:
    
    score = 0
    sword = 0
    potion = 0
    isAlive = True

    def __init__(self):
        self.score = 0
        self.sword = 0
        self.potion = 0
        self.isAlive = True

class Game:
    col = 0
    rowNumber = 0
    treasures = 0
    monster = 0
    sword = 0
    potion = 0
    venom = 0
    rowsStarter = []
    rowsPlayer = []
    rowStart = 0
    columnStart = 0
    currentRow = 0
    currentColumn = 0
    
    def __init__(self, col, rowNumber, treasures, monster, sword, potion, venom):
        self.col = col
        self.rowNumber = rowNumber
        self.treasures = treasures
        self.monster = monster
        self.sword = sword
        self.potion = potion
        self.venom = venom
        self.rowsPlayer = []
        self.rowsStarter = []
        self.rowStart = 0
        self.columnStart = 0
        self.currentRow = 0
        self.currentColumn = 0
    
    def rowGenerator(self):
        rows = []
        for i in range(0,self.rowNumber):
            row = []
            for x in range (0, self.col): 
                row.append(" ")
            rows.append(row)
        return rows

    
    def start(self):
        
        self.rowsStarter = self.rowGenerator()
        self.rowsPlayer = self.rowGenerator()
     
        t = 0
        m = 0
        s = 0
        p = 0
        v = 0
        isEmpty = True

        while t != self.treasures:
             row = random.randint(0,5)
             column = random.randint(0,6)
             if self.rowsStarter[row][column] == " ":
                 self.rowsStarter[row][column] = 'T'
                 t += 1
        while m != self.monster:
             row = random.randint(0,5)
             column = random.randint(0,6)
             if self.rowsStarter[row][column] == " ":
                 self.rowsStarter[row][column] = 'M'
                 m += 1
        while s != self.sword:
             row = random.randint(0,5)
             column = random.randint(0,6)
             if self.rowsStarter[row][column] == " ":
                 self.rowsStarter[row][column] = 'S'
                 s += 1
        while p != self.potion:
             row = random.randint(0,5)
             column = random.randint(0,6)
             if self.rowsStarter[row][column] == " ":
                 self.rowsStarter[row][column] = 'P'
                 p += 1
        while v != self.venom:
             row = random.randint(0,5)
             column = random.randint(0,6)
             if self.rowsStarter[row][column] == " ":
                 self.rowsStarter[row][column] = 'V'
                 v += 1
    
        while isEmpty == True:
            self.rowStart = random.randint(0,5)
            self.columnStart = random.randint(0,6)
            if self.rowsStarter[self.rowStart][self.columnStart] == " ":
                self.rowsStarter[self.rowStart][self.columnStart] = 'E' 
                self.rowsPlayer[self.rowStart][self.columnStart] = 'E' 
                isEmpty = False
    

    def game(self, user):
        self.currentRow = self.rowStart
        self.currentColumn = self.columnStart
        
        while user.isAlive:
            #os.system('clear')

            for x in range (0, self.rowNumber): 
                print(self.rowsStarter[x])
            print("\n")
            for x in range (0, self.rowNumber): 
                print(self.rowsPlayer[x])

            choise = input("Press L, R, U, D, to move: ")
            if choise == "L" or choise == "l":
                if self.currentColumn != 0:
                    self.currentColumn -= 1
            if choise == "R" or choise == "r":
                if self.currentColumn != self.col-1:
                    self.currentColumn += 1
            if choise == "U" or choise == "u":
                if self.currentRow != 0:
                    self.currentRow -= 1
            if choise == "D" or choise == "d":
                if self.currentRow != self.rowNumber-1:
                    self.currentRow += 1

            
            


def main():
    user = Player()
    game = Game(7,6,5,5,2,3,3)
    game.start()
    game.game(user)

main()










