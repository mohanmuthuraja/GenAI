import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:5000"

st.title("Employee Management System")

menu = st.sidebar.selectbox(
    "Select Action",
    ["Add Employee", "View Employees", "Search Employee", "Delete Employee"]
)

# Add Employee
if menu == "Add Employee":
    st.subheader("Add New Employee")

    emp_id = st.text_input("Employee ID")
    name = st.text_input("Name")
    department = st.text_input("Department")
    salary = st.number_input("Salary", min_value=0)

    if st.button("Add"):
        response = requests.post(
            f"{BASE_URL}/employee",
            json={
                "id": emp_id,
                "name": name,
                "department": department,
                "salary": salary
            }
        )

        if response.status_code == 201:
            st.success("Employee Added Successfully!")
        else:
            st.error(response.json()["error"])


# View Employees
elif menu == "View Employees":
    st.subheader("All Employees")

    response = requests.get(f"{BASE_URL}/employees")
    data = response.json()

    if data:
        st.table(data)
    else:
        st.info("No employees found")


# Search Employee
elif menu == "Search Employee":
    st.subheader("Search Employee by ID")

    search_id = st.text_input("Enter Employee ID")

    if st.button("Search"):
        response = requests.get(f"{BASE_URL}/employee/{search_id}")

        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Employee not found")


# Delete Employee
elif menu == "Delete Employee":
    st.subheader("Delete Employee")

    delete_id = st.text_input("Enter Employee ID")

    if st.button("Delete"):
        response = requests.delete(f"{BASE_URL}/employee/{delete_id}")
        st.success("Delete operation completed")