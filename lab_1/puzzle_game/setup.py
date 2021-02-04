import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="puzzle_game_bmykhaylivvv",
    version="0.0.1",
    author="Bohdan Mykhayliv",
    author_email="bohdan.mykhailiv@ucu.edu.ua",
    description="Project which validate a board of symbols for \"Puzzle game\"",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bmykhaylivvv/coding_semester_2/tree/main/lab_1/puzzle_game",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8'
