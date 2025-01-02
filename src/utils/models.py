import click
import toml
import os
import subprocess
import mistune

from utils import MarkdownConverter

def search(config: list, key: tuple):
    for item in config:
        if key[0] in item:
            return item.get(key[0], key[1])
    return None

def readme_template(config: list):
    README = f"""
<div id="readme-top"></div>

<!-- PROJECT SHIELDS -->
[![Creator][creatorLogo]][creatorProfile]
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPL License][license-shield]][license-url]

<!-- PROJECT HEADER -->
# {search(config, ('title', '404'))}

{search(config, ('subtitle', 'No description provided.'))}

<!-- CALL TO ACTIONS -->
[![🚀 Explore Demo][demoLogo]][demoLogo-url]
[![🐛 Report Bug][bugLogo]][bugLogo-url]
[![✨ Request Feature][featureLogo]][featureLogo-url]

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#installation">Installation</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#setup">Setup</a></li>
      </ul></li>
    <li><a href="#usage">Usage</a>
      <ul>
        <li><a href="#getting-started">Getting Started</a></li>
        <li><a href="#advanced">Advanced</a></li>
      </ul></li>
    </li>
    <li><a href="#structure">Structure</a></li>
    <li><a href="#tasks">Tasks</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<br />

<!-- ABOUT THE PROJECT -->
## About The Project

The Open Source Software (OSS) community underpins countless businesses worldwide, with over 50% of Fortune 500 companies relying on it for their workflows—a number poised to grow as more projects gain traction. However, this growth hinges on consistent feature development, which is challenging without more developers. Research by Ravi Sen, Siddhartha S. Singh, and Sharad Borle found that adding 10 developers to a project increases average subscribers by 5.65%, demonstrating a clear link between developer engagement and user adoption.

Given this, OSS projects must prioritize lowering barriers to entry and welcoming community contributions—the very ethos of OSS. Unfortunately, this is far from the norm. A 2014 study revealed that only 5.4% of 2,000 projects included architectural documentation, a crucial tool for scaling and collaboration. While many OSS projects have achieved remarkable growth, more widespread emphasis on software architecture documentation could drive success for countless lesser-known initiatives.

Effective documentation should guide users and developers through a project’s purpose, workflow, and future direction. A basic overview and installation guide are insufficient; developers need clear navigation of the source code and actionable tasks, while users benefit from insight into future plans and transparent communication channels.

This README aims to set a standard for OSS documentation, improving project accessibility and fostering contributions from both the community and aspiring developers.

### Built With

Listing the major tools and languages used in the project helps it appear in filtered search results for any included library. Additionally, it allows developers to quickly identify whether a library they are proficient in is part of the project. Refer to the "Markdown Links and Images" section of the HTML version of this file to learn how these logo URLs are created.

[![Python][pythonLogo]][pythonLogo-url]
[![Markdown][markdownLogo]][markdownLogo-url]
[![HTML][htmlLogo]][htmlLogo-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Installation

This section should walk through installation on various operating systems as well as any installation options. The readability of this section will make or break whether someone will use the project, since this section is often the most looked at section

### Prerequisites
Ensure you have [git](https://git-scm.com/), [python][pythonLogo-url] (and presumably pip too). Best bet, download the official release for your platform (Operating System) from the provided homepages and their download section. On Windows, your best bet is to use the resulting Git Bash application that will become available after installing git.

Comfirm prerequisites by running the following command:
```bash
git --version && python --version && pip --version
```

Download and navigate into the repository:
```bash
git clone https://github.com/montymi/ClearDocs/ && cd ClearDocs
```

### Setup

Convert contents of README.md to the raw form, copy file and paste into your project. (Boring ik, that is a WIP for after the holidays 😊.)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Users are much more likely to use and test a project if they can quickly determine how best to use the software and whether or not it really is what they are looking for. Clear usage examples also give incoming developers a chance to better understand the code and its intended use.

*Here is an example from this project that hopefully won't stand for very long:*

### Getting Started

Manually convert the section information to fit project, including the URLs for tools, tests, and contact cards which need to be found, added, and called. 

### Advanced

TODO; Check [Tasks](#tasks) for updates coming soon!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- STRUCTURE -->
## Structure

Less than 6% of GitHub projects include documentation or diagrams about the software's architecture. Since larger projects can often have a very convoluted source code structure, diagrams are the ideal method of displaying the flow of the project. 

```
ClearDocs
├── README.md
├── src
│   ├── __init__.py
│   ├── cli.py
│   └── utils.py
└── docs
    ├── index.md
    ├── installation.md
    ├── usage.md
    ├── configuration.md
    ├── contributing.md
    ├── api
    │   └── overview.md
    ├── tutorials
    │   ├── getting_started.md
    │   └── advanced_features.md
    └── references
        ├── glossary.md
        └── faq.md
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- TASKS -->
## Tasks

By publicly displaying the to-do list of the project, users are able to see any feature that is nearing implementation. The list also allows new developers to quickly find potential tasks for them to complete which is an ideal way to familiarize them with the source code and to continue to make commits.

- [X] Emphasize 5.4% of projects section (speculation about what the observable differences would be if it were a higher figure)
- [X] Fix "Built With" logos section
- [X] Revision at the sentence level
- [X] Center architecture image
- [X] Add Author's Note
- [X] Fix some links
- [X] Change code examples to be ClearDocs project
- [ ] Add CLI capabilities for README creation
- [ ] Improve CLI with docs/ folder
- [ ] Automate deployment to gh-pages through CLI
- [ ] package and post to PIP

See the [open issues](https://github.com/montymi/ClearDocs/issues) for a full list of issues and proposed features.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are, in my opinion, the greatest part of OSS and are what will be the key to continuing the growth of the community. One of the main goals of this README is to facilitate contributions of potential developers. In this section, developers must be sure to lay out any coding styling choices that they may have so that the source code can remain as uniform as possible. One such project that has an immpressive contributions page is *htop* by [htop-dev](https://github.com/htop-dev/htop) who point all potential incoming contributors to their [style guide](https://github.com/htop-dev/htop/blob/main/docs/styleguide.md)

1. [Fork the Project](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. [Open a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

*Documentation must include a license section in which the type of license and a link or reference to the full license in the repository is given.*

Distributed under the GPL-3.0 License. See `LICENSE.txt` for more information.

<br />

<!-- CONTACT -->
## Contact

Michael Montanaro

[![LinkedIn][linkedin-shield]][linkedin-url] 
[![GitHub][github-shield]][github-url]

<br />

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list any resources used or that may be helpful in understanding the project

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[demoLogo]: https://img.shields.io/badge/🚀%20Explore%20Demo-grey?style=for-the-badge
[demoLogo-url]: https://github.com/montymi/ClearDocs
[bugLogo]: https://img.shields.io/badge/🐛%20Report%20Bug-grey?style=for-the-badge
[bugLogo-url]: https://github.com/montymi/ClearDocs/issues
[featureLogo]: https://img.shields.io/badge/✨%20Request%20Feature-grey?style=for-the-badge
[featureLogo-url]: https://github.com/montymi/ClearDocs/issues
[pythonLogo]: https://img.shields.io/badge/Python-black?style=for-the-badge&logo=python&logoColor=natural
[pythonLogo-url]: https://python.org/
[markdownLogo]: https://img.shields.io/badge/Markdown-black?style=for-the-badge&logo=markdown&logoColor=natural
[markdownLogo-url]: https://daringfireball.net/projects/markdown/
[htmlLogo]: https://img.shields.io/badge/HTML5-black?style=for-the-badge&logo=html5&logoColor=natural
[htmlLogo-url]: https://html.spec.whatwg.org/
[creatorLogo]: https://img.shields.io/badge/-Created%20by%20montymi-maroon.svg?style=for-the-badge
[creatorProfile]: https://montymi.com/
[contributors-shield]: https://img.shields.io/github/contributors/montymi/ClearDocs.svg?style=for-the-badge
[contributors-url]: https://github.com/montymi/ClearDocs/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/montymi/ClearDocs.svg?style=for-the-badge
[forks-url]: https://github.com/montymi/ClearDocs/network/members
[stars-shield]: https://img.shields.io/github/stars/montymi/ClearDocs.svg?style=for-the-badge
[stars-url]: https://github.com/montymi/ClearDocs/stargazers
[issues-shield]: https://img.shields.io/github/issues/montymi/ClearDocs.svg?style=for-the-badge
[issues-url]: https://github.com/montymi/ClearDocs/issues
[license-shield]: https://img.shields.io/github/license/montymi/ClearDocs.svg?style=for-the-badge
[license-url]: https://github.com/montymi/ClearDocs/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin
[linkedin-url]: https://linkedin.com/in/michael-montanaro
[github-shield]: https://img.shields.io/badge/-GitHub-black.svg?style=for-the-badge&logo=github
[github-url]: https://github.com/montymi
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
"""

