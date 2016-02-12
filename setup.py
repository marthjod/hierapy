import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
with open(os.path.join(here, 'requirements.txt')) as f:
    requirements = f.read().split('\n')


setup(
    name='hipy',
    version='0.1',
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
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=requirements,
    setup_requires=['nose', 'nose-parameterized'],
    entry_points={
        'console_scripts': [
            'hipy=hipy:convert',
        ]
    }
)
