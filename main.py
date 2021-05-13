from flask import Flask, render_template, request, redirect, url_for       #la variabile request serve per richiedere un'informazione
from db import getTaskList, addTask
app = Flask(__name__)

#tasklist = [["Walk Dog", True], ["Wash Dishes", False], ["Take out Trash", True]]


app = Flask(__name__)
@app.route("/")
def home():
    tasklist = getTaskList()
    return render_template("tasklist.html", TaskList = tasklist)         #("Hello World !!!!!!!!!")

@app.route("/add", methods=['POST'])
def add():
    taskname = request.form['taskName']
    duedate = request.form['dueDate']
    addTask(taskname, duedate)
    return redirect(url_for('home'))
app.run()