from setuptools import setup, find_packages

setup(
    name='restrict_www_access',
    version='0.0.1',
    description='Restrict public access to ERPNext desk. Allow only website access on public domain.',
    author='Miyanda Hakooma',
    author_email='mh@antares.co.zm',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[],
)
