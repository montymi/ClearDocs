"""ClearDocs command line interface."""
import json
from pathlib import Path
import subprocess
import sys

import click


WORKFLOW = '''name: Documentation
on:
  push:
    branches: [main]
  pull_request:
  workflow_dispatch:
permissions:
  contents: read
concurrency:
  group: pages-${{ github.ref }}
  cancel-in-progress: true
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: python -m pip install -r requirements-docs.txt
      - run: python -m mkdocs build --strict
      - uses: actions/upload-pages-artifact@v3
        if: github.event_name != 'pull_request'
        with:
          path: site
  deploy:
    if: github.event_name != 'pull_request'
    needs: build
    runs-on: ubuntu-latest
    permissions:
      pages: write
      id-token: write
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/deploy-pages@v4
        id: deployment
'''
DOC_REQUIREMENTS = 'mkdocs==1.6.1\nmkdocs-material==9.6.14\n'


def write_files(root, files, force=False):
    """Preflight every destination before writing any scaffold file."""
    for name in files:
        target = root / name
        for path in [target, *target.parents]:
            if path == root.parent:
                break
            if path.is_symlink():
                raise click.ClickException(f'Refusing symlink destination: {path}')
        if target.exists() and (not force or not target.is_file()):
            raise click.ClickException(f'{target} already exists; use --force to replace files.')
        for parent in target.parents:
            if parent == root.parent:
                break
            if parent.exists() and not parent.is_dir():
                raise click.ClickException(f'{parent} is not a directory.')
    for name, content in files.items():
        target = root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding='utf-8')
        click.echo(f'Created {target}')


@click.group()
@click.version_option()
def main():
    """Initialize, preview, and build project documentation."""


@main.command()
@click.argument('path', type=click.Path(path_type=Path, file_okay=False), default='.')
@click.option('--site-name', help='Defaults to the project directory name.')
@click.option('--template', type=click.Choice(['minimal', 'standard']), default='standard', show_default=True)
@click.option('--hosting', type=click.Choice(['none', 'github-pages']), default='none', show_default=True)
@click.option('--force', is_flag=True, help='Replace conflicting generated files.')
def init(path, site_name, template, hosting, force):
    """Create a MkDocs site in an existing or new project directory."""
    root = path.resolve()
    title = site_name or root.name
    nav = '  - Home: index.md\n'
    files = {'requirements-docs.txt': DOC_REQUIREMENTS}
    readme_path = root / 'README.md'
    files['docs/index.md'] = (readme_path.read_text(encoding='utf-8')
                              if readme_path.is_file() else f'# {title}\n\nWelcome to the project documentation.\n')
    if template == 'standard':
        nav += '  - Getting started: getting-started.md\n  - Configuration: configuration.md\n  - Contributing: contributing.md\n'
        files.update({
            'docs/getting-started.md': '# Getting started\n\nDescribe installation and a first working example here.\n',
            'docs/configuration.md': '# Configuration\n\nDocument project settings and environment variables here.\n',
            'docs/contributing.md': '# Contributing\n\nDescribe the development workflow and how to run tests here.\n',
        })
    files['mkdocs.yml'] = f'site_name: {json.dumps(title)}\ntheme:\n  name: material\nnav:\n{nav}'
    if hosting == 'github-pages':
        files['.github/workflows/docs.yml'] = WORKFLOW
    write_files(root, files, force)
    click.echo('Install: python -m pip install -r requirements-docs.txt\nPreview: cleardocs serve\nValidate: cleardocs build --strict')
    if hosting == 'github-pages':
        click.echo('In GitHub Settings > Pages, select GitHub Actions as the source. Commit and push the generated files to main to publish.')


@main.command()
@click.argument('path', type=click.Path(path_type=Path, file_okay=False), default='.')
@click.option('--name', help='Defaults to the project directory name.')
@click.option('--description', default='Describe what your project does.')
@click.option('--force', is_flag=True, help='Replace an existing README.md.')
def readme(path, name, description, force):
    """Generate a project README without replacing one by default."""
    root = path.resolve()
    title = name or root.name
    content = f'# {title}\n\n{description}\n\n## Installation\n\nDescribe installation here.\n\n## Usage\n\nAdd a working example here.\n\n## Contributing\n\nContributions are welcome. Please open an issue or pull request.\n\n## License\n\nSee the project license.\n'
    write_files(root, {'README.md': content}, force)


def run_mkdocs(command, config_file, extra):
    if not config_file.is_file():
        raise click.ClickException(f'Configuration not found: {config_file}. Run cleardocs init first.')
    result = subprocess.run([sys.executable, '-m', 'mkdocs', command, '-f', str(config_file), *extra])
    if result.returncode:
        raise click.exceptions.Exit(result.returncode)


@main.command()
@click.option('--config-file', '-f', type=click.Path(path_type=Path), default='mkdocs.yml')
@click.option('--strict/--no-strict', default=True, show_default=True)
def build(config_file, strict):
    """Build the site, treating documentation warnings as errors by default."""
    run_mkdocs('build', config_file, ['--strict'] if strict else [])


@main.command()
@click.option('--config-file', '-f', type=click.Path(path_type=Path), default='mkdocs.yml')
@click.option('--dev-addr', default='127.0.0.1:8000', show_default=True)
def serve(config_file, dev_addr):
    """Preview documentation using the MkDocs development server."""
    run_mkdocs('serve', config_file, ['--dev-addr', dev_addr])
