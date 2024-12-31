import os
import requests
from typing import Any

from dotenv import load_dotenv

load_dotenv()
base_url = os.environ["base_url"]


def handle_response(response: requests.Response) -> dict[str, Any]:
    """Handle API response and return structured data."""
    try:
        response.raise_for_status()
        return {
            "status": "success",
            "data": response.json(),
            "message": "Request successful",
        }
    except requests.exceptions.HTTPError as http_err:
        return {
            "status": "error",
            "data": None,
            "message": f"HTTP error occurred: {http_err}",
        }
    except requests.exceptions.RequestException as req_err:
        return {
            "status": "error",
            "data": None,
            "message": f"Request error occurred: {req_err}",
        }
    except Exception as ex:
        return {
            "status": "error",
            "data": None,
            "message": f"An unexpected error occurred: {ex}",
        }


def login_user(
    username: str,
    password: str,
    endpoint: str = "/auth/login/",
) -> dict[str, Any]:
    """
    Logs in a user with the given username and password.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.

        endpoint (str): The specific route of the API.

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}"
    payload = {
        "username": username,
        "password": password,
    }

    try:
        response = requests.post(
            endpoint_url,
            json=payload,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {"status": "error", "data": None, "message": f"Login failed: {ex}"}


def pass_question_to_router(
    username: str,
    question: str,
    endpoint: str = "/request/route/",
) -> dict[str, Any]:
    """
    Send request and handle response.

    Args:
        username (str): The username of the user.
        question (str): The question to ask the chatbot.
        base_url (str): The base URL of the API.
        endpoint (str): The specific route of the API.
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
        handled_response = handle_response(response)
        return handled_response["data"]["message"]
    except Exception as ex:
        return {
            "status": "error",
            "data": None,
            "message": f"Failed to process request: {ex}",
        }


# region USERS
# The following code snippet is used to interact with the user management API.
# It is used to create, update, and delete users.
# The functions are used in the admin panel to manage users.


def create_user(
    username: str,
    email: str,
    password: str,
    endpoint: str = "/users/",
) -> dict[str, Any]:
    """
    Create a new user with the given username, email, and password.

    Args:
        username (str): The username of the user.
        email (str): The email of the user.
        password (str): The password of the user.
        endpoint (str): The specific route of the API.

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}"
    payload = {
        "username": username,
        "email": email,
        "password": password,
    }

    try:
        response = requests.post(
            endpoint_url,
            json=payload,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": None,
            "message": f"Failed to create user: {ex}",
        }


def update_user(
    user_id: str,
    username: str,
    email: str,
    password: str,
    endpoint: str = "/users/",
) -> dict[str, Any]:
    """
    Update an existing user with the given user_id, username, email, and password.

    Args:
        user_id (str): The id of the user.
        username (str): The username of the user.
        email (str): The email of the user.
        password (str): The password of the user.
        endpoint (str): The specific route of the API.

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}{user_id}/"
    payload = {
        "username": username,
        "email": email,
        "password": password,
    }

    try:
        response = requests.put(
            endpoint_url,
            json=payload,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": None,
            "message": f"Failed to update user: {ex}",
        }


def delete_user(
    user_id: str,
    endpoint: str = "/users/",
) -> dict[str, Any]:
    """
    Delete an existing user with the given user_id.

    Args:
        user_id (str): The id of the user.
        endpoint (str): The specific route of the API.

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}{user_id}/"

    try:
        response = requests.delete(
            endpoint_url,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": None,
            "message": f"Failed to delete user: {ex}",
        }


def get_user(
    user_id: str,
    endpoint: str = "/users/",
) -> dict[str, Any]:
    """
    Get an existing user with the given user_id.

    Args:
        user_id (str): The id of the user.

        endpoint (str): The specific route of the API.

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}{user_id}/"

    try:
        response = requests.get(
            endpoint_url,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": None,
            "message": f"Failed to get user: {ex}",
        }


def get_users(
    endpoint: str = "/users/",
) -> dict[str, Any]:
    """
    Get all users from the FastAPI endpoint.

    Args:

        endpoint (str): API endpoint for users

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}"

    try:
        response = requests.get(
            endpoint_url,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": [],
            "message": f"Failed to fetch users: {ex}",
        }


# endregion USERS


# region ROLES
# The following code snippet is used to interact with the role management API.
# It is used to create, update, and delete roles.
# The functions are used in the admin panel to manage roles.


def create_role(
    role_name: str,
    endpoint: str = "/roles/",
) -> dict[str, Any]:
    """
    Create a new role with the given role_name.

    Args:
        role_name (str): The name of the role.
        endpoint (str): The specific route of the API.

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}"
    payload = {
        "name": role_name,
    }
    print(f"Payload: {payload}")
    print(f"type: {type(payload)}")

    try:
        response = requests.post(
            endpoint_url,
            json=payload,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": None,
            "message": f"Failed to create role: {ex}",
        }


