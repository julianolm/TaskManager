from classes import Task, TaskBoard 

# # Usage:
# task1 = Task("TSK-9831", "Not Started", "Implement User Authentication Flow", "Set up the user login and registration flow using OAuth 2.0")
# task2 = Task("TSK-4012", "In Progress", "Optimize Database Query Performance", "Profile and optimize slow-running queries in the user dashboard section")
# task1.add_child(task2)
# task2.set_parent(task1)

# print(f'task1\n{task1}')
# print()
# print(f'task2\n{task2}')

input_csv = '''Parent,ID,Status,Title,Description
root,TSK-9831,Not Started,Implement User Authentication Flow,Set up the user login and registration flow using OAuth 2.0
TSK-9831,TSK-4012,In Progress,Optimize Database Query Performance,Profile and optimize slow-running queries in the user dashboard section.
TSK-9831,TSK-5720,Under Review,Develop RESTful API for Product Management,Design and implement CRUD operations for the product entity.
TSK-9831,TSK-6892,In Progress,Integrate Third-party Payment Gateway,Incorporate Stripe (or any other payment gateway) for processing user payments.
TSK-5720,TSK-2357,On Hold,Refactor Legacy Code in User Module,"Improve code quality, remove deprecated functions, and ensure compatibility with the latest libraries."
TSK-5720,TSK-9145,In Progress,Design Responsive Landing Page,Create a responsive landing page that is compatible with both desktop and mobile devices.
TSK-5720,TSK-3086,Deployed,Set Up Continuous Integration Pipeline,Implement a CI/CD pipeline using Jenkins (or any other CI tool) to automate the testing and deployment process.
TSK-5720,TSK-7023,Testing,Enhance Security with Rate Limiting,Implement rate limiting on critical API endpoints to prevent abuse.
TSK-5720,TSK-5214,Deployed,Migrate User Data to New Schema,Develop scripts to migrate existing user data to the newly designed database schema without data loss.
TSK-7023,TSK-8490,Deployed,Implement Error Logging and Monitoring,"Integrate tools like Sentry or Loggly to track, monitor, and alert on application errors in real-time."'''

tasks = TaskBoard(input_csv)
returned_csv = tasks.csv()

# build a set with each line of the csv
input_csv_set = set(input_csv.split("\n"))
returned_csv_set = set(returned_csv.split("\n"))
print(input_csv_set == returned_csv_set)