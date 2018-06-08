
from setuptools import setup, find_packages
import os

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'chem99',
    version = '0.1.5',
    packages = find_packages(),
    entry_points = {'scrapy': ['settings = chem99.settings']},
)