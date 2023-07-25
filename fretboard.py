# fretboard.py
import click
from rich.console import Console
import random

STRING1 = 0
STRING2 = 1
STRING3 = 2
STRING4 = 3
STRING5 = 4
STRING6 = 5

FRET_LOW = 0
FRET_MAX = 12

string_number = random.randint(STRING1, STRING6)
fret_number = random.randint(FRET_LOW, FRET_MAX)

console = Console(width=80)

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
    console.clear()
    console.rule(f"[bold blue]:leafy_green: Fretboard Fundamentals :leafy_green:[/]\n")

    # print(f"fretboard practice - string: {string_number} fret: {fret_number}")
    # print("D#" in fretboard["string2"])

    # console.input note

    notes = 2 * "A A# B C C# D D# E F F# G G# "
    # notes = "A A# B C C# D D# E F F# G G# "

    lookup = {}
    for start_note in "EADGB":
        index = notes.index(start_note)
        lookup[start_note] = notes[index:].split()[:12]

    print(f'Fret 2 of the E string is: {lookup["E"][2]}')
    print(f'Fret 10 of the A string is: {lookup["A"][10]}')

    print(f'E string: {lookup["E"]}')
    print(f'D string: {lookup["D"]}')


if __name__ == "__main__":
    main()


