<div id="readme-top"></div>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h2 align="center">Reviving OSS Documentation</h2>

  <p align="center">
    Created by: Michael Montanaro
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/montymi/ClearDocs">View Demo</a>
    ·
    <a href="https://github.com/montymi/ClearDocs/issues">Report Bug</a>
    ·
    <a href="https://github.com/montymi/ClearDocs/issues">Request Feature</a>
  </p>
</div>



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
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#structure">Structure</a></li>
    <li><a href="#tasks">Tasks</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The Open Source Software (OSS) community is the backbone of countless businesses around the world, with more than 50% of Fortune 500 companies relying on it in their workflow. That number is set to continue to grow as more open source projects advance and gain traction in the work force, which will only happen with consistent feature implementation. In a study done by Ravi Sen, Siddhartha S. Singh, and Sharad Borle, it was found that "an increase in the number of developers by 10 leads to a 5.65% increase in the average number of subscribers." As is evident by the statistic, there is a direct correlation to the number of workers on a project and the number of users/subscribers to the service that is being created. 

This would lead you to believe that the OSS community should be doing everything in its power to lower the projects barrier of entry and welcome edits and suggestions from the community, which is the main goal of OSS. However, not only is this not a priority, but structural documentation is usually omitted altogether, with only 5.4% of 2000 projects investigated in a 2014 study having any sort of architecture documentation.

Documentation must serve to guide a user or possible developer through the project's intended use case as well as the current workflow and future plans. It isn't enough to just have a brief explanation of the project and an installation guide with a few use case examples. Outside developers must be able to quickly navigate the source code and pick up on the tasks that are waiting to be completed. Users should have a sense of the future plans for the project as well as a clear means of communicating with the current developers. 

This README hopes to serve as a template for what documentation should look like in order to greatly improve the approachability of OSS projects and encourage more contribution from the community and any newcomers trying to grow as a programmer. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

List the major libraries used in the project, this will help with filtering search results as well as allowing a developer to quickly see if a library they are well-versed in is a part of the project. Leave any add-ons/plugins for the acknowledgements section.

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

*Here is an example of installation instructions by one of the largest Python projects on GitHub: **cpython**.*

On Unix, Linux, BSD, macOS, and Cygwin:

```
./configure
make
make test
sudo make install
```
This will install Python as python3.

You can pass many options to the configure script; run ./configure --help to find out more. On macOS case-insensitive file systems and on Cygwin, the executable is called python.exe; elsewhere it's just python.

Building a complete Python installation requires the use of various additional third-party libraries, depending on your build platform and configure options. Not all standard library modules are buildable or useable on all platforms. Refer to the Install dependencies section of the Developer Guide for current detailed information on dependencies for various Linux distributions and macOS.

On macOS, there are additional configure and build options related to macOS framework and universal builds. Refer to Mac/README.rst.

On Windows, see PCbuild/readme.txt.

If you wish, you can create a subdirectory and invoke configure from there. For example:

```
mkdir debug
cd debug
../configure --with-pydebug
make
make test
```
(This will fail if you also built at the top-level directory. You should do a make clean at the top-level first.)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Users are much more likely to use and test a project if they can quickly determine how best to use the software and whether or not it really is what they are looking for. Clear usage examples also give incoming developers a chance to better understand the code and its intended use.

