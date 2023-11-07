try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Gothon Web Game',
    'author': 'Muriel Gordon',
    'url': 'https://github.com/MurielGordon/gothon-web-game',
    'download_url': 'https://github.com/MurielGordon/gothon-web-game',
    'author_email': 'murielgordon6@gmail.com',
    'version': '0.1',
    'install_requires': ['flask'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'gothonweb'
}

setup(**config)