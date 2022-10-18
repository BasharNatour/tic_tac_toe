arr = [[None, None, None], [None, None, None], [None, None, None]]


def display(arr):

    for y in range(len(arr)):

        for x in range(len(arr[y])):
            print("|", end="")

            if (arr[y][x] == None):

                num = y * 3 + (x + 1)

                print(" " + str(num) + " ", end="")
            else:
                print(" " + arr[y][x] + " ", end='')

            if (x == 2):
                print("|", end="")

        print()


def check(arr, current_player):
    '''
    | 0, 0 | 0, 1 | 0, 2 |
    | 1, 0 | 1, 1 | 1, 2 |
    | 2, 0 | 2, 1 | 2, 2 |
    '''

    if (arr[0][0] == arr[1][1] and arr[1][1] == arr[2][2]
            and arr[2][2] == current_player):
        return True
    if (arr[0][2] == arr[1][1] and arr[1][1] == arr[2][0]
            and arr[2][0] == current_player):
        return True

    # Check rows
    for row in arr:
        count = 0
        for cell in row:
            if cell == current_player:
                count += 1
        if count == 3:
            return True

    # Check columns
    for x in range(3):
        count = 0
        for y in range(3):
            # y = 0
            #
            cell = arr[y][x]
            if cell == current_player:
                count += 1
        if count == 3:
            return True


def check_draw(arr):
    count = 0

    for row in arr:
        for cell in row:

            if cell is not None:
                count += 1

    return count == 9


display(arr)
player = "X"

while (True):
    print("Put number to BE " + player)

    u1 = input()

    num = int(u1) - 1
    y = int(num / 3)
    x = num % 3

    if (arr[y][x] is not None):
        print("Can't use this cell")
        continue

    arr[y][x] = player

    display(arr)

    if (check(arr, player)):
        print("Player " + player + " wins!")
        break
    if (check_draw(arr)):
        print("It's a draw")
        break

    player = "O" if player == "X" else "X"
'''
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

| X | 2 | 3 |

| X | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

| X | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
'''
