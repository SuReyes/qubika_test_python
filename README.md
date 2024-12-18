# QubikaTest
This repository is to store the automated tests for the Qubika Technical Test

# Project Structure
- apis/: Handles interactions with the backend API (e.g., creating the new user).
- pages/: Implements the Page Object Model. Each file represents a page of the web application (e.g., login_page.py, category_page.py).
- tests/: Contains the test files that automate the actions for different user scenarios (creating a user, logging in, etc.).
- requirements.txt: Lists the necessary Python dependencies.
- Jenkinsfile/: Jenkinsfile defines the CI/CD pipeline for automating the build, test, and deployment processes
- Dockerfile/: The Dockerfile defines the steps to build a Docker image for the project

# Prerequisites
Make sure you have the following installed:
- Python 3.7 or higher
- pip (Python package manager)

# Steps to run tests
- Create a python virtual environment and activate it

- Install the required dependencies
  ```pip install -r requirements.txt```

- Install the required browsers
  ```playwright install```

## Run the tests
  - Execute the test
  ```pytest```
  - Parallel Testing
    ```pytest -n 4```
  - Reporting
    ```pytest --html=report.html```

# Improvements and Future Work
- API Error Handling: Improve API tests with more robust error handling and edge case testing (e.g., invalid data, timeout).
- test_utils: Integrate a utilities file with helper functions like generating random data or logging messages.
- config file: Integrate configuration file which can store environment-specific settings like API URLs or browser configurations
- Login Retry Mechanism: Add logic to handle retries in case of intermittent login failures or network issues.
- Browser Compatibility Testing: Integrate cross-browser testing to ensure compatibility across Chromium, Firefox, and WebKit.
- Data-Driven Testing: Use external files (CSV, JSON) for data-driven tests to run the same tests with multiple datasets.
- CI/CD Automation: Test and validate the entire process—from pulling the latest code, building the Docker image, running tests, and archiving results.