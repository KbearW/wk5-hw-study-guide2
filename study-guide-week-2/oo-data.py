from oo import *

Student('Jasmine','Debugger','0101 Computer Street')    
Student('Jacqui','Console','888 Binary Ave')
# Should return XXX has been added!

Question("What's the capital of Alberta?", "Edmonton")
Question("Who's the author of Python?", "Guido Van Rossum")
#Should return Question: XXX has been added!

Exam('Midterm')
# 'alberta_capital')
# ,'python_author')

Exam('Final')
# Exam('ubermelon','ubermelon_competitor')
# Exam('ubermelon','balloonicorn_color')
list_q = Question('python lists are M, I and What?','ordered')
Exam('final').add_question(list_q)

set_q = Question('Name?','1')
exam = Exam('Midterm')
exam.add_question(set_q)

pwd_q = Question('Stand for?','2')
exam.add_question(pwd_q)





# exam.administer()