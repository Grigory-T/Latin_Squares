# python 3.8.8
# jupyter notebook
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

from IPython.display import clear_output
from copy import deepcopy
from numpy.random import choice, default_rng; rng = default_rng(42)
from numpy import zeros
from time import sleep

def game_of_life(size, limit, sleep_time):
    # generate random initial field with 1 and 0 (1 alive *, 0 dead ' ')
    arr = zeros((size, size))
    arr[1 : size - 1, 1 : size - 1] = choice([1, 0], size=(size - 2, size - 2))
    cur_state = list(map(list, arr))  

    prev_state = None  # technical assignment. for first loop
    for _ in range(limit):
        fut_state = deepcopy(cur_state)  # initialize future state of field

        # update future state based on current state
        for x in range(1, size - 1):  # do not take edges of field
            for y in range(1, size - 1):  # do not take edges of field
                # calculate nearby alive cells for each cell in the field
                result = sum([cur_state[x-1][y-1], cur_state[x-1][y  ], cur_state[x-1][y+1],
                              cur_state[x  ][y-1],                      cur_state[x  ][y+1],
                              cur_state[x+1][y-1], cur_state[x+1][y  ], cur_state[x+1][y+1],])

                if cur_state[x][y] == 1: # cell was alive    
                    if result <= 1:      # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                        fut_state[x][y] = 0
                    elif result <= 3:    # Any live cell with two or three live neighbours lives on to the next generation.    
                        pass
                    else:                # Any live cell with more than three live neighbours dies, as if by overpopulation.
                        fut_state[x][y] = 0

                else:                    # cell was dead    
                    if result == 3:      # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                        fut_state[x][y] = 1

        if fut_state == cur_state:
            print('not moving')
            break
        elif fut_state == prev_state:
            print('inf loop')
            break

        prev_state, cur_state = cur_state, fut_state
        clear_output(wait=True)
        sleep(sleep_time)
        
        print('\n'.join(
                            [''.join(['*' if el == 1 else ' ' for el in row]) 
                                                                            for row in cur_state]
                        )
             )
    else:
        print('limit of iterations')

        
if __name__ == '__main__':
    size = 40  # size of the field
    limit = 300 # number of iterations
    sleep_time = 0.005  # sleep between iterations
    game_of_life(size, limit, sleep_time)
