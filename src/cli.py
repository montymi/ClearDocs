import os
import click
from utils import create_readme, create_docs_index, deploy_to_github_pages

@click.command()
@click.option('--project-name', prompt='Project name', help='The name of your project.')
@click.option('--description', prompt='Project description', help='A brief description of your project.')
@click.option('--author', prompt='Your name', help='Your name for the documentation.')
def initialize(project_name, description, author):
    """Initialize the project documentation and setup."""
    # Create README.md
    create_readme(project_name, description, author)

    # Create docs folder and index.md
    create_docs_index(project_name, description)

    # Link project with documentation
    click.echo(f'Project "{project_name}" documentation initialized.')

    # Deploy to GitHub Pages
    deploy_to_github_pages(project_name)

if __name__ == '__main__':
    initialize()