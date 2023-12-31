<h1 align="center">Django-Todolist</h1>

## Installation

### Cloning from GitHub Repository

To get started with the Todo_List Django Web App, you can clone the repository from GitHub using the following steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/iliazhigalev/MY-TO-DO.git

2. Navigate to the project folder:
   ```bash
   cd MY-TO-DO/todo

3. Installing Docker and Docker Compose.
   Make sure that users have Docker and Docker Compose installed. Installation instructions can be found on the official
   Docker website:
   https://docs.docker.com/get-docker/
4. Create and activate a virtual environment (optional but recommended, in a file MY-TO-DO):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
5. Install project dependencies:
   ```bash
   pip install -r requirements.txt

6. Launching and assembling containers:
   ```bash
   docker-compose up --build

7. Applying migrations and collecting static Django files:
   ```bash
   docker-compose exec django python manage.py migrate
   docker-compose exec django python manage.py collectstatic

8. Create a superuser account in the container (for admin access):
   ```bash
   python manage.py createsuperuser

9. Open your web browser and go to http://localhost:8000 to access the Todo_List Django Web App.

### Installing from ZIP Archive

1. Download the zip file.
2. Extract the ZIP archive to your desired location on your computer.
3. Navigate to the project folder:
   --Right click on the project folder and 'Copy as path' and paste the path like below
   ```bash
   cd project_path
4. Continue with steps 3 to 8 from the "Cloning from GitHub Repository" section to set up and run the project
