from flask import Flask, render_template, url_for

app = Flask(__name__)
href="{{ url_for('static', filename='images/Rijk_Lianne_vakantie2022.jpg') }}"

@app.route("/")
def World():
   return render_template("home.html")

@app.route("/templates")
def Ons():
  return render_template("ons.html")

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
