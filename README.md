# Test Results Analyzer

## Overview
This script, `test_results_analyzer.py`, is designed to analyze and process test results stored in a JSON file. It extracts relevant information from the JSON file, exports it to a CSV file, and calculates various metrics based on the test results.

## How to Run
1. Make sure you have Python version > 3.5 installed on your system.
2. Download the script, `test_results_analyzer.py`, to your local machine.
3. Place the JSON file containing the test results in the same directory as the script. Ensure the JSON file follows the required format with a 'test_cases' key containing an array of test cases.

4. Open a terminal or command prompt and navigate to the directory where the script is located.
5. Run the script using the following command:
   ```bash
   python test_results_analyzer.py
   ```
6. The script will process the test results, export them to a CSV file named `test_results.csv`, and print calculated metrics to the console.

## Input
- The script expects a JSON file named `test_data.json` by default. You can change the `json_filename` variable in the script to point to your desired JSON file.
- JSON Structure

    The JSON object must contain a key named "test_cases", which holds an array of test cases.
    Each test case is represented by a JSON object with the following fields:
    "name": The name or identifier of the test case (string).
    "status": The status of the test case, either "pass" or "fail" (string).
    "execution_time": The time taken for test execution in seconds (integer or float).
    "timestamp": The timestamp of when the test was executed in the format %Y-%m-%dT%H:%M:%S (string).
    Ensure your JSON file adheres to this structure for proper processing by the script.
## Output
- The script generates a CSV file (`test_results.csv`) containing test results with columns: 'Test Case Name', 'Status', 'Execution Time', and 'Timestamp'.
- The calculated metrics are printed to the console, including total test cases, passed test cases, failed test cases, average execution time, minimum execution time, maximum execution time, and Pass Rate.
## Example
```bash
python test_results_analyzer.py
```

## Dependencies
- The script uses the `json` and `csv` modules, which are part of the Python standard library so no more installation is required.

## Note
- Ensure that the timestamp format in the input JSON file is in the format `%Y-%m-%dT%H:%M:%S` for accurate processing.
- The script will overwrite any existing CSV file with the same name as the output file.