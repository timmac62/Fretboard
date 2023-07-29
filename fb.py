# fb.py
import click
from rich import print
from rich.console import Console
from rich.theme import Theme
from rich.panel import Panel
from rich.table import Table

import random
import time

STRING1 = 1
STRING2 = 2
STRING3 = 3
STRING4 = 4
STRING5 = 5
STRING6 = 6

FRET_LOW = 0
FRET_MAX = 12

COMMAND_NONE        = ' '
COMMAND_GUESS_NOTE  = 'G'
COMMAND_MAIN_MENU   = 'M'
COMMAND_QUIT        = 'Q'
COMMAND_PREV_FRET   = 'J'
COMMAND_NEXT_FRET   = 'K'
COMMAND_FRET_3      = '3'
COMMAND_FRET_5      = '5'
COMMAND_FRET_7      = '7'
COMMAND_FRET_10     = 'T'

string_names = ["E", "B", "G", "D", "A", "E"]

# our fretboard as a dictionary of strings and each string with a list of notes
# signifying open string through fret 12
# print(fretboard)
# print(fretboard["string1"][10]) # prints D
fretboard = {
    "string1": ("E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E"),
    "string2": ("B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"),
    "string3": ("G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G"),
    "string4": ("D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D"),
    "string5": ("A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A"),
    "string6": ("E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E"),
}

custom_theme = Theme(
    {
        "guess_wrong": "bold red",
        "guess_right": "green",
        "normal_fret": "white on black",
        "highlighted_fret": "white on green",
    }
)

console = Console(width=80, theme=custom_theme)

def random_notes():
    command = COMMAND_NONE
    while command != COMMAND_MAIN_MENU:
        string_number = random.randint(STRING1, STRING6)
        fret_number = random.randint(FRET_LOW, FRET_MAX)
        string = "string" + str(string_number)
        note = fretboard[string][fret_number]
        console.clear()
        console.rule(f"[bold blue]:guitar: Guess the note! :guitar:[/]\n")
        console.print(
            f"\n[bold white]What note is at the {string_names[string_number-1]} string fret {fret_number} / S{string_number}F{fret_number}?[/]\n",
            justify="center",
        )
        console.rule(f"[bold blue]:musical_notes: Master Your Axe! :musical_notes:[/]\n")

        start = time.time()
        guess = console.input("\nYour guess: ").upper()
        end = time.time()

        if guess == note:
            result = f"\n[green]CORRECT[/]"
        else:
            result = f"\n[bold red]WRONG[/], the correct note is {note}"
        console.print(f"{result} in {end - start:3.2f} seconds")

        command = console.input(
            "\nTry again? (Any key - guess again, M - Main menu): "
        ).upper()


def display_fretboard(which_fret):
    console.clear()
    console.rule(f"[bold blue]:guitar: Fretboard Fundamentals :guitar:[/]\n")
    table = Table(title="Guitar Fretboard - Standard Tuning")
    if (which_fret == 0):
        table.add_column("0", justify="center", style="highlighted_fret", no_wrap=True)
    else:
        table.add_column("0", justify="center", style="normal_fret", no_wrap=True)
    if (which_fret == 1):
        table.add_column("1", justify="center", style="highlighted_fret", no_wrap=True)
    else:
        table.add_column("1", justify="center", style="normal_fret", no_wrap=True)
    if (which_fret == 2):
        table.add_column("2", justify="center", style="highlighted_fret", no_wrap=True)
    else:
        table.add_column("2", justify="center", style="normal_fret", no_wrap=True)
    if (which_fret == 3):
        table.add_column("3", justify="center", style="highlighted_fret", no_wrap=True)
    else:
        table.add_column("3", justify="center", style="normal_fret", no_wrap=True)
    if (which_fret == 4):
        table.add_column("4", justify="center", style="highlighted_fret", no_wrap=True)
    else:
        table.add_column("4", justify="center", style="normal_fret", no_wrap=True)
    if (which_fret == 5):
        table.add_column("5", justify="center", style="highlighted_fret", no_wrap=True)
    else:
        table.add_column("5", justify="center", style="normal_fret", no_wrap=True)
    if (which_fret == 6):
        table.add_column("6", justify="center", style="highlighted_fret", no_wrap=True)
    else:
        table.add_column("6", justify="center", style="normal_fret", no_wrap=True)
    if (which_fret == 7):
        table.add_column("7", justify="center", style="highlighted_fret", no_wrap=True)
    else:
        table.add_column("7", justify="center", style="normal_fret", no_wrap=True)
    if (which_fret == 8):
        table.add_column("8", justify="center", style="highlighted_fret", no_wrap=True)
    else:
        table.add_column("8", justify="center", style="normal_fret", no_wrap=True)
    if (which_fret == 9):
        table.add_column("9", justify="center", style="highlighted_fret", no_wrap=True)
    else:
        table.add_column("9", justify="center", style="normal_fret", no_wrap=True)
    if (which_fret == 10):
        table.add_column("10", justify="center", style="highlighted_fret", no_wrap=True)
    else:
        table.add_column("10", justify="center", style="normal_fret", no_wrap=True)
    if (which_fret == 11):
        table.add_column("11", justify="center", style="highlighted_fret", no_wrap=True)
    else:
        table.add_column("11", justify="center", style="normal_fret", no_wrap=True)
    if (which_fret == 12):
        table.add_column("12", justify="center", style="highlighted_fret", no_wrap=True)
    else:
        table.add_column("12", justify="center", style="normal_fret", no_wrap=True)

# print(fretboard["string1"][10]) # prints D

    table.add_row("E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E")   
    table.add_row("B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")
    table.add_row("G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G")
    table.add_row("D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D")
    table.add_row("A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A")
    table.add_row("E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E")

    console.print(table, justify="center")
    # console.print(str(fretboard["string1"]), justify="center") # generates rich.errors.NotRenderableError


@click.command()
def main():
    """
    A simple fretboard practice tool which will randomly select a position on
    the fretboard and give you the specified number of seconds to guess
    which note it is.

    Examples:

    String #1 Fret 5 - answer is A

    String #5 Fret 4 - C#

    """
    command = COMMAND_NONE
    fret_number = 0
    while command != COMMAND_QUIT:
        display_fretboard(fret_number)
        console.rule(f"[bold blue]:musical_notes: Master Your Axe! :musical_notes:[/]\n")
        command = console.input(
            "\nQ quit J < K >: "
        ).upper()

        if command == COMMAND_GUESS_NOTE:
             random_notes()
        else:
            if command == COMMAND_NEXT_FRET:
                fret_number += 1
                if fret_number > FRET_MAX:
                    fret_number = FRET_LOW
            if command == COMMAND_PREV_FRET:
                fret_number -= 1
                if fret_number < FRET_LOW:
                    fret_number = FRET_MAX
            if command == COMMAND_FRET_3:
                fret_number = 3
            if command == COMMAND_FRET_5:
                fret_number = 5
            if command == COMMAND_FRET_7:
                fret_number = 7
            if command == COMMAND_FRET_10:
                fret_number = 10
        
if __name__ == "__main__":
    main()

