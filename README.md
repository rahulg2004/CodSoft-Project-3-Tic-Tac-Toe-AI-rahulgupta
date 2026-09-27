# 🎮 Tic-Tac-Toe AI

A professional desktop-based **Tic-Tac-Toe AI application** developed using Python and Tkinter, where a human player competes against an Artificial Intelligence opponent powered by the **Minimax algorithm**.

The application provides an interactive graphical interface with AI-based decision-making, score tracking, result history across rounds, winning-cell highlighting and a dedicated result screen after every game.

This project was developed as part of the **CodSoft Artificial Intelligence Internship – Task 2: Tic-Tac-Toe AI**.

---

# 📌 Internship Task

**Organisation:** CodSoft
**Internship:** Artificial Intelligence Internship
**Task:** Task 2 – Tic-Tac-Toe AI

The task requires developing an AI agent that can play the classic Tic-Tac-Toe game against a human player. The project focuses on implementing game logic and an AI decision-making approach such as the **Minimax algorithm**.

---

# 📖 Table of Contents

* [Project Overview](#-project-overview)
* [Objectives](#-objectives)
* [Key Features](#-key-features)
* [Technologies Used](#-technologies-used)
* [Artificial Intelligence](#-artificial-intelligence)
* [Minimax Algorithm](#-minimax-algorithm)
* [How the AI Works](#-how-the-ai-works)
* [Game Flow](#-game-flow)
* [Result Screen](#-result-screen)
* [Score Recording](#-score-recording)
* [Project Structure](#-project-structure)
* [System Requirements](#-system-requirements)
* [Installation](#-installation)
* [How to Run](#-how-to-run)
* [How to Play](#-how-to-play)
* [Game Rules](#-game-rules)
* [Testing](#-testing)
* [Learning Outcomes](#-learning-outcomes)
* [Future Improvements](#-future-improvements)
* [Internship Context](#-internship-context)
* [GitHub](#-github)
* [License](#-license)

---

# 🚀 Project Overview

Tic-Tac-Toe AI is an interactive desktop application that allows a human player to play the classic 3×3 Tic-Tac-Toe game against an Artificial Intelligence opponent.

The human player uses **X**, while the AI uses **O**.

The AI uses the **Minimax algorithm** to evaluate possible future game states and select an optimal move.

The application is designed as a complete game experience rather than a simple command-line implementation. It provides:

* Interactive graphical gameplay
* AI decision-making
* Win detection
* Draw detection
* Score tracking
* Move counting
* Winning-cell highlighting
* Game result screen
* New game functionality
* Exit functionality
* Persistent score across multiple rounds

---

# 🎯 Objectives

The main objectives of this project are:

* To understand the fundamentals of Artificial Intelligence.
* To implement an AI agent for a two-player game.
* To understand game-state evaluation.
* To implement the Minimax search algorithm.
* To use recursion for decision-making.
* To develop a desktop GUI using Tkinter.
* To handle user interaction through GUI events.
* To implement win and draw detection.
* To maintain game results across multiple rounds.
* To create a complete interactive AI application.

---

# ✨ Key Features

## 🎮 Gameplay

* Human vs AI gameplay.
* Human player uses **X**.
* AI player uses **O**.
* Interactive 3×3 game board.
* Click-based player moves.
* Automatic AI responses.
* Win detection.
* Draw detection.
* Occupied-position prevention.

## 🧠 Artificial Intelligence

* Minimax-based AI.
* Recursive game-state evaluation.
* AI evaluates possible future moves.
* AI identifies winning opportunities.
* AI attempts to block potential human wins.
* AI selects the best available move based on evaluated game states.

## 📊 Score Tracking

The application records results from previous rounds.

The scoreboard contains:

```text
You: 0    Draws: 0    AI: 0
```

When a game ends, the appropriate score is increased.

For example:

```text
You win Round 1
You: 1    Draws: 0    AI: 0
```

If the player starts another game, the score remains:

```text
You: 1    Draws: 0    AI: 0
```

After another round:

```text
You: 1    Draws: 1    AI: 0
```

The score therefore represents the results of all completed rounds during the current application session.

---

# 🏁 Result Screen

After every game, the application displays a dedicated **GAME OVER** window.

The result screen shows:

* Game result
* Result message
* Current scoreboard
* Start New Game button
* Exit button

Possible results include:

```text
YOU WIN!
```

```text
AI WINS!
```

```text
IT'S A DRAW!
```

---

# 🔄 Start New Game

After a game ends, select:

```text
Start New Game
```

The current board is cleared and a new round begins.

The previous result is **not deleted**.

For example:

### Round 1

```text
You win.

Score:
You: 1    Draws: 0    AI: 0
```

### Start New Game

The board becomes empty.

The score remains:

```text
You: 1    Draws: 0    AI: 0
```

### Round 2

Suppose the AI wins.

The score becomes:

```text
You: 1    Draws: 0    AI: 1
```

This allows multiple rounds to be played while maintaining the session's cumulative results.

---

# 🚪 Exit After Result

After every completed game, the result screen provides an:

```text
Exit
```

button.

Selecting **Exit** closes the result window and terminates the application.

The player therefore has two choices after every completed round:

```text
              GAME OVER
                  │
        ┌─────────┴─────────┐
        ↓                   ↓
Start New Game             Exit
        ↓                   ↓
New Round               Close App
```

---

# 🧠 Artificial Intelligence

The main Artificial Intelligence component of this project is the **Minimax algorithm**.

Minimax is a decision-making algorithm commonly used in two-player games where one player attempts to maximise their outcome while the opponent attempts to minimise it.

In this project:

```text
Human Player = X
AI Player    = O
```

The AI evaluates possible future game states.

The outcomes are assigned scores:

```text
AI Win      = +1
Draw        =  0
Human Win   = -1
```

The AI attempts to maximise its score while considering the human player's possible responses.

---

# 🔍 Minimax Algorithm

The Minimax algorithm works recursively.

The basic process is:

```text
Current Board
     ↓
Check Game Result
     ↓
Is Game Finished?
     ↓
Yes ───────────→ Return Score
     │
     No
     ↓
Find Empty Positions
     ↓
Simulate Possible Move
     ↓
Run Minimax Recursively
     ↓
Evaluate Result
     ↓
Undo Simulated Move
     ↓
Compare Scores
     ↓
Select Best Move
```

This allows the AI to make decisions by analysing possible future game states.

---

# ⚙️ How the AI Works

For every available position, the AI temporarily places `O`.

The Minimax algorithm then evaluates the resulting board.

Example:

```text
Possible Move 1 → Score 0
Possible Move 2 → Score +1
Possible Move 3 → Score -1
```

The AI selects the move with the highest score.

```text
Highest Score
      ↓
Best Move
      ↓
Place O
```

After evaluating a simulated move, the board is restored before another possibility is checked.

---

# 🔄 Game Flow

```text
Start Application
       ↓
Display Empty Board
       ↓
Human's Turn
       ↓
Human selects a position
       ↓
Place X
       ↓
Check Game Result
       ↓
Game Over?
   ↙         ↘
 Yes          No
 ↓             ↓
Result      AI's Turn
Screen          ↓
             Minimax
                ↓
          Select Best Move
                ↓
             Place O
                ↓
          Check Game Result
                ↓
           Game Over?
           ↙        ↘
         Yes         No
          ↓           ↓
      Result      Human's Turn
       Screen
```

---

# 📊 Result and Score Flow

The result-management process works as follows:

```text
Game Ends
    ↓
Determine Result
    ↓
Update Score
    ↓
Disable Board
    ↓
Display Result Screen
    ↓
    ┌─────────────────────┐
    │                     │
    ↓                     ↓
Start New Game           Exit
    ↓                     ↓
Reset Board            Close App
    ↓
Keep Previous Score
    ↓
New Round
```

---

# 🖥️ Application Interface

The application includes:

### Header

```text
TIC-TAC-TOE AI
Human vs Artificial Intelligence
```

### Player Information

```text
YOU  X                         AI  O
```

### Scoreboard

```text
You: 0    Draws: 0    AI: 0
```

### Move Counter

```text
Moves: 0
```

### Game Status

Examples:

```text
Your Turn
```

```text
AI is thinking...
```

```text
You Win!
```

```text
AI Wins!
```

```text
It's a Draw!
```

### Game Board

A clickable 3×3 board is provided for player interaction.

---

# 📂 Project Structure

```text
CODSOFT_TASK2/
│
├── tic_tac_toe_gui.py
│       └── Main Tkinter application
│
├── README.md
│       └── Project documentation
│
└── requirements.txt
        └── Dependency information
```

---

# 📄 File Description

## `tic_tac_toe_gui.py`

The main application file.

It contains:

* Tkinter GUI
* Game board
* Player interaction
* AI interaction
* Minimax algorithm
* Winner detection
* Draw detection
* Score tracking
* Result screen
* New Game functionality
* Exit functionality
* Move counter
* Winning-cell highlighting

---

## `README.md`

Project documentation containing:

* Project overview
* Features
* AI methodology
* Game flow
* Installation instructions
* Usage instructions
* Testing
* Learning outcomes

---

## `requirements.txt`

Contains dependency information.

No external Python packages are required.

Tkinter is generally included with standard Python installations.

---

# 💻 System Requirements

## Software

* Python 3.x
* Windows, Linux or macOS
* VS Code or another Python-compatible IDE

## Hardware

A basic computer capable of running Python is sufficient.

Recommended:

* 4 GB RAM or more
* Modern processor
* Keyboard and mouse

---

# 📥 Installation

## Step 1: Install Python

Verify Python installation:

```bash
python --version
```

Example:

```text
Python 3.12.5
```

---

## Step 2: Open the Project

Open the `CODSOFT_TASK2` folder in VS Code or another Python-compatible IDE.

---

## Step 3: Check Dependencies

No external packages are required.

Tkinter is used for the graphical interface.

---

# ▶️ How to Run

Open the terminal inside the project folder and run:

```bash
python tic_tac_toe_gui.py
```

The Tic-Tac-Toe AI application will open.

---

# 🎮 How to Play

You are:

```text
X
```

The AI is:

```text
O
```

Click any empty square to place your `X`.

The AI will automatically calculate its move using Minimax.

The game continues until:

* You win
* AI wins
* The game ends in a draw

---

# 🏆 Winning Combinations

The application checks eight possible winning combinations.

### Horizontal

```text
X | X | X
---------
  |   |
---------
  |   |
```

### Vertical

```text
X |   |
---------
X |   |
---------
X |   |
```

### Diagonal

```text
X |   |
---------
  | X |
---------
  |   | X
```

---

# 🧪 Testing

The application can be tested using the following scenarios.

| Test                        | Expected Result             |
| --------------------------- | --------------------------- |
| Human wins                  | Player score increases      |
| AI wins                     | AI score increases          |
| Draw                        | Draw score increases        |
| Occupied position           | Position cannot be selected |
| AI blocking opportunity     | AI attempts to block        |
| AI winning opportunity      | AI selects winning move     |
| Start New Game              | Board resets                |
| Start New Game after result | Previous score remains      |
| Exit                        | Application closes          |
| Multiple rounds             | Scores accumulate           |

---

# 📈 Example Score Progression

### Initial State

```text
You: 0    Draws: 0    AI: 0
```

### After Player Wins

```text
You: 1    Draws: 0    AI: 0
```

### After Starting New Game

```text
You: 1    Draws: 0    AI: 0
```

### After AI Wins

```text
You: 1    Draws: 0    AI: 1
```

### After Another Draw

```text
You: 1    Draws: 1    AI: 1
```

The previous results remain recorded in the cumulative scoreboard throughout the application session.

---

# 🧩 Important Functions

## `check_winner()`

Checks whether:

* X has won
* O has won
* The board is full
* The game is still active

---

## `minimax()`

Implements the recursive AI decision-making algorithm.

---

## `get_best_move()`

Evaluates available moves and selects the best move for the AI.

---

## `human_move()`

Handles the human player's board selection.

---

## `ai_turn()`

Calculates and performs the AI's move.

---

## `end_game()`

Handles the game result, updates the scoreboard and displays the result screen.

---

## `show_result_screen()`

Displays:

* Result
* Current score
* Start New Game button
* Exit button

---

## `start_new_game()`

Clears the current board while preserving the scores from previous rounds.

---

## `exit_from_result()`

Closes the result window and exits the application.

---

# 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Artificial Intelligence
* Game theory
* Minimax algorithm
* Recursive algorithms
* Search algorithms
* Game-state evaluation
* Python programming
* Object-Oriented Programming
* Tkinter GUI development
* Event-driven programming
* User input handling
* Score management
* Application testing
* Problem-solving

---

# 🚀 Future Improvements

Possible future improvements include:

* Multiple difficulty levels
* Easy, Medium and Hard modes
* Alpha-Beta Pruning
* Player name customisation
* First-player selection
* Sound effects
* Game history
* Persistent score storage
* Match statistics
* Game replay
* AI strategy visualisation
* Multiplayer mode
* Custom themes
* Animations

---

# 📸 Project Demonstration

A project demonstration can show:

1. Launching the application.
2. Displaying the game board.
3. Making a human move.
4. AI calculating a move.
5. AI making its move.
6. AI blocking a potential winning move.
7. Completing a winning round.
8. Displaying the result screen.
9. Showing the recorded score.
10. Selecting **Start New Game**.
11. Demonstrating that the previous score remains.
12. Playing another round.
13. Selecting **Exit** after the result.

---

# 🎥 Internship Video Demonstration

The video demonstration can follow this structure:

```text
Introduction
     ↓
Project Objective
     ↓
Technologies Used
     ↓
GUI Demonstration
     ↓
Human Move
     ↓
AI Move
     ↓
Minimax Explanation
     ↓
Game Result
     ↓
Score Recording
     ↓
Start New Game
     ↓
Previous Score Retained
     ↓
Exit Option
     ↓
GitHub Repository
```

---

# 🔗 GitHub

🔗 GitHub🚀 : [Add your repository link]

---

# 🎓 Internship

Developed as part of the:

**CodSoft Artificial Intelligence Internship**

**Task 2 – Tic-Tac-Toe AI**

This project provided practical experience in Artificial Intelligence, game theory, recursive search, algorithmic decision-making and GUI application development.

---

# 📜 License

This project was developed for educational and internship purposes.