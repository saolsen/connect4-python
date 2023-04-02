from setuptools import setup, find_packages  # type: ignore

setup(
    name="connect4",
    version="1.0",
    author="Steve Olsen",
    author_email="steve@steve.computer",
    description="connect4 ai",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
