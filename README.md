## Calendar Automation


### For everyone

You need to install python on your computer. [Download Python page](https://www.python.org/downloads/).

#### Option #1 

If python installed, you have several options, either run it globally (not recommended), just pull/download the source code and run

```
pip install -r requirements.txt
python src/schedule_planner.py
```

#### Option #2

Work with virtual environments and install dependencies in there. [Python virtual environments guide](https://realpython.com/python-virtual-environments-a-primer/)

Do all the same steps as in Option #1 but with activated virtual environment.

### For developers

We are using `pyenv` and `poetry`. As long as you have `poetry` installed do:

```
poetry install
poetry run python src/schedule_planner.py
```

### Notes

This is project under development, the main file is [schedule_planner.py](src/schedule_planner.py), all the rest are related to the experiments.
Beware, that at the moment dates are between 1 July 2022 and now (recalculates every time after y/N keystroke). Feel free to change it as you need.

### Huh?

- Ask in the Github issues, if you need any features
- Ask in the GitHub issues, if you find a bug
- Want to support, buy me a coffee or star the project
- Anything else? Open Github issue

### How and why it all started

[How to automate Google Calendar without automating it](https://www.buymeacoffee.com/chameleontartu/how-automate-google-calendar-without-automating)
