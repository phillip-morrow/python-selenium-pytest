## Python Selenium and Requests
Tests using selenium wire and requests must be run from within `pipenv shell`

### Run Tests
Run `python -m pytest tests/` to run all tests.
Run `python -m pytest tests/end-to-end` to run end to end tests only.
Run `python -m pytest tests/api` to run api tests only.

### Reports 
Reports are auto generated.  The output is in the root at `pytest_html_report.html`.

Test runs are archived in a generated folder.  `rm -rf archive` in the root directory to wipe out previous test runs.