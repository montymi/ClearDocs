from pathlib import Path
import runpy
from setuptools import setup, find_packages # type: ignore

setup(
    name='cleardocs',
    version=runpy.run_path(str(Path(__file__).parent / 'src/cleardocs/__init__.py'))['__version__'],
    author='montymi',
    author_email='mcmontanaro01@gmail.com',
    description='A CLI tool to initialize project documentation and deploy it to GitHub Pages.',
    long_description=(Path(__file__).parent / 'README.md').read_text(encoding='utf-8'),
    long_description_content_type='text/markdown',
    url='https://github.com/montymi/ClearDocs',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={'console_scripts': ['cleardocs=cleardocs.cli:main']},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    install_requires=[
        'click>=8.1,<9',
        'mkdocs==1.6.1',
        'mkdocs-material==9.6.14',
    ],
)