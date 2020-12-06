# Advent of Code Leaderboard Parser

This is a program to parse the JSON given by the Advent of Code API for local leaderboards. 

Currently, the only feature is that it will print out the 

## Installation

`git clone git@github.com:NotQuiteAmish/aoc_scoreboard.git` \

`pip install -r requirements.txt`

## Running the program

To run, first gather your session cookie and the link to the json file for your local leaderboard.

Change the name of `config.py-example` to `config.py`, and fill in the appropriate data that was collected.

The program can then be run using `python leaderboard.py > output.txt`, or simply `python leaderboard.py`