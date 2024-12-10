from flask import Flask, render_template, request
from exceptions import APIError
from api import get_weather
from weather import get_message


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    
    try:
        weather_city1 = get_weather(request.form.get("city1"))
    except APIError as err:
        return render_template("index.html", error=err.message)

    try:
        weather_city2 = get_weather(request.form.get("city2"))
    except APIError as err:
        return render_template("index.html", error=err.message)

    message_city1 = get_message(*weather_city1)
    message_city2 = get_message(*weather_city2)

    return render_template("index.html", message_city1=message_city1, message_city2=message_city2)

if __name__ == '__main__':
    app.run(debug=True)
