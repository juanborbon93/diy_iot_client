  
import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

version = os.getenv("VERSION")
setuptools.setup(
    name="diy-iot-client", # Replace with your own username
    version=version,
    author="MakeHax",
    author_email="juanborbon93@gmail.com",
    description="api client library for communicating with the diy iot rest api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/juanborbon93/fast_pony_crud",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
        "pydantic"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)