import os
import requests

from dotenv import load_dotenv

load_dotenv()


def pass_question_to_router(
    username,
    question,
    base_url: str = os.environ["base_url"],
    # TODO: change this to use the env variable?
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
