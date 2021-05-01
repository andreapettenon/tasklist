from flask import Flask, render_template

tasklist = [["Walk Dog", True], ["Wash Dishes", False], ["Take out Trash", True]]
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("tasklist.html", TaskList = tasklist)         #("Hello World !!!!!!!!!")

app.run()