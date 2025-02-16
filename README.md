# Rick and Morty API

This project is a Flask-based web application that fetches and displays characters from the Rick and Morty API. It provides a RESTful API and a user-friendly web interface to view character details.

## Features

- Fetches and displays live characters from the Rick and Morty API.
- Provides a `/docs` endpoint for API documentation using Swagger UI.
- Offers a simple web UI to browse characters with images and locations.
- Dockerized and deployed to a Kubernetes cluster.
- Includes automated tests using GitHub Actions.

## Installation

### Prerequisites

- Python 3
- Flask
- Docker
- Kubernetes (Minikube, K3s, or a cloud provider)
- Helm

### Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/steinberg1989/rickandmorty-api.git
   cd rickandmorty-api
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python app.py
   ```
4. Access the app:
    - Web UI: http://127.0.0.1:5000/
    - API Docs: http://127.0.0.1:5000/docs

## Docker Usage

### Build and Run

1. Build the Docker image:
   ```sh
   docker build -t rickandmorty-api .
   ```
2. Run the container:
   ```sh
   docker run -p 5000:5000 rickandmorty-api
   ```
3. Access the app at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Kubernetes Deployment

### Using YAML Manifests

1. Apply Kubernetes configurations:
   ```sh
   kubectl apply -f yamls/
   ```
2. Check the running pods:
   ```sh
   kubectl get pods
   ```
3. Forward the service to a local port:
   ```sh
   kubectl port-forward svc/rickandmorty-service 8080:80
   ```
4. Access the app at: [http://127.0.0.1:8080](http://127.0.0.1:8080)

### Using Helm

1. Install the Helm chart:
   ```sh
   helm install rickandmorty-app rickandmorty-chart/
   ```
2. Verify deployment:
   ```sh
   kubectl get pods,svc
   ```

## API Endpoints

| Endpoint       | Method | Description |
|---------------|--------|-------------|
| `/`           | GET    | Homepage with character viewer |
| `/characters` | GET    | Returns a list of human, alive characters |
| `/healthcheck`| GET    | Health status of the API |
| `/docs`       | GET    | API documentation |

## Running Tests

### Unit Tests

1. Make sure the application is running.
2. Run the tests:
   ```sh
   python -m unittest tests/test_api.py
   ```

### GitHub Actions CI

This project includes a GitHub Actions workflow that:
- Sets up a small Kubernetes cluster on the GitHub Actions runner.
- Deploys the application to the local cluster.
- Runs API endpoint tests.

To view the CI pipeline:
1. Go to the repository on GitHub.
2. Navigate to the `Actions` tab.
3. Check the latest workflow run for logs and results.

## Technologies Used

- Python & Flask
- HTML, CSS (for UI rendering)
- Docker & Kubernetes
- Helm (for deployment)
- GitHub Actions (for automated testing and CI/CD)

## Future Enhancements

- Add filtering options for character search
- Implement a database cache for faster responses
- Deploy to a cloud Kubernetes provider (e.g., AWS)



