# adastra_assignment
Dockerised FastAPI Application 
Flask and PostgreSQL Dockerized App Exercise

Steps to Set Up the Project

1️. Clone the Git Repository

git clone <repository_url>
cd CodingAssignmentEverestek
2️. Create a Virtual Environment

python3 -m venv env
3️. Activate the Virtual Environment

On macOS/Linux:
source env/bin/activate
On Windows (Command Prompt):
env\Scripts\activate
On Windows (PowerShell):
env\Scripts\Activate.ps1
4️. Build and Start the Docker Containers

sudo docker-compose build
sudo docker-compose up
5️. Access Swagger API Documentation

Once the app is running, open the Swagger UI in browser: Swagger API Docs

Additional Notes

Make sure Docker and Docker Compose are installed before running the commands.
To stop the running containers:
docker-compose down
To rebuild everything from scratch (clearing old volumes):
docker-compose down -v
docker-compose up --build
Data from users.json is inserted in DB on intialising the docker-compose
