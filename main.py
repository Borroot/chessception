import click
from controller.controller import Controller

@click.command()
@click.option('--ui', type=click.Choice(['gui', 'tui']), default='tui', show_default=True)
@click.option('--mic/--no-mic', default=False, show_default=True)
def main(ui, mic):
    """
    A program to play chess with a robot arm and speech recognition.
    """
    Controller(ui, mic)

if __name__ == "__main__":
    main()
