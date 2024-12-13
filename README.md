Firebird Automation Framework

This repository contains the automation framework for testing the Firebird mobile application using Appium and Python.

Features

Appium Integration: Enables mobile application testing for Android devices.

Pytest Support: Provides test execution and reporting.

Modular Framework: Based on the Page Object Model (POM).

Customizable Configuration: Easy setup for desired capabilities and test parameters.

Prerequisites

Python: Ensure Python 3.8 or higher is installed.

Appium Server: Install Appium globally using Node.js:

npm install -g appium

Mobile Device/Emulator:

For Android, ensure you have adb installed and your device/emulator is detected using:

adb devices

APK File: The application file (e.g., app.apk) should be available locally.

Setup

Clone the repository:

git clone https://github.com/<username>/<repository>.git
cd <repository>

Install dependencies:

pip install -r requirements.txt

Framework Structure

project/
├── tests/
│   ├── test_launch_app.py     # Contains test cases
├── pages/
│   ├── base_page.py           # Base page for common methods
│   ├── login_page.py          # Login page implementation
├── utils/
│   ├── config.py              # Desired capabilities and configurations
├── reports/                   # Test reports (generated after execution)
├── requirements.txt           # Required Python libraries
├── README.md                  # Project documentation

Configuration

Edit the test_launch_app.py file to include your app and device-specific configurations:

    desired_capabilities = {
        "platformName": "Android",
        "appium:deviceName": "OnePlus Nord 2T",  # Replace with your device name
        "appium:udid": "CYINPR4PIV6PJNKF",       # Replace with your device UDID
        "appium:appPackage": "com.firebird.artist360.uat",  # Application package name
        "appium:appActivity": "com.firebird.artist360.MainActivity",  # Application main activity
        "appium:automationName": "UiAutomator2",
        "appium:ignoreHiddenApiPolicyError": True,
        "appium:noReset": True
    }

For different devices, adjust the deviceName, udid, and platformVersion as required.

Running Tests

Launch the Appium server:

appium

Run the test cases using pytest:

pytest --html=reports/report.html

Reports

After test execution, an HTML report will be generated in the reports/ directory.

Contributing

Contributions are welcome! Please fork the repository and create a pull request for any enhancements or bug fixes.

License

This project is licensed under the MIT License. See the LICENSE file for details.
