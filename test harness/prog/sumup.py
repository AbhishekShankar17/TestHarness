import csv
import argparse
import sys

def sum_columns(csv_file, columns):
    try:
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            total = {column: 0 for column in columns}

            for row in reader:
                for column in columns:
                    total[column] += float(row[column])

            print(f"Sum of columns {', '.join(columns)}:")
            for column, value in total.items():
                print(f"{column}: {value}")

        sys.exit(0)

    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        # Set exit status to 1 (error)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        # Set exit status to 1 (error)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Sum specified columns in a CSV file.")
    parser.add_argument("file", help="Path to the CSV file")
    parser.add_argument("columns", nargs="+", help="Columns to sum")
    
    args = parser.parse_args()
    sum_columns(args.file, args.columns)

if __name__ == "__main__":
    main()
