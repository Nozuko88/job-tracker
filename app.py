from flask import Flask,render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    print(">>>Recreating database...")
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS jobs")
    c.execute('''CREATE TABLE IF NOT EXISTS jobs 
                    (id INTEGER PRIMARY KEY, company TEXT, role TEXT, status TEXT, date_applied TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute("SELECT* FROM jobs")
    jobs = c.fetchall()
    conn.close
    return render_template('index.html', jobs=jobs)

@app.route('/add', methods=['POST'])
def add():
    company = request.form['company']
    role = request.form['role']
    status = request.form['status']
    date = request.form['date']
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute("INSERT INTO jobs(company,role,status,date_applied) VALUES (?, ?, ?, ?)", (company, role, status, date))

    conn.commit()
    conn.close()
    return redirect('/')


if __name__== '__main__':
    init_db()
    app.run(debug=True)    