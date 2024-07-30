# To Do List

  <title>To-Do List</title>
</head>
<body>
  <h1>To-Do List</h1>
  <p>The To-Do List is a command-line application that helps users manage their tasks efficiently by adding, listing, removing, and marking tasks as complete.</p>

  <h2>Contents</h2>
  <ul>
    <li><a href="#to-do-list">To-Do List</a></li>
    <li><a href="#contents">Contents</a></li>
    <li><a href="#user-experience-ux">User Experience (UX)</a>
      <ul>
        <li><a href="#initial-discussion">Initial Discussion</a></li>
        <li><a href="#key-information-for-the-application">Key Information for the Application</a></li>
      </ul>
    </li>
    <li><a href="#user-stories">User Stories</a>
      <ul>
        <li><a href="#client-goals">Client Goals</a></li>
        <li><a href="#first-time-user-goals">First Time User Goals</a></li>
        <li><a href="#returning-user-goals">Returning User Goals</a></li>
      </ul>
    </li>
    <li><a href="#design">Design</a>
      <ul>
        <li><a href="#colour-scheme">Colour Scheme</a></li>
        <li><a href="#flowcharts">Flowcharts</a></li>
      </ul>
    </li>
    <li><a href="#features">Features</a>
      <ul>
        <li><a href="#existing-features">Existing Features</a>
          <ul>
            <li><a href="#welcome-page">Welcome Page</a></li>
            <li><a href="#new-user">New User</a></li>
            <li><a href="#existing-user">Existing User</a></li>
            <li><a href="#main-menu">Main Menu</a></li>
            <li><a href="#add-task">Add Task</a></li>
            <li><a href="#list-tasks">List Tasks</a></li>
            <li><a href="#remove-task">Remove Task</a></li>
            <li><a href="#mark-task-complete">Mark Task Complete</a></li>
            <li><a href="#exit">Exit</a></li>
          </ul>
        </li>
        <li><a href="#future-implementations">Future Implementations</a></li>
      </ul>
    </li>
    <li><a href="#technologies-used">Technologies Used</a>
      <ul>
        <li><a href="#languages-used">Languages Used</a></li>
        <li><a href="#frameworks-libraries-and-programs-used">Frameworks, Libraries and Programs Used</a></li>
      </ul>
    </li>
    <li><a href="#deployment">Deployment</a></li>
    <li><a href="#testing">Testing</a></li>
    <li><a href="#credits">Credits</a>
      <ul>
        <li><a href="#code-used">Code Used</a></li>
        <li><a href="#content">Content</a></li>
        <li><a href="#media">Media</a></li>
        <li><a href="#other">Other</a></li>
        <li><a href="#acknowledgements">Acknowledgements</a></li>
      </ul>
    </li>
  </ul>

  <p><a href="#to-do-list">Back to top</a></p>

  <h2>User Experience (UX)</h2>

<h3>Initial Discussion</h3>
<p>The To-Do List is a tool for users to manage their tasks efficiently. The program is designed to be simple and intuitive, allowing users to add tasks, list tasks, remove tasks, and mark tasks as complete.</p>

<h4>Key Information for the Application</h4>
<ul>
  <li>New users can set up a new account.</li>
  <li>Existing users can access their accounts.</li>
  <li>Functions to:
    <ul>
      <li>Add tasks</li>
      <li>List tasks</li>
      <li>Remove tasks</li>
      <li>Mark tasks as complete</li>
    </ul>
  </li>
</ul>

<h3>User Stories</h3>

<h4>Client Goals</h4>
<ul>
  <li>A simple and user-friendly application.</li>
  <li>An application that meets the user’s needs.</li>
  <li>Users to feel their data is secure.</li>
</ul>

<h4>First Time User Goals</h4>
<ul>
  <li>To be able to set up a new account.</li>
  <li>To understand how to use the application.</li>
  <li>To be able to choose their own username.</li>
</ul>

<h4>Returning User Goals</h4>
<ul>
  <li>For personal data to be stored securely.</li>
  <li>To access an existing account.</li>
  <li>To be able to add tasks, list tasks, remove tasks, and mark tasks as complete.</li>
  <li>A pleasant user experience.</li>
</ul>

<p><a href="#to-do-list">Back to top</a></p>

<h2>Design</h2>

<h3>Flowcharts</h3>
<p>Flowcharts were created to map out the user experience and the validation process within the application.</p>

<h4>User Experience Flowchart</h4>
<img src="assets/images/user-experience-flowchart.png" alt="User Experience Flowchart">

<h4>Validation Flowchart</h4>
<img src="assets/images/validation-flowchart.png" alt="Validation Flowchart">

<p><a href="#to-do-list">Back to top</a></p>

<h2>Features</h2>

<h3>Existing Features</h3>

<h4>Welcome Page</h4>
<p>When the program is first run, the user is greeted with a welcome message and asked to enter their name. The name must only contain alphabetic characters.</p>

<h4>New User</h4>
<p>If the user is new, they can enter their name, which will be validated to ensure it only contains alphabetic characters.</p>

<h4>Main Menu</h4>
<p>After entering their name, the user is presented with the main menu with the following options:</p>
<ul>
  <li>Add a new task</li>
  <li>List all tasks</li>
  <li>Remove a task</li>
  <li>Mark a task as complete</li>
  <li>Exit</li>
</ul>

<h4>Add Task</h4>
<p>The user can add a new task by entering a description and an optional due date.</p>

<h4>List Tasks</h4>
<p>The user can list all tasks, which displays the tasks along with their status (complete or incomplete).</p>

<h4>Remove Task</h4>
<p>The user can remove a task by specifying its index in the list.</p>

<h4>Mark Task Complete</h4>
<p>The user can mark a task as complete by specifying its index in the list.</p>

<h4>Exit</h4>
<p>The user can exit the application.</p>

<h3>Future Implementations</h3>
<ul>
  <li>Implement user authentication to store and retrieve user-specific task lists.</li>
  <li>Add a feature to edit existing tasks.</li>
  <li>Improve error handling and validation for user inputs.</li>
  <li>Allow tasks to be categorized.</li>
</ul>

<p><a href="#to-do-list">Back to top</a></p>

<h2>Technologies Used</h2>

<h3>Languages Used</h3>
<ul>
  <li>Python</li>
</ul>

<h3>Frameworks, Libraries, and Programs Used</h3>
<ul>
  <li><strong>argparse</strong>: For parsing command-line arguments.</li>
  <li><strong>os</strong>: For clearing the terminal screen.</li>
  <li><strong>time</strong>: For adding delays to certain outputs.</li>
  <li><strong>sys</strong>: For system-specific parameters and functions.</li>
</ul>

<p><a href="#to-do-list">Back to top</a></p>


