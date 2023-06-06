import mysql.connector
import pymysql
from prettytable import PrettyTable


class Quiz:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="aws.connect.psdb.cloud",
            user="idktomi37oen62h4el4m",
            passwd="pscale_pw_GtlKhGeoxf58WfRJoJakmUJisvdDlhH8gyyGG1zGikt",
            db="skinnybase",
            autocommit=True,
            ssl_mode="VERIFY_IDENTITY",
            ssl={
                "ca": "/etc/ssl/certs/ca-certificates.crt"
            }
        )
        self.cursor = None
  
    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()


    def display_quiz(self):

        self.cursor = self.connection.cursor() 
        query = "SELECT question, option1, option2, option3, option4 FROM music_questions"
        self.cursor.execute(query)
        questions = self.cursor.fetchall()

        for question in questions:
            print("Question: ", question[0])
            print("Options:")
            for i in range(1,5):
                print(f"{i}. {question[i]}")
            print()

    def take_quiz(self):
        score = 0
        total_questions = 0
        self.cursor = self.connection.cursor() 

        query = "SELECT question, correct_answer FROM music_questions"
        self.cursor.execute(query)
        questions = self.cursor.fetchall()

        for question in questions:
            total_questions += 1
            print("Question:", question[0])
            user_answer = input("Your answer (enter the option number): ")
            if user_answer == question[1]:
                score += 1

            print("Quiz completed")
            print("Your score: ", score, "/", total_questions)


    def show_leaderboard(self):
        self.cursor = self.connection.cursor() 
        query = "SELECT username, score FROM leaderboard ORDER BY score DESC LIMIT 10"
        self.cursor.execute(query)
        leaderboard = self.cursor.fetchall()

        print("Leaderboard:")
        for rank, entry in enumerate(leaderboard, start=1):
            print(f"{rank}. {entry[0]} - Score: {entry[1]}")

