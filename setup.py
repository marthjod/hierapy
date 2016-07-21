import os
from setuptools import setup, find_packages
from hipy import __version__ as package_version


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()
with open(os.path.join(here, 'requirements.txt')) as f:
    requirements = f.read().split()


setup(
    name='hipy',
    version=package_version,
    description='Convert Ruby output of older Hiera versions to equivalent Python or JSON data structures',
    long_description=long_description,
    url='https://github.com/marthjod/hipy',
    author='marthjod',
    author_email='marthjod@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=requirements,
    scripts=['hipy/hipy']
)
