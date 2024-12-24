from setuptools import setup, find_packages # type: ignore

setup(
    name='cleardocs',
    version='0.1.0',
    author='montymi',
    author_email='mcmontanaro01@gmail.com',
    description='A CLI tool to initialize project documentation and deploy it to GitHub Pages.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/montymi/ClearDocs',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'click',
    ],
)