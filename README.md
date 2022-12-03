# Event Hosting Management Backend

## Quick Start

- Clone the repository

    ```bash
    git clone https://github.com/blackprince001/Event-Hosting-Management
    ```

- Move into the directory

    ```bash
    cd Event-Hosting-Management
    ```

- Set up a virtual environment with Venv on Vscode or any python environment manager you have installed, and it will automatically install the dependencies. This project uses pipenv to handle dependency installs and virtual environments.

- To simply install project dependencies, run the command below.

  ```console
  pipenv sync
  ```

- Set up a dev environment by running the command to install dependencies to work on the project. Do note that the make command is already dependent on the one above. So if you use this command, there will be no need for you to run the prev one.
  
  ```console
  pipenv sync --dev
  ```

  while you're in `/Event-Hosting-Management`

## Testing

To run the tests in the project:

- You need to install the dev packages:

  ```bash
  pipenv install --dev
  ```

## Backend Design

![Backend](backend_design.png)

```console
.
├── api
│   ├── event.py
│   ├── executive_event.py
│   ├── __init__.py
│   ├── issues.py
│   └── user.py
├── backend_design.png
├── database
│   ├── core.py
│   ├── __init__.py
│   └── models.py
├── error_handling
│   ├── error_handling.py
│   └── __init__.py
├── Pipfile
├── Pipfile.lock
├── README.md
├── schemas
│   ├── event.py
│   ├── executive_event.py
│   ├── __init__.py
│   ├── issues.py
│   └── user.py
└── tests
    ├── api
    │   ├── __init__.py
    │   ├── test_event.py
    │   ├── test_executive_event.py
    │   └── test_user.py
    ├── conftest.py
    ├── __init__.py
    └── storage

7 directories, 25 files
```
