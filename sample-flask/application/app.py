from flask import Flask, render_template
import os
import mysql.connector

app = Flask(__name__)
db_host = "db"  # MySQL host
db_user = "tomer"  # MySQL username
db_password = "1234"  # MySQL password
db_name = "develop"  # MySQL database name

# Function to execute the init.sql file
def execute_init_script():
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = conn.cursor()
    print("connected")

# Function to increment the visit count
def increment_visit_count():
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = conn.cursor()
    cursor.execute("UPDATE visits SET count = count + 1")
    conn.commit()
    conn.close()

# Function to retrieve the current visit count
def get_visit_count():
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT count FROM visits")
    count = cursor.fetchone()
    conn.close()
    return count[0] if count else 0

# Function to retrieve the fun facts from the database
def get_fun_facts():
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT fun_facts FROM solar_system")
    facts = cursor.fetchall()
    conn.close()
    return [fact[0] for fact in facts]

@app.route("/")
def hello_world():
    increment_visit_count()
    count = get_visit_count()
    return render_template("index.html", count=count)

@app.route("/sun")
def sun():
    return render_template("sun.html")

@app.route("/moons")
def moons():
    return render_template("moons.html")

@app.route("/the-planets")
def the_planets():
    return render_template("The-planets.html")

@app.route("/dwarf-planets")
def dwarf_planets():
    return render_template("Dwarf-planets.html")

@app.route("/exploration")
def exploration():
    return render_template("Exploration.html")

@app.route("/fun-facts")
def fun_facts():
    facts = get_fun_facts()
    return render_template("Fun-facts.html", facts=facts)

if __name__ == "__main__":
    execute_init_script()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
