from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Foo Physics'
LONG_DESCRIPTION = 'This package deals with operations relating to Foo Physics'

setup(
        name="FooEtAl", 
        version=VERSION,
        author="Ethan Warren",
        author_email="ethanwrn@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], 
        keywords=['python', 'foo', 'physics'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)