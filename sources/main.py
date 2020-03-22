from controller.controller import Controller
from view.gui import Gui
from view.tui import Tui
import click

@click.command()
@click.option('--ui', type=click.Choice(['gui', 'tui']), default='tui', show_default=True)
@click.option('--mic/--no-mic', default=False, show_default=True)
@click.option('--arm/--no-arm', default=False, show_default=True)
def main(ui, mic, arm):
    """
    A program to play chess with a robot arm and speech recognition.
    """
    if ui == 'tui':
        Tui(mic, arm)
    else:  # ui == 'gui'
        Gui(mic, arm)

if __name__ == "__main__":
    main()
