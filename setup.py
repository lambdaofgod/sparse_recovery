from setuptools import setup

VERSION=0.1
INSTALL_REQUIRES = [
    'numpy'
]

setup(
    name='sparse_recovery',
    packages=['sparse_recovery'],
    version=0.1,
    url='https://www.github.com/lambdaofgod/sparse_recovery',
    install_requires=INSTALL_REQUIRES
)
