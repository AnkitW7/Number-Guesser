# Number Guesser

A simple command-line number guessing game written in Python. Choose the maximum number, then try to guess the random number selected by the computer.

## Features

- Custom upper-number limit
- Random number generation
- Above and below hints
- Guess counter
- Input validation for numeric entries

## Requirements

- Python 3

## How to Run

From the project folder, run:

```bash
python number_guesser.py
```

1. Enter a number greater than 0 to set the maximum range.
2. Guess the random number the computer chose between `0` and your chosen maximum.
3. Use the hints to adjust each guess.

The game ends when your guess is correct.

## Example

```text
Type a number : 10
Make a guess: 5
You were below the number
Make a guess: 8
You were above the number
Make a guess: 7
This is correct guess.
You go it in 3 guesses
```

## Project Structure

```text
number_guesser.py  Main game script
README.md          Project documentation
```
