import os
import click
from utils.models import Project

@click.command()
@click.option('--file', default='docconfig.yml', help='The configuration file for the project documentation.')
@click.option('--deploy', is_flag=True, help='Deploy the project documentation to a remote server.')
def initialize(file: str= 'docconfig.yml', deploy: bool = False):
    """Initialize the project documentation and setup."""

    try:
        project = Project(file, deploy)
        project.execute("initialize")

        click.echo(f'Project documentation successfully initialized for {project}.')
    except Exception as e:
        click.echo(f'An error occurred from call: {e}')
        return

if __name__ == '__main__':
    initialize()