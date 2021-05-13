import psycopg2
db_name = "TaskListDB"
db_user = "tasklist_user"
db_pwd = "abc123"
db_host = "localhost"

def getTaskList():
    conn = psycopg2.connect(dbname = db_name, user = db_user, password = db_pwd, host = db_host)
    cur = conn.cursor()
    cur.execute('SELECT task_name, is_done FROM public."TaskList"')
    tasklist = cur.fetchall()
    cur.close
    conn.close
    return tasklist

def addTask(name, date):
    conn = psycopg2.connect(dbname = db_name, user = db_user, password = db_pwd, host = db_host)
    cur = conn.cursor()
    cur.execute('INSERT INTO public."TaskList" (task_name, due_date) values(\'%s\', \'%s\'); commit;' % (name, date)) # %s è un segnaposto di tipo stringa nel quale inseriamo il valore "name"
    cur.close
    conn.close