def update_role(
    role_id: str,
    role_name: str,
    endpoint: str = "/roles/",
) -> dict[str, Any]:
    """
    Update an existing role with the given role_id and role_name.

    Args:
        role_id (str): The id of the role.
        role_name (str): The name of the role.

        endpoint (str): The specific route of the API.

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}{role_id}/"
    payload = {
        "name": role_name,
    }

    try:
        response = requests.put(
            endpoint_url,
            json=payload,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": None,
            "message": f"Failed to update role: {ex}",
        }


def delete_role(
    role_id: str,
    endpoint: str = "/roles/",
) -> dict[str, Any]:
    """
    Delete an existing role with the given role_id.

    Args:
        role_id (str): The id of the role.

        endpoint (str): The specific route of the API.

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}{role_id}/"

    try:
        response = requests.delete(
            endpoint_url,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": None,
            "message": f"Failed to delete role: {ex}",
        }


def get_role(
    role_id: str,
    endpoint: str = "/roles/",
) -> dict[str, Any]:
    """
    Get an existing role with the given role_id.

    Args:
        role_id (str): The id of the role.

        endpoint (str): The specific route of the API.

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}{role_id}/"

    try:
        response = requests.get(
            endpoint_url,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": None,
            "message": f"Failed to get role: {ex}",
        }


def get_roles(
    endpoint: str = "/roles/",
) -> dict[str, Any]:
    """
    Get all roles from the FastAPI endpoint.

    Args:

        endpoint (str): API endpoint for roles

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}"

    try:
        response = requests.get(
            endpoint_url,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": [],
            "message": f"Failed to fetch roles: {ex}",
        }


# endregion ROLES

# region PERMISSIONS
# The following code snippet is used to interact with the permission management API.
# It is used to create, update, and delete permissions.
# The functions are used in the admin panel to manage permissions.


def create_permission(
    permission_name: str,
    endpoint: str = "/permissions/",
) -> dict[str, Any]:
    """
    Create a new permission with the given permission_name.

    Args:
        permission_name (str): The name of the permission.

        endpoint (str): The specific route of the API.

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}"
    payload = {
        "name": permission_name,
    }

    try:
        response = requests.post(
            endpoint_url,
            json=payload,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": None,
            "message": f"Failed to create permission: {ex}",
        }


def update_permission(
    permission_id: str,
    permission_name: str,
    endpoint: str = "/permissions/",
) -> dict[str, Any]:
    """
    Update an existing permission with the given permission_id and permission_name.

    Args:
        permission_id (str): The id of the permission.
        permission_name (str): The name of the permission.

        endpoint (str): The specific route of the API.

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}{permission_id}/"
    payload = {
        "name": permission_name,
    }

    try:
        response = requests.put(
            endpoint_url,
            json=payload,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": None,
            "message": f"Failed to update permission: {ex}",
        }


def delete_permission(
    permission_id: str,
    endpoint: str = "/permissions/",
) -> dict[str, Any]:
    """
    Delete an existing permission with the given permission_id.

    Args:
        permission_id (str): The id of the permission.

        endpoint (str): The specific route of the API.

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}{permission_id}/"

    try:
        response = requests.delete(
            endpoint_url,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": None,
            "message": f"Failed to delete permission: {ex}",
        }


def get_permission(
    permission_id: str,
    endpoint: str = "/permissions/",
) -> dict[str, Any]:
    """
    Get an existing permission with the given permission_id.

    Args:
        permission_id (str): The id of the permission.

        endpoint (str): The specific route of the API.

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}{permission_id}/"

    try:
        response = requests.get(
            endpoint_url,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": None,
            "message": f"Failed to get permission: {ex}",
        }


