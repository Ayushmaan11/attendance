from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'dlib',
    ],
    entry_points={
        'console_scripts': [
            # add your command-line scripts here
        ]
    }
)
