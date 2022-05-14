from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ['pandas>=1.3.2', 'Beautifulsoup4>=4.9.3', 'requests>=2.26.0']

setup(
    name="pyremote",
    version="0.0.1",
    author="Matthew Qandil",
    description="A package to determine most interesting live sports games",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/mqandil/pyremote/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
)