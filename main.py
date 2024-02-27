## /in/henrique-af
# objetive: create a etl using faker lib to generate data, transform these data using random lib and them write that data to a csv file.

import csv
from faker import Faker
import random
import datetime

fake = Faker();


#Step: Extract
def extract_data():
    data = []
    for i in range(100):
        data.append({
            'name': fake.name(),
            'email': fake.email(),
            'address': fake.address()
        })
    return data

# Step: Transform
def transform_data(raw_data):
    transformed_data = []
    for entry in raw_data:
        # Replace newline characters in the address with spaces
        cleaned_address = entry['address'].replace('\n', ' ')

        transformed_data.append({
            'full_name': entry['name'],
            'email_contact': entry['email'],
            'address': cleaned_address,
            'age': random.randint(18, 65),
            'salary': round(random.uniform(30000, 100000), 2),
            'updated_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    return transformed_data

# Load
def load_data(transformed_data, output_file='output.csv'):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['full_name', 'email_contact', 'address', 'age', 'salary', 'updated_at']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for entry in transformed_data:
            writer.writerow(entry)

# Execute
data = extract_data()
data_transformed = transform_data(data)
load_data(data_transformed)