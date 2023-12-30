```python
class UserInputHandler:
    def __init__(self):
        pass

    def get_user_input(self):
        # Get user's preferred programming language
        programming_language = input("Enter your preferred programming language: ")

        # Get user's project requirements
        project_requirements = input("Enter your project requirements: ")

        # Get user's project name, if any
        project_name = input("Enter your project name (optional): ")

        # Return the user input as a dictionary
        return {
            'programming_language': programming_language,
            'project_requirements': project_requirements,
            'project_name': project_name if project_name else None
        }
```
