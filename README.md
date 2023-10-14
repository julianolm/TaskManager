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

- **GET /api/cards**: Returns a hierarchical map of all engineering task cards.
- **GET /api/cards/search**: Searches for cards based on a query string provided in the request.
- **DELETE /api/cards/{card_id}**: Deletes a card based on its reference.

### API Example

**Request: GET /api/cards/search?query=Feature A**

```http
GET /api/cards/search?query=Feature A
```

**Response:**

```json
{
    "Feature A - In Progress": [
        "Task 1 - Not Started",
        "Task 2 - Completed",
        "Sub-task 2.1 - In Progress",
        "Sub-task 2.2 - Completed",
        "Task 3 - In Progress"
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