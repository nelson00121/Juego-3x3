import tkinter as tk
import random
# búsqueda en profundidad
class PuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de 9 Dígitos")
        self.root.configure(bg="#f0f0f0")  
        
        self.numbers = list(range(1, 9)) + [None]
        random.shuffle(self.numbers)
        self.buttons = []
        
        self.create_board()
        self.update_board()
    
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(self.root, text='', width=5, height=2, font=('Arial', 20),
                                bg="#4CAF50", fg="white", activebackground="#45a049", 
                                activeforeground="white", command=lambda r=i, c=j: self.move_tile(r, c))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)
    
    def update_board(self):
        for i in range(3):
            for j in range(3):
                num = self.numbers[i * 3 + j]
                self.buttons[i][j]['text'] = num if num is not None else ''
    
    def move_tile(self, row, col):
        empty_index = self.numbers.index(None)
        empty_row, empty_col = divmod(empty_index, 3)
        
        if abs(empty_row - row) + abs(empty_col - col) == 1:
            self.numbers[empty_index], self.numbers[row * 3 + col] = self.numbers[row * 3 + col], self.numbers[empty_index]
            self.update_board()
            if self.numbers[:-1] == list(range(1, 9)):
                self.show_win_message()
    
    def solve_puzzle(self):
        self.numbers = list(range(1, 9)) + [None]
        self.update_board()
    
    def show_win_message(self):
        win_label = tk.Label(self.root, text='¡Has ganado!', font=('Arial', 20), fg='green', bg='#f0f0f0')
        win_label.grid(row=3, column=0, columnspan=3)
    
    def create_solve_button(self):
        solve_btn = tk.Button(self.root, text='Resolver', font=('Arial', 14), bg="#2196F3", fg="white", 
                              activebackground="#1976D2", activeforeground="white", command=self.solve_puzzle)
        solve_btn.grid(row=4, column=0, columnspan=3, pady=10)

    def move_random_tile(self):
        empty_index = self.numbers.index(None)
        empty_row, empty_col = divmod(empty_index, 3)
        
        # Obtener las posibles posiciones adyacentes
        adjacent_positions = []
        if empty_row > 0: adjacent_positions.append(((empty_row - 1) * 3 + empty_col))  # Arriba
        if empty_row < 2: adjacent_positions.append(((empty_row + 1) * 3 + empty_col))  # Abajo
        if empty_col > 0: adjacent_positions.append((empty_row * 3 + (empty_col - 1)))  # Izquierda
        if empty_col < 2: adjacent_positions.append((empty_row * 3 + (empty_col + 1)))  # Derecha
        
        # Elegir un movimiento aleatorio
        random_position = random.choice(adjacent_positions)
        self.numbers[empty_index], self.numbers[random_position] = self.numbers[random_position], self.numbers[empty_index]
        self.update_board()
        
        if self.numbers[:-1] == list(range(1, 9)):
            self.show_win_message()

    def create_next_button(self):
        next_btn = tk.Button(self.root, text='Siguiente', font=('Arial', 14), bg="#FF9800", fg="white", 
                             activebackground="#FB8C00", activeforeground="white", command=self.move_random_tile)
        next_btn.grid(row=5, column=0, columnspan=3, pady=10)

if __name__ == '__main__':
    root = tk.Tk()
    game = PuzzleGame(root)
    game.create_solve_button()
    game.create_next_button()
    root.mainloop()
