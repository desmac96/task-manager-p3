<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To-Do List README</title>
</head>
<body>

<h1>To-Do List</h1>

<p>The To-Do List is a command-line application that allows users to manage their tasks efficiently. Users can add, list, remove, and mark tasks as complete.</p>

<h2>Contents</h2>
<ul>
    <li><a href="#to-do-list">To-Do List</a></li>
    <li><a href="#contents">Contents</a></li>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#user-experience-ux">User Experience (UX)</a>
        <ul>
            <li><a href="#site--user-goals">Site & User Goals</a></li>
            <li><a href="#user-stories">User Stories</a></li>
        </ul>
    </li>
    <li><a href="#development-planes">Development Planes</a>
        <ul>
            <li><a href="#strategy">Strategy</a></li>
            <li><a href="#scope">Scope</a></li>
            <li><a href="#functional-specifications">Functional Specifications</a></li>
            <li><a href="#structure">Structure</a></li>
            <li><a href="#flow-logic">Flow Logic</a></li>
        </ul>
    </li>
    <li><a href="#surface-and-features">Surface and Features</a></li>
    <li><a href="#technologies-used">Technologies Used</a></li>
    <li><a href="#bugs--issues">Bugs & Issues</a></li>
    <li><a href="#libraries-imported">Libraries Imported</a></li>
    <li><a href="#testing">Testing</a>
        <ul>
            <li><a href="#manual-testing">Manual Testing</a></li>
            <li><a href="#automated-testing">Automated Testing</a></li>
            <li><a href="#pep-8-testing">Pep-8 Testing</a></li>
        </ul>
    </li>
    <li><a href="#deployment">Deployment</a></li>
    <li><a href="#credits--acknowledgements">Credits & Acknowledgements</a></li>
</ul>

<p><a href="#to-do-list">Back to top</a></p>

<h2>Introduction</h2>
<p>The To-Do List is a Python-based command-line application designed to help users manage their daily tasks. This tool offers a straightforward way to add, edit, delete, and view tasks, making task management simple and efficient.</p>

<h2>User Experience (UX)</h2>

<h3>Site & User Goals</h3>
<h4>Site Goals</h4>
<ul>
    <li>Provide an easy-to-use interface: Ensure that users can navigate and use the application without any difficulties.</li>
    <li>Facilitate task management: Allow users to easily add, modify, delete, and view tasks.</li>
    <li>Ensure data persistence: Store tasks in a reliable way so that they are available even after restarting the application.</li>
    <li>Offer real-time feedback: Provide immediate confirmation or error messages for user actions.</li>
    <li>Support multiple platforms: Ensure the application works on various operating systems.</li>
</ul>

<h4>User Goals</h4>
<ul>
    <li>Efficient task management: Quickly add, view, modify, and remove tasks.</li>
    <li>Access task history: View a list of all tasks to keep track of work.</li>
    <li>Receive instant feedback: Get confirmation when tasks are added, modified, or deleted.</li>
    <li>Secure data storage: Ensure that tasks are stored securely and are not lost.</li>
</ul>

<h3>User Stories</h3>

<h4>1. Adding a Task</h4>
<p>As a user, I want to add a new task with a description so that I can keep track of my upcoming work.</p>
<p><strong>Acceptance Criteria:</strong></p>
<ul>
    <li>The application should prompt the user to enter a task description.</li>
    <li>The task should have a unique ID, the current date, and time.</li>
    <li>The task should be saved and visible in the task list.</li>
    <li>A confirmation message should be displayed.</li>
</ul>

<h4>2. Modifying a Task</h4>
<p>As a user, I want to update the description of an existing task so that I can keep my task details current.</p>
<p><strong>Acceptance Criteria:</strong></p>
<ul>
    <li>The application should prompt the user to enter the task ID they wish to modify.</li>
    <li>The user should be able to enter a new task description.</li>
    <li>The task should be updated with the new description.</li>
    <li>A confirmation message should be displayed if the update is successful.</li>
</ul>

<h4>3. Deleting a Task</h4>
<p>As a user, I want to remove a task by its ID so that I can keep my task list current.</p>
<p><strong>Acceptance Criteria:</strong></p>
<ul>
    <li>The application should prompt the user to enter the task ID they wish to delete.</li>
    <li>The task should be removed from the list.</li>
    <li>A confirmation message should be displayed if the deletion is successful.</li>
    <li>An error message should be displayed if the task ID does not exist.</li>
</ul>

<h4>4. Viewing All Tasks</h4>
<p>As a user, I want to see all my tasks in a list so that I can manage my time effectively.</p>
<p><strong>Acceptance Criteria:</strong></p>
<ul>
    <li>The application should display all tasks with their ID, date, time, and description.</li>
    <li>The tasks should be displayed in a readable format.</li>
    <li>The task list should be up-to-date with all changes.</li>
