from setuptools import setup, find_packages

import homeslice

with open('README.rst') as f:
    readme = f.read()

setup(
    name='homeslice',
    version=homeslice.__version__,
    description='Home directory / dotfile / rcfile management with git.',
    long_description=readme,
    author='Dave Forgac',
    author_email='tylerdave@tylerdave.com',
    url='https://github.com/tylerdave/homeslice',
    packages=find_packages(),
    include_package_data=False,
    install_requires=[],
    license='MIT',
    entry_points={
        'console_scripts': [
            'homeslice = homeslice.cli:main',
            ],
        },
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3'
        )
)
