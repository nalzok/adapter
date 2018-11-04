import requests
from flask import Flask
from flask_restful import Resource, Api


key = '10586160-ad0baa48d53693e1114bf544d'

app = Flask(__name__)
api = Api(app)


def summary_text(text):
    keyword = text
    return keyword


class MakeSuggestion(Resource):
    def get(self, text):
        payload = {'key': key, 'q': summary_text(text)}
        r = requests.get('https://pixabay.com/api/', params=payload)
        resp = r.json()
        return [hit['largeImageURL'] for hit in resp['hits']]


api.add_resource(MakeSuggestion, '/api/<string:text>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
