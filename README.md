
# Phase 3 CLI+ORM Project: Python Typ-On
Welcome to Python Typ-on, a command-line project that puts your typing skills to the test using Object-Oriented Python! In Python Typ-On, your challenge is to advance through the levels, typing the provided sentences with accuracy and speed.

The levels get progressively harder the longer you play.

For each game you play, Python Typ-On shows the mistakes you made, and calculates your typing accuracy and speed.

The games and stats are then saved to an SQLite database, allowing you to see your overall average.

**Table of contents:**
- [1. Introduction](#introduction)
- [2. Features](#features)
- [3. Installation](#installation)
- [4. Usage](#usage)
- [5. Feedback and Support](#feedback)

<a id="introduction"></a>

## 1. Introduction
Python Typ-On is a fun and interactive project built in Python. The command-line interface makes it easy to play.

<a id="features"></a>

## 2. Features
- **New Game:** When starting a new game, you will be prompted to enter your name. Then, you will enter a loop of games. In each game, you are given a sentence and expected to type it out as an input.
- **Difference highlight:** After you enter an input sentence, the game calculates the difference between the provided sentence and your input. Correct characters are displayed in green, and mistakes are displayed in red. If you missed a key, it's displayed with a minus sign ("-"), and if you aded an extra key, it's displayed with a plus sign ("+").
- **Typing accuracy:** The typing accuracy is calculated based on the ratio between the provided sentence and your input.
- **Typing speed:** A timer starts when the sentence is shown, and ends when you finish your input. This is your typing time.
- **Stats:** The Stats feature contains a leaderboard showcasing all the players along with their average typing accuracy, average typing speed, and the highest level played. The leaderboard is sorted by average accuracy in descending order (from highest to lowest).
- **List all levels:** Prints a list of all available levels in the game.

<a id="installation"></a>

## 3. Installation
To run Python Typ-On on your local machine, follow these steps:

Clone the repository from GitHub Repo URL.

Navigate to the project directory.

Install the required dependencies (SQLite support is included in Python's standard library, so no additional installations are needed): `pip install` or `pipenv install`

<a id="usage"></a>

## 4. Usage
Once installed, you can start Python Typ-On from the command line: python cli.py

The main menu will guide you through the available options.

<a id="feedback"></a>

## 5. Feedback and Support
We hope you enjoy the game! If you encounter any issues, have suggestions for improvement, or need assistance, please feel free to reach out.

Thank you for playing! Happy typing!