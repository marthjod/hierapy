import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()
with open(os.path.join(here, 'requirements.txt')) as f:
    requirements = f.read().split()

print requirements
print find_packages(exclude=['tests'])

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
    test_suite='nose.collector',
    scripts=['hipy/hipy'],
)
