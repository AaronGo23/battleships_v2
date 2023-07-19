from flask import Flask, render_template, jsonify, request
from database import load_games_from_db, load_game_from_db, add_history_to_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  games = load_games_from_db()
  return render_template('home.html', games=games)


@app.route("/game/<id>")
def show_game_history(id):
  game = load_game_from_db(id)
  if not game:
    return "Not Found", 404
  else:
    return render_template('gamehistory.html',game=game)

@app.route("/fillhistory",methods=['post'])
def fill_history1():
  data=request.form
  add_history_to_db(data)
  return render_template("history_submitted.html", history=data)

@app.route("/fill_history")
def fill_history():
  return render_template('history_form.html')



if __name__ == "__main__":
  app.run('0.0.0.0', debug=True)
