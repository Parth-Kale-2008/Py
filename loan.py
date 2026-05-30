from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle # use to arrange serialwise
import numpy as np

X = np.array([
    #salary,credit score and if there is existing loan
    [33000,550,1],
    [65000,630,0],
    [70000,670,0],
    [85000,710,1],
    [35000,330,0],
    [43000,560,1]
])

y = np.array([0,1,1,1,0,0]) #0 means loan won't be scantioned 1 means loan is scantioned 

model = LogisticRegression()
model.fit(X,y)

#we have taken the user input 
salary = float(input("enter the salary:"))
credit_score = float(input("enter your credit score:"))
loan_input = input("wheater there is any existing loan ?(yes/no)").lower()

existing_loan = 1 if loan_input == "yes" else 0
prediction = model.predict([[salary, credit_score, existing_loan]])
print("if 0 is output loan is rejected and if the output is 1 loan is approved :", prediction[0])