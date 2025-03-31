# 🚀 OpenCart Test Automation & CI/CD Pipeline Project

📢 **Automated testing framework for OpenCart** with **UI, API, and Performance testing** integrated into a **CI/CD pipeline** using **GitHub Actions**.

---

## 📖 Table of Contents

- [✨ Features](#-features)
- [🛠️ Technologies Used](#%EF%B8%8F-technologies-used)
- [📥 Installation](#-installation)
- [🚀 Running the Tests](#-running-the-tests)
- [⚙️ CI/CD Pipeline](#️-cicd-pipeline)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

---

## ✨ Features

✅ **UI Automation**: Selenium & pytest for OpenCart’s UI testing.  
✅ **API Testing**: Validates OpenCart's REST API using pytest.  
✅ **Performance Testing**: Load tests using **Locust**.  
✅ **CI/CD Integration**: Automated tests triggered via **GitHub Actions**.  
✅ **Test Artifacts**: Uploads test results for easy review.  
✅ **Reporting**: Generates structured reports for UI & API test results.  

---

## 🛠️ Technologies Used

🔹 **Selenium** - UI automation  
🔹 **pytest** - Test framework for UI & API  
🔹 **Locust** - Load & performance testing  
🔹 **GitHub Actions** - CI/CD automation  
🔹 **Python 3.9+** - Programming language  

---

## 📥 Installation

### 📝 Prerequisites
- Python 3.9+
- Git installed
- pip (Python package manager)

### 📌 Clone the Repository

git clone https://github.com/tripurari13/sdetProject.git
cd sdetProject
📌 Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
🚀 Running the Tests
🔹 Run UI Tests
sh
Copy
Edit
pytest tests/ui_tests/
🔹 Run API Tests
sh
Copy
Edit
pytest tests/api_tests/test_products.py
🔹 Run Load Tests
sh
Copy
Edit
locust -f tests/performance_tests/load_test_locust.py --host=https://the-internet.herokuapp.com
⚙️ CI/CD Pipeline
This project is integrated with GitHub Actions to automate test execution on push and pull requests.

🔹 Workflow Overview
✅ Checks out code
✅ Sets up Python
✅ Installs dependencies
✅ Runs UI, API, and Performance tests
✅ Uploads test results

📌 GitHub Actions Workflow
yaml
Copy
Edit
name: Run Tests

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run UI Tests
        run: pytest tests/ui_tests/

      - name: Run API Tests
        run: pytest tests/api_tests/test_products.py

      - name: Run Load Tests
        run: locust -f tests/performance_tests/load_test_locust.py --host=https://the-internet.herokuapp.com

      - name: Upload Test Results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: test-results
          path: ./test_results/
🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository.

Clone the forked repository:

sh
Copy
Edit
git clone https://github.com/tripurari13/sdetProject.git
Create a new branch for your feature:

sh
Copy
Edit
git checkout -b feature-branch
Make changes and commit:

sh
Copy
Edit
git commit -m "Added a new feature"
Push to GitHub and create a Pull Request.

📜 License
This project is licensed under the MIT License.

🚀 Happy Testing!

markdown
Copy
Edit

---

### ✅ **What’s Included in This README?**
- **Badges**: Displays CI/CD pipeline status, Python version, and last commit details.
- **Features**: Overview of the test automation framework.
- **Technologies**: Lists tools used (Selenium, pytest, Locust, GitHub Actions, Python).
- **Installation & Running Tests**: Step-by-step guide for setting up and running tests.
- **CI/CD Pipeline**: Explanation and YAML workflow for GitHub Actions.
- **Contribution Guide**: Steps to contribute.
- **License**: Open-source MIT License.

This will make your **GitHub README** look professional and well-structured. Let me know if you need any modification
