import os
import requests

from dotenv import load_dotenv

load_dotenv()
base_url = os.environ["base_url"]


def pass_question_to_router(
    username,
    question,
    endpoint: str = "/request/route/",
):
    """
    Sends a username and question to the FastAPI endpoint and returns the response.

    Args:
        username (str): The name of the user asking the question.
        question (str): The question to be sent to the endpoint.
        base_url (str): The base URL of the API endpoint.
        endpoint (str): The specific route of the API.

    Returns:
        str: The response from the endpoint.
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}"
    payload = {
        "username": username,
        "question": question,
    }

    try:
        response = requests.post(
            endpoint_url,
            json=payload,
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()
        if data.get("status") == "success":
            return data.get("message")
        else:
            # TODO : better error handling
            return "Couldn't get answer"
    except requests.exceptions.RequestException as e:
        return f"An error occurred while handling request: {e}"
    except Exception as ex:
        return f"An error : {ex}"


def get_all_users(endpoint: str = "/users/"):
    """
    Get all users from the FastAPI endpoint.

    Returns:
        list: A list of all users.
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}"
    try:
        response = requests.get(
            endpoint_url,
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            # TODO : better error handling
            return []
    except requests.exceptions.RequestException as e:
        return f"An error occurred while handling request: {e}"
    except Exception as ex:
        return f"An error : {ex}"
