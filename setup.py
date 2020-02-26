from distutils.core import setup

version = open('VERSION').read()

with open('requirements.txt') as fd:
    requirements = [dep.strip() for dep in fd]

setup(
    name='BulkWhois',
    version=version,
    author='CSIRT Foundry / Chris Horsley',
    author_email='chris.horsley@csirtfoundry.com',
    packages=['bulkwhois'],
    scripts=[],
    url='http://pypi.python.org/pypi/BulkWhois/',
    download_url='http://github.com/csirtfoundry/BulkWhois/tarball/master',
    license='LICENSE.txt',
    description='Interfaces for popular bulk WHOIS servers',
    long_description=open('README.txt').read(),
    install_requires=requirements,
 )
