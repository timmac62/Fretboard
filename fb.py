# fb.py
# refactored the fretboard table creation code
#
# TODO: eliminate extra ,menu for guess note - do everything from main menu
# TODO: ensure proper commenting and PEP8 for readability
# TODO: refactor random_notes to use table
# TODO: convert to layout and live 
#
import click
from rich import print
from rich import box
from rich.console import Console
from rich.theme import Theme
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

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
COMMAND_GUESS_NOTE  = 'N'
COMMAND_MAIN_MENU   = 'M'
COMMAND_QUIT        = 'Q'

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

def guess_which_note():
    """
    Guess which note is randomly selected
    """
    command = COMMAND_NONE
    while command != COMMAND_MAIN_MENU:
        string_number = random.randint(STRING1, STRING6)
        fret_number = random.randint(FRET_LOW, FRET_MAX)
        string = "string" + str(string_number)
        note = fretboard[string][fret_number] # print(fretboard["string1"][10]) # prints D

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


def display_fretboard(which_note):
    """
    display the notes of our fretboard
    """
    console.clear()
    console.rule(f"[bold blue]:guitar: Fretboard Fundamentals :guitar:[/]\n")

    table = Table(
        title=f"Guitar Fretboard - Standard Tuning",
        style="green",
        box=box.SIMPLE_HEAVY,
        padding=0,
    )
    for fret in range(13):
        table.add_column(
            str(fret), style="normal_fret", justify="center"
        )
    for string_number in range(STRING1, STRING6+1):
        string_key = "string" + str(string_number)
        notes = []
        for note in fretboard[str(string_key)]:
            note_label = Text(str(note), style="normal_fret")
            if note == which_note:
                note_label.stylize("highlighted_fret")
            notes.append(note_label)
        table.add_row(*notes)

    console.print(table, justify="center")
    console.rule(f"[bold blue]:musical_notes: Master Your Axe! :musical_notes:[/]\n")


@click.command()
def main():
    """
    A simple fretboard practice tool which aims to help you learn all of
    the notes on a standard tuned guitar fretboard

    Menu:

        C, G, D, A, E, B, F - highlight that note on the main fretboard
        Space: highlight no notes
        N: Guess a note, guess which note is randomly selected
        Q: Quit application

    """
    command = COMMAND_NONE
    note_to_highlight = ' '
    while command != COMMAND_QUIT:
        display_fretboard(note_to_highlight)
        command = console.input(
            "\nQ - Quit, N - Guess Note: "
        ).upper()

        if command == COMMAND_GUESS_NOTE:
             guess_which_note()
        else:
            if command in fretboard["string1"]:
                note_to_highlight = command
            elif command == COMMAND_NONE:
                note_to_highlight = COMMAND_NONE
        
if __name__ == "__main__":
    main()
