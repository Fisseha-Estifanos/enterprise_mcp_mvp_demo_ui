# enterprise_mcp_mvp_demo_

The UI for the enterprise MCP MVP demo feature.

## Prerequisites

- Python 3.13
- Poetry
- Docker (optional, for containerization)

## Installation

1. Clone the repository:

    ```sh
    git clone git@github.com:Fisseha-Estifanos/enterprise_mcp_mvp_demo_ui.git
    cd enterprise_mcp_mvp_demo_ui
    ```

2. Create a virtual environment and activate it:

    ```sh
    poetry init
    poetry shell
    ```

3. Install dependencies using Poetry:

    ```sh
    poetry install
    ```

4. Copy the example environment file and configure it as needed:

    ```sh
    cp .env.dev.example .env.dev
    ```

    Edit the [.env.dev](http://_vscodecontentref_/1) file to set the appropriate values for your environment.

## Running the Application

1. Start the application in development mode:

    ```sh
    poe start-dev
    ```

    This will source the [.env.dev](http://_vscodecontentref_/2) file and run the Streamlit application.

2. Open your web browser and navigate to `http://localhost:8501` to view the application.

## Using Docker

1. Build the Docker image:

    ```sh
    docker build -t enterprise_mcp_mvp_demo_ui .
    ```

2. Run the Docker container:

    ```sh
    docker run -p 8501:8501 enterprise_mcp_mvp_demo_ui
    ```

    This will start your Streamlit application and make it accessible on port 8501.

## Linting and Formatting

1. To lint the code:

    ```sh
    poe lint
    ```

2. To format the code:

    ```sh
    poe format
    ```


3. Before committing/contributing to this repo please run:

    ```sh
    poe pre-commit
    ```
