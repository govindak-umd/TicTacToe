import random

print('Welcome to tic-tac-toe')


class TicTacToe(object):
    
    """TicTacToe Class"""

    tictactoe_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    position_played = []
    user_choice = None
    robot_choice = None
    victory_flag = 0

    def __init__(self, count):
        self.count = count

    def draw_position_board(cls):
        tutorial_board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        print(tutorial_board[0:3])
        print(tutorial_board[3:6])
        print(tutorial_board[6:9])

    def draw_board(cls):
        print(cls.tictactoe_board[0:3])
        print(cls.tictactoe_board[3:6])
        print(cls.tictactoe_board[6:9])

    def keep_count(self):
        self.count += 1

    def print_count(self):
        print('Game finished in {} turns'.format(self.count))
        print('\n')

    def ask_choice(cls):
        print('What side are you on "x" or "o" ???')
        cls.user_choice = input()
        if cls.user_choice == 'x':
            cls.robot_choice = 'o'
        elif cls.user_choice == 'o':
            cls.robot_choice = 'x'
        else:
            print('Try again. Thats not a valid input. Enter x or o.')
        print('The user has chosen to be : ', cls.user_choice)
        print('\n')

    def take_input(cls):
        while True:
            print('What position would you like to place the {} ?'.format(
                cls.user_choice))
            user_pos = int(input())
            if user_pos not in cls.position_played:
                print(cls.user_choice, ' at  pos : ', user_pos)
                cls.position_played.append(user_pos)
                cls.tictactoe_board[user_pos] = cls.user_choice
                cls.check_victory()
                break
            else:
                print('Please try another position .... .')

    def robot_plays(cls):
        while True:
            robot_pos = random.randint(0, 8)
            if robot_pos not in cls.position_played:
                cls.position_played.append(robot_pos)
                print('robot is placing {} at : '.format(
                    cls.robot_choice), robot_pos)
                cls.tictactoe_board[robot_pos] = cls.robot_choice
                cls.check_victory()
                break
            else:
                print('The position : ', robot_pos,
                      'was already played, so retrying...')

    def check_victory(cls):

        # case 1 : diagonal checking

        if cls.tictactoe_board[0] == cls.tictactoe_board[4] and cls.tictactoe_board[0] == cls.tictactoe_board[8]:
            if cls.tictactoe_board[0] != 0 and cls.tictactoe_board[4] != 0 and cls.tictactoe_board[8] != 0:
                print(cls.tictactoe_board[0], 'wins!')
                cls.victory_flag = 1
        if cls.tictactoe_board[2] == cls.tictactoe_board[4] and cls.tictactoe_board[2] == cls.tictactoe_board[6]:
            if cls.tictactoe_board[2] != 0 and cls.tictactoe_board[4] != 0 and cls.tictactoe_board[6] != 0:
                print(cls.tictactoe_board[0], 'wins!')
                cls.victory_flag = 1
       
        # case 2: check vertical

        for col in range(0, 3):
            if cls.tictactoe_board[col] == cls.tictactoe_board[col+3] and cls.tictactoe_board[col] == cls.tictactoe_board[col+6]:
                if cls.tictactoe_board[col] != 0 and cls.tictactoe_board[col] != 0 and cls.tictactoe_board[col] != 0:
                    print(cls.tictactoe_board[col], 'wins!')
                    cls.victory_flag = 1

        # case 3: check horizontals

        for row in range(0, 8, 3):
            if cls.tictactoe_board[row] == cls.tictactoe_board[row+1] and cls.tictactoe_board[row] == cls.tictactoe_board[row+2]:
                if cls.tictactoe_board[row] != 0 and cls.tictactoe_board[row] != 0 and cls.tictactoe_board[row] != 0:
                    print(cls.tictactoe_board[row], 'wins!')
                    cls.victory_flag = 1


turns = 0
my_ttt = TicTacToe(turns)
my_ttt.draw_position_board()
my_ttt.ask_choice()
while True:
    my_ttt.take_input()
    my_ttt.draw_board()
    if my_ttt.victory_flag == 1:
        break
    my_ttt.robot_plays()
    my_ttt.draw_board()
    if my_ttt.victory_flag == 1:
        break
