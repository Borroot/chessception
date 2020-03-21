#!/usr/bin/env python3

import click
from controller.handler import Controller


@click.command()
@click.option('--ui', type=click.Choice(['gui', 'tui']), default='tui', show_default=True)
@click.option('--mic/--no-mic', default=False, show_default=True)
@click.option('--arm/--no-arm', default=False, show_default=True)
def main(ui, mic, arm):
    """
    A program to play chess with a robot arm and speech recognition.
    """
    Controller(ui, mic, arm)


if __name__ == "__main__":
    main()
