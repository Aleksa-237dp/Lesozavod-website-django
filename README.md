# Lesozavod-website-django 🐍
Web application created in Python using the Django framework

## Instructions for connecting to the site "Lesozavod №10 Belka"

| Download the repository |

* In the repository you selected, click the green ‘Code’ button and copy the URL.
* Then, in Visual Studio Code (or other code editor), open a terminal and type the command:
  
```python
  git clone [repository address]
```

| Create a virtual environment |

* Open a terminal (or command line) and navigate to the project directory.
* Create a virtual environment using the command:
  
```python
  python -m venv env (replace ‘env’ with the desired environment name)
```

* Activate the virtual environment in Windows: `env\Scripts\activate`
* Or activate the virtual environment in macOS/Linux: `source env/bin/activate`
  
| Install dependencies |

* After activating the virtual environment, install the required libraries from the `requirements.txt` file
 
```python
  pip install -r requirements.txt
```
| Start the game |

* Navigate to the directory containing the file (usually the root directory of the project) `main.py`
* Start the game using the command:
  
```python
  python main.py
```
| Additional Notes |
  
* Make sure you have the appropriate version of Python installed, as specified in `requirements.txt`
* And have all the necessary libraries `pip install pygame` installed
  
  (If you are using a different IDE or editor, you may need to configure the environment so that it can find the virtual environment and installed libraries)
