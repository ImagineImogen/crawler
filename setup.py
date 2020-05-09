import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Web-Scrapper-ImagineImogen",
    version="1.0",
    author="Ielizaveta Iakovenko",
    author_email="lieschen.yakov@gmail.com",
    description="Web scrapper package for Google and Yandex",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ImagineImogen/webscrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
