from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

jobs = {
    '001': {
        'title': 'Brynn\'s big boi Company',
        'description': 'Company description',
        'skills': ['these','are', 'my', 'skills']
    }
}

class JobList(Resource):
    def get(self):
        return jobs

# Set up restful Jobs section
class Jobs(Resource):

    def get(self, jobId):
        return {jobId: jobs[jobId]}
    
    def put(self, jobId):
        jobs[jobId] = request.get_json()
        return {jobId: jobs[jobId]}
    
    def delete(self, jobId):
        del jobs[jobId]

class Profile(Resource):
    def post(self):
        return 'Aye boi'


api.add_resource(Jobs, '/jobs/<string:jobId>')
api.add_resource(JobList, '/jobs')

if __name__ == '__main__':
    app.run(debug=True)