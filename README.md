# Python-Translate-SRT-file-AI

This is a python script that converts the languages.

The python script used Free Google Translate API for Python to translate the languages.
Translates totally free of charge.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install translators.
### From PyPI

```bash
# Windows, Mac, Linux
pip install translators --upgrade

# Linux javascript runtime environment:
sudo yum -y install nodejs
```
### From Source
```bash
git clone https://github.com/UlionTse/translators.git
cd translators
python setup.py install
```

## Usage

```python
import translators as ts

# input languages
line = "Python script for translate languages"

# host service
Trans = ts.google(line.rstrip('\n'), if_use_cn_host=True, from_language='auto', to_language='si')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
