from setuptools import setup, find_packages

setup(
    name='gensys',
    version='0.1.0',
    packages=find_packages(include=['gensys', 'gensys.*']),
    install_requires=[
        'z3-solver'
    ]

)