<div id="readme-top"></div>

<!-- PROJECT SHIELDS -->
[![Creator][creatorLogo]][creatorProfile]
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPL License][license-shield]][license-url]

<!-- PROJECT HEADER -->
# ClearDocs

OSS Documentation Assistant. Dynamically create README and docs for your projects. 

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

ClearDocs requires Python 3.10 or newer. From this repository:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Usage

Run ClearDocs in the project you want to document:

```bash
cleardocs init --template standard --hosting github-pages
cleardocs serve
cleardocs build --strict
```

`init` creates a Material for MkDocs site, copies an existing README into
`docs/index.md`, and creates `requirements-docs.txt`. The standard template also
includes getting started, configuration, and contributing pages. Use
`--template minimal` for just the homepage, `--site-name "My Project"` to set the
title, or pass a target directory: `cleardocs init path/to/project`.

Existing scaffold files are protected by default. `--force` explicitly replaces
conflicting generated files. The original README is never changed by `init`.
README links and image paths may need adjusting when copied into `docs/`.
Generated files belong to your project and work directly with MkDocs; ClearDocs
is not needed to host the resulting site.

Create a README separately:

```bash
cleardocs readme --name "My Project" --description "What the project does"
```

An existing README is preserved unless you pass `--force`. Review generated
placeholder sections before publishing.

### GitHub Pages

`--hosting github-pages` generates `.github/workflows/docs.yml`. In the target
repository, open **Settings → Pages** and select **GitHub Actions** as the build
source. Commit and push the generated files to `main`. If your default branch
has another name, update the workflow branch filter. Pull requests build and
validate the docs; pushes to `main` and manual workflow runs build and deploy.
The workflow installs only `requirements-docs.txt`, so the target project does
not need ClearDocs installed in CI. Any configured GitHub environment protection
rules still apply. No Terraform or cloud credentials are required.

To host elsewhere, upload the contents of `site/` after `cleardocs build`.
Custom domains and additional hosting providers are not configured automatically.

### Development

```bash
python -m unittest discover -s tests -v
```

The suite exercises scaffold protection, README generation, strict MkDocs builds,
and command failure handling. `cleardocs serve --dev-addr 127.0.0.1:8000` starts
the preview server. Both `serve` and `build` accept `--config-file path/to/mkdocs.yml`.

<!-- STRUCTURE -->
## Structure

Less than 6% of GitHub projects include documentation or diagrams about the software's architecture. Since larger projects can often have a very convoluted source code structure, diagrams are the ideal method of displaying the flow of the project. 

```
ClearDocs
├── README.md
├── requirements.txt
├── setup.py
├── src/cleardocs
│   ├── __init__.py
│   └── cli.py
└── tests
    └── test_cli.py
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
- [X] Add CLI capabilities for README creation
- [X] Improve CLI with docs/ folder
- [X] Generate GitHub Pages deployment workflow through CLI
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

[linkedin-shield]: https://cdn-icons-png.flaticon.com/512/174/174857.png
[github-shield]: https://cdn-icons-png.flaticon.com/512/733/733553.png
[linkedin-url]: https://linkedin.com/in/michael-montanaro
[github-url]: https://github.com/montymi

<a href="https://linkedin.com/in/michael-montanaro/" target="_blank">
  <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20" height="20" />
</a>
<a href="https://github.com/montymi/" target="_blank">
  <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" width="20" height="20" />
</a>

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
