import tkinter as tk

class TicTacToeAI:

    def __init__(self, root):
        self.root = root

        self.root.title("Tic-Tac-Toe AI")
        self.root.geometry("560x780")
        self.root.resizable(False, False)
        self.root.configure(bg="#111827")

        self.board = [" " for _ in range(9)]

        self.winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

        self.player_score = 0
        self.ai_score = 0
        self.draw_score = 0
        self.move_count = 0
        self.game_over = False
        self.ai_job = None

        self.background = "#111827"
        self.card_background = "#1F2937"
        self.board_background = "#0F172A"
        self.button_background = "#374151"
        self.button_hover = "#4B5563"

        self.text_color = "#F9FAFB"
        self.secondary_text = "#9CA3AF"

        self.x_color = "#60A5FA"
        self.o_color = "#F87171"

        self.success_color = "#34D399"
        self.warning_color = "#FBBF24"
        self.result_color = "#8B5CF6"

        self.create_interface()

    def create_interface(self):

        title = tk.Label(
            self.root,
            text="TIC-TAC-TOE AI",
            font=("Segoe UI", 28, "bold"),
            bg=self.background,
            fg=self.text_color
        )

        title.pack(pady=(25, 2))

        subtitle = tk.Label(
            self.root,
            text="Human vs Artificial Intelligence",
            font=("Segoe UI", 12),
            bg=self.background,
            fg=self.secondary_text
        )

        subtitle.pack()

        player_info = tk.Frame(
            self.root,
            bg=self.card_background
        )

        player_info.pack(
            padx=35,
            pady=18,
            fill="x"
        )

        player_label = tk.Label(
            player_info,
            text="YOU  X",
            font=("Segoe UI", 13, "bold"),
            bg=self.card_background,
            fg=self.x_color
        )

        player_label.pack(
            side="left",
            padx=25,
            pady=12
        )

        ai_label = tk.Label(
            player_info,
            text="AI  O",
            font=("Segoe UI", 13, "bold"),
            bg=self.card_background,
            fg=self.o_color
        )

        ai_label.pack(
            side="right",
            padx=25,
            pady=12
        )

        self.score_label = tk.Label(
            self.root,
            text="You: 0    Draws: 0    AI: 0",
            font=("Segoe UI", 13, "bold"),
            bg=self.background,
            fg=self.text_color
        )

        self.score_label.pack(
            pady=(0, 8)
        )

        self.move_label = tk.Label(
            self.root,
            text="Moves: 0",
            font=("Segoe UI", 10),
            bg=self.background,
            fg=self.secondary_text
        )

        self.move_label.pack()

        self.status_label = tk.Label(
            self.root,
            text="Your Turn",
            font=("Segoe UI", 16, "bold"),
            bg=self.background,
            fg=self.success_color
        )

        self.status_label.pack(
            pady=12
        )

        board_container = tk.Frame(
            self.root,
            bg=self.board_background
        )

        board_container.pack(
            padx=35,
            pady=8
        )

        self.buttons = []

        for i in range(9):

            button = tk.Button(
                board_container,
                text="",
                font=("Segoe UI", 30, "bold"),
                width=4,
                height=2,
                bg=self.button_background,
                fg=self.text_color,
                activebackground=self.button_hover,
                activeforeground=self.text_color,
                relief="flat",
                bd=0,
                cursor="hand2",
                command=lambda position=i: self.human_move(position)
            )

            button.grid(
                row=i // 3,
                column=i % 3,
                padx=4,
                pady=4
            )

            self.buttons.append(button)

        instructions_frame = tk.Frame(
            self.root,
            bg=self.card_background
        )

        instructions_frame.pack(
            padx=35,
            pady=18,
            fill="x"
        )

        instructions_title = tk.Label(
            instructions_frame,
            text="HOW TO PLAY",
            font=("Segoe UI", 11, "bold"),
            bg=self.card_background,
            fg=self.text_color
        )

        instructions_title.pack(
            pady=(10, 3)
        )

        instructions = tk.Label(
            instructions_frame,
            text="Click an empty square to place X.\n"
                 "The AI uses the Minimax algorithm to choose its move.",
            font=("Segoe UI", 10),
            bg=self.card_background,
            fg=self.secondary_text,
            justify="center"
        )

        instructions.pack(
            pady=(0, 12)
        )

        footer = tk.Label(
            self.root,
            text="After each result, choose Start New Game or Exit.",
            font=("Segoe UI", 9),
            bg=self.background,
            fg=self.secondary_text
        )

        footer.pack(
            pady=(0, 5)
        )

    def check_winner(self):

        for combination in self.winning_combinations:

            a, b, c = combination

            if (
                self.board[a] == self.board[b]
                and self.board[b] == self.board[c]
                and self.board[a] != " "
            ):
                return self.board[a], combination

        if " " not in self.board:
            return "Draw", None

        return None, None

    def minimax(self, is_maximizing):

        result, _ = self.check_winner()

        if result == "O":
            return 1

        if result == "X":
            return -1

        if result == "Draw":
            return 0

        if is_maximizing:

            best_score = -float("inf")

            for i in range(9):

                if self.board[i] == " ":

                    self.board[i] = "O"

                    score = self.minimax(False)

                    self.board[i] = " "

                    if score > best_score:
                        best_score = score

            return best_score

        else:

            best_score = float("inf")

            for i in range(9):

                if self.board[i] == " ":

                    self.board[i] = "X"

                    score = self.minimax(True)

                    self.board[i] = " "

                    if score < best_score:
                        best_score = score

            return best_score

    def get_best_move(self):

        best_score = -float("inf")
        best_move = None

        for i in range(9):

            if self.board[i] == " ":

                self.board[i] = "O"

                score = self.minimax(False)

                self.board[i] = " "

                if score > best_score:
                    best_score = score
                    best_move = i

        return best_move

    def human_move(self, position):

        if self.game_over:
            return

        if self.board[position] != " ":
            return

        self.board[position] = "X"

        self.move_count += 1

        self.buttons[position].config(
            text="X",
            fg=self.x_color,
            disabledforeground=self.x_color,
            state="disabled"
        )

        self.update_move_count()

        result, combination = self.check_winner()

        if result is not None:

            self.end_game(
                result,
                combination
            )

            return

        self.status_label.config(
            text="AI is thinking...",
            fg=self.warning_color
        )

        self.disable_empty_buttons()

        self.ai_job = self.root.after(
            350,
            self.ai_turn
        )

    def ai_turn(self):

        self.ai_job = None

        if self.game_over:
            return

        best_move = self.get_best_move()

        if best_move is not None:

            self.board[best_move] = "O"

            self.move_count += 1

            self.buttons[best_move].config(
                text="O",
                fg=self.o_color,
                disabledforeground=self.o_color,
                state="disabled"
            )

        self.update_move_count()

        result, combination = self.check_winner()

        if result is not None:

            self.end_game(
                result,
                combination
            )

            return

        self.enable_empty_buttons()

        self.status_label.config(
            text="Your Turn",
            fg=self.success_color
        )

    def disable_empty_buttons(self):

        for i in range(9):

            if self.board[i] == " ":

                self.buttons[i].config(
                    state="disabled"
                )

    def enable_empty_buttons(self):

        for i in range(9):

            if self.board[i] == " ":

                self.buttons[i].config(
                    state="normal"
                )

    def end_game(self, result, combination):

        self.game_over = True

        if self.ai_job is not None:

            try:
                self.root.after_cancel(
                    self.ai_job
                )
            except:
                pass

            self.ai_job = None

        if combination is not None:

            for position in combination:

                self.buttons[position].config(
                    bg=self.result_color
                )

        if result == "X":

            self.player_score += 1

            result_text = "YOU WIN!"

            result_message = (
                "Congratulations! You won this round."
            )

            self.status_label.config(
                text="You Win!",
                fg=self.success_color
            )

        elif result == "O":

            self.ai_score += 1

            result_text = "AI WINS!"

            result_message = (
                "The AI wins this round."
            )

            self.status_label.config(
                text="AI Wins!",
                fg=self.o_color
            )

        else:

            self.draw_score += 1

            result_text = "IT'S A DRAW!"

            result_message = (
                "This round ended in a draw."
            )

            self.status_label.config(
                text="It's a Draw!",
                fg=self.warning_color
            )

        self.update_score()

        for button in self.buttons:

            button.config(
                state="disabled"
            )

        self.show_result_screen(
            result_text,
            result_message
        )

    def show_result_screen(
        self,
        result_text,
        result_message
    ):

        result_window = tk.Toplevel(
            self.root
        )

        result_window.title(
            "Game Result"
        )

        result_window.geometry(
            "430x330"
        )

        result_window.resizable(
            False,
            False
        )

        result_window.configure(
            bg=self.background
        )

        result_window.transient(
            self.root
        )

        result_window.grab_set()

        title = tk.Label(
            result_window,
            text="GAME OVER",
            font=("Segoe UI", 22, "bold"),
            bg=self.background,
            fg=self.text_color
        )

        title.pack(
            pady=(30, 8)
        )

        result_label = tk.Label(
            result_window,
            text=result_text,
            font=("Segoe UI", 20, "bold"),
            bg=self.background,
            fg=self.result_color
        )

        result_label.pack(
            pady=5
        )

        message_label = tk.Label(
            result_window,
            text=result_message,
            font=("Segoe UI", 11),
            bg=self.background,
            fg=self.secondary_text
        )

        message_label.pack(
            pady=5
        )

        score_label = tk.Label(
            result_window,
            text=(
                f"Current Score\n\n"
                f"You: {self.player_score}    "
                f"Draws: {self.draw_score}    "
                f"AI: {self.ai_score}"
            ),
            font=("Segoe UI", 11, "bold"),
            bg=self.card_background,
            fg=self.text_color,
            justify="center"
        )

        score_label.pack(
            padx=35,
            pady=15,
            fill="x"
        )

        button_frame = tk.Frame(
            result_window,
            bg=self.background
        )

        button_frame.pack(
            pady=10
        )

        new_game_button = tk.Button(
            button_frame,
            text="Start New Game",
            font=("Segoe UI", 11, "bold"),
            bg=self.success_color,
            fg="#111827",
            activebackground="#6EE7B7",
            activeforeground="#111827",
            relief="flat",
            bd=0,
            width=17,
            height=2,
            cursor="hand2",
            command=lambda: self.start_new_game(
                result_window
            )
        )

        new_game_button.grid(
            row=0,
            column=0,
            padx=5
        )

        exit_button = tk.Button(
            button_frame,
            text="Exit",
            font=("Segoe UI", 11, "bold"),
            bg="#7F1D1D",
            fg="#FEE2E2",
            activebackground="#991B1B",
            activeforeground="#FFFFFF",
            relief="flat",
            bd=0,
            width=12,
            height=2,
            cursor="hand2",
            command=lambda: self.exit_from_result(
                result_window
            )
        )

        exit_button.grid(
            row=0,
            column=1,
            padx=5
        )

        result_window.protocol(
            "WM_DELETE_WINDOW",
            lambda: self.exit_from_result(
                result_window
            )
        )

    def start_new_game(self, result_window):

        result_window.destroy()

        self.board = [" " for _ in range(9)]

        self.move_count = 0

        self.game_over = False

        self.ai_job = None

        for button in self.buttons:

            button.config(
                text="",
                state="normal",
                bg=self.button_background,
                fg=self.text_color
            )

        self.status_label.config(
            text="Your Turn",
            fg=self.success_color
        )

        self.update_move_count()

    def exit_from_result(self, result_window):

        result_window.destroy()

        self.root.destroy()

    def update_score(self):

        self.score_label.config(
            text=(
                f"You: {self.player_score}    "
                f"Draws: {self.draw_score}    "
                f"AI: {self.ai_score}"
            )
        )

    def update_move_count(self):

        self.move_label.config(
            text=f"Moves: {self.move_count}"
        )


if __name__ == "__main__":

    root = tk.Tk()

    game = TicTacToeAI(root)

    root.mainloop()