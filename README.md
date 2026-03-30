## Selenium Automation Suite

## .)Project Overview
This project is a collection of Selenium-based automation scripts developed to demonstrate modern web automation techniques using Selenium 4, explicit waits, proper exception handling, and cross-platform compatibility.

## .)The project automates:
PyPI package download & installation
Website auto-refresh
Zomato sign-in
Zomato sign-up
Zomato profile actions (login, profile access, logout)
All scripts are written using modern Selenium syntax and follow best practices such as:
find_element(By.*)
WebDriverWait with expected_conditions
No hardcoded driver paths
Proper exception handling
Clean modular structure

## .)Project Structure
Selenium-Automation/
│
├── downloadpythreadkiller.py
├── autorefresh.py
├── zomatosignin.py
├── zomatosigninacton.py
├── zomatosignup.py
└── README.md

## 1️) downloadpythreadkiller.py
## Purpose
Automates downloading the latest PyThreadKiller wheel file from PyPI and installs/upgrades it automatically using pip.

## Features

Uses headless Chrome
Navigates to Release History
Downloads latest .whl file
Detects file from system Downloads folder
Installs using sys.executable -m pip
Deletes file after installation
Cross-platform support (Windows/Linux)
Uses multiprocessing with timeout protection
Robust exception handling

## Concepts Used
By.ID, By.CSS_SELECTOR
WebDriverWait
Expected Conditions
subprocess
multiprocessing
OS detection

## 2) autorefresh.py
## Purpose
Automatically refreshes a webpage multiple times using Selenium.

## Features
Opens GitHub repository page
Refreshes page 5 times
Uses explicit waits instead of time.sleep
Clean and minimal structure

## Concepts Used
driver.refresh()
Explicit wait
Loop control

## 3️)zomatosignin.py
## Purpose
Automates login to Zomato using Email + OTP authentication.
## Features
Click Sign-in
Choose login via email
Enter email
Accept OTP input from console
Submit OTP
Confirms login success
Uses multiple locator strategies

## Locator Types Demonstrated

By.ID
By.NAME
By.CLASS_NAME
By.XPATH
By.CSS_SELECTOR

## Error Handling
TimeoutException
NoSuchElementException

## 4️) zomatosigninacton.py
## Purpose
Extends login automation to perform post-login actions.

## Features
Login via OTP
Open Profile section
Logout successfully
Demonstrates navigation after authentication

## Concepts Used

XPath text-based locators
Link text locators
ID locators
Sequential user interaction automation

## 5️) zomatosignup.py

##  Purpose
Automates Zomato user registration process.

## Features

Click Signup
Enter Full Name
Enter Email
Select newsletter option
Submit form

