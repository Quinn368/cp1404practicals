import datetime
from prac_07.project import Project

FILENAME = "projects.txt"

MENU = """- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"""


def main():
    """Load file of project details, save as objects, display, filter by year, add new project, update."""
    projects = load_projects()  # load file directly without asking user input
    # projects = []
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from projects.txt")
    print(MENU)
    option = input(">>> ").lower()
    while option != 'q':
        if option == 'l':
            projects = load_projects()
        elif option == 's':
            save_projects(projects)
        elif option == 'd':
            display_projects(projects)
        elif option == 'f':
            filter_projects(projects)
        elif option == 'a':
            projects = add_new_project(projects)
        elif option == 'u':
            projects = update_project(projects)
        else:
            print("Invalid option. Please try again.")
        print(MENU)
        option = input(">>> ").lower()
    save_changes(projects)


def load_projects():
    """Load the project details."""
    projects = []
    in_file = open(FILENAME, 'r')  # load file directly without asking user input
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        projected = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
        projects.append(projected)
    return projects


def save_projects(projects):
    """Save the project details"""
    # save_filename == input("Filename: ")
    # with open(save_filename, 'w') as out_file:
    with open(FILENAME, 'w') as out_file:  # load file directly without asking user input
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            out_file.write(project.line_format() + '\n')


def display_projects(projects):
    """Display by differing the incompleted and completed project."""
    sorted_projects = sorted(projects, key=lambda x: x.priority)

    print("Incomplete projects:")
    incomplete_projects = [f"\t{project}" for project in sorted_projects if not project.is_completed()]
    print('\n'.join(incomplete_projects))

    print("Completed projects:")
    completed_projects = [f"\t{project}" for project in sorted_projects if project.is_completed()]
    print('\n'.join(completed_projects))


def filter_projects(projects):
    """Filter the project by year given."""
    while True:
        try:
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            date_formatted = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            break
        except:
            print("Invalid date (check for the date format)")

    filtered_projects = [project for project in projects if datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date() > date_formatted]

    display_projects(filtered_projects)


def add_new_project(projects):
    """Add new project."""
    print("Let's add a new project")
    name = input("Name: ")

    while True:
        try:
            start_date = input("Start date (dd/mm/yyyy): ")
            datetime.datetime.strptime(
                start_date, "%d/%m/%Y").date()
            break
        except:
            print("Invalid date (check for the date format)")

    while True:
        try:
            priority = int(input("Priority: "))
            if priority < 0 or priority > 10:
                print("Priority must be between 0 to 10")
            else:
                break
        except ValueError:
            print("Invalid priority")

    while True:
        try:
            cost_estimate = float(input("Cost estimate: $"))
            if cost_estimate < 0:
                print("Cost estimation must be in number form")
            else:
                break
        except ValueError:
            print("Invalid cost estimation")

    while True:
        try:
            completion_percentage = int(input("Percent complete: "))
            if completion_percentage < 0 or completion_percentage > 100:
                print("Completion percentage must be between 0 to 100")
            else:
                break
        except ValueError:
            print("Invalid completion percentage")

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)

    save_projects(projects)

    return projects


def update_project(projects):
    """Update project details of priority and completion percentage"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    while True:
        try:
            project_choice = int(input("Project choice: "))
            if project_choice >= len(projects):
                print("Project choice should be within the range of project choice index")
            else:
                break
        except ValueError:
            print("Invalid choice index")

    project_updated = projects[project_choice]
    print(project_updated)

    while True:
        try:
            change_percentage = int(input("Percent complete: "))
            if change_percentage < 0 or change_percentage > 100:
                print("Completion percentage must be between 0 to 100")
            else:
                break
        except ValueError:
            print("Invalid completion percentage")

    while True:
        try:
            change_priority = int(input("Priority: "))
            if change_priority < 0 or change_priority > 10:
                print("Priority must be between 0 to 10")
            else:
                break
        except ValueError:
            print("Invalid priority")

    project_updated.completion_percentage = change_percentage
    project_updated.priority = change_priority

    projects[project_choice] = project_updated

    save_projects(projects)

    return projects


def save_changes(projects):
    """Save changes in project."""
    save_after_quit = input("Would you like to save to projects.txt? ").lower()
    while save_after_quit not in ['yes', 'no']:
        print("Invalid choice (yes/no)")
        save_after_quit = input("Would you like to save to projects.txt? ").lower()
    if save_after_quit == 'yes':
        save_projects(projects)
    print("Thank you for using custom-built project management software.")


main()
