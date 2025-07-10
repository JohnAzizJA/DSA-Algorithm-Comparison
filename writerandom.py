import csv
import random

def generate_random_csv(filename):
    """Generates a CSV file with 1000 random elements, one element per row."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(1000):
            random_element = random.randint(1, 1000)  # Random integer between 1 and 10,000
            writer.writerow([random_element])

def main():
    generate_random_csv("data.csv")

if __name__ == "__main__":
    main()