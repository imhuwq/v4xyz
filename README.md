# v4xyz

---
<div align="center">
<p align="center">

<!-- prettier-ignore -->

## v4xyz, way for doing kinds of things.

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/v4xyz?style=social)
![PyPI](https://img.shields.io/pypi/v/v4xyz?style=social)
![PyPI - Downloads](https://img.shields.io/pypi/dm/v4xyz?style=social)
![GitHub](https://img.shields.io/github/license/imhuwq/v4xyz?style=social)

**A cli tool that ask GPT4 for programming solutions and get answers directly in terminal.**

```
 ______   __    _              _             __    __            _      __             
/_  __/  / /   (_)  ___       (_)  ___      / /_  / /  ___      | | /| / / ___ _  __ __
 / /    / _ \ / /  (_-<      / /  (_-<     / __/ / _ \/ -_)     | |/ |/ / / _ `/ / // /
/_/    /_//_//_/  /___/     /_/  /___/     \__/ /_//_/\__/      |__/|__/  \_,_/  \_, / 
                                                                                /___/  
```

https://user-images.githubusercontent.com/10917115/238183926-b682f0d0-44c2-4815-9728-9ce8f8601319.mp4

---

</p>
</div>

## 1. Installation

### 1.1 Installing from pypi

```shell
pip install v4xyz
```

### 1.2 Installing from github

```shell
git clone https://github.com/imhuwq/v4xyz
cd v4xyz
python setup.py install
```

## 2. Setup config

Once you have `v4xyz` installed, you have to config the OpenAI API key and the proxies if necessary.

```shell
v4 -e # this will open the config file with your editor
```

The config file is on json format:

```json
{
  "openai_secret": "",
  "http_proxy": "",
  "https_proxy": ""
}
```

The `openai_secret` must be set to your OpenAI key.   
The `http_proxy` and `https_proxy` are optional if the OpenAI API is directly accessible from your region.

## 3. Ask GPT4 in Terminal

```shell
v4 'How to config a reverse proxy with Nginx?'
v4 'send a HTTP GET request using telnet'
v4 'any thing here'
```
