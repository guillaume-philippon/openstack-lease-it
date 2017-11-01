from setuptools import setup

setup(
    name='openstack-lease-it',
    version='1.0',
    packages=['openstack_lease_it',
              'openstack_lease_it.openstack_lease_it',
              'openstack_lease_it.lease_it'],
    include_package_data=True,
    install_requires=['django'],
    license='Apache License',
    description='A Django app lease openstack instances',
    long_description='',
    url='https://github.com/LAL/openstack-lease-it',
    author='G. Philippon',
    author_email='guillaume.philippon@lal.in2p3.fr',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Cloud Administrator',
        'License :: OSI Approved :: Apache License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)