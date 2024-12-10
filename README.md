## Alten suite documentation

This README is documentation that explains the features of the test harness as well as the execution process.

### Features:

It is composed of:

1. **./deps/requirements**  
   A file that contains the dependencies required for executing the tests.

2. **./src**  
   A directory that contains the test harness.

3. **./src/execution_results**  
   This is where three folders will be stored: logs, reports, and screenshots. If they do not exist, they will be created during the test execution.

4. **./src/features**  
   Contains the `steps` folder, the test suites written in Gherkin format (.feature), and `environment.py`.

5. **./src/features/steps**  
   Contains reusable components, which are scripts that automate the commands used in the .feature files.

6. **./src/features/environment.py**  
   Contains the necessary setup for using Chromedriver, as well as the start and end of the tests with their configuration.

7. **./src/features/*.feature**  
   These are the tests that will be executed. They can be run individually or as a group.

8. **./src/pages**  
   These are the PageObjects that contain paths and reusable commands for each page.

9. **./src/tools/Tools.py**  
   Contains tools that are used in the PageObjects.

10. **./src/utils**  
    A folder that contains the system for logging, reports, and screenshots.

---

### Execution of Tests

It is recommended to create a virtual environment (venv) for running the tests.  
For this, it is suggested to follow the official documentation: [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html).

After creating the virtual environment, activate it and install the requirements using the following command from the `./deps` directory:

```
pip3 install -r requirements.txt
```

After installation, you can run the tests.

To do so, navigate to `./src` and execute:

```
behave features/<test>.feature
```

The execution will generate reports in the **./src/execution_results** folder, where you can view the logs, the report in CSV format, and the captured screenshots.

