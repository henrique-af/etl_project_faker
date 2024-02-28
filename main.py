import csv
from faker import Faker
import random
import datetime
import re

faker = Faker()

# Step: Extract
def extract_data(input_source='generate'):
    data = []

    if input_source == 'generate':
        for i in range(100):
            name = faker.name()
            fullname_validator(name)
            email = faker.email()
            email_validator(email)
            address = faker.address()

            data.append({
                'name': name,
                'email': email,
                'address': address
            })

    elif input_source == 'csv':
        with open('output.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            required_columns = ['name', 'email', 'address']
            if not all(column in csv_reader.fieldnames for column in required_columns):
                print("Error: Required columns are not present in the CSV file.")
                return data

            for row in csv_reader:
                data.append({
                    'name': row.get('name', ''),
                    'email': row.get('email', ''),
                    'address': row.get('address', '')
                })

    return data


# Step: Transform
def transform_data(raw_data):
    transformed_data = []

    for id_counter, entry in enumerate(raw_data, start=1):
        cleaned_address = entry['address'].replace('\n', ' ')

        transformed_data.append({
            'id': id_counter,
            'full_name': entry['full_name'],
            'email': entry['email'],
            'address': cleaned_address,
            'age': random.randint(18, 65),
            'salary': round(random.uniform(30000, 100000), 2),
            'updated_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    return transformed_data

# Step: Load
def load_data(transformed_data, output_file='output.csv'):
    try:
        with open(output_file, 'a', newline='') as csvfile:
            fieldnames = ['id', 'full_name', 'email', 'address', 'age', 'salary', 'updated_at']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            for entry in transformed_data:
                writer.writerow(entry)
    except FileNotFoundError:
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = ['id', 'full_name', 'email', 'address', 'age', 'salary', 'updated_at']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

if __name__ == "__main__":
    user_input = input("Enter 'g' to generate data, 'c' to use data from CSV, or 'a' to add new data: ")
    source_key = user_input.lower()

    if source_key == 'g':
        data_source = extract_data(input_source='generate')
    elif source_key == 'c':
        data_source = extract_data(input_source='csv')
    elif source_key == 'a':
        name = input("Enter full name: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        new_data = {
            'full_name': name,
            'email': email,
            'address': address
        }

        existing_data = extract_data(input_source='csv')  
        existing_data.append(new_data)

        data_source = existing_data
        
        load_data(transform_data(data_source), output_file='output.csv')
    else:
        print("Invalid input. Using the default data generation.")
        data_source = extract_data(input_source='generate')

    data_transformed = transform_data(data_source)