import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.resizable(False, False)

        self.width = 600
        self.height = 600
        self.grid_size = 20
        self.speed = 100

        self.score = 0
        self.high_score = 0
        self.direction = "Right"
        self.next_direction = "Right"
        self.running = False
        self.game_loop_id = None

        self.score_frame = tk.Frame(self.root, bg="#1a1a2e")
        self.score_frame.pack(fill="x")

        self.score_label = tk.Label(
            self.score_frame,
            text=f"Score: {self.score}   |   High Score: {self.high_score}",
            font=("Arial", 16, "bold"),
            fg="#e94560",
            bg="#1a1a2e",
            pady=10
        )
        self.score_label.pack()

        self.canvas = tk.Canvas(
            self.root,
            width=self.width,
            height=self.height,
            bg="#16213e",
            highlightthickness=0
        )
        self.canvas.pack()

        self.root.bind("<Up>", lambda event: self.change_direction("Up"))
        self.root.bind("<Down>", lambda event: self.change_direction("Down"))
        self.root.bind("<Left>", lambda event: self.change_direction("Left"))
        self.root.bind("<Right>", lambda event: self.change_direction("Right"))
        self.root.bind("<w>", lambda event: self.change_direction("Up"))
        self.root.bind("<s>", lambda event: self.change_direction("Down"))
        self.root.bind("<a>", lambda event: self.change_direction("Left"))
        self.root.bind("<d>", lambda event: self.change_direction("Right"))
        self.root.bind("<space>", lambda event: self.restart_game())

        self.start_game()

    def start_game(self):
        if self.game_loop_id:
            self.root.after_cancel(self.game_loop_id)

        self.score = 0
        self.update_score()
        self.direction = "Right"
        self.next_direction = "Right"
        self.running = True

        start_x = self.width // 2
        start_y = self.height // 2
        self.snake = [
            [start_x, start_y],
            [start_x - self.grid_size, start_y],
            [start_x - 2 * self.grid_size, start_y]
        ]

        self.food = self.spawn_food()
        self.canvas.delete("all")
        self.draw_grid()
        self.run_loop()

    def draw_grid(self):
        for x in range(0, self.width, self.grid_size):
            self.canvas.create_line(x, 0, x, self.height, fill="#0f3460", width=1)
        for y in range(0, self.height, self.grid_size):
            self.canvas.create_line(0, y, self.width, y, fill="#0f3460", width=1)

    def spawn_food(self):
        while True:
            x = random.randint(0, (self.width // self.grid_size) - 1) * self.grid_size
            y = random.randint(0, (self.height // self.grid_size) - 1) * self.grid_size
            if [x, y] not in self.snake:
                return [x, y]

    def change_direction(self, new_dir):
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if new_dir != opposites.get(self.direction):
            self.next_direction = new_dir

    def run_loop(self):
        if not self.running:
            return

        self.direction = self.next_direction
        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            head_y -= self.grid_size
        elif self.direction == "Down":
            head_y += self.grid_size
        elif self.direction == "Left":
            head_x -= self.grid_size
        elif self.direction == "Right":
            head_x += self.grid_size

        new_head = [head_x, head_y]

        if (
            head_x < 0 or head_x >= self.width or
            head_y < 0 or head_y >= self.height or
            new_head in self.snake
        ):
            self.game_over()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 10
            if self.score > self.high_score:
                self.high_score = self.score
            self.update_score()
            self.food = self.spawn_food()
        else:
            self.snake.pop()

        self.draw_elements()
        self.game_loop_id = self.root.after(self.speed, self.run_loop)

    def draw_elements(self):
        self.canvas.delete("game_elem")

        fx, fy = self.food
        self.canvas.create_oval(
            fx + 2, fy + 2,
            fx + self.grid_size - 2, fy + self.grid_size - 2,
            fill="#e94560", outline="#ff6b81", tags="game_elem"
        )

        for i, segment in enumerate(self.snake):
            sx, sy = segment
            color = "#4ecca3" if i == 0 else "#23a393"
            self.canvas.create_rectangle(
                sx + 1, sy + 1,
                sx + self.grid_size - 1, sy + self.grid_size - 1,
                fill=color, outline="#1b7a6d", tags="game_elem"
            )

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}   |   High Score: {self.high_score}")

    def game_over(self):
        self.running = False
        self.canvas.create_rectangle(
            50, self.height // 2 - 80,
            self.width - 50, self.height // 2 + 80,
            fill="#1a1a2e", outline="#e94560", width=3, tags="game_elem"
        )
        self.canvas.create_text(
            self.width // 2, self.height // 2 - 25,
            text="GAME OVER", fill="#e94560",
            font=("Arial", 28, "bold"), tags="game_elem"
        )
        self.canvas.create_text(
            self.width // 2, self.height // 2 + 25,
            text="Press SPACE or Button to Play Again",
            fill="#ffffff", font=("Arial", 14), tags="game_elem"
        )

    def restart_game(self):
        self.start_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()