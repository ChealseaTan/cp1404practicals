"""
The client
Estimated Time: 2hours
Actual Time:
"""

from prac_07.project import Project


FILENAME = "projects.txt"
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

projects = []
with open(FILENAME, "r") as in_file:
    for line in in_file:
        name, start_date, priority, cost_estimate, completion_percentage = line.strip().split("\t")
        projects.append((Project(name, start_date, priority, cost_estimate, completion_percentage)))
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == 'L':
        filename = input("File to load: ")
        projects = []
        with open(filename, "r") as in_file:
            for line in in_file:
                name, start_date, priority, cost_estimate, completion_percentage = line.strip().split("\t")
                projects.append((Project(name, start_date, priority, cost_estimate, completion_percentage)))
    elif choice == 'S':
        filename = input("File to save: ")
        with open(filename, "w") as out_file:
            for project in projects:
                out_file.write(f"{name}\t{start_date}\t{priority}\t{cost_estimate}\t{completion_percentage}")
    elif choice == 'D':
        incomplete_projects = []
        completed_projects = []

        for project in projects:
            if project.is_complete():
                completed_projects.append(project)
            else:
                incomplete_projects.append(project)
        print("Incomplete projects:")
        for incomplete_project in incomplete_projects:
            print(incomplete_project)
        print("Completed projects:")
        for completed_project in completed_projects:
            print(completed_project)
    elif choice == 'F':
        pass
    elif choice == 'A':
        print("Let's add a new project")
        try:
            name = input("Name:")
            start_date = input("Start date (dd/mm/yy): ")
            priority = int(input("Priority: "))
            cost_estimate = int(input("Cost estimate: $"))
            completion_percentage = int(input("Percent complete: "))
            project = (Project(name, start_date, priority, cost_estimate, completion_percentage))
            projects.append(project)
        except ValueError:
            print("Invalid input")
    elif choice == 'U':
        pass
    else:
        print("Invalid input")
        choice = input(">>> ").upper()


