"""
Tick-Tack-Toe Game inside the Python Console based on a Dictionary as a place where the cells are stored.
"""


class TickTackToe:
    def __init__(self):
        self.cells_value = {
            1: "    ",
            2: "    ",
            3: "    ",
            4: "    ",
            5: "    ",
            6: "    ",
            7: "    ",
            8: "    ",
            9: "    "
        }

        self.game_map = ""
        self.player = None

    def drawing_game_map(self):
        """ Method to draw the game map. """

        self.game_map = ""

        for cel_num in range(9, 0, -3):
            if cel_num == 3:
                self.game_map += self.cells_value[cel_num - 2] + "|" + self.cells_value[cel_num - 1] + "|" + \
                                 self.cells_value[
                                     cel_num] + "\n\n"
                break

            self.game_map += self.cells_value[cel_num - 2] + "|" + self.cells_value[cel_num - 1] + "|" + \
                             self.cells_value[cel_num]
            self.game_map += "\n" + "--------------" + "\n"

        print(self.game_map)

    def reset_cell_values(self):
        """ Method to reset a dictionary where the values of cells are stored. """

        self.cells_value = {
            1: "    ", 2: "    ", 3: "    ", 4: "    ", 5: "    ", 6: "    ", 7: "    ", 8: "    ", 9: "    "
        }

    def gameplay(self):
        """ Method where the whole game is running. """

        player = self.choose_player()
        selected_cell_text = ""

        while True:
            self.reset_cell_values()

            for i in range(1, 10):
                self.drawing_game_map()  # Draw/redraw a game map

                if player == 1:
                    selected_cell_number = self.selected_cell("X")

                    selected_cell_text = self.cells_value[int(selected_cell_number)] = "  O "

                    # Checking if the player_1 is the winner and if True break
                    if self.is_winner(selected_cell_text):
                        break
                    player = self.player = 2

                elif player == 2:
                    selected_cell_number = self.selected_cell("X")

                    selected_cell_text = self.cells_value[int(selected_cell_number)] = "  X "

                    # Checking if the player_2 is the winner and if True break
                    if self.is_winner(selected_cell_text):
                        break
                    player = self.player = 1

            if self.is_winner(selected_cell_text):
                print("Player {} has won the game!".format(player))
            else:
                print("\nWe have a tie!")

            if not self.is_rematch():
                return False

    def selected_cell(self, letter):
        """Method that inputs players cells and checks if the cell has not been previously selected """
        is_override = True

        # Choosing the cell
        cel_num = input("Insert cell for player {} ({}): ".format(self.player, letter))

        # Running if the cell has not been previously selected
        while is_override:
            if cel_num == "" or int(cel_num) > 9:
                cel_num = input("Please, Insert cell from 1 to 9.\nInsert cell for player {} ({}): ".format(self.player, letter))
                print()
                is_override = True
                continue
            if "O" in self.cells_value[int(cel_num)] or "X" in self.cells_value[int(cel_num)]:
                is_override = True
                cel_num = input("This cell has been taken already!\nInsert cell for player {} ({}): ".format(self.player, letter))
                print()
            else:
                return cel_num

    def take_symbol(self):
        if self.player == 1:
            return

    def choose_player(self):
        """ To choose a player's symbol in a game ('x' or 'o') """

        player_temp = input("Press 'x' or 'o' for Player 1: ")

        while True:
            if player_temp.lower() == "x":
                self.player = 2
                return 2
            elif player_temp.lower() == "o":
                self.player = 1
                return 1
            else:
                player_temp = input("You've input a wrong sign!\nPress 'x' or 'o' and ENTER for Player 1: ")

    def is_winner(self, cell_text):
        """ Taken a dictionary when are stored the players inputs and checking if a letter(as an argument) is in a
        dictionary value.
        Returns True if player has won(3 same chars in a row). """

        letter = cell_text.strip().upper()

        return (
                (letter in self.cells_value[7] and letter in self.cells_value[8] and letter in self.cells_value[
                    9]) or  # across the top
                (letter in self.cells_value[4] and letter in self.cells_value[5] and letter in self.cells_value[
                    6]) or  # across the middle
                (letter in self.cells_value[1] and letter in self.cells_value[2] and letter in self.cells_value[
                    3]) or  # across the bottom
                (letter in self.cells_value[7] and letter in self.cells_value[4] and letter in self.cells_value[
                    1]) or  # down the left side
                (letter in self.cells_value[8] and letter in self.cells_value[5] and letter in self.cells_value[
                    2]) or  # down the middle
                (letter in self.cells_value[9] and letter in self.cells_value[6] and letter in self.cells_value[
                    3]) or  # down the right side
                (letter in self.cells_value[7] and letter in self.cells_value[5] and letter in self.cells_value[
                    3]) or  # diagonal
                (letter in self.cells_value[9] and letter in self.cells_value[5] and letter in self.cells_value[
                    1]))  # diagonal

    @staticmethod
    def is_rematch():
        """ Static method that checks if we want to rematch in case of a tie """
        rematch = input("Rematch? (y/n): ")
        is_incorrect = True

        while is_incorrect:
            if rematch == "y":
                return True
            elif rematch == "n":
                return False
            else:
                rematch = input("Press 'y' for 'yes' or 'n' for 'no.'\nRematch? (y/n): ")
                is_incorrect = True


def run_the_game():
    tick_tack_toe = TickTackToe()
    tick_tack_toe.gameplay()


run_the_game()