def get_permissions(
    endpoint: str = "/permissions/",
) -> dict[str, Any]:
    """
    Get all permissions from the FastAPI endpoint.

    Args:

        endpoint (str): API endpoint for permissions

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}"

    try:
        response = requests.get(
            endpoint_url,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": [],
            "message": f"Failed to fetch permissions: {ex}",
        }


# endregion PERMISSIONS

# region ASSOCIATIONS
# The following code snippet is used to interact with the association management API.
# It is used to create, update, and delete associations between users, roles, and permissions.
# The functions are used in the admin panel to manage associations.


def create_association(
    user: str,
    role: str,
    resource: str,
    permission: str,
    endpoint: str = "/associations/",
) -> dict[str, Any]:
    """
    Create a new association with the given user, role, resource, and permission.

    Args:
        user (str): The name of the user.
        role (str): The name of the role.
        resource (str): The name of the resource.
        permission (str): The name of the permission.
        endpoint (str): The specific route of the API.

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}"
    payload = {
        "subject": user,
        "role": role,
        "domain": resource,
        "permission": permission,
    }

    try:
        response = requests.post(
            endpoint_url,
            json=payload,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": None,
            "message": f"Failed to create association: {ex}",
        }


def get_associations(
    endpoint: str = "/associations/",
) -> dict[str, Any]:
    """
    Get all associations from the FastAPI endpoint.

    Args:
        endpoint (str): API endpoint for associations

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}"

    try:
        response = requests.get(
            endpoint_url,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": [],
            "message": f"Failed to fetch associations: {ex}",
        }


def get_role_subject():
    """
    Get all role_subject associations from the FastAPI endpoint.

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}/associations/role_subject/"
    try:
        response = requests.get(
            endpoint_url,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": [],
            "message": f"Failed to fetch role_subject: {ex}",
        }


def test_permissions(
    user: str,
    resource: str,
    permission: str,
    endpoint: str = "/associations/test_permissions/",
) -> dict[str, Any]:
    """
    Test permissions for a user on a resource.

    Args:
        user (str): The name of the user.
        resource (str): The name of the resource.
        permission (str): The name of the permission.
        endpoint (str): The specific route of the API.

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}"
    payload = {
        "user": user,
        "resource": resource,
        "permission": permission,
    }
    try:
        response = requests.post(
            endpoint_url,
            json=payload,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": None,
            "message": f"Failed to test permissions: {ex}",
        }


# endregion ASSOCIATIONS


# region RESOURCES
# The following code snippet is used to interact with the resource management API.
# It is used to create, update, and delete resources.
# The functions are used in the admin panel to manage resources.


def create_resource(
    resource_name: str,
    endpoint: str = "/servers/",
) -> dict[str, Any]:
    """
    Create a new resource with the given resource_name.

    Args:
        resource_name (str): The name of the resource.

        endpoint (str): The specific route of the API.

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}"
    payload = {
        "name": resource_name,
    }

    try:
        response = requests.post(
            endpoint_url,
            json=payload,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": None,
            "message": f"Failed to create resource: {ex}",
        }


def update_resource(
    resource_id: str,
    resource_name: str,
    endpoint: str = "/servers/",
) -> dict[str, Any]:
    """
    Update an existing resource with the given resource_id and resource_name.

    Args:
        resource_id (str): The id of the resource.
        resource_name (str): The name of the resource.

        endpoint (str): The specific route of the API.

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}{resource_id}/"
    payload = {
        "name": resource_name,
    }

    try:
        response = requests.put(
            endpoint_url,
            json=payload,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": None,
            "message": f"Failed to update resource: {ex}",
        }


def delete_resource(
    resource_id: str,
    endpoint: str = "/servers/",
) -> dict[str, Any]:
    """
    Delete an existing resource with the given resource_id.

    Args:
        resource_id (str): The id of the resource.

        endpoint (str): The specific route of the API.

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}{resource_id}/"

    try:
        response = requests.delete(
            endpoint_url,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": None,
            "message": f"Failed to delete resource: {ex}",
        }


def get_resource(
    resource_id: str,
    endpoint: str = "/servers/",
) -> dict[str, Any]:
    """
    Get an existing resource with the given resource_id.

    Args:
        resource_id (str): The id of the resource.

        endpoint (str): The specific route of the API.

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}{resource_id}/"

    try:
        response = requests.get(
            endpoint_url,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": None,
            "message": f"Failed to get resource: {ex}",
        }


def get_resources(
    endpoint: str = "/servers/",
) -> dict[str, Any]:
    """
    Get all resources from the FastAPI endpoint.

    Args:

        endpoint (str): API endpoint for resources

    Returns:
        Dict[str, Any]: Response containing status, data and message
    """
    endpoint_url = f"{base_url.rstrip('/')}{endpoint}"

    try:
        response = requests.get(
            endpoint_url,
            timeout=30,
        )
        return handle_response(response)
    except Exception as ex:
        return {
            "status": "error",
            "data": [],
            "message": f"Failed to fetch resources: {ex}",
        }


# endregion RESOURCES
