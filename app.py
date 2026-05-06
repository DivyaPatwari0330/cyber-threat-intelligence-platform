from flask import Flask, render_template, request
from intel import check_ip

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def home():

    result = {}

    if request.method == "POST":

        ip = request.form["ip"]

        result = check_ip(ip)

    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)
