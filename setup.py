import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sharepp",
    version="1.1",
    author="Lukas Brauckmann",
    author_email="lukas.brauckmann@gmail.com",
    description="Library for getting current prices of stocks, ETFs and cryptocurrency.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Plebo13/sharepp",
    license="Apache License 2.0",
    packages=["sharepp"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
        "bs4"
    ],
)
