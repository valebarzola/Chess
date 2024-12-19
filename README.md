# ♔♕♖Chess♗♘♙
Valentin Barzola Vilela

# CodeClimate
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-VbarzolaEdu/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-VbarzolaEdu/tree/master)

# Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/208101193e41b815847e/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-VbarzolaEdu/maintainability)

# Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/208101193e41b815847e/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-VbarzolaEdu/test_coverage)

# 📝 Description
The followiing proyect is an educational chees game. 

# 📋 Requirements
- Python 3.x...
- 📚Library:

coverage==7.6.1 (included on requirements.txt)

# 🎮 Game
- Board: An 8x8 cell board with the standard initial configuration of pieces.
- Pieces: Traditional chess pieces are included: king, queen, rooks, bishops, knights and pawns.
- Playability: Players can move their pieces according to the official rules of chess, with move validation.
- Endgame: the game ends when one player runs out of pieces or both players decide to end the game writting "Stop".

# 🛠️ Characteristics
- Game Board: represented by an 8x8 matrix, with the initial positions of the pieces.
- Piece Moves: each type of piece follows its valid moves according to the rules of chess.
- Command Line Interface (CLI): allows you to play by entering commands in the console.

# 👨🏼‍💻 Execution
1- Clone repository:
git clone https://github.com/um-computacion-tm/ajedrez-2024-VbarzolaEdu.git

2- Install dependencies:

pip install -r requirements.txt

3- Play on console:

python3 juego.Cli.py

# Dockerfile
commands:
1- docker buildx build -t ajedrez-2024-vbarzolaedu .

2- docker run -i ajedrez-2024-vbarzolaedu