</ul>

<h4>5. Persistent Storage</h4>
<p>As a user, I want my tasks saved in a file so that I can access them later even if the application is closed.</p>
<p><strong>Acceptance Criteria:</strong></p>
<ul>
    <li>The tasks should be saved in a file.</li>
    <li>The file should be updated with every add, modify, or delete action.</li>
    <li>The system should load tasks from the file when the application starts.</li>
</ul>

<h4>6. Real-Time Feedback</h4>
<p>As a user, I want to receive immediate feedback on my actions so that I know whether my task was successfully added, modified, or deleted.</p>
<p><strong>Acceptance Criteria:</strong></p>
<ul>
    <li>The application should display a confirmation message after a task is added, modified, or deleted.</li>
    <li>Error messages should be displayed if an action fails (e.g., invalid task ID).</li>
    <li>Feedback messages should be clear and concise.</li>
</ul>

<h4>7. Secure Data Handling</h4>
<p>As a user, I want my tasks to be stored securely and not lost so that I can trust the task manager with my data.</p>
<p><strong>Acceptance Criteria:</strong></p>
<ul>
    <li>Tasks should not be lost even if the application is closed or restarted.</li>
    <li>The log file should be saved in a reliable and persistent manner.</li>
</ul>

<p><a href="#to-do-list">Back to top</a></p>

<h2>Development Planes</h2>

<h3>Strategy</h3>
<p>The idea behind the To-Do List application is to create a simple, effective tool for managing tasks. The command-line interface is chosen to ensure it is quick and easy for users to interact with their tasks directly from the terminal.</p>

<h3>Scope</h3>
<p>This application provides functionality for managing tasks. It allows users to add, modify, delete, and list tasks. Each task includes an ID, date, time, and description. Tasks are stored in a log file on the user's system for persistent storage.</p>

<h3>Functional Specifications</h3>
<ul>
    <li>Add tasks with a description, date, and time.</li>
    <li>Modify the description of existing tasks.</li>
    <li>Delete tasks by their ID.</li>
    <li>Display a list of all tasks.</li>
    <li>Store tasks in a log file for persistent storage.</li>
</ul>

<h3>Structure</h3>
<p>The To-Do List application is structured to be used entirely within the terminal. The text-based interface provides a straightforward way for users to manage their tasks.</p>

<h3>Flow Logic</h3>
<p>The flow logic diagram below illustrates the interactions and processes within the To-Do List application.</p>
<ol>
    <li><strong>Start</strong>: The user launches the program.</li>
    <li><strong>Load Tasks</strong>: The program loads existing tasks from the log file.</li>
    <li><strong>Main Menu</strong>: The user is presented with a menu to choose an action.
        <ul>
            <li><strong>Add Task</strong>:
                <ul>
                    <li>Input task description.</li>
                    <li>Task added to list and saved to log file.</li>
                    <li>Confirmation message displayed.</li>
                    <li>Return to Main Menu.</li>
                </ul>
            </li>
            <li><strong>Modify Task</strong>:
                <ul>
                    <li>Input task ID and new description.</li>
                    <li>Task is modified and saved to log file.</li>
                    <li>Confirmation message displayed.</li>
                    <li>Return to Main Menu.</li>
                </ul>
            </li>
            <li><strong>Show Tasks</strong>:
                <ul>
                    <li>Display all tasks with details.</li>
                    <li>Return to Main Menu.</li>
                </ul>
            </li>
            <li><strong>Delete Task</strong>:
                <ul>
                    <li>Input task ID to delete.</li>
                    <li>Task is deleted from the list and saved to log file.</li>
                    <li>Confirmation message displayed.</li>
                    <li>Return to Main Menu.</li>
                </ul>
            </li>
            <li><strong>Exit</strong>:
                <ul>
                    <li>Display exit message.</li>
                    <li>End program.</li>
                </ul>
            </li>
        </ul>
    </li>
    <li><strong>Exit</strong>: The user exits the program.</li>
</ol>

<p><a href="#to-do-list">Back to top</a></p>

<h2>Surface and Features</h2>

<p>The To-Do List operates entirely within a terminal interface, offering a straightforward and text-based user experience. Below is a description of the main screens and interactions within the program.</p>

<h3>Main Menu</h3>
<p>Upon starting the program, users are greeted with the main menu, which displays the available actions:</p>
<ul>
    <li>Add task</li>
    <li>Modify task</li>
    <li>Show tasks</li>
    <li>Delete task</li>
    <li>Exit</li>
</ul>

<h3>Adding a Task</h3>
<p>When the user selects the option to add a task, they are prompted to enter a task description:</p>
<ul>
    <li>Input task description.</li>
    <li>Task added to list and saved to log file.</li>
    <li>Confirmation message displayed.</li>
    <li>Return to Main Menu.</li>
