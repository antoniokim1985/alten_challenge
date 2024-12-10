import csv
import os

def generate_report(scenario_name, result, error_message=None):
    """
    Generates or appends to a CSV report logging the results of test scenarios.

    Args:
        scenario_name (str): Name of the test scenario.
        result (str): Result of the test (e.g., "Passed", "Failed").
        error_message (str, optional): Error message or description if the test failed. Defaults to None.

    Side Effects:
        Creates the 'reports' directory if it doesn't exist.
        Appends the test result to 'execution_report.csv', creating the file if it doesn't exist.

    Example:
        generate_report("Test_Login", "Failed", "Invalid credentials error")
    """
    # Define the path to the 'reports' directory
    report_directory = os.path.join(os.path.dirname(__file__), '..', 'execution_results', 'reports')

    # Create the reports directory if it does not exist
    if not os.path.exists(report_directory):
        os.makedirs(report_directory)

    # Define the path to the report file
    report_file = os.path.join(os.path.dirname(__file__), '..', 'execution_results', 'reports', 'execution_report.csv')

    # Check if the report file already exists
    file_exists = os.path.isfile(report_file)

    # Open the report file in append mode and write the test result
    with open(report_file, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Write the header row if the file is new
        if not file_exists:
            writer.writerow(['Scenario Name', 'Result', 'Error Description'])

        # Write the test scenario details
        writer.writerow([scenario_name, result, error_message if error_message else ''])
