"""
Admin page for the Streamlit app.
"""

import streamlit as st
from time import sleep

import utils


def display_admin_ui():
    """Display the admin UI."""
    st.title("Admin Panel")

    tabs = st.tabs(
        ["Roles and Permissions", "User Management", "Resources", "Associations"]
    )

    with tabs[0]:
        st.header("Roles and Permissions")
        roles_and_permissions = st.tabs(["Roles", "Permissions"])

        with roles_and_permissions[0]:
            st.subheader("Manage roles here")
            roles = utils.get_roles()
            roles = roles["data"]
            st.data_editor(roles, num_rows="dynamic")

            st.subheader("Create New Role")
            new_role_name = st.text_input("Role Name")
            if st.button("Create Role"):
                role_created = utils.create_role(new_role_name)
                if role_created["status"] == "success":
                    st.success(f"Role {new_role_name} created")
                    sleep(2)
                    st.rerun()
                else:
                    st.error(f"Error creating role: {role_created["message"]}")
        with roles_and_permissions[1]:
            st.subheader("Manage permissions here")
            permissions = utils.get_permissions()
            permissions = permissions["data"]
            st.data_editor(permissions, num_rows="dynamic")

            st.subheader("Create New Permission")
            new_permission_name = st.text_input("Permission Name")
            if st.button("Create Permission"):
                permission_created = utils.create_permission(new_permission_name)
                if permission_created["status"] == "success":
                    st.success(f"Permission {new_permission_name} created")
                    sleep(2)
                    st.rerun()
                else:
                    st.error(
                        f"Error creating permission: {permission_created["message"]}"
                    )

    with tabs[1]:
        st.header("User Management")
        st.write("Manage users here.")

        users = utils.get_users()
        users = users["data"]
        st.data_editor(users, num_rows="dynamic")

        st.subheader("Create New User")
        username = st.text_input("User Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Create User"):
            try:
                user_created = utils.create_user(
                    username=username,
                    email=email,
                    password=password,
                )
                if user_created["status"] == "success":
                    st.success(f"User {username} created")
                    sleep(2)
                    st.rerun()
                else:
                    st.error(f"Error creating user: {user_created["message"]}")
            except Exception as e:
                st.error(f"Error creating user: {e}")

    with tabs[2]:
        st.header("Resources")
        st.write("Manage resources here.")

        resources = utils.get_resources()
        resources = resources["data"]
        st.data_editor(resources, num_rows="dynamic")

        st.subheader("Create New Resource")
        resource_name = st.text_input("Resource Name")
        if st.button("Create Resource"):
            resource_created = utils.create_resource(resource_name)
            if resource_created["status"] == "success":
                st.success(f"Resource {resource_name} created")
                sleep(2)
                st.rerun()
            else:
                st.error(f"Error creating resource: {resource_created["message"]}")

    with tabs[3]:
        st.header("Associations")
        st.write("Observe overall associations here.")

        associations = utils.get_associations()
        associations = associations["data"]
        st.data_editor(associations, num_rows="dynamic")

        st.divider()
        st.write("Observe user/group roles here.")
        users_and_roles = utils.get_role_subject()
        users_and_roles = users_and_roles["data"]
        st.data_editor(users_and_roles, num_rows="dynamic")

        st.divider()
        # create associations
        st.subheader("Create New Association")
        users = utils.get_users()
        users = users["data"]
        usernames = []
        for user in users:
            usernames.append(user["username"])
        user = st.selectbox("User", usernames)

        roles = utils.get_roles()
        roles = roles["data"]
        role_names = []
        for role in roles:
            role_names.append(role["name"])
        role = st.selectbox("Role", role_names)

        resources = utils.get_resources()
        resources = resources["data"]
        resource_names = []
        for resource in resources:
            resource_names.append(resource["name"])
        resource = st.selectbox("Resource", resource_names)

        permissions = utils.get_permissions()
        permissions = permissions["data"]
        permission_names = []
        for permission in permissions:
            permission_names.append(permission["name"])
        permission = st.selectbox("Permission", permission_names)

        if st.button("Create Association"):
            association_created = utils.create_association(
                user=user,
                role=role,
                resource=resource,
                permission=permission,
            )
            print(f"Association created: {association_created}")
            if association_created["status"] == "success":
                st.success(association_created["data"])
                sleep(2)
                st.rerun()
            else:
                st.error(
                    f"Error creating association: {association_created["message"]}"
                )

        st.divider()
        # test associations
        st.subheader("Test User Permissions")
        user = st.selectbox("User_", usernames)
        resource = st.selectbox("Resource_", resource_names)
        permission = st.selectbox("Permission_", permission_names)

        if st.button("Test Permissions"):
            test_permissions = utils.test_permissions(
                user=user,
                resource=resource,
                permission=permission,
            )
            if test_permissions["status"] == "success":
                if test_permissions["data"] == "Permission granted":
                    st.success(
                        f"User {user} has the required {permission} permission"
                        + f"over the {resource} resource"
                    )
                    st.success(test_permissions["data"])
                else:
                    st.error(
                        f"User {user} does not have the required {permission}"
                        + f"permission over the {resource} resource"
                    )
                    st.error(test_permissions["data"])

            else:
                st.error(f"Error testing permissions: {test_permissions["message"]}")
