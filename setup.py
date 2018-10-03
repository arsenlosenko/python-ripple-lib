from setuptools import setup

version = '1.0.3.1'

setup(
    name='python-ripple-lib',
    version=version,
    packages=['ripple_api'],
    url='https://github.com/arsenlosenko/python-ripple-rpc',
    license='MIT',
    author='Arsen Losenko',
    author_email='arsenlosenko@gmail.com',
    description='Ripple JSON-RPC API wrapper for python',
    long_description=open('README.rst').read(),
    keywords='ripple rippled json-rpc',
    classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Utilities',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.5'

    ]
)
