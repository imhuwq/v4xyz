# v4xyz

---
A command line tool to chat with GPT4 and render markdown response.

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

## 3. Chat with GPT4 in Terminal
```shell
v4 'How to config a reverse proxy with Nginx?'
v4 'send a HTTP GET request using telnet'
v4 'any thing here'
```
