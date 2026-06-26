import sys
import os

from tshirt_data_reader import read_data
from tshirt_analyzer import analyze_tshirts, generate_insights
from tshirt_report_writer import write_report, print_summary

def main():
    if len(sys.argv) != 3:
        print("Usage: py tshirt_main.py tshirt_sales.csv tshirt_report.txt")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return

    print(f"Reading data from {input_file}...")
    data = read_data(input_file)

    if not data:
        print("No data found.")
        return

    print(f"Total records: {len(data)}")

    results = analyze_tshirts(data)
    insights = generate_insights(results)

    write_report(results, insights, output_file)
    print_summary(results)

    print(f"\nReport created: {output_file}")

if __name__ == "__main__":
    main()