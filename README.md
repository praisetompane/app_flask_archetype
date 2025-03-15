# app_flask_archetype
![build status](https://github.com/praisetompane-utilities/app_flask_archetype/actions/workflows/app.yaml/badge.svg)

##  Objectives
- A Flask archetype with common patterns to enable focusing on the unique aspects of your application instead of setup ceremony.
- Features:
    - [Project Conversion](#usage)
    - HTTP REST API
        - [Application Logic Resource](src/app_flask_archetype/api/api.py)
        - [Health Check Resource](src/app_flask_archetype/api/health_check.py)
        - [Input Validator](src/app_flask_archetype/api/validator.py)
    - [External API Gateway](src/app_flask_archetype/gateway/external_api.py)
    - [Repository Pattern implemented with SQLAlchemy and Postgres](src/app_flask_archetype/repository/computation_result_repository.py)
    - [Alembic Migrations](src/app_flask_archetype/migrations/versions)
    - [Tests](tests/app_flask_archetype)
    - [GitHub Actions CI/CD](.github/workflows/app.yaml)

## Project Structure
- docs: Project documentation lives in here.
- src: Production code lives in this folder and is divided in the modules below:
    - app_flask_archetype: Project package.
        - api:
            - The HTTP API to the application lives in this module.
            - The current implementation is a HTTP REST API, but a gRPC, CLI API, etc would be implemented in here.
        - config:
            - Configuration lives in here.
        - core:
            - the domain logic of the application lives in this module.
        - gateway:
            - Integration with external objects(e.g. files, external APIs etc) lives in here.
        - model:
            - The domain model lives in here.
        - repository:
            - Integration with internal data store (persistence and access) lives in here.
        - app.py:
            - The application factory to bootstrap the system lives in here.
- tests: Test code lives in here.
    - The tests are intentionally separated from production code.
        - Benefits of this structure:
            - Tests can run against an installed version of the app after using `pip install .`.
            - Tests can run against the local copy with an editable install after executing `pip install --edit`.
        - [more in depth discussion here](https://docs.pytest.org/en/latest/explanation/goodpractices.html#choosing-a-test-layout-import-rules)

- utilities: Ad-hoc utilities such as scripts, curl & postman requests, JSON payloads, software installations, etc live in here.

## Dependencies
- [Docker](https://docs.docker.com/get-started/)

## Package Management
- [Pipenv](https://pipenv.pypa.io/en/latest/)
    - [Quick Reference](https://pipenv.pypa.io/en/latest/cli.html#install)

## Setup Instructions
- The repository is configured to use [devcontainers](https://containers.dev) for development.
    - [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers)

## Usage
- Project Conversion: Converts the project name to your desired name. This renames all import, configuration, etc.
    ```shell
    #target_app_name is desired project name
    ./convert_project.sh target_app_name
    ```
- Steps Executed:
    - Renames all occurrences of `app_flask_archetype` to `target_app_name`
    - Optional Step: Rename the project folder to user desired project name.
    This is a manual step, it is the folder you cloned this repository into.
   
## Run Program
- The system automatically starts up as part of loading the project into an editor/IDE that supports devcontainers.
    - If you would like to run the prod image, change `dockerfile: Dockerfile.dev` to `dockerfile: Dockerfile` in [docker-compose](docker-compose.debug.yaml).

- Manual
    - Execute the required update detailed here: [app_flask_archetype_postgres_service](https://github.com/praisetompane/app_flask_archetype/blob/aa89f106fa6485ab00719d4df5c094621604fb94/docker-compose.yaml#L11)
    - Manually start
        ```shell
        ./start_system_development.sh
        ```

    - Manually stop
        ```shell
        ./stop_system_development.sh
        ```

- Invoke an endpoint
    ```shell
    # specifically imports malaria_annual_confirmed_cases from WHO API
    ./utilities/curl/computation/computation.sh
    ```

- Debugging
    - Debug with VSCode:
        - Open the "Run and Debug" view.
        - Execute the "Python Debugger: Remote Attach" task.
            ![start system output](./docs/vscode_debugging.png)<br>
        - Allow debugging without frozen modules by clicking "Debug Anyway".
            ![bypass frozen modules](./docs/vscode_debugging_frozen.png)
        - The server will inform you the host and port in the terminal output at the bottom.<br>
        - Debug as you normally do(i.e. add break points, step into code definitions, evaluate code snippets, etc) <br>

    - If you would like to debug the prod image, change `dockerfile: Dockerfile.dev` to `dockerfile: Dockerfile` in [docker-compose.debug](docker-compose.debug.yaml).

## Testing
- ### Execute Unit Tests
    ```shell
    pytest
    ```
- ### Execute Integration Tests
    ```shell
    pytest tests/app_flask_archetype/integration
    ```
- ### Execute System Tests
    ```shell
    Not Implemented
    ```
- ### Execute Spellcheck
    ```shell
    pyspelling -c spellcheck.yaml
    ```

## Database State Management
- The database state (i.e. tables, stored procedures, indexes, etc) are managed using [Alembic](https://alembic.sqlalchemy.org/en/latest/).
    - Migrations location: src/app_flask_archetype/migrations
    - Migrations naming scheme: YYYY_MM_DD_HHMM_rev_name
        - uses alembic's full revision scheme defined in alembic.ini
        - example: `2025_02_10_1349-9e2772c6755f_create_schema_computation.py`
    - Current database state can be queried with `SELECT * FROM public.alembic_version;`
- To upgrade the database to latest migrations:
    ```shell
    alembic upgrade head
    ```
- To downgrade the database to the base state:
    ```shell
    alembic downgrade base
    ```

## Spell Check
```shell
pyspelling -c spellcheck.yaml
```

## Git Conventions
- **NB:** The main is locked and all changes must come through a Pull Request.
- Commit Messages:
    - Provide concise commit messages that describe what you have done.
        ```shell
        # example:
        git commit -m "feat(core): algorithm" -m"implement my new shiny faster algorithm"
        ```
    - screen shot of GitHub view
    - references:
        - https://www.conventionalcommits.org/en/v1.0.0/
        - https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/

**Disclaimer**: This is still work in progress.