class Project:
    def __init__(self, file: str, deploy: bool):
        self.file = file
        self.config = self.load_config()
        self.project_name = search(self.config.get('readme', {}), ('name', '404'))
        self.author = search(self.config.get('readme', []), ('author', 'Anonymous'))
        self.readme = Readme(self.config.get('readme', []))
        self.docs = Docs(self.config.get('docs', []))
        self.deploy = Deploy(self.project_name, deploy)
        self.actions = self.set_actions()

    def load_config(self):
        if not os.path.exists(self.file):
            default_template_path = os.path.join(os.path.dirname(__file__), '../docconfig.toml')
            if os.path.exists(default_template_path):
                with open(default_template_path, 'r') as f:
                    template = toml.load(f) or {}
                    with open(self.file, 'w') as f:
                        toml.dump(template, f)
                    return template
            else:
                raise Exception(f'Default template not found at {default_template_path}')
        try:
            with open(self.file, 'r+') as f:
                return toml.load(f) or {}
        except Exception as e:
            raise Exception(f'An error occurred while loading the configuration file: {e}')

    def set_actions(self):
        return {'initialize': self._init_project}
    
    def _init_project(self, action):
        try:
            self.readme.execute(action)
            click.echo('> README ☑')
            self.docs.execute(action)
            click.echo('> docs/ ☑')
            if self.deploy.state:
                self.deploy.execute(action)
                click.echo('> Deploy ☑')
            click.echo(f'> {self.project_name} ☑')
        except Exception as e:
            raise Exception(f'An error occurred during initialization: {e}')
    
    def execute(self, action: str):
        if action in self.actions:
            self.actions[action](action)

    def __str__(self):
        return f'{self.project_name or '404'} created by {self.author or 'Anonymous'}' 

