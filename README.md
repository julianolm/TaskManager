# Engineering Task Cards Explorer

This project is a back-end service that provides functionality to explore a set of engineering task cards, allowing users to map all the cards, delete a card, and search for a card based on its title or description. This README file will guide you through the project, its architecture, and how to use the service effectively.

## Table of Contents

- [Architecture](#architecture)
- [Coding Project](#coding-project)
- [API Endpoints](#api-endpoints)
- [Running the Service](#running-the-service)
- [Testing](#testing)
- [Swagger Interface](#swagger-interface)
- [Contributing](#contributing)
- [License](#license)

## Architecture

The first step in this project is to design the architecture. A clear and efficient architecture is essential for the success of this service. The architecture should include modules, services, and interfaces, and it should be detailed and well-documented. You can either draw the architecture on paper or create a digital diagram to visualize how the components interact with each other.

### Architecture Diagram

Your architecture diagram should illustrate the key components of the system, including:

- **API Interface**: The entry point for interacting with the service.
- **Data Access Layer**: Responsible for handling the interaction with the dataset.
- **Search Module**: Implements the search functionality.
- **Delete Module**: Implements the card deletion functionality.
- **Mapping Module**: Generates a hierarchical map of all cards.

### Coding Project

This service is implemented using Python, and it's preferably deployed using AWS Lambda. It is triggered by API calls, and it allows users to search, delete, and map engineering task cards. The backend is responsible for processing requests and interacting with the dataset. Here are the primary features of the service:

- **Search**: Users can search for cards based on their title or description. The search results will include the card hierarchy.
- **Delete**: Users can delete a card using its reference.
- **Mapping**: The service can generate a hierarchical map of all cards.

## API Endpoints

The service provides the following API endpoints:

- **POST /search**: Searches for cards based on a query string provided in the request and returns a shallow list of them.
- **POST /map**: Returns a hierarchical map of all engineering task cards descendants from the requested one.
- **POST /delete**: Deletes a card on cascade based on its id and returns the updated dataset in csv format.

### API Example - Map

**Request: POST /map**

```http
POST /map
```
**Body:**

```json
{
    "dataset": "Parent,ID,Status,Title,Description\nroot,TSK-9831,Not Started,Implement User Authentication Flow,Set up the user login and registration flow using OAuth 2.0\nTSK-9831,TSK-4012,In Progress,Optimize Database Query Performance,Profile and optimize slow-running queries in the user dashboard section.\nTSK-9831,TSK-5720,Under Review,Develop RESTful API for Product Management,Design and implement CRUD operations for the product entity.\nTSK-9831,TSK-6892,In Progress,Integrate Third-party Payment Gateway,Incorporate Stripe (or any other payment gateway) for processing user payments.\nTSK-5720,TSK-2357,On Hold,Refactor Legacy Code in User Module,\"Improve code quality, remove deprecated functions, and ensure compatibility with the latest libraries.\"\nTSK-5720,TSK-9145,In Progress,Design Responsive Landing Page,Create a responsive landing page that is compatible with both desktop and mobile devices.\nTSK-5720,TSK-3086,Deployed,Set Up Continuous Integration Pipeline,Implement a CI/CD pipeline using Jenkins (or any other CI tool) to automate the testing and deployment process.\nTSK-5720,TSK-7023,Testing,Enhance Security with Rate Limiting,Implement rate limiting on critical API endpoints to prevent abuse.\nTSK-5720,TSK-5214,Deployed,Migrate User Data to New Schema,Develop scripts to migrate existing user data to the newly designed database schema without data loss.\nTSK-7023,TSK-8490,Deployed,Implement Error Logging and Monitoring,\"Integrate tools like Sentry or Loggly to track, monitor, and alert on application errors in real-time.\"",
    "text_to_search": "implement"
}

```

**Response:**

```json
{
    "tasks": [
        {
            "id": "TSK-9831",
            "status": "Not Started",
            "title": "Implement User Authentication Flow",
            "description": "Set up the user login and registration flow using OAuth 2.0",
            "children": [
                "TSK-4012",
                "TSK-5720",
                "TSK-6892"
            ]
        },
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
            "id": "TSK-3086",
            "status": "Deployed",
            "title": "Set Up Continuous Integration Pipeline",
            "description": "Implement a CI/CD pipeline using Jenkins (or any other CI tool) to automate the testing and deployment process.",
            "children": []
        },
        {
            "id": "TSK-7023",
            "status": "Testing",
            "title": "Enhance Security with Rate Limiting",
            "description": "Implement rate limiting on critical API endpoints to prevent abuse.",
            "children": [
                "TSK-8490"
            ]
        },
        {
            "id": "TSK-8490",
            "status": "Deployed",
            "title": "Implement Error Logging and Monitoring",
            "description": "Integrate tools like Sentry or Loggly to track, monitor, and alert on application errors in real-time.",
            "children": []
        }
    ]
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

The project includes unit tests and lint checks to ensure code quality. To run the tests, use the following command:

```bash
pytest
```

Additionally, you should set up a strong CI/CD pipeline to automate these tests and deployments for a production environment.

## Swagger Interface

A SWAGGER-like interface for the API is provided, making it easier to explore and interact with the service. You can access it at `http://localhost:5000/api/docs`.

## Contributing

We welcome contributions from the open-source community. If you have ideas for improvements or want to report issues, please submit a pull request or create an issue on our GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

Thank you for your interest in the Engineering Task Cards Explorer service. We hope you find this project both informative and useful for your engineering task management needs.