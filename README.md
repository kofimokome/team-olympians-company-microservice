# team-olympians-company-microservice
github repo for team olympians hng internship task

# How to run with docker

- Clone / fork the repository
- Open `.env` and set the port you want the application to run on. The default port is 5000
- In the root of the project, open a terminal window and run `docker-compose up -d`
- Then navigate to your IP, port 5000. example: 127.0.0.1:5000, or localhost:5000 or 192.168.10.103:5000
- Open `/swagger` to access the swagger ui


# How to run without docker
- Clone / fork the repository
- In the root of your project, open a terminal window and run `touch env/activate`. This will activate the virtual environment
- Run `pip install -r requirements.txt`
- Finally start the application by running `python app.py`
- Then navigate to your IP, port 5000. example: 127.0.0.1:5000, or localhost:5000 or 192.168.10.103:5000
- Open `/swagger` to access the swagger ui


