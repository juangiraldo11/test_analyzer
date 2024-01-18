import json
import csv
from typing import List, Dict


class TestResultsAnalyzer:
    def __init__(self, json_filename: str) -> None:
        """
        Initializes the test result analyzer.
        :param json_filename: Path to the JSON file containing test results.
        """
        self.json_filename = json_filename
        self.csv_filename = '../test_results.csv'
        self.results = []

    def parse_results(self) -> List[Dict[str, str]]:
        """
        Parses the JSON data and returns a list of test results.
        """
        with open(self.json_filename, 'r') as json_file:
            data = json.load(json_file)
            return data['test_cases']

    def export_to_csv(self, csv_filename: str) -> None:
        """
        Exports the test results to a CSV file.
        :param csv_filename: Output CSV file name.
        """
        with open(csv_filename, 'w', newline='') as csvfile:
            fieldnames = ['Test Case Name', 'Status', 'Execution Time', 'Timestamp']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for result in self.results:
                writer.writerow({
                    'Test Case Name': result['name'],
                    'Status': result['status'],
                    'Execution Time': result['execution_time'],
                    'Timestamp': result['timestamp']
                })

    def calculate_metrics(self) -> Dict[str, float]:
        """
         Calculates metrics based on the test results.
        """
        total_test_cases = len(self.results)
        passed_test_cases = sum(1 for result in self.results if result['status'] == 'pass')
        failed_test_cases = total_test_cases - passed_test_cases
        pass_rate = (passed_test_cases / total_test_cases) * 100 if total_test_cases > 0 else 0
        execution_times = [result['execution_time'] for result in self.results]
        average_execution_time = sum(execution_times) / total_test_cases
        min_execution_time = min(execution_times)
        max_execution_time = max(execution_times)

        return {
            'Total Test Cases': total_test_cases,
            'Passed Test Cases': passed_test_cases,
            'Failed Test Cases': failed_test_cases,
            'Pass Rate': round(pass_rate, 2),
            'Average Execution Time': round(average_execution_time, 2),
            'Min Execution Time': min_execution_time,
            'Max Execution Time': max_execution_time,
        }

    def process(self) -> Dict[str, float]:
        """
          Process the test results, export them to a CSV file, and calculate metrics.

          This method performs the following steps:
          1. Parses the test results from the input JSON file.
          2. Exports the parsed results to a CSV file with the specified filename.
          3. Calculates various metrics based on the processed test results.
        """
        self.results = self.parse_results()
        self.export_to_csv(self.csv_filename)
        metrics = self.calculate_metrics()
        return metrics


if __name__ == "__main__":
    json_filename = 'src/test_data.json'
    analyzer = TestResultsAnalyzer(json_filename)
    result_metrics = analyzer.process()
    print(result_metrics)
