  <h1>To-Do List Application</h1>

    <p>This is a command-line based To-Do List application that allows users to add, list, remove, and complete tasks.
        The application provides both interactive mode and command-line arguments for flexibility.</p>

    <h2>Contents</h2>
    <ul>
        <li><a href="#introduction">Introduction</a></li>
        <li><a href="#user-experience">User Experience</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#technologies-used">Technologies Used</a></li>
        <li><a href="#deployment">Deployment</a></li>
        <li><a href="#testing">Testing</a></li>
        <li><a href="#credits">Credits</a></li>
    </ul>

    <h2 id="introduction">Introduction</h2>
    <p>The To-Do List application is designed to help users manage their tasks efficiently. Users can add tasks with
        descriptions and optional due dates, list all tasks, remove tasks by index, and mark tasks as complete. The
        application supports both interactive mode for direct user input and command-line arguments for automation and
        scripting.</p>

    <h2 id="user-experience">User Experience</h2>
    <h3>Site & User Goals</h3>
    <h4>Site Goals</h4>
    <ul>
        <li>Provide an intuitive command-line interface for task management.</li>
        <li>Enable users to easily add, list, remove, and complete tasks.</li>
    </ul>
    <h4>User Goals</h4>
    <ul>
        <li>Efficiently manage tasks through a simple and intuitive interface.</li>
        <li>Quickly add, modify, and delete tasks as needed.</li>
        <li>View the current list of tasks at any time.</li>
    </ul>

    <h3>User Stories</h3>
    <h4>Adding a Task</h4>
    <p>As a user, I want to add a new task with a description so that I can keep track of my upcoming work.</p>
    <ul>
        <li>The system should prompt the user to enter a task description.</li>
        <li>The task should be assigned a unique ID, current date, and time.</li>
        <li>The task should be saved and visible in the task list.</li>
        <li>A confirmation message should be displayed.</li>
    </ul>

    <h4>Modifying a Task</h4>
    <p>As a user, I want to modify the description of an existing task so that I can update the task details if they
        change.</p>
    <ul>
        <li>The system should prompt the user to enter the task ID they wish to modify.</li>
        <li>The system should allow the user to enter a new description.</li>
        <li>The task should be updated with the new description.</li>
        <li>A confirmation message should be displayed if the modification is successful.</li>
    </ul>

    <h4>Deleting a Task</h4>
    <p>As a user, I want to delete a task by its ID so that I can remove tasks that are no longer needed.</p>
    <ul>
        <li>The system should prompt the user to enter the task ID they wish to delete.</li>
        <li>The task should be removed from the list.</li>
        <li>A confirmation message should be displayed if the deletion is successful.</li>
        <li>An error message should be displayed if the task ID does not exist.</li>
    </ul>

    <h4>Viewing All Tasks</h4>
    <p>As a user, I want to view a list of all tasks so that I can see what work needs to be done and track my
        progress.</p>
    <ul>
        <li>The system should display all tasks with their ID, date, time, and description.</li>
        <li>The tasks should be displayed in a readable format.</li>
        <li>The list should be up-to-date with all added, modified, or deleted tasks.</li>
    </ul>

    <h2 id="features">Features</h2>
    <h3>Existing Features</h3>
    <h4>Interactive Mode</h4>
    <ul>
        <li>Allows users to interact with the application via a simple menu.</li>
        <li>Users can add, list, remove, and complete tasks through interactive prompts.</li>
    </ul>

    <h4>Command-Line Arguments</h4>
    <ul>
        <li>Provides flexibility for users to add, list, remove, and complete tasks through command-line arguments.</li>
        <li>Allows for automation and scripting of task management.</li>
    </ul>

    <h4>Error Handling</h4>
    <ul>
        <li>Handles invalid input gracefully, providing meaningful error messages to the user.</li>
        <li>Ensures the application continues to run smoothly even when errors occur.</li>
    </ul>

    <h4>Validation</h4>
    <ul>
        <li>Validates user input to ensure it meets the required criteria (e.g., alphabetic names, valid task
            indices).</li>
        <li>Prompts users to re-enter information if validation fails.</li>
    </ul>

    <h3>Future Implementations</h3>
    <ul>
        <li>Implementing due dates and reminders for tasks.</li>
        <li>Adding priority levels to tasks.</li>
        <li>Allowing users to categorize tasks.</li>
        <li>Integrating with external calendars or task management tools.</li>
    </ul>

    <h2 id="technologies-used">Technologies Used</h2>
    <h3>Languages</h3>
    <ul>
        <li>Python</li>
    </ul>

    <h3>Libraries</h3>
    <ul>
        <li>argparse: For parsing command-line arguments.</li>
    </ul>

    <h2 id="deployment">Deployment</h2>
    <p>This project was deployed using Heroku. Follow these steps to deploy your own instance:</p>
    <ol>
        <li>Log in or sign up for a Heroku account.</li>
        <li>Create a new app from the Heroku dashboard.</li>
        <li>Set up the necessary config vars.</li>
        <li>Add the required buildpacks (Python and Node.js).</li>
        <li>Connect your GitHub repository to Heroku.</li>
        <li>Deploy the app manually or set up automatic deploys from the desired branch.</li>
    </ol>

    <h2 id="testing">Testing</h2>
    <h3>Manual Testing</h3>
    <ul>
        <li>Adding a Task: Verified that tasks are added correctly and displayed in the task list.</li>
        <li>Modifying a Task: Confirmed that task descriptions can be updated and the changes are saved.</li>
        <li>Deleting a Task: Ensured that tasks are removed from the list and the changes are saved.</li>
        <li>Viewing All Tasks: Checked that the task list displays all tasks with their details.</li>
    </ul>

    <h3>Automated Testing</h3>
    <p>Automated tests were written using the <code>unittest</code> module to validate the functionality of adding,
        modifying, and deleting tasks.</p>

    <h2 id="credits">Credits</h2>
    <h3>Code</h3>
    <ul>
        <li>The code for parsing command-line arguments was adapted from the official Python <code>argparse</code>
            documentation.</li>
    </ul>

    <h3>Content</h3>
    <ul>
        <li>All content was written by [Your Name].</li>
    </ul>

    <h3>Acknowledgements</h3>
    <ul>
        <li>Thanks to my mentor for guidance and support throughout the development of this project.</li>
        <li>Thanks to the Code Institute for providing the project template and resources.</li>
    </ul>
