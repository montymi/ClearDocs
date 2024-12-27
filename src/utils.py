import click
import yaml

MKDOCS_YML_PATH = 'mkdocs.yml'

class Project:
    def __init__(self, project_name: str, description: str, author: str, deploy: bool=False):
        self.project_name = project_name
        self.description = description
        self.author = author
        self.isDeploying = deploy
        self.readme = Readme(self.project_name, self.description, self.author)
        self.docs = Docs(self.project_name, self.description)
        self.deploy = Deploy(self.project_name)
        self.actions = self.set_actions()


    def update_site_name(self, new_name):
        with open(MKDOCS_YML_PATH, "r") as file:
            config = yaml.safe_load(file)
        
        # Ensure 'extra' exists
        if 'extra' not in config:
            config['extra'] = {}

        # Update the site name
        config['extra']['site_name'] = new_name

        # Write back to the mkdocs.yml file
        with open(MKDOCS_YML_PATH, "w") as file:
            yaml.dump(config, file, default_flow_style=False)


    def set_actions(self):
        return {'initialize': self._init_project}
    
    def _init_project(self, action):
        try:
            self.update_site_name(self.project_name)
            self.readme.execute(action)
            click.echo('> README ☑')
            self.docs.execute(action)
            click.echo('> docs/ ☑')
            if self.isDeploying:
                self.deploy.execute(action)
                click.echo('> README ☑')
            click.echo(f'> {self.project_name} ☑')
        except Exception as e:
            raise Exception(f'An error occurred: {e}')

    
    def execute(self, action: str):
        if action in self.actions:
            self.actions[action](action)

    def __str__(self):
        return f'{self.project_name} created by {self.author}' 

class Readme:
    def __init__(self, project_name, description, author):
        self.project_name = project_name
        self.description = description
        self.author = author
        self.actions = self.set_actions()

    def set_actions(self):
        return {'initialize': self._create_readme}
    
    def _create_readme(self, project_name, description, author):
        with open('README.md', 'w') as f:
            f.write(f"# {project_name}\n\n")
            f.write(f"\nCreated by: {author}\n\n")
            f.write(f"## Description\n{description}\n\n")
            f.write("## Installation\n\n")
            f.write("## Usage\n\n")

    def execute(self, action):
        if action in self.actions:
            self.actions[action](self.project_name, self.description, self.author)

class Docs: 
    def __init__(self, project_name, description):
        self.project_name = project_name
        self.description = description
        self.actions = self.set_actions()

    def set_actions(self):
        return {'initialize': self._create_docs_index}
    
    def _create_docs_index(self, project_name, description):
        with open('docs/index.md', 'w') as f:
            f.write(f"# {project_name} Documentation\n\n")
            f.write(f"## Description\n{description}\n\n")
            f.write("## Installation Instructions\n\n")
            f.write("## Usage Examples\n\n")

    def execute(self, action):
        if action in self.actions:
            self.actions[action](self.project_name, self.description)

class Deploy:
    def __init__(self, project_name):
        self.project_name = project_name
        self.actions = self.set_actions()

    def set_actions(self):
        return {'initialize': self.deploy_to_github_pages}

    def deploy_to_github_pages(self, project_name):
        # Logic to deploy the documentation to GitHub Pages
        pass

    def execute(self, action):
        if action in self.actions:
            self.actions[action](self.project_name)