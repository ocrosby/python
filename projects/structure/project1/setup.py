from setuptools import setup, find_packages

setup(
    name='project1',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'project1 = run:main',
        ],
    },
)
