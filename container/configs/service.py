# grafana - container
# prometheus - container
# Both containers below should use a docker compose shared volume
# python code - every 10 seconds goes and reads the file
# from the shared volume and runs the code for each line in the file
# api flask server - saves a new site to a shared volume - https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/
from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/add_site', methods=['POST'])
def add_site():
    if request.method == 'POST':
        website = request.get_json()
        with open('/tmp/site_list.txt', 'a+') as f:
           print(website , file=f)
        # Add the website to a list in a file that's inside a docker volume
    return "Site {} was added".format(website['site'])
if __name__ == "__main__":
    app.run()