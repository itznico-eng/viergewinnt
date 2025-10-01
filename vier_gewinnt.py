class VierGewinnt:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = 'X'

    def print_board(self):
        print('\n'.join(['|'.join(row) for row in self.board]))
        print('-' * (self.cols * 2 - 1))
        print(' '.join(str(i) for i in range(self.cols)))

    def drop_piece(self, col):
        for row in reversed(range(self.rows)):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                return True
        return False

    def check_win(self):
        # Horizontal, vertical, diagonal checks
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == ' ':
                    continue
                if self.check_direction(r, c, 0, 1) or \
                   self.check_direction(r, c, 1, 0) or \
                   self.check_direction(r, c, 1, 1) or \
                   self.check_direction(r, c, 1, -1):
                    return True
        return False

    def check_direction(self, r, c, dr, dc):
        piece = self.board[r][c]
        for i in range(1, 4):
            nr, nc = r + dr * i, c + dc * i
            if nr < 0 or nr >= self.rows or nc < 0 or nc >= self.cols:
                return False
            if self.board[nr][nc] != piece:
                return False
        return True

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def is_full(self):
        return all(self.board[0][c] != ' ' for c in range(self.cols))

    def play(self):
        while True:
            self.print_board()
            col = input(f"Spieler {self.current_player}, wähle eine Spalte (0-{self.cols-1}): ")
            if not col.isdigit() or not (0 <= int(col) < self.cols):
                print("Ungültige Eingabe. Versuche es erneut.")
                continue
            col = int(col)
            if not self.drop_piece(col):
                print("Spalte voll. Versuche eine andere.")
                continue
            if self.check_win():
                self.print_board()
                print(f"Spieler {self.current_player} gewinnt!")
                break
            if self.is_full():
                self.print_board()
                print("Unentschieden!")
                break
            self.switch_player()

if __name__ == "__main__":
    game = VierGewinnt()
    game.play()
