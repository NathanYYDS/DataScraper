import click
from datascraper.platform.config import init_platform_config

@click.group()
def cli():
    """DataScraper CLI Tool"""
    pass

@cli.command(name="platform")
@click.option('--init', '-i', is_flag=True, help='Initialize platform config file.')
def platform_command(init):
    if init:
        init_platform_config()

if __name__ == '__main__':
    cli()