# RAG Testing Framework

An enterprise-style Python-based QA automation and RAG testing framework designed for validating Retrieval-Augmented Generation (RAG) systems, Playwright workflows, and AI-powered applications.

This project combines:

- QA Automation
- Playwright
- Pytest
- GitHub Actions CI/CD
- RAG Testing Concepts
- AI Workflow Validation

---

# Features

- Automated smoke and regression test execution
- Playwright browser automation
- Pytest-based test framework
- GitHub Actions CI integration
- HTML report generation
- Modular and scalable framework structure
- RAG workflow experimentation
- AI testing learning playground

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pytest | Test execution framework |
| Playwright | Browser automation |
| GitHub Actions | CI/CD automation |
| pytest-html | HTML report generation |
| RAG | Retrieval-Augmented Generation testing |

---

# Project Structure

```text
rag_testing/
│
├── .github/
│   └── workflows/
│       ├── smoke.yml
│       └── regression.yml
│
├── tests/
│   ├── smoke/
│   ├── regression/
│   └── rag/
│
├── reports/
├── utils/
├── config/
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/satnam-malhotra/rag_testing.git
```

## Navigate to Project

```bash
cd rag_testing
```

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install Playwright Browsers

```bash
python -m playwright install --with-deps
```

---

# Running Tests

## Run All Tests

```bash
python -m pytest
```

---

## Run Smoke Tests

```bash
python -m pytest -m smoke
```

---

## Run Regression Tests

```bash
python -m pytest -m regression
```

---

# Generate HTML Reports

```bash
python -m pytest --html=reports/report.html
```

---

# GitHub Actions CI/CD

This project uses GitHub Actions for continuous integration.

## Current CI Features

- Automated smoke test execution
- Pull request validation
- Scheduled regression execution
- Dependency installation
- Playwright browser setup
- HTML report artifact upload

---

# Example Workflow

```yaml
name: QA Automation Task

on:
  pull_request:
  push:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - run: pip install -r requirements.txt

      - run: python -m pytest -m smoke
```

---

# Future Enhancements

Planned improvements:

- Allure reporting integration
- Parallel execution using pytest-xdist
- Docker support
- AI response validation
- Vector database testing
- RAG evaluation metrics
- Screenshot and trace capture
- Slack notifications
- API automation integration

---

# Learning Goals

This repository is part of an advanced QA automation and AI testing learning journey focused on:

- Modern SDET practices
- CI/CD automation
- AI system validation
- RAG workflow testing
- Enterprise automation architecture

---

# Author

## Satnam Malhotra

QA Automation Engineer | Python | Playwright | RAG Testing | GitHub Actions | AI QA Engineering

GitHub:
https://github.com/satnam-malhotra

---

# License

This project is licensed under the MIT License.