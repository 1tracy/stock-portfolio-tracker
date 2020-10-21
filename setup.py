"""setup"""
import setuptools

with open("README.md", "r") as fh:
    LONGDESC = fh.read()

setuptools.setup(
    name="Portfolio-report-1tracy", # Replace with your own username
    version="0.0.1",
    author="Tracy",
    author_email="dongtracy2002@gmail.com",
    description="This is a portfolio report.",
    LONGDESC=LONGDESC,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
