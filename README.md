# AI-Powered Programming Framework Generator

This project generates a tailored programming framework based on the user's preferred programming language and project requirements. The framework is tailored to the user's needs and preferences, and includes all necessary components and libraries. If the user has provided a name for their project, this is used to generate a unique name for the framework. The project uses a search capability to find the most up-to-date and relevant information about the programming language and project requirements.

## Files

- `main.py`: This is the main file that runs the program. It creates instances of the UserInputHandler, FrameworkGenerator, and SearchEngine classes, gets user input, uses the search engine to get the most up-to-date and relevant information, and generates and prints the framework.

- `user_input_handler.py`: This file contains the UserInputHandler class, which gets user input for the preferred programming language, project requirements, and project name.

- `framework_generator.py`: This file contains the FrameworkGenerator class, which generates a unique name for the framework and the necessary components and libraries based on the language info and requirements info.

- `search_engine.py`: This file contains the SearchEngine class, which sends a GET request to Google Search and parses the HTML content of the page to find the first search result.

- `requirements.txt`: This file lists the project dependencies, which include requests for making HTTP requests, BeautifulSoup for web scraping, and Python as the standard library.

## How to Run

1. Install the dependencies listed in `requirements.txt` using pip:

```bash
pip install -r requirements.txt
```

2. Run `main.py`:

```bash
python main.py
```

3. Follow the prompts to enter your preferred programming language, project requirements, and project name (optional).

## Example

```bash
python main.py
Enter your preferred programming language: Python
Enter your project requirements: Web scraping, data analysis
Enter your project name (optional): MyProject
```

This will generate a framework named `MyProject_Python_Framework` with the necessary components and libraries for web scraping and data analysis in Python.
