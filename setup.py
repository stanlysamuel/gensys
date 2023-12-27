from setuptools import setup, find_packages

setup(
    name='gensys-ltl',
    version='0.2.0',
    packages=find_packages(include=['gensys', 'gensys.*']),
    install_requires=[
        'z3-solver'
    ]

)