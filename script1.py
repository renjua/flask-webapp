import flask
import sys

app=flask.Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"]=0

@app.route("/")
def home():
  return flask.render_template("home.html")

@app.route("/about/")
def about():
  return flask.render_template("about.html")

if __name__=="__main__":
  app.run()