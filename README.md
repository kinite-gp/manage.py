[![Python 3.9](https://img.shields.io/badge/Python-3.9-yellow.svg)](http://www.python.org/download/) 
[![readline 6.2.4.2](https://img.shields.io/badge/Readline-6.2.4.2-yellow.svg)](https://pypi.org/project/readline/) 
[![colorama 0.4.6](https://img.shields.io/badge/Colorama-0.4.6-yellow.svg)](https://pypi.org/project/colorama/) 


# manage.py
Run manage.py task or easier execution of "Django" commands

## prerequisites
- realine
- colorama
- json

## Capabilities
- Prediction and help by pressing Tab
- Ability add to path
- Simple settings (Python virtual environment address and Django project address)
- Can be moved without problems

## use and configure
You have two ways to use and adjust, which are:
 


## `The first method`:
In the first method, you put the main files that include admin-shell.py and path.json in the base directory of your project.

Then run the admin-shell.py file in cmd
```bash
cd ...
pip install readline
pip install colorama
python admin-shell.py
```


## `The second method`:
You can get an exe output from the Python file and after adding it to the path, just write the name of the file and run it
```bash
pip install pyinstaller
pyinstaller --onefile admin-shell.py
```

`Don't forget the path.json file
and adjust its contents according to your project`


### something interesting
I have written this file according to my interest and for the ease of my work and decided to put it on my github. I would be happy to know your opinion about my idea

### Contact us
- instagram : https://www.instagram.com/kinite_gp/
