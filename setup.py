try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "Platformer game with a bit of geometry in it",
    "author": "Boredom Games",
    "url": "https://github.com/boredomgames/GeoBounce",
    "download_url": "https://github.com/boredomgames/GeoBounce",
    "version": "0.1.0",
    "install_requires": ["pillow"],
    "packages": ["GeoBounce"],
    "scripts": [],
    "name": "GeoBounce",
    "python_requires": ">=3.6",
}

setup(**config)