</ul>

<h3>Modifying a Task</h3>
<p>When the user selects the option to modify a task, they are prompted to enter the task ID and the new description:</p>
<ul>
    <li>Input task ID and new description.</li>
    <li>Task is modified and saved to log file.</li>
    <li>Confirmation message displayed.</li>
    <li>Return to Main Menu.</li>
</ul>

<h3>Showing Tasks</h3>
<p>When the user selects the option to show tasks, all tasks are displayed with their details:</p>
<ul>
    <li>Display all tasks with details.</li>
    <li>Return to Main Menu.</li>
</ul>

<h3>Deleting a Task</h3>
<p>When the user selects the option to delete a task, they are prompted to enter the task ID to delete:</p>
<ul>
    <li>Input task ID to delete.</li>
    <li>Task is deleted from the list and saved to log file.</li>
    <li>Confirmation message displayed.</li>
    <li>Return to Main Menu.</li>
</ul>

<h3>Exiting the Program</h3>
<p>When the user selects the option to exit, a farewell message is displayed, and the program terminates:</p>
<ul>
    <li>Display exit message.</li>
    <li>End program.</li>
</ul>

<p><a href="#to-do-list">Back to top</a></p>

<h2>Technologies Used</h2>

<h3>Languages Used</h3>
<ul>
    <li>Python</li>
</ul>

<h3>Libraries and Frameworks Used</h3>
<ul>
    <li><code>os</code>: Interact with the operating system.</li>
    <li><code>time</code>: Handle time-related tasks.</li>
    <li><code>pathlib</code>: Work with filesystem paths in an object-oriented way.</li>
</ul>

<h2>Bugs & Issues</h2>

<p>During the development of the To-Do List project, the following bugs and issues were encountered and resolved:</p>

<h3>1. Incorrect Task ID Handling</h3>
<ul>
    <li><strong>Issue</strong>: Task IDs were not handled properly when tasks were deleted or modified. This led to incorrect task IDs being displayed or referenced.</li>
    <li><strong>Solution</strong>: Ensured that task IDs are consistently managed and updated when tasks are added, modified, or deleted. Used list indexing and string conversion to handle task IDs correctly.</li>
</ul>

<h3>2. File Path Issues</h3>
<ul>
    <li><strong>Issue</strong>: The application faced issues in determining the correct file path for storing the task log file, especially when deployed in different environments (local vs. cloud).</li>
    <li><strong>Solution</strong>: Used the <code>pathlib</code> module to handle file paths in an object-oriented way and ensured compatibility across different operating systems. Added checks to determine the environment (local or cloud) and set the file path accordingly.</li>
</ul>

<h3>3. User Input Validation</h3>
<ul>
    <li><strong>Issue</strong>: There were issues with user input validation, such as accepting empty inputs or invalid task IDs.</li>
    <li><strong>Solution</strong>: Implemented the <code>input_handler</code> function to handle and validate user inputs for different data types. Added checks to ensure inputs are not empty and fall within acceptable ranges.</li>
</ul>

<h3>4. Task Display Formatting</h3>
<ul>
    <li><strong>Issue</strong>: Tasks were not displayed in a readable and organized format, making it difficult for users to read task details.</li>
    <li><strong>Solution</strong>: Improved the <code>show_tasks</code> function to format task display using consistent separators and clear headings. This enhanced readability and provided a better user experience.</li>
</ul>

<h3>5. Error Handling</h3>
<ul>
    <li><strong>Issue</strong>: The application lacked proper error handling, leading to crashes or undefined behavior when unexpected inputs or conditions occurred.</li>
    <li><strong>Solution</strong>: Added try-except blocks to handle exceptions gracefully and provide meaningful error messages to the user. Ensured that the application continues to run smoothly even when errors occur.</li>
</ul>

<h3>6. Persistent Storage Reliability</h3>
<ul>
    <li><strong>Issue</strong>: Tasks were sometimes not saved or loaded correctly, leading to data loss or inconsistency.</li>
    <li><strong>Solution</strong>: Enhanced the <code>save_tasks</code> and <code>load_tasks</code> functions to ensure tasks are reliably saved to and loaded from the log file. Added checks to verify file existence and integrity.</li>
</ul>

<h3>7. Cross-Platform Compatibility</h3>
<ul>
    <li><strong>Issue</strong>: The application faced issues with terminal commands and file paths that differed between operating systems (Windows, macOS, Linux).</li>
    <li><strong>Solution</strong>: Used the <code>os</code> and <code>pathlib</code> modules to handle system-specific operations in a cross-platform manner. Ensured that terminal commands for clearing the screen and file path handling work correctly on all supported platforms.</li>
</ul>

