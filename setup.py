#/usr/bin/env python
import io
import re
from setuptools import setup, find_packages


with io.open('./toga_demo/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with io.open('README.rst', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='toga-demo',
    version=version,
    description='A demonstration of the capabilities of the Toga widget toolkit.',
    long_description=long_description,
    author='Russell Keith-Magee',
    author_email='russell@keith-magee.com',
    url='http://pybee.org/toga-demo',
    include_package_data=True,
    packages=find_packages(),
    package_data={
        'toga_demo': ['icons/*.icns', 'icons/*.png'],
    },
    extras_require={
        ':sys_platform=="win32"': ['toga[win32]'],
        ':sys_platform=="linux2"': ['toga[gtk]'],
        ':sys_platform=="darwin"': ['toga[cocoa]'],
    },
    entry_points={
        'console_scripts': [
            'toga-demo = toga_demo.__main__:main',
        ]
    },
    license='New BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)