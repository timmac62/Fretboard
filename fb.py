# fb.py
import click
from rich import print
from rich.console import Console
from rich.theme import Theme
from rich.panel import Panel

import random

STRING1 = 1
STRING2 = 2
STRING3 = 3
STRING4 = 4
STRING5 = 5
STRING6 = 6

FRET_LOW = 0
FRET_MAX = 12

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

custom_theme = Theme({
    "guess_wrong": "bold red",
    "guess_right":  "green",
})

console = Console(width=80)

def display_menu():
    console.clear()
    console.rule(f"[bold blue]:guitar: Fretboard Fundamentals:guitar:[/]\n")
    console.print(f"\n[bold white]Enhance your knowledge of the fretboard[/]\n", justify="center")
    console.print(f"[bold red]And master your Axe[/]\n", justify="center")
    console.rule(f"[bold blue]:guitar: Q to Quit, N Another Note :guitar:[/]\n")

    # print(Panel.fit("E"), Panel.fit("F"))


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
    command = ' '
    while command != 'Q':
        string_number = random.randint(STRING1, STRING6)
        fret_number = random.randint(FRET_LOW, FRET_MAX)
        string = "string"+str(string_number)
        note = fretboard[string][fret_number]
        console.clear()
        console.rule(f"[bold blue]:guitar: Fretboard Fundamentals:guitar:[/]\n")
        console.print(f"\n[bold white]What note is at the {string_names[string_number-1]} string fret {fret_number} / S{string_number}F{fret_number}?[/]\n", justify="center")
        console.rule(f"[bold blue]:guitar: Master Your Axe! :guitar:[/]\n")

        guess = console.input("\nYour guess: ").upper()
        if guess == note:
            console.print(f"\n[green]CORRECT[/]")
        else:
            console.print(f"\n[bold red]WRONG[/], the correct note is {note}")
        
        command = console.input("\nTry again? (Any key - guess again, Q - quit): ").upper()


if __name__ == "__main__":
    main()


