import json
from flask import Flask, jsonify, render_template, request, Response


app = Flask(__name__)


with open('movies.json') as json_data:
    movie_json = json.load(json_data)
    list_of_movies = []
    for movie in movie_json['movies']:
    	list_of_movies.append(movie)

@app.route('/movies', methods =['GET'])
def test1():
	return render_template("index.html",list_data=list_of_movies)

@app.route('/movies/<string:movie_id>', methods =['GET'])
def test2(movie_id):
	list_movie_id = [movie for movie in list_of_movies if movie['id'] == movie_id]
	return render_template("index.html",list_data=list_movie_id)

if __name__ == '__main__':
	 app.run(host='0.0.0.0')
