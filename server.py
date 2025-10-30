from flask import Flask
from random import *

app = Flask(__name__)

random_number = randint(0, 9)
@app.route("/")
def create_greetings():
    return ("<p>Guess a number between 0 and 9<p>"
            "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbHQyZ2dqa2ozdnBzcXYyOWhiMTVuazYxNHVoYWx0NnhkMHVkaTN3eCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/IsfrRWvbUdRny/200.webp' />")

@app.route("/<number>")
def check_number(number):
    global random_number
    if int(number) < random_number:
        return ('<p>Too low. </p>'
                '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWZ4a2tqY3EwOXdsNmQxdmNneDdwemZ4aXgyNmtxb20wd255eHFnZCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/vFKqnCdLPNOKc/200.webp" />')
    elif int(number) > random_number:
        return ('<p>Too high!!. </p>'
                '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWZ4a2tqY3EwOXdsNmQxdmNneDdwemZ4aXgyNmtxb20wd255eHFnZCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/q1MeAPDDMb43K/giphy.webp"/>')
    else:
        return ('<p>You won!! </p>'
                '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWZ4a2tqY3EwOXdsNmQxdmNneDdwemZ4aXgyNmtxb20wd255eHFnZCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/C9x8gX02SnMIoAClXa/giphy.webp"/>')
if __name__ == "__main__":
    app.run(debug=True)