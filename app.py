from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about-us.html')


@app.route("/faq")
def faq():
    return render_template('faq.html')


@app.route("/services")
def services():
    return render_template('services.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/coming-soon")
def coming():
    return render_template('coming-soon.html')


if __name__ == "__main__":
    app.run(debug=True, host="10.0.0.4", port=80)
