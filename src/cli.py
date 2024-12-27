import os
import click
from utils import Project

@click.command()
@click.option('--project-name', prompt='Project name', help='The name of your project.')
@click.option('--description', prompt='Project description', help='A brief description of your project.')
@click.option('--author', prompt='Your name', help='Your name for the documentation.')
@click.option('--deploy', is_flag=True, help='Deploy the documentation to GitHub Pages.')
def initialize(project_name: str, description: str, author: str, deploy: bool):
    """Initialize the project documentation and setup."""

    try:
        project = Project(project_name, description, author, deploy)
        project.execute("initialize")

        click.echo(f'Project documentation successfully initialized for {project}.')
    except Exception as e:
        click.echo(f'An error occurred: {e}')
        return

if __name__ == '__main__':
    initialize()