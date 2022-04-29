import click

from sigil.storage.cli import storage

cli = click.Group(name="cli")
cli.add_command(storage)

cli()
