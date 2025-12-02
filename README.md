# Automated Registration Form Using Selenium (Python)

This project contains a Python-based automation script that performs complete registration form submission on a sample web application using Selenium WebDriver. It demonstrates clean element selection, structured automation logic, and best practices for browser interaction.

## Overview

The automation script performs the following steps:
- Launches Google Chrome using ChromeDriver
- Navigates to the registration page
- Inputs first name, last name, email, and mobile number
- Selects occupation and gender
- Enters and confirms password
- Checks the agreement checkbox
- Submits the registration form

This repository serves as a reference for learning Selenium-based browser automation and form handling.

## Technologies Used

- Python 3.x
- Selenium WebDriver
- Chrome Browser
- ChromeDriver

## Installation and Setup

1. Install Selenium:
   pip install selenium

2. Download ChromeDriver matching your Chrome browser version:
   https://chromedriver.chromium.org/downloads

3. Update the ChromeDriver path in the script:
   Service(r"C:\path\to\chromedriver.exe")

4. Run the automation script:
   python main.py

## Target Website

The script interacts with the registration page:
https://rahulshettyacademy.com/client/#/auth/register

## Key Concepts Demonstrated

- Locating elements using ID, XPath, and CSS Selector
- Automating form input actions
- Handling dropdowns and radio buttons
- Managing browser window actions
- Applying wait time for stable execution
