# fullstack-python-project

```
fullstack-python-project/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── schema.py
│   │   └── mongo.py
│   ├── scripts/
│   │   └── manage.py (bootstrap)
│   ├── tests/
│   │   ├── test_main.py
│   │   ├── test_schema.py
│   │   └── test_mongo.py
│   ├── conftest.py (pytest)
│   ├── pyproject.toml (poetry)
│   ├── sonar-project.properties
│   └── Dockerfile
├── docker-compose.yml
├── .gitignore
├── README.md
```
## Project Structure

The project is organized as follows:

### Backend
- **`app/`**: Contains the main application code.
    - **`main.py`**: Entry point for the backend application.
    - **`schema.py`**: Defines the data models and schemas.
    - **`mongo.py`**: Handles MongoDB interactions.
- **`scripts/`**: Contains utility scripts.
    - **`manage.py`**: Bootstrap script for managing tasks.
- **`tests/`**: Includes unit tests for the backend.
    - **`test_main.py`**: Tests for `main.py`.
    - **`test_schema.py`**: Tests for `schema.py`.
    - **`test_mongo.py`**: Tests for `mongo.py`.
- **`conftest.py`**: Configuration for pytest.
- **`pyproject.toml`**: Poetry configuration file for dependency management.
- **`sonar-project.properties`**: Configuration for SonarQube analysis.
- **`Dockerfile`**: Docker configuration for the backend.

### Root
- **`docker-compose.yml`**: Defines services for Docker Compose.
- **`.gitignore`**: Specifies files and directories to ignore in Git.
- **`README.md`**: Documentation for the project.

## Getting Started

1. **Clone the repository**:
     ```bash
     git clone https://github.com/your-username/fullstack-python-project.git
     cd fullstack-python-project
     ```

2. **Set up the backend**:
     - Install dependencies using Poetry:
         ```bash
         cd backend
         poetry install
         ```
     - Run the seed to populate BD:
         ```bash
         poetry run manage seed
         ```
     - Run the application:
         ```bash
         poetry run manage start
         ```

3. **Run tests**:
     ```bash
     cd backend
     poetry run pytest
     ```
     It generates a temporal directory under ```backend/coverage_reports``` including boths, xml file (for sonarqube) and html directory. _Tip!: you can use Coverage Gutters to see in live on files._

4. **Start services with Docker Compose**:
     ```bash
     docker-compose up
     ```

## Contributing

Feel free to submit issues or pull requests to improve the project. Follow the [contribution guidelines](CONTRIBUTING.md) if available.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.