<p>By addressing these bugs and issues, the To-Do List project was improved to provide a reliable, user-friendly, and cross-platform task management solution.</p>

<p><a href="#to-do-list">Back to top</a></p>

<h2>Libraries Imported</h2>
<ul>
    <li><code>os</code></li>
    <li><code>time</code></li>
    <li><code>pathlib</code></li>
</ul>

<p><a href="#to-do-list">Back to top</a></p>

<h2>Testing</h2>

<h3>Manual Testing</h3>

<h4>1. Adding a Task Test</h4>
<ul>
    <li><strong>Steps</strong>: Run the program. Select the option to add a task. Enter a task description.</li>
    <li><strong>Expected Result</strong>: The task should be added to the list and a confirmation message should be displayed.</li>
    <li><strong>Result</strong>: Pass</li>
</ul>

<h4>2. Modifying a Task Test</h4>
<ul>
    <li><strong>Steps</strong>: Run the program. Select the option to modify a task. Enter the task ID and the new description.</li>
    <li><strong>Expected Result</strong>: The task should be updated with the new description and a confirmation message should be displayed.</li>
    <li><strong>Result</strong>: Pass</li>
</ul>

<h4>3. Deleting a Task Test</h4>
<ul>
    <li><strong>Steps</strong>: Run the program. Select the option to delete a task. Enter the task ID.</li>
    <li><strong>Expected Result</strong>: The task should be removed from the list and a confirmation message should be displayed.</li>
    <li><strong>Result</strong>: Pass</li>
</ul>

<h4>4. Showing All Tasks Test</h4>
<ul>
    <li><strong>Steps</strong>: Run the program. Select the option to show all tasks.</li>
    <li><strong>Expected Result</strong>: All tasks should be displayed with their details.</li>
    <li><strong>Result</strong>: Pass</li>
</ul>

<h4>5. Persistent Storage Test</h4>
<ul>
    <li><strong>Steps</strong>: Run the program and add several tasks. Exit the program. Run the program again.</li>
    <li><strong>Expected Result</strong>: All previously added tasks should be loaded and displayed correctly.</li>
    <li><strong>Result</strong>: Pass</li>
</ul>

<h3>Automated Testing</h3>

<p>We use the <code>unittest</code> module in Python to create unit tests for this project. Here are some examples of the tests performed:</p>

<h4>1. test_add_task</h4>
<p><strong>Description</strong>: Tests the functionality of adding a new task.</p>
<p><strong>Expected Result</strong>: The task should be added to the list.</p>

<h4>2. test_modify_task</h4>
<p><strong>Description</strong>: Tests the functionality of modifying an existing task.</p>
<p><strong>Expected Result</strong>: The task should be updated with the new description.</p>

<h3>Pep-8 Testing</h3>

<p>PEP-8 compliance was checked using a linter, and the code was adjusted to adhere to the standards, ensuring better readability and consistency.</p>

<p><a href="#to-do-list">Back to top</a></p>

<h2>Deployment</h2>

<p>The project was created using the Code Institute Python template and was deployed through Heroku.</p>

<h3>Steps to Deploy:</h3>
<ol>
    <li>Login / Sign Up to Heroku:
        <ul>
            <li>Go to Heroku and log in or sign up.</li>
        </ul>
    </li>
    <li>Create a New App:
        <ul>
            <li>From your Heroku dashboard, click on “New” &gt; “Create New App”.</li>
            <li>Name your app uniquely and choose the region closest to you.</li>
        </ul>
    </li>
    <li>Config Vars Setup:
        <ul>
            <li>Navigate to the settings tab and reveal config vars.</li>
            <li>Add any necessary config vars (e.g., TASKS_LOG_PATH if you are using a custom path).</li>
        </ul>
    </li>
    <li>Buildpacks:
        <ul>
            <li>Add Python first, then Node.js as buildpacks. This ensures the correct environment is set up.</li>
        </ul>
    </li>
    <li>Deployment via GitHub:
        <ul>
            <li>Go to the deploy tab, select GitHub as the deployment method, and connect your GitHub account.</li>
            <li>Find your repository and connect it to Heroku.</li>
        </ul>
    </li>
    <li>Automatic Deployment:
        <ul>
            <li>Choose the branch you want to deploy (e.g., main).</li>
            <li>Enable automatic deploys to automatically update the Heroku app with new commits to the selected branch.</li>
        </ul>
    </li>
    <li>Finalize Deployment:
        <ul>
            <li>Heroku will build and deploy your application. Once done, you will receive a confirmation message with a link to your live application.</li>
        </ul>
    </li>
</ol>

<p><a href="#to-do-list">Back to top</a></p>

<h2>Credits & Acknowledgements</h2>
<p>My mentor Viktor Michlovich</p>

</body>
</html>
