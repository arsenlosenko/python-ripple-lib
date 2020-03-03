from setuptools import setup

version = '1.0.8'

setup(
    name='python-ripple-lib',
    version=version,
    packages=['ripple_api'],
    url='https://github.com/arsenlosenko/python-ripple-lib',
    license='MIT',
    author='Arsen Losenko',
    author_email='arsenlosenko@protonmail.com',
    description='Ripple JSON-RPC API and Data API wrapper for Python',
    long_description=open('README.rst').read(),
    keywords='ripple rippled json-rpc',
    classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Utilities',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.6'
    ]
)
