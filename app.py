import os
import requests
from flask import Flask
from flask_restful import Resource, Api

key = os.environ['PIXABAY_API_KEY']

app = Flask(__name__)
api = Api(app)


def summary_text(text):
    keyword = text
    return keyword


class Hello(Resource):
    def get(self):
        return {'hello': 'world'}


class MakeSuggestion(Resource):
    def get(self, text):
        payload = {'key': key, 'q': summary_text(text)}
        r = requests.get('https://pixabay.com/api/', params=payload)
        if r.status_code != 200:
            return 'there is some error'
        resp = r.json()
        return [hit['largeImageURL'] for hit in resp['hits']]


api.add_resource(Hello, '/')
api.add_resource(MakeSuggestion, '/api/<string:text>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
