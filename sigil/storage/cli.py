import asyncio

import click

from sigil.storage import actions

storage = click.Group(name="storage", help="Manage the system storage")


async def _init_command():
    click.echo("Creating new storage")
    await actions.init()
    click.echo("Storage created")


@click.command(
    name="init", help="Initialize the system storage (destroys existing data)"
)
def init_command():
    asyncio.run(_init_command())


async def _seed_command(init):
    if init:
        await _init_command()

    click.echo("Seeding your storage")
    await actions.seed()
    click.echo("Seed complete")


@click.command(name="seed", help="Add initial data to system")
@click.option(
    "--init/--no-init",
    default=False,
    help="Storage is initialized before seeding (default: false)",
)
def seed_command(init):
    asyncio.run(_seed_command(init))


async def _upgrade_command():
    click.echo("Upgrading storage to latest version")
    await actions.upgrade()
    click.echo("Upgrade finished")


@click.command(name="upgrade", help="Upgrade storage to latest version")
def upgrade_command():
    asyncio.run(_upgrade_command())


storage.add_command(init_command)
storage.add_command(seed_command)
storage.add_command(upgrade_command)
