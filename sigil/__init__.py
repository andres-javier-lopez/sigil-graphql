import os

__version__ = '0.0.0'
dirname = os.path.dirname(__file__)
with open(os.path.join(dirname, '..', 'version.txt')) as f:
    __version__ = f.read().strip()
