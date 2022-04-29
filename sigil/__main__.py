import click

from sigil.store.cli import store

cli = click.Group(name="cli")
cli.add_command(store)

cli()
