def solve(board):
    '''
    Parameters:
        board: board to be solved
    '''
    # Find next value to solve for
    if not find_next_open(board):
        return True
    row, column = find_next_open(board)

    # Try values 1-9
    for i in range(1, 10):
        # Check whether value is valid
        if is_valid(row, column, board, i):
            # Adds value to the board
            board[row][column] = i

            # Recursive algorithm for backtracking
            solved = solve(board)
            # Returns the correct board
            if solved:
                return True
            
            board[row][column] = 0
    
    return False

def is_valid(row, column, board, value):
    '''
    Parameters:
        row: the row in which the value is located on the board
        column: the column in which the value is located on the board
        board: board to be solved
        value: number to be verified as valid or invalid
    '''
    for i in range(len(board[row])):
        if i != column and board[row][i] == value:
            return False

    column_values = []
    for i in range(len(board)):
        column_values.append(board[i][column])

    for i in range(len(column_values)):
        if i != row and column_values[i] == value:
            return False
    
    box_row = row // 3
    box_column = column // 3

    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_column * 3, box_column * 3 + 3):
            if i != row and j != column and board[i][j] == value:
                return False
    
    return True

def find_next_open(board):
    '''
    Parameters:
        board: board to be solved
    '''
    # Gets the row 
    for row in range(len(board)):
        row_position = board[row]
        for column in range(len(row_position)):
            if board[row][column] == 0:
                return row, column
    
    return False

def print_board(board):
    '''
    Parameters:
        board: board to be solved
    '''
    # Board should look like:
    # 3 4 5 | 6 7 8 | 9 1 2
    # 4 5 6 | 7 8 9 | 1 2 3
    # 5 6 7 | 8 9 1 | 2 3 4
    # - - - + - - - + - - -
    # 6 7 8 | 9 1 2 | 3 4 5
    # 7 8 9 | 1 2 3 | 4 5 6
    # 8 9 1 | 2 3 4 | 5 6 7
    # - - - + - - - + - - -
    # 9 1 2 | 3 4 5 | 6 7 8
    # 1 2 3 | 4 5 6 | 7 8 9
    # 2 3 4 | 5 6 7 | 8 9 1
    row_div = 0
    column_div = 0
    print_list = []
    print_string = ''
    for row_index in range(len(board)):
        if row_div == 3 or row_div == 6:
            print('- - - + - - - + - - -')
        row_div += 1
        row = board[row_index]
        for column_index in range(len(row)):
            if column_div == 3 or column_div == 6:
                print_list.append('| ')
            column_div += 1
            print_list.append(f'{row[column_index]} ')
        column_div = 0
        for i in print_list:
            print_string = print_string + i
        print(print_string)
        print_list.clear()
        print_string = ''

def main():
    run = True
    while run:
        board = []
        sample_board = input('Do you want to use the sample board, or input your own?(sb/io): ')
        if sample_board == 'io':
            for i in range(9):
                line = input('Please write the next line of your sudoku board. Don\'t include spaces, and use "0" to indicate an empty square: ')
                line_map = map(int, line)
                line_list = list(line_map)
                board.append(line_list)
            print_board(board)
            right_board = input('Is the board correct?(y/n) ')
            if right_board == 'n':
                continue
        else:
            board = [[4, 3, 8, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 7],
                [0, 0, 5, 0, 0, 0, 0, 2, 1],
                [0, 0, 0, 8, 3, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 3, 0],
                [5, 0, 0, 4, 0, 0, 0, 8, 0],
                [0, 0, 0, 0, 0, 2, 6, 0, 9],
                [0, 4, 0, 0, 0, 5, 0, 0, 0],
                [6, 0, 0, 0, 1, 0, 0, 0, 0]]
            print_board(board)
        solve(board)
        print('_______________________________\n')
        print_board(board)
        keep_running = input('Press enter to input a new board, or write "q" to quit.\n')
        if keep_running == 'q':
            break
        
if __name__ == "__main__":
    main()