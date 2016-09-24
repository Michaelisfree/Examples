# -*- coding: utf-8 -*-
from flask import Flask,request,render_template
import sqlite3
import hashlib
def getmd5(paw):
    md5=hashlib.md5()
    md5.update(paw.encode("utf-8"))
    return md5.hexdigest()
conn=sqlite3.connect('zhuce.db')
cursor=conn.cursor()
cursor.execute('create table iuser(ider varchar(20) primary key,username varchar(20),password varchar(50))')
cursor.execute("insert into iuser values('A-001','admin','5f4dcc3b5aa765d61d8327deb882cf99')")
cursor.execute("insert into iuser values('A-002','admin2','6cb75f652a9b52798eb6cf2201057c73')")
cursor.execute("insert into iuser values('A-003','admin3','819b0643d6b89dc9b579fdfc9094f28e')")
cursor.close()
conn.commit()
conn.close()
app=Flask(__name__)
@app.route('/',methods=["GET","POST"])
def home():
    return render_template("home.html")
@app.route('/signin',methods=["GET"])
def signin_form():
    return render_template("form.html")
@app.route('/register',methods=["GET"])
def reg_form():
    return render_template("register.html")
@app.route('/register',methods=['POST'])
def reg():
    username=request.form['account']
    password=request.form['password']
    ider=request.form['ID']
    conn=sqlite3.connect('zhuce.db')
    cursor=conn.cursor()
    cursor.execute("select username,password from iuser")
    values=cursor.fetchall()
    d=dict(values)
    if username in d.keys():
        return render_template('register.html',message="account name existed")
    else:
        cursor.execute("insert into iuser values('%s','%s','%s')"%(ider,username,getmd5(password)))
    conn.commit()
    cursor.execute("select username,password from iuser")
    values=cursor.fetchall()
    return render_template('register-ok.html',username=username,values=values)
    cursor.close()
    conn.close()
@app.route('/signin',methods=["POST"])
def signin():
    conn=sqlite3.connect('zhuce.db')
    cursor=conn.cursor()
    cursor.execute("select username,password from iuser")
    values=cursor.fetchall()
    d=dict(values)
    print(d.keys())
    print(d.values())
    cursor.close()
    conn.close()
    username=request.form['username']
    password=request.form['password']
    if username in d.keys():
        if d[username]==getmd5(password):
            return render_template("signin-ok.html",username=username)
        else:
            return render_template("form.html",message="Wrong password",password=password,username=username)
    return render_template("form.html",message="Wrong username",username=username)
if __name__=='__main__':
    app.run()