class Readme:
    def __init__(self, config):
        self.project_name = search(config, ('name', '404'))
        self.description = search(config, ('description', 'No description provided.'))
        self.author = search(config, ('author', 'Anonymous'))
        self.actions = self.set_actions()

    def set_actions(self):
        return {'initialize': self._create_readme}
    
    def _create_readme(self):
        import pdb; pdb.set_trace()
        if os.path.exists('README.md'):
            if not click.confirm('README.md already exists. Overwrite?', abort=True):
                return
        try:
            converter = MarkdownConverter('docconfig.yml')        
            markdown_content = converter.convert_to_markdown()
            with open('README.md', 'w') as f:
                f.write(markdown_content)
        except Exception as e:
            raise Exception(f'An error occurred while creating the README: {e}')

    def execute(self, action):
        if action in self.actions:
            self.actions[action]()

class Docs: 
    def __init__(self, config):
        self.config = config
        self.actions = self.set_actions()

    def set_actions(self):
        return {'initialize': self._create_docs_index}
    
    def _create_docs_index(self):
        def create_docs_structure(base_path, structure):
            for item in structure:
                if isinstance(item, dict):
                    for key, value in item.items():
                        if isinstance(value, list):
                            dir_path = os.path.join(base_path, key.replace(' ', '-').lower())
                            os.makedirs(dir_path, exist_ok=True)
                            create_docs_structure(dir_path, value)
                        else:
                            file_path = os.path.join(base_path, value)
                            os.makedirs(os.path.dirname(file_path), exist_ok=True)
                            open(file_path, 'a').close()
                else:
                    file_path = os.path.join(base_path, item)
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    open(file_path, 'a').close()

        def create_docs():
            try:
                create_docs_structure('docs', self.config)
            except Exception as e:
                raise Exception(f'An error occurred while creating the docs structure: {e}')
    
        create_docs()

    def execute(self, action):
        if action in self.actions:
            self.actions[action]()

class Deploy:
    def __init__(self, project_name, state):
        self.project_name = project_name
        self.state = state
        self.actions = self.set_actions()

    def set_actions(self):
        return {'initialize': self.deploy_to_github_pages}

    def deploy_to_github_pages(self, project_name):
        # Logic to deploy the documentation to GitHub Pages
        pass

    def execute(self, action):
        if action in self.actions:
            self.actions[action](self.project_name)