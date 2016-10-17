"""Our python packaging stuff."""


from os.path import abspath, dirname, join, normpath

from setuptools import setup


setup(

    # Basic package information:
    name = 'stormpath-export',
    version = '0.1.1',
    scripts = ('stormpath-export', ),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = ['docopt>=0.6.2', 'stormpath>=2.2.0'],

    # Metadata for PyPI:
    author = 'Randall Degges',
    author_email = 'r@rdegges.com',
    license = 'UNLICENSE',
    url = 'https://github.com/rdegges/stormpath-export',
    keywords = 'user authentication auth security api stormpath bcrypt utility',
    description = 'Easily export your Stormpath user data.',
    long_description = open(normpath(join(dirname(abspath(__file__)),
        'README.rst'))).read()

)
