#/usr/bin/env python
from setuptools import setup, find_packages
from toga_demo import VERSION

try:
    readme = open('README.rst')
    long_description = str(readme.read())
finally:
    readme.close()

required_pkgs = [
    'toga',
]

setup(
    name='toga-demo',
    version=VERSION,
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
    install_requires=required_pkgs,
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