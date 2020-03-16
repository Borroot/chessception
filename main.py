import click
from controller.controller import Controller

@click.command()
@click.option('--ui', type=click.Choice(['gui', 'tui']), default='gui', show_default=True)
def main(ui):
    """
    A program to play chess with a robot arm and speech recognition.
    """
    Controller(ui)

if __name__ == "__main__":
    main()
