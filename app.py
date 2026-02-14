from flask import Flask, render_template, send_file
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template("base.html")


@app.route("/download_cv")
def download():
    return send_file("static/stamatis_cv", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
