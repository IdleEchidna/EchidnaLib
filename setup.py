import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="echidnalib",
    version="0.0.3",
    author="IdleEchidna",
    author_email="",
    description="A modular discord bot package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IdleEchidna/EchidnaLib",
    project_urls={
        "Bug Tracker": "https://github.com/IdleEchidna/EchidnaLib/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
