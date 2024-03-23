import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool, WebsiteSearchTool

with open('api_key.txt', 'r') as f:
    API_KEY = f.read()

os.environ["OPENAI_API_KEY"] = API_KEY
os.environ["SERPER_API_KEY"] = "539afe9040c137672fcd254f20c67c9e6f1a555b"

search_tool = SerperDevTool()
website_search = WebsiteSearchTool()

# Defining the agents
# Shiva
Architect = Agent(
    role="Analyzes user needs, defines project scope, breaks down features into actionable tasks, oversees development "
         "workflow, and ensures all agents collaborate effectively.",
    goal="Deliver high-quality, functional software that meets user requirements on time and within budget.",
    backstory="codename Shiva. Shiva was trained on vast "
              "amounts of software development methodologies, project management principles, and user experience "
              "design data.",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool, website_search]
)
# Hanuman
Codesmith = Agent(
    role="Writes clean, efficient, and well-documented code based on the Architect's specifications",
    goal="Produce bug-free, maintainable code that adheres to best practices",
    backstory="codename Hanuman. Hanuman is a deep learning model trained on massive code repositories across various "
              "programming languages especially in python.",
    verbose=True,
    allow_delegation=True,
    tools=[search_tool, website_search]
)
# Arjun
Auditor = Agent(
    role=" Identifies and reports bugs, performs automated and manual testing, ensures code adheres to security "
         "protocols, and monitors software performance.",
    goal="Deliver robust, secure software with minimal defects.",
    backstory="codename Arjun. Arjun utilizes machine learning algorithms to analyze code for vulnerabilities, run "
              "test suites, and identify potential flaws",
    verbose=True,
    allow_delegation=True,
    tools=[search_tool, website_search]
)
# Krishna
Muse = Agent(
    role="Generates creative ideas for functionalities, user interfaces, and problem-solving approaches.",
    goal="Inject innovation and user-centric design thinking into the development process.",
    backstory="codename Krishna. Krishna is a large language model trained on design principles, user behavior data, "
              "and creative problem-solving techniques.",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool, website_search]
)
# Vishnu
Archivist = Agent(
    role="Stores and retrieves project information, code snippets, design documents, and past development decisions.",
    goal="Facilitate knowledge sharing among AI agents and human developers, enabling faster learning and efficient "
         "project continuity",
    backstory="codename Vishnu. Vishnu is a powerful information retrieval system trained on vast software development "
              "resources, documentation, and project history data.",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool, website_search]
)
# Bheem
Tester = Agent(
    role=" Implements various testing methodologies (unit testing, integration testing, etc.) to identify and report "
         "bugs throughout the development lifecycle.",
    goal="Ensure the software functions as intended, catching bugs early and preventing regressions.",
    backstory="codename Bheem. Bheem is an deep learning model trained on massive datasets of software tests and "
              "bug reports.",
    verbose=True,
    allow_delegation=True,
    tools=[search_tool, website_search]
)

# Define Tasks

task1 = Task(
    description="Define project scope and functionalities. Break down functionalities into modules (File Selection, "
                "Conversion Engine, User Interface, Output Management).",
    expected_output="Project plan document outlining modules, dependencies, and communication flow between agents.",
    agent=Architect
)

task2 = Task(
    description="Develop functions to allow users to select the input folder containing video files using a user-"
                "friendly GUI element (e.g., file picker).",
    expected_output="Python code for a GUI element that returns the selected folder path.",
    agent=Codesmith
)

task3 = Task(
    description="Develop functions that handle video conversion based on user-selected output format. (Initially a "
                "single function, but can be expanded to support multiple formats)",
    expected_output="Python code for the conversion process using libraries like `moviepy` or `ffmpeg`. This could "
                    "include a function that takes the input file path, output format, and output folder path and "
                    "performs the conversion.",
    agent=Codesmith
)

task4 = Task(
    description="Develop a user-friendly GUI using a library like `Tkinter` or `PyQt`. The GUI should include options "
                "for selecting the input folder, choosing the output format (initially a dropdown list), "
                "specifying the output folder, and a button to initiate the conversion process.",
    expected_output="Python code that creates the user interface window with these functionalities.",
    agent=Codesmith
)

task5 = Task(
    description="Develop functions for managing the output video files. Initially, this could be a function that "
                "generates unique output filenames and saves the converted video in the specified output folder. But "
                "in the future, it can be expanded to include functionalities like progress bars or error handling.",
    expected_output="Python code for managing output video files, including filename generation and saving the "
                    "converted video.",
    agent=Codesmith
)

task6 = Task(
    description="Write unit tests for each module (File Selection, Conversion Engine, User Interface) to ensure "
                "individual functionalities work as expected.",
    expected_output="Automated unit tests using a testing framework like `unittest` or `pytest` that verify the "
                    "correctness of each module's behavior.",
    agent=Auditor
)

task7 = Task(
    description="Brainstorm ideas for future features like batch processing, supporting multiple input and output "
                "formats, or adding progress bars.",
    expected_output="A document outlining potential feature ideas for future development.",
    agent=Muse
)

task8 = Task(
    description="Store all project-related code, documentation, and test cases in a version control system like Git.",
    expected_output="A well-organized code repository with clear commit messages and documentation for "
                    "future reference.",
    agent=Archivist
)

crew = Crew(
    agents=[Architect, Codesmith, Auditor, Archivist, Muse, Tester],
    tasks=[task1, task2, task3, task4, task5, task6, task7, task8],
    verbose=2,  # You can set it to 1 or 2 to different logging levels
)

result = crew.kickoff()

print("######################")
print(result)

with open('output_agents.txt', 'w', encoding='utf-8') as f:
    f.write(result)
