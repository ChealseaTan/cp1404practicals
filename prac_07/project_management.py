"""
The client
Estimated Time: 1 hour 30mins
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
    for i, line in enumerate(in_file, 0):
        name, start_date, priority, cost_estimate, completion_percentage = line.strip().split("\t")
        projects.append((Project(name, start_date, priority, cost_estimate, completion_percentage)))
print(MENU)
