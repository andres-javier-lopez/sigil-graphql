import asyncio

import click

from sigil.store import actions

store = click.Group(name="store", help="Manage the system store")


async def _init_command():
    click.echo("Creating new store")
    await actions.init()
    click.echo("Store created")


@click.command(name="init", help="Initialize the system store (destroys existing data)")
def init_command():
    asyncio.run(_init_command())


async def _seed_command(init):
    if init:
        await _init_command()

    click.echo("Seeding your store")
    await actions.seed()
    click.echo("Seed complete")


@click.command(name="seed", help="Add initial data to system")
@click.option(
    "--init/--no-init",
    default=False,
    help="Store is initialized before seeding (default: false)",
)
def seed_command(init):
    asyncio.run(_seed_command(init))


async def _upgrade_command():
    click.echo("Upgrading store to latest version")
    await actions.upgrade()
    click.echo("Upgrade finished")


@click.command(name="upgrade", help="Upgrade store to latest version")
def upgrade_command():
    asyncio.run(_upgrade_command())


store.add_command(init_command)
store.add_command(seed_command)
store.add_command(upgrade_command)
