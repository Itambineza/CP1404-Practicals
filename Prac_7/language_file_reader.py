"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""
import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage

def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    # Open the file for reading
    with open('languages.csv', 'r') as in_file:
        # File format is like: Language,Typing,Reflection,Year,Pointer Arithmetic
        # 'Consume' the first line (header) - we don't need its contents
        header = in_file.readline().strip().split(',')
        print(f"Header: {header}")  # Debugging line
        # Ensure the header matches our expectation
        if header != ['Language', 'Typing', 'Reflection', 'Year', 'Pointer Arithmetic']:
            print("Header does not match expected format. Please check the CSV file.")
            return
        # All other lines are language data
        for line in in_file:
            # Strip newline from end and split it into parts (CSV)
            parts = line.strip().split(',')
            print(f"Parts: {parts}")  # Debugging line
            # Ensure we have the correct number of parts
            if len(parts) != 5:
                print(f"Skipping line due to unexpected format: {line}")
                continue
            # Reflection and Pointer Arithmetic are stored as strings (Yes/No) and we want Booleans
            reflection = parts[2] == "Yes"
            pointer_arithmetic = parts[4] == "Yes"
            # Construct a ProgrammingLanguage object using the elements
            # year should be an int
            language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
            # Add the language we've just constructed to the list
            languages.append(language)

    # Loop through and display all languages (using their str method)
    for language in languages:
        print(language)

main()

def using_csv():
    """Language file reader version using the csv module."""
    # First, open the file for reading - note: specify newline
    # to avoid quoted \n in strings being considered a new record
    with open('languages.csv', 'r', newline='') as in_file:
        in_file.readline()
        reader = csv.reader(in_file)  # use default dialect, Excel
        for row in reader:
            print(row)

# using_csv()

def using_namedtuple():
    """Language file reader version using a named tuple."""
    with open('languages.csv', 'r', newline='') as in_file:
        file_field_names = in_file.readline().strip().split(',')
        print(f"Field names: {file_field_names}")  # Debugging line
        # Language will be a new subclass of the tuple data type class
        Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
        reader = csv.reader(in_file)  # use default dialect, Excel

        for row in reader:
            # Ensure we have the correct number of fields
            if len(row) != 5:
                print(f"Skipping row due to unexpected format: {row}")
                continue
            # Convert reflection and pointer_arithmetic to Booleans
            row[2] = row[2] == "Yes"
            row[4] = row[4] == "Yes"
            language = Language._make(row)
            print(repr(language))

# using_namedtuple()

def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
    with open("languages.csv", "r") as in_file:
        in_file.readline()
        for language in map(Language._make, csv.reader(in_file)):
            # Ensure we have the correct number of fields
            if len(language) != 5:
                print(f"Skipping language due to unexpected format: {language}")
                continue
            # Convert reflection and pointer_arithmetic to Booleans
            language = language._replace(reflection=(language.reflection == "Yes"),
                                         pointer_arithmetic=(language.pointer_arithmetic == "Yes"))
            print(language.name, 'was released in', language.year)
            print(repr(language))

# using_csv_namedtuple()
