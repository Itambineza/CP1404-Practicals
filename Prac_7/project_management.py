import csv
from datetime import datetime
from project import Project

FILENAME = "projects.txt"

def main():
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    while True:
        display_menu()
        choice = input(">>> ").lower()
        
        if choice == 'l':
            filename = input("Filename: ")
            projects = load_projects(filename)
        
        elif choice == 's':
            filename = input("Filename: ")
            save_projects(filename, projects)
        
        elif choice == 'd':
            display_projects(projects)
        
        elif choice == 'f':
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            date = datetime.strptime(date_string, "%d/%m/%Y").date()
            filter_projects_by_date(projects, date)
        
        elif choice == 'a':
            add_new_project(projects)
        
        elif choice == 'u':
            update_project(projects)
        
        elif choice == 'q':
            save_choice = input(f"Would you like to save to {FILENAME}? (y/n): ").lower()
            if save_choice == 'y':
                save_projects(FILENAME, projects)
            break
        
        else:
            print("Invalid choice")

def display_menu():
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")

def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # skip header
        for row in reader:
            projects.append(Project(*row))
    return projects

def save_projects(filename, projects):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow([project.name, project.start_date.strftime('%d/%m/%Y'), project.priority, project.cost_estimate, project.completion_percentage])

def display_projects(projects):
    print("Incomplete projects:")
    incomplete_projects = [p for p in projects if not p.is_complete()]
    incomplete_projects.sort(key=lambda p: p.priority)
    for project in incomplete_projects:
        print(project)
    
    print("Completed projects:")
    completed_projects = [p for p in projects if p.is_complete()]
    completed_projects.sort(key=lambda p: p.priority)
    for project in completed_projects:
        print(project)

def filter_projects_by_date(projects, date):
    filtered_projects = [p for p in projects if p.matches_date(date)]
    filtered_projects.sort(key=lambda p: p.start_date)
    for project in filtered_projects:
        print(project)

def add_new_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion_percentage = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))

def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    new_completion = input("New Percentage: ")
    new_priority = input("New Priority: ")
    project.update_completion(new_completion)
    project.update_priority(new_priority)

main()


