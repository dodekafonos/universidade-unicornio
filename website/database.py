import mysql.connector


def create_database():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mulinhas",
    )
    cur = db.cursor()
    sql = "CREATE DATABASE unes; USE unes"
    cur.execute(sql)
    db.commit()


def connect_db():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mulinhas",
        database="unes"
    )
    return db

def create_table_contato():
    db = connect_db()
    mycursor = db.cursor()
    sql = "CREATE TABLE contato (email varchar(255), assunto varchar(255), descricao varchar(255));"
    mycursor.execute(sql)
    db.commit()

def insert(email, assunto, desc):
    db = connect_db()
    mycursor = db.cursor()
    sql = "INSERT INTO contato (email, assunto, descricao) VALUES (%s, %s, %s)"
    val = [email, assunto, desc]
    mycursor.execute(sql, val)
    db.commit()

def buscar():
    db = connect_db()
    cur = db.cursor()
    cur.execute("SELECT *  FROM contato;")
    info = cur.fetchall()
    return info

