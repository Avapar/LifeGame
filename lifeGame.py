# defining class Universe for the Universe blueprint
class Universe:
    def __init__(self, size):
        self.size = size

        temp_grid=[]
        for x in range(size):
            temp=[]
            for y in range(size):
                temp.append(0)
            temp_grid.append(temp)

        self.grid = temp_grid

    def get_cell(self, row, col):
        return self.grid[row][col]

    def set_cell(self, row, col, value):
        self.grid[row][col] = value

    def count_neighbors(self, row, col):
        count = 0
        for i in range(max(row - 1, 0), min(row + 2, self.size)):
            for j in range(max(col - 1, 0), min(col + 2, self.size)):
                if i == row and j == col:
                    continue
                count += self.get_cell(i, j)
        return count

    def next_tick(self):
        new_universe = Universe(self.size)
        for x in range(self.size):
            for y in range(self.size):
                neighbors = self.count_neighbors(x, y)
                if self.get_cell(x, y) == 1:
                    if neighbors == 2 or neighbors == 3:
                        new_universe.set_cell(x, y, 1)
                else:
                    if neighbors == 3:
                        new_universe.set_cell(x, y, 1)
        return new_universe

    def output_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 1:
                    print('*', end='')
                else:
                    print('.', end='')
            print()
        print("-------------------------------")



universe = Universe(13) # size 13 chosen for simulation

universe.set_cell(5, 6, 1)
universe.set_cell(6, 7, 1)
universe.set_cell(7, 5, 1)
universe.set_cell(7, 6, 1)
universe.set_cell(7, 7, 1)

# simulating 7 iterations
for _ in range(7):
    universe.output_grid()
    universe = universe.next_tick()
