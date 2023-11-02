#!/usr/bin/python3

import requests

# Get employee TODO list progress
def get_employee_todo_progress(employee_id):
    """Retrieves and displays the TODO list progress of a given employee using a REST API.

    Args:
        employee_id (int): The ID of the employee for whom the TODO list progress is to be retrieved.

    Returns:
        None: Displays the employee TODO list progress on the standard output.
    """

    # Validate the employee ID
    if not isinstance(employee_id, int) or employee_id <= 0:
        raise ValueError("Employee ID should be a positive integer.")

    # Send a GET request to the API endpoint
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    # Check for errors
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")

    # Get the employee name
    employee_name = response.json()[0]["user"]["name"]

    # Get the total number of tasks
    total_number_of_tasks = len(response.json())

    # Count the number of completed tasks
    number_of_done_tasks = 0
    for task in response.json():
        if task.get("completed", False):
            number_of_done_tasks += 1

    # Display the employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
    for task in response.json():
        if task.get("completed", False):
            print(f"\t{task['title']}")

if __name__ == "__main__":
    # Get the employee ID from the user
    employee_id = int(input("Enter employee ID: "))

    # Get the employee TODO list progress
    get_employee_todo_progress(employee_id)

