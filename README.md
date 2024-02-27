# etl_project_faker
A personal project that utilizes the Faker library to generate data for a simple ETL job.

### Day 1: Initial Implementation
Objective: Create an ETL job using the Faker library to generate data, transform the data, and write it to a CSV file.

- Implemented the extraction phase using the Faker library, generating mock data for names, emails, and addresses.
- Developed the transformation phase using the Random library, adding age and salary fields, replacing newline characters in addresses, and adding an 'updated_at' timestamp.
- Implemented the loading phase to write transformed data to a CSV file, specifying the output file format and field names.
- Executed the ETL job, verifying the creation of the CSV file containing the transformed data.

(Release date: 26/02/2024)

### Future Steps

Consume data from a API.
Generate a Company that create relationship with the employes.