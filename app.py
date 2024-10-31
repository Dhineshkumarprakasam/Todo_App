from flask import Flask,render_template,request,url_for,redirect
import sqlite3
app = Flask(__name__)


con=sqlite3.connect("data.db")
cursor=con.cursor()

cursor.execute("""
               Create table if not exists todo (
                    task_id varchar(5), 
                    task_Name varchar(20), 
                    task_date date,
                    task_remarks varcahr(100))
""")
cursor.close()
con.close()

@app.route("/delete/<string:task_id>",methods=['GET','POST'])
def delete(task_id):
    con=sqlite3.connect("data.db")
    cursor=con.cursor()
    q="delete from todo where task_id='{}'".format(task_id)
    cursor.execute(q)
    con.commit()
    cursor.close()
    con.close()
    return redirect('/')

@app.route("/",methods=['GET','POST'])
def index():
    con=sqlite3.connect("data.db")
    cursor=con.cursor()
    cursor.execute("Select * from todo")
    data=cursor.fetchall()
    cursor.close()
    con.close()
    if request.method=="POST":
        task_id=request.form['task_id']
        task_name=request.form['task_name']
        task_date=request.form['task_date']
        task_remarks=request.form['task_remarks']
        con=sqlite3.connect("data.db")
        cursor=con.cursor()
        cursor.execute("insert into todo values(?,?,?,?)",(task_id,task_name,task_date,task_remarks))
        con.commit()
        cursor.close()
        con.close()
        return redirect("/")
    return render_template("index.html",data=data)


if __name__=="__main__":
    app.run(debug=True)
