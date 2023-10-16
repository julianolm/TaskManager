import json
import csv
from io import StringIO

from lambda_handler import lambda_handler

input_csv = 'Parent,ID,Status,Title,Description\\nroot,TSK-9831,Not Started,Implement User Authentication Flow,Set up the user login and registration flow using OAuth 2.0\\nTSK-9831,TSK-4012,In Progress,Optimize Database Query Performance,Profile and optimize slow-running queries in the user dashboard section.\\nTSK-9831,TSK-5720,Under Review,Develop RESTful API for Product Management,Design and implement CRUD operations for the product entity.\\nTSK-9831,TSK-6892,In Progress,Integrate Third-party Payment Gateway,Incorporate Stripe (or any other payment gateway) for processing user payments.\\nTSK-5720,TSK-2357,On Hold,Refactor Legacy Code in User Module,\\"Improve code quality, remove deprecated functions, and ensure compatibility with the latest libraries.\\"\\nTSK-5720,TSK-9145,In Progress,Design Responsive Landing Page,Create a responsive landing page that is compatible with both desktop and mobile devices.\\nTSK-5720,TSK-3086,Deployed,Set Up Continuous Integration Pipeline,Implement a CI/CD pipeline using Jenkins (or any other CI tool) to automate the testing and deployment process.\\nTSK-5720,TSK-7023,Testing,Enhance Security with Rate Limiting,Implement rate limiting on critical API endpoints to prevent abuse.\\nTSK-5720,TSK-5214,Deployed,Migrate User Data to New Schema,Develop scripts to migrate existing user data to the newly designed database schema without data loss.\\nTSK-7023,TSK-8490,Deployed,Implement Error Logging and Monitoring,\\"Integrate tools like Sentry or Loggly to track, monitor, and alert on application errors in real-time.\\"'

def print_csv(csv_string):
    # Create a file-like object from the CSV string
    csv_file = StringIO(csv_string)
    
    # Create a CSV reader
    csv_reader = csv.reader(csv_file)
    
    # Iterate over the rows and print each row
    for row in csv_reader:
        print(', '.join(row))

def test_search_success():
    event = {
        "path": '/search',
        "body": f'{{"text_to_search": "implement", "dataset": "{input_csv}"}}',
        "httpMethod": "POST"
    }
    context = {}

    # Expects response to be an object containinng 'statusCode': 200
    response = lambda_handler(event, context)
    print(response)

def test_search_bad_request():
    event = {
        "path": '/search',
        "body": f'{{"text": "implement", "dataset": "{input_csv}"}}',
        "httpMethod": "POST"
    }
    context = {}

    # Expects response to be an object containinng 'statusCode': 400 and a body containing an error message "Request body missing on field: 'text_to_search'"
    response = lambda_handler(event, context)
    print(response)


if __name__ == "__main__":
    test_search_success()
    # test_search_bad_request()