from setuptools import setup, find_packages

setup(
    name="etpclient",
    version="0.0.0",
    packages=find_packages(),
    install_requires=[
        "lxml",
        "xmljson",
        "websocket-client",
        "requests",
        "h5py",
        "etptypes",
        "etpproto",
    ],
)
