from setuptools import setup, find_packages

setup(
    name="b16",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["b16=script.main:main"],
    },
)
