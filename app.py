from flask import Flask, render_template, send_file, request
from flask_bootstrap import Bootstrap5
from forms import ContactForm
import smtplib
import os


EMAIL_ENV = os.environ.get("ENV_EMAIL")
EMAIL_PASSWORD = os.environ.get("ENV_PASSWORD")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
bootstrap = Bootstrap5(app)


@app.route("/", methods=["GET", "POST"])
def home():

    form = ContactForm()

    if form.validate_on_submit():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL_ENV, password=EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=EMAIL_ENV,
                to_addrs=EMAIL_ENV,
                msg=f"Subject:A person tries to get in contact.\n\n"
                    f"Name: {request.form["name"]}\nEmail: {request.form["email"]}\n"
                    f"Message: {request.form["message"]}"
            )
    return render_template("index.html", form=form)


@app.route("/download_cv")
def download():
    return send_file("static/stamatis_cv", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)


