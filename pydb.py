'''
Created on 22-Apr-2020

@author: GOPAL WAGH
'''
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "1234",
    database = "login"    
    )

mycursor = mydb.cursor()

class Register:
    def reg(self):
        try :
            name = input("Enter your good name :")
            email = input("Enter your Email id :")
            user_id = input("Enter your user ID :")
            ppass = input("Enter your password ")
            cpass = input("Conform your password :")
            
            if ppass == cpass :
                
                sql =(" INSERT INTO register (name , email, user_id, ppass) VALUES (%s, %s, %s , %s) ")
                val = (name,email,user_id,ppass)
                mycursor.execute(sql,val)
                mydb.commit()
                print("Data inserted successfully")
                
        except Exception as e:
            print(e) 

class Log(Register):
    def putData(self):
        try :
            user_id = input("Enter your user ID :")
            ppass = input("Enter your password ")
            
            sql = (" select * from register where user_id = %s && ppass = %s ")
            val =(user_id, ppass)
            mycursor.execute(sql,val)
            myresult = mycursor.fetchall()
            for user_id in myresult:
                print("LOgin successful \n welcome")
                break
            else:
                print("Invalid login crediantials")
        except Exception as e:
            print(e) 
            
o = Log()
ans = int(input("\n \n Do you want to continue\n ENter 1 to continue \n 2 to exit"))
while ans ==1:
    if ans ==1:
        a = int(input("ENter 1 to login, \n 2 to register "))
        if a == 1:
            o.putData()
        elif a == 2:
            o.reg()
        elif ans ==2:
            exit
        ans = int(input("\n \n Do you want to continue\n ENter 1 to continue \n 2 to exit"))
