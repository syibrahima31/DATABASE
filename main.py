import psycopg2
from psycopg2 import Error
from utils import *

def connection():
    try:
        conn = psycopg2.connect(
            dbname = DATABASE,
            user = USER, 
            password = PASSWORD, 
            host = HOST, 
            port = PORT
        ) 
        print("Connection réussie")
        return conn
    except Error as e: 
        print(f"Erreur de connexion {e}")
        return None 


def insert_student(nom, prenom): 
    try:
        # ouvrir une connexion 
        conn = connection()
        cur = conn.cursor()
        requete = "INSERT INTO students (nom, prenom) VALUES(%s, %s)"
        cur.execute(requete, (nom, prenom))
        conn.commit()
        print("Insertion réussie !!! ")
        conn.close()
    except Error as e: 
        print(f"Erruer insertion {e}")


def lister_students():
    try:
        # ouvrir une connexion 
        conn = connection()
        cur = conn.cursor()
        requete = "SELECT * FROM students"
        cur.execute(requete)
        res = cur.fetchall()
        for st in res: 
            print(st)
        print("recuperation réussie !!!")
        conn.close()
    except Error as e: 
        print(f"Erreur de recuparation {e}")




if __name__ == "__main__": 
    #insert_student("DIEYE", "MAMADOU")
    lister_students()

