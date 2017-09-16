'''
Setup tools config for running the registry authz server.
'''

from setuptools import setup, find_packages

setup(
    name='registry-authorization-server',
    version='0.0.0',
    include_package_data=True,
    description='Server that handles authorization requests for docker registries.',
    author='Compute Canada',
    url='https://github.com/c3tp/docker-registration-service',
    packages=find_packages(),
    install_requires=[
        'Flask==0.12.2',
        'PyYAML==3.12'
    ],
    entry_points={
        'console_scripts': [
            'registry_authz=registry_authz.main:run'
        ]
    }
)
