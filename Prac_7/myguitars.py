import csv
from guitar import Guitar

def main():
    guitars = load_guitars("guitars.csv")
    display_guitars(guitars)
    
    print("\nSorted by year:")
    guitars.sort()
    display_guitars(guitars)

def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars

def display_guitars(guitars):
    """Display a list of guitars."""
    for guitar in guitars:
        print(guitar)

main()

