from setuptools import setup, find_packages

setup(
    name='PyKATh',
    version='0.1.1',
    description='This library leverages PyKTL to generate and sign Knox Cloud Tokens using Python.',
    long_description=open('README.md').read(),  # Read the long description from a file
    long_description_content_type='text/markdown',  # Specify the type of markup used (reStructuredText in this case)
    author='Matt Hills',
    author_email='mattintech@gmail.com',
    url='https://github.com/mattintech/PyKATh',
    packages=find_packages(),
    install_requires=[
        'PyKTL',
        'requests'
    ],
)