*Here is an example from a project for getting the weather via CLI by [genuinetools](https://github.com/genuinetools)*

```
# get the current weather in your current location
$ weather

# change the units to metric
$ weather -l "Paris, France" -u si

# it will auto guess the units though so changing
# the location to paris will change the units to `si`
$ weather -l "Paris, France"

# get three days forecast for NY
$ weather -l 10028 -d 3

# or you can autolocate and get three days forecast
$ weather -d 3

# get the weather in Manhattan Beach, CA
# even includes alerts
$ weather -l "Manhattan Beach, CA"
#                             .;odc
#                           ;kXNNNO
#                         .0NNO0NN:
#                        'XNK; dNNl
#                        KNX'  'XNK.
#                       ,NNk    cXNK,
#                       ,NNk     '0NNO:.
#                     .'cXNXl;,.   ,xXNNKOxxxk0Xx
#                 'lOXNNNNNNNNNNXOo'  ':oxkOXNNXc
#               cKNNKd:'.    ..;d0NNKl    ,xXNK,
#        .;:cclKNXd.              .oXNXxOXNNXl
#    .cOXNNNNNNNO.                  .kNNNNNNNXOc.
#   lXNXx;.    .                      .    .;dXNXo
#  ONNd.                                       oXN0.
# dNNo                                          cNNk
# XNN.                                           NNX
# 0NN'                                          .NNK
# ;XN0.                                        .ONNc
#  ;XNXo.                                    .lXNX:
#   .oXNX0dlcclx0Xo.              .oXKxlccldOXNXd.
#      ,lk0KXXK0xKNN0o;..    ..;o0NNKx0KXXX0ko,
#                 'lOXNNNNNNNNNNXOo,
#                     :x0XNNX0x:.
#
#
# Current weather is Partly Cloudy in Manhattan Beach in California for July 14 at 4:14am EDT
# The temperature is 69.2°F, but it feels like 69.2°F
#
# Special Weather Statement for Los Angeles, CA
# ...THREAT OF MONSOONAL THUNDERSTORMS LATE TONIGHT THROUGH WEDNESDAY...
# A STRONG UPPER LEVEL HIGH PRESSURE SYSTEM CURRENTLY CENTERED OVER NEVADA
# WILL BRING INCREASING EAST TO SOUTHEAST FLOW OVER SOUTHERN
# CALIFORNIA. AS A RESULT...A SIGNIFICANT SURGE OF MONSOONAL MOISTURE
# WILL MOVE INTO SOUTHWEST CALIFORNIA LATE TONIGHT THROUGH WEDNESDAY.
# THE GREATEST THREAT OF SHOWERS AND THUNDERSTORMS WILL BE ACROSS THE
# MOUNTAINS AND ANTELOPE VALLEY LATE TONIGHT INTO TUESDAY. DUE TO THE
# EASTERLY UPPER LEVEL FLOW ON MONDAY...THERE WILL ALSO BE A SLIGHT
# CHANCE OF SHOWERS AND THUNDERSTORMS ACROSS MOST COASTAL AND VALLEY
# AREAS.
# THE DEEPER MONSOONAL MOISTURE WILL BRING THE POTENTIAL FOR BRIEF HEAVY
# RAINFALL WITH STORMS THAT DEVELOP ON MONDAY AND TUESDAY...ESPECIALLY
# ACROSS THE MOUNTAINS AND ANTELOPE VALLEY. WHILE STORMS ARE EXPECTED
# TO BE FAST MOVING...THERE WILL BE THE POTENTIAL FOR LOCALIZED FLOODING
# OF ROADWAYS AND ARROYOS. ON TUESDAY...THE THREAT OF THUNDERSTORMS IS
# EXPECTED TO REMAIN CONFINED TO THE MOUNTAINS AND DESERTS. WITH WEAKER
# UPPER LEVEL WINDS ON TUESDAY...STORMS WILL LIKELY MOVE SLOWER. AS A
# RESULT...THERE WILL BE AN INCREASED THREAT OF FLASH FLOODING.
# IT WILL NOT BE AS HOT ACROSS MUCH OF THE REGION TOMORROW DUE TO THE
# INCREASED MOISTURE AND CLOUD COVERAGE...WITH INTERIOR SECTIONS
# GENERALLY REMAINING IN THE 90S. HOWEVER...THERE WILL BE A
# SIGNIFICANT INCREASE IN HUMIDITY ON MONDAY THAT WILL CONTINUE TO
# BRING DISCOMFORT.
# ANYONE PLANNING OUTDOOR ACTIVITIES IN THE MOUNTAINS AND DESERTS
# DURING THE NEXT FEW DAYS SHOULD CAREFULLY MONITOR THE LATEST
# NATIONAL WEATHER SERVICE FORECASTS AND STATEMENTS DUE TO THE
# POTENTIAL HAZARDS ASSOCIATED WITH THUNDERSTORMS.
#             Created: July 13 at 10:50pm EDT
#             Expires: July 14 at 7:00pm EDT
#
# Ick! The humidity is 85%
# The nearest storm is 18 miles NE away
# The wind speed is 3.96 mph SE
# The cloud coverage is 35%
# The visibility is 9.58 miles
# The pressure is 1012.99 mbar
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- STRUCTURE -->
## Structure

As is stated above, less than 6% of GitHub projects include documentation or diagrams about the software's architecture. Since larger projects can often have a very convoluted source code structure, diagrams are the ideal method of displaying the flow of the project. 

*Here is an example given by the official [PlantUML](https://github.com/plantuml-stdlib/C4-PlantUML) GitHub page which utilizes both graphical and verbal descriptions to portray the workflow of a web application.*

<img align="center" width="830" alt="Example software architecture drawn via PlantUML" src="https://user-images.githubusercontent.com/84359773/201444996-30331b8e-69c2-4440-bf0b-a79610282772.png">

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- TASKS -->
## Tasks

By publicly displaying the to-do list of the project, it helps users to see any feature that is nearing implementation. The list also allows new developers to quickly find potential tasks for them to complete which is a wonderful way to get them familiarized with the source code and continuing to make commits.

- [ ] Add Multi-Language Support
- [ ] Add Additional Structural Templates w/ Examples
- [ ] Add Example Project to Repository

See the [open issues](https://github.com/montymi/ClearDocs/issues) for a full list of issues and proposed features.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are, in my opinion, the greatest part of OSS and is what will be the key to continuing the growth of the community. One of the main goals of this README is to make contributing a lot easier for potential developers. In this section, developers must be sure to layout any coding styling choices that you may have so that the source code can remain as uniform as possible. One such project that has an incredible contributions page is *htop* by [htop-dev](https://github.com/htop-dev/htop) who point all potential incoming contributors to their [style guide](https://github.com/htop-dev/htop/blob/main/docs/styleguide.md)

1. [Fork the Project](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. [Open a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

*Documentation must include a license section in which the type of license and a link or reference to the full license in the repository is given.*

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Michael Montanaro - [LinkedIn](https://www.linkedin.com/in/michael-montanaro/) - montanaro.m@northeastern.edu

Project Link: [https://github.com/montymi/ClearDocs](https://github.com/montymi/ClearDocs)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



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
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/montymi
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
