from setuptools import setup

version = "0.0.4"
description = "A command line tool to chat with GPT4 and render markdown response."
with open("README.md") as fp:
    long_description = fp.read()
url = "https://github.com/imhuwq/v4xyz"
author = "imhuwq"
author_email = "imhuwq@gmail.com"
classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Topic :: Communications :: Chat",
    "Topic :: Terminals",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
]

setup(name="v4xyz",
      version=version,  # the package version, it may be different from the release version
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url=url,
      author=author,
      author_email=author_email,
      packages=[],
      py_modules=["v4"],
      entry_points={
          "console_scripts": [
              "v4=v4:main",
          ],
      },
      install_requires=[
          "art==5.9",
          "click==8.1.3",
          "openai==0.27.6",
          "rich==13.3.5"
      ],
      classifiers=classifiers,
      )
