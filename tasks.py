from encodings.aliases import aliases

from invoke import task
import os
import shutil

@task(aliases=['i'])
def install(c):
    """Install required packages from requirements.txt."""
    c.run('pip install --upgrade pip')
    c.run('pip install -r requirements.txt')

@task(aliases=['c'])
def clean(c):
    """Clean up the project by removing __pycache__ directories and .pyc files."""
    c.run('find . -name "__pycache__" -type d -exec rm -r {} +')
    c.run('find . -name "*.pyc" -type f -delete')