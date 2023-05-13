# v4xyz

---
<div align="center">
<p align="center">

<!-- prettier-ignore -->

**A command line tool to chat with GPT4 and render markdown response.**

---
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/v4xyz?style=social)
![PyPI](https://img.shields.io/pypi/v/v4xyz?style=social)
![PyPI - Downloads](https://img.shields.io/pypi/dm/v4xyz?style=social)
![PyPI - License](https://img.shields.io/pypi/l/v4xyz?style=social)

```
 ______   __    _              _             __    __            _      __             
/_  __/  / /   (_)  ___       (_)  ___      / /_  / /  ___      | | /| / / ___ _  __ __
 / /    / _ \ / /  (_-<      / /  (_-<     / __/ / _ \/ -_)     | |/ |/ / / _ `/ / // /
/_/    /_//_//_/  /___/     /_/  /___/     \__/ /_//_/\__/      |__/|__/  \_,_/  \_, / 
                                                                                /___/  
```

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
The `http_proxy` and `https_proxy` are optional if the OpenAI API is accessible from your region.

## 3. Chat with GPT4 in Terminal

```shell
v4 'How to config a reverse proxy with Nginx?'
v4 'send a HTTP GET request using telnet'
v4 'any thing here'
```
