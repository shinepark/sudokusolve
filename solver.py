import copy
import random

class Game:
    def __init__(self, code = None):
        self.__resetGame()


        if code:
            self.code = code

            for row in range(9):
                for col in range(9):
                    self.game[row][col] = int(code[0])
                    code = code[1:]

        else:
            self.code = None

    def resetGame(self):
        self.game = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        return self.game

    def gametoCode(self, input_game = None):
        if input_game:
            _code = ''.join([str(i) for j in input_game for i in j])
            return _code
        else:
            self.code = ''.join([str(i) for j in self.game for i in j])
            return self.code



    def findEmpty(self):
        for row in range(len(self.game)):
            for col in range(len(self.game[0])):
                if self.game[row][col] == 0:
                    return(row, col)

        return False

    def checkSpace(self, num, space):
        if not self.game[space[0]][space[1]] == 0:
            return False

        for col in self.game[space[0]]:
            if col == num:
                return False

        for row in range(len(self.game)):
            if self.game[row][space[1]] == num:
                return False

        _internalBoxRow = space[0]

        _internalBoxCol = space[1]



        for i in range(3):
            for j in range(3):
                if self.game[i + (_internalBoxRow *3)][j + (_internalBoxCol *3)] == num:
                    return False

        return True

    def solver(self):
        _spaces = self.findSpaces()

        if not _spaces:
            return True

        else:
            row,col = _spaces

        for n in range(1, 10):
            if self.checkSpace(n, (row, col)):
                self.game[row][col] = n

                if self.solver():
                    return self.game

                self.game[row][col] = 0


        return False

     def solved(self):
         return self.gametoCode(self.solver())


    def genRandom(self):
        self.resetGame()

        l = list(range(1, 10))
        for row in range(3):
            for col in range(3):
                _num = random.choice(l)
                self.game[row][col] = _num
                l.remove(_num)

        l = list(range(1, 10))
        for row in range(3, 6):
            for col in range(3, 6):
                _num = random.choice(l)
                self.game[row][col] = _num
                l.remove(_num)

        l = list(range(1, 10))
        for row in range(6, 9):
            for col in range(6, 9):
                _num = random.choice(l)
                self.game[row][col] = _num
                l.remove(_num)

        return self.genFinish()

    def genFinish(self):
        for row in range(len(self.game)):
            for col in range(len(self.game[row])):
                if self.game[row][col] == 0:
                    _num = random.randint(1, 9)

                    if self.checkSpace(_num, (row, col)):
                        self.game[row][col] = _num

                        if self.solver():
                            self.genFinish()
                            return self.game

                        self.game[row][col] = 0

        return False

      def SolveNumofSol(self, row, col):
          for n in range(1, 10):
              if self.checkSpace(n, (row, col)):
                  self.game[row][col] = n

              if self.solver():
                  return self.game


              self.game[row][col] = 0

          return False

      def findEmptyforSol(self, game, h):
          k = 1
          for row in range(len(game)):
              for col in range(len(game[row])):
                  if game[row][col] == 0:
                      if k = h:
                          return (row, col)

                       k += 1

           return False

       def findNumofSol(self):
           z = 0
           solns = []

           for row in range(len(self.game)):
               for col in range(len(self.game[row])):
                   if self.game[row][col] == 0:
                       z += 1

            for i in range(1, z + 1):
                copies = copy.deepcopy(self)

                _row, _col = self.findEmptyforSol(copies.game, i)
                copiessol = copies.SolveNumofSol(_row, _col)

                solns.append(self.gametoCode(input_game = copiessol))

            return list(set(solns))


        def makeGame(self, full, difficulty):
            self.game = copy.deepcopy(full)


            if difficulty == 0:
                squareremove = 36
            elif difficulty == 1:
                squareremove = 46
            elif difficulty == 2:
                squareremove = 52
            else:
                return

            counter = 0
            while counter < 4:
                rRow = random.randint(0, 2)
                rCol = random.randint(0, 2)
                if self.game[rRow][rCol] != 0:
                    self.game[rRow][rCol] = 0
                    counter += 1

            counter = 0
            while counter < 4:
                rRow = random.randint(3, 5)
                rCol = random.randint(3, 5)
                if self.game[rRow][rCol] != 0:
                    self.game[rRow][rCol] = 0
                    counter += 1

            counter = 0
            while counter < 4:
                rRow = random.randint(6, 8)
                rCol = random.randint(6, 8)
                if self.game[rRow][rCol] != 0:
                    self.game[rRow][rCol] = 0
                    counter += 1

            squareremove -= 12
            counter = 0

            while counter < squareremove:
                _row = random.randint(0, 8)
                _col = random.randint(0, 8)

                if self.game[_row][_col] != 0:
                    n = self.game[_row][_col]
                    self.game[_row][_col] = 0

                    if len(self.findNumofSol()) != 1:
                        self.game[_row][_col] = n
                        continue

                    counter += 1
            return self.game, full

    def genGame(self, difficulty):
        self.game, solution = self.makeGame(self.genRandom(), difficulty)
        return self.gametoCode(), self.gametoCode(solution)


if name = 'main':
    game = Game()

    gamenum = game.genGame(1)
    print(gamenum[0])
