FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry install --no-dev

# Copy the rest of the application code into the container
COPY enterprise_mcp_mvp_demo_ui /app/enterprise_mcp_mvp_demo_ui

# Copy the .env file into the container if it exists
COPY .env /app/enterprise_mcp_mvp_demo_ui/.env

# Install python-dotenv
RUN poetry add python-dotenv

# Set environment variables
ENV STREAMLIT_SERVER_PORT=8501

# Expose the port Streamlit runs on
EXPOSE 8501

# Run the application
CMD ["poetry", "run", "streamlit", "run", "enterprise_mcp_mvp_demo_ui/main.py"]
