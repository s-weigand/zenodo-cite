"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.md") as history_file:
    history = history_file.read()

requirements = ["requests"]

setup_requirements = ["pytest-runner"]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Sebastian Weigand",
    author_email="s.weigand.phy@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description=(
        "Tool to generate a version sensitive citation or your software published on zenodo"
    ),
    install_requires=requirements,
    license="Apache Software License 2.0",
    project_urls={
        "Documentation": "https://zenodo-cite.readthedocs.io/en/latest/",
        "Source": "https://github.com/s-weigand/zenodo-cite",
        "Tracker": "https://github.com/s-weigand/zenodo-cite/issues",
    },
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="zenodo_cite",
    name="zenodo_cite",
    packages=find_packages(include=["zenodo_cite", "zenodo_cite.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/s-weigand/zenodo_cite",
    version="0.1.0",
    zip_safe=False,
)
