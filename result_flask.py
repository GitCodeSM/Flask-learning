'''
flask program to show two web pages with 2nd page route following the 1st page route to display the test topper among students
'''

# imports
from flask import Flask, render_template, Response, request, redirect, url_for

# calling instance of class Flask
app = Flask(__name__)

# student dictionary with student names and scores
student = {'Student Name':['Ri', 'Leo', 'Mi', 'Nupur', 'Dee', 'Sam', 'Mukula'], 'Student Marks':[40, 35, 60, 80, 75, 55, 90]}

# function to return strings with topper score and name
def topper(student):
    list_marks = student['Student Marks']
    list_name = student['Student Name']
    s_list_copy = list_marks.copy()
    s_list_copy.sort()
    top = s_list_copy.pop()
    pos = list_marks.index(top)
    return f"With {top} score, the topper is: {list_name[pos]}"

# 1st web page using html template for some statements display
@app.route('/')
def index():
    return render_template('student_result.html')

# 2nd web page without html template to display topper() function result on page route 'our_topper' following 1st page route
@app.route('/<our_topper>')
def result(our_topper):
    our_topper = topper(student)
    return f"Test Result: {our_topper}"

if __name__ == '__main__':
    app.run(debug=True)
