# Engineering Task Cards Explorer

This project is a back-end service that provides functionality to explore a set of engineering task cards, allowing users to map all the cards, delete a card, and search for a card based on its title or description. This README file will guide you through the project, its architecture, and how to use the service effectively.

## Table of Contents

- [Architecture](#architecture)
- [Coding Project](#coding-project)
- [API Endpoints](#api-endpoints)
- [Running the Service](#running-the-service)
- [Testing](#testing)

## Architecture

This project was implemented based on the clean architecture pattern and deployed on an AWS Lambda Function using an AWS API Gateway as trigger.

One of the particularities of the architecture is the Singleton implementation of the TaskBoardRepository, which allows to simulate with simplicity a system with a persistent storage.

### Architecture Diagram

![image](https://github.com/julianolm/TaskManager/assets/65794514/c56b35b0-8708-4603-bd83-5039ba4f52ce)

## API Endpoints

The service provides the following API endpoints:

- **POST /search**: Searches for cards based on a query string provided in the request and returns a shallow list of them.
- - Requires two fields in the body: `dataset` and `text_to_search`
- **POST /map**: Returns a hierarchical map of all engineering task cards descendants from the requested one.
- - Requires two fields in the body: `dataset` and `task_id`
- **POST /delete**: Deletes a card on cascade based on its id and returns the updated dataset in csv format.
- - Requires two fields in the body: `dataset` and `task_id`

### API Example - Search

**Request: POST /search**

```http
POST /search
```
**Body:**

```json
{
    "dataset": "Parent,ID,Status,Title,Description\nroot,TSK-9831,Not Started,Implement User Authentication Flow,Set up the user login and registration flow using OAuth 2.0\nTSK-9831,TSK-4012,In Progress,Optimize Database Query Performance,Profile and optimize slow-running queries in the user dashboard section.\nTSK-9831,TSK-5720,Under Review,Develop RESTful API for Product Management,Design and implement CRUD operations for the product entity.\nTSK-9831,TSK-6892,In Progress,Integrate Third-party Payment Gateway,Incorporate Stripe (or any other payment gateway) for processing user payments.\nTSK-5720,TSK-2357,On Hold,Refactor Legacy Code in User Module,\"Improve code quality, remove deprecated functions, and ensure compatibility with the latest libraries.\"\nTSK-5720,TSK-9145,In Progress,Design Responsive Landing Page,Create a responsive landing page that is compatible with both desktop and mobile devices.\nTSK-5720,TSK-3086,Deployed,Set Up Continuous Integration Pipeline,Implement a CI/CD pipeline using Jenkins (or any other CI tool) to automate the testing and deployment process.\nTSK-5720,TSK-7023,Testing,Enhance Security with Rate Limiting,Implement rate limiting on critical API endpoints to prevent abuse.\nTSK-5720,TSK-5214,Deployed,Migrate User Data to New Schema,Develop scripts to migrate existing user data to the newly designed database schema without data loss.\nTSK-7023,TSK-8490,Deployed,Implement Error Logging and Monitoring,\"Integrate tools like Sentry or Loggly to track, monitor, and alert on application errors in real-time.\"",
    "text_to_search": "design"
}

```

**Response:**

```json
{
    "tasks": [
        {
            "id": "TSK-5720",
            "status": "Under Review",
            "title": "Develop RESTful API for Product Management",
            "description": "Design and implement CRUD operations for the product entity.",
            "children": [
                "TSK-2357",
                "TSK-9145",
                "TSK-3086",
                "TSK-7023",
                "TSK-5214"
            ]
        },
        {
            "id": "TSK-9145",
            "status": "In Progress",
            "title": "Design Responsive Landing Page",
            "description": "Create a responsive landing page that is compatible with both desktop and mobile devices.",
            "children": []
        },
        {
            "id": "TSK-5214",
            "status": "Deployed",
            "title": "Migrate User Data to New Schema",
            "description": "Develop scripts to migrate existing user data to the newly designed database schema without data loss.",
            "children": []
        }
    ]
}
```


### API Example - Map

**Request: POST /map**

```http
POST /map
```
**Body:**

```json
{
    "dataset": "Parent,ID,Status,Title,Description\nroot,TSK-9831,Not Started,Implement User Authentication Flow,Set up the user login and registration flow using OAuth 2.0\nTSK-9831,TSK-4012,In Progress,Optimize Database Query Performance,Profile and optimize slow-running queries in the user dashboard section.\nTSK-9831,TSK-5720,Under Review,Develop RESTful API for Product Management,Design and implement CRUD operations for the product entity.\nTSK-9831,TSK-6892,In Progress,Integrate Third-party Payment Gateway,Incorporate Stripe (or any other payment gateway) for processing user payments.\nTSK-5720,TSK-2357,On Hold,Refactor Legacy Code in User Module,\"Improve code quality, remove deprecated functions, and ensure compatibility with the latest libraries.\"\nTSK-5720,TSK-9145,In Progress,Design Responsive Landing Page,Create a responsive landing page that is compatible with both desktop and mobile devices.\nTSK-5720,TSK-3086,Deployed,Set Up Continuous Integration Pipeline,Implement a CI/CD pipeline using Jenkins (or any other CI tool) to automate the testing and deployment process.\nTSK-5720,TSK-7023,Testing,Enhance Security with Rate Limiting,Implement rate limiting on critical API endpoints to prevent abuse.\nTSK-5720,TSK-5214,Deployed,Migrate User Data to New Schema,Develop scripts to migrate existing user data to the newly designed database schema without data loss.\nTSK-7023,TSK-8490,Deployed,Implement Error Logging and Monitoring,\"Integrate tools like Sentry or Loggly to track, monitor, and alert on application errors in real-time.\"",
    "task_id": "TSK-7023"
}

```

**Response:**

```json
{
    "task": {
        "id": "TSK-7023",
        "status": "Testing",
        "title": "Enhance Security with Rate Limiting",
        "description": "Implement rate limiting on critical API endpoints to prevent abuse.",
        "children": [
            {
                "id": "TSK-8490",
                "status": "Deployed",
                "title": "Implement Error Logging and Monitoring",
                "description": "Integrate tools like Sentry or Loggly to track, monitor, and alert on application errors in real-time.",
                "children": []
            }
        ]
    }
}
```

### API Example - Delete

**Request: POST /delete**

```http
POST /delete
```
**Body:**

```json
{
    "dataset": "Parent,ID,Status,Title,Description\nroot,TSK-9831,Not Started,Implement User Authentication Flow,Set up the user login and registration flow using OAuth 2.0\nTSK-9831,TSK-4012,In Progress,Optimize Database Query Performance,Profile and optimize slow-running queries in the user dashboard section.\nTSK-9831,TSK-5720,Under Review,Develop RESTful API for Product Management,Design and implement CRUD operations for the product entity.\nTSK-9831,TSK-6892,In Progress,Integrate Third-party Payment Gateway,Incorporate Stripe (or any other payment gateway) for processing user payments.\nTSK-5720,TSK-2357,On Hold,Refactor Legacy Code in User Module,\"Improve code quality, remove deprecated functions, and ensure compatibility with the latest libraries.\"\nTSK-5720,TSK-9145,In Progress,Design Responsive Landing Page,Create a responsive landing page that is compatible with both desktop and mobile devices.\nTSK-5720,TSK-3086,Deployed,Set Up Continuous Integration Pipeline,Implement a CI/CD pipeline using Jenkins (or any other CI tool) to automate the testing and deployment process.\nTSK-5720,TSK-7023,Testing,Enhance Security with Rate Limiting,Implement rate limiting on critical API endpoints to prevent abuse.\nTSK-5720,TSK-5214,Deployed,Migrate User Data to New Schema,Develop scripts to migrate existing user data to the newly designed database schema without data loss.\nTSK-7023,TSK-8490,Deployed,Implement Error Logging and Monitoring,\"Integrate tools like Sentry or Loggly to track, monitor, and alert on application errors in real-time.\"",
    "task_id": "TSK-5720"
}

```

**Response:**

```json
{
    "dataset": "Parent,ID,Status,Title,Description\nroot,TSK-9831,Not Started,Implement User Authentication Flow,Set up the user login and registration flow using OAuth 2.0\nTSK-9831,TSK-4012,In Progress,Optimize Database Query Performance,Profile and optimize slow-running queries in the user dashboard section.\nTSK-9831,TSK-6892,In Progress,Integrate Third-party Payment Gateway,Incorporate Stripe (or any other payment gateway) for processing user payments."
}
```

## Running the Service

To deploy this service on your aws account, first download and configure `aws-cli` and `cdk` and then follow these steps:

1. Clone the repository.
2. Install the necessary dependencies.
3. Deploy

```bash
git clone https://github.com/your/repo.git
cd project-directory
pip install -r requirements.txt
cdk deploy
```

Then you should see the deployed services on your AWS account.

## Testing

Tests were not developed to this project in order to save time, since up to this point I don't know any python testing framewokrs nor have any prior experience writing tests in python.
