"""
The client
Estimated Time: 2hours
Actual Time:
"""

from prac_07.project import Project
import datetime

FILENAME = "projects.txt"
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    projects = get_projects(FILENAME)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == 'L':
            filename = input("File to load: ")
            projects = get_projects(filename)
        elif choice == 'S':
            filename = input("File to save: ")
            save_projects(filename, projects)
        elif choice == 'D':
            completed_projects, incomplete_projects = get_incomplete_completed_projects(projects)
            display_no_index_project("Incomplete Projects: ", incomplete_projects)
            display_no_index_project("Completed Projects: ", completed_projects)
        elif choice == 'F':
            filter_date = input("Show projects that start after date (dd/mm/yy): ")
            filter_date = get_date_time(filter_date)
            filter_projects = get_filter_projects(filter_date, projects)
            display_filter_projects(filter_projects)
        elif choice == 'A':
            print("Let's add a new project")
            project = get_new_project()
            projects.append(project)
        elif choice == 'U':
            for index, project in enumerate(projects, 0):
                print(f"{index} {str(project)}")

            project_choice = int(input("Project choice: "))
            print(projects[project_choice])

            new_percentage, new_priority = get_new_values(project_choice, projects)

            projects[project_choice].completion_percentage = int(new_percentage)
            projects[project_choice].priority = int(new_priority)
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()


def get_date_time(date):
    return datetime.datetime.strptime(date, "%d/%m/%Y").date()


def get_new_values(project_choice, projects):
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_percentage == '':
        new_percentage = projects[project_choice].completion_percentage
    if new_priority == '':
        new_priority = projects[project_choice].priority
    return new_percentage, new_priority


def get_new_project():
    try:
        name = input("Name:")
        start_date = input("Start date (dd/mm/yy): ")
        start_date = get_date_time(start_date)
        priority = int(input("Priority: "))
        cost_estimate = int(input("Cost estimate: $"))
        completion_percentage = int(input("Percent complete: "))
        project = (Project(name, start_date, priority, cost_estimate, completion_percentage))
    except ValueError:
        print("Invalid Input")
    return project


def display_filter_projects(filter_projects):
    for filter_project in filter_projects:
        filter_project.start_date = get_date_string(filter_project.start_date)
        print(str(filter_project))


def get_filter_projects(filter_date, projects):
    filter_projects = []
    for project in projects:
        if project.start_date >= filter_date:
            filter_projects.append(project)
    filter_projects = sorted(filter_projects)
    return filter_projects


def display_no_index_project(prompt, projects):
    print(prompt)
    for project in projects:
        print(f"  {project}")


def get_incomplete_completed_projects(projects):
    incomplete_projects = []
    completed_projects = []
    for project in projects:
        if project.is_completed():
            completed_projects.append(project)
            completed_projects.sort()
        else:
            incomplete_projects.append(project)
            incomplete_projects.sort()
    return completed_projects, incomplete_projects


def get_date_string(data):
    return data.strftime("%d/%m/%Y")


def save_projects(filename, projects):
    with open(filename, "w") as out_file:
        for project in projects:
            out_file.write(
                f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}")


def get_projects(filename):
    projects = []
    with open(filename, "r") as in_file:
        for line in in_file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split("\t")
            projects.append((Project(name, start_date, priority, cost_estimate, completion_percentage)))
    return projects

main()

