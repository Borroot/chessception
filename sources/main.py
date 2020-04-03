from view.gui import Gui
from view.tui import Tui
import click


@click.command()
@click.option('--ui', type=click.Choice(['gui', 'tui']), default='tui', show_default=True)
@click.option('--mic/--no-mic', default=False, show_default=True)
@click.option('--arm/--no-arm', default=False, show_default=True)
@click.option('--enc', type=click.Choice(['unicode', 'ascii']), default='ascii', show_default=True)
def main(ui, mic, arm, enc):
    """
    A program to play chess with a robot arm and speech recognition.
    """
    unicode = True if enc == 'unicode' else False
    if ui == 'tui':
        Tui(mic, arm, unicode)
    else:  # ui == 'gui'
        Gui(mic, arm, unicode)


if __name__ == "__main__":
    main()
