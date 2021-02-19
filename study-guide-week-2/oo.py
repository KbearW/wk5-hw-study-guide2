class Student:
    '''Student'''
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

        print(f'{self.first_name} has been added!')



class Question:
    '''list of questions'''
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

        print(f'Question: {self.question} has been added!')

    def ask_and_evaluate(self):
        return input(f'{self.question} >') == self.correct_answer
    

class Exam:
    '''exam'''
    def __init__(self, name):
        self.name = name
        # The following variable modify the next method/ function- add_question
        self.questions = []

        # print(f'Name: {self.name} has been added!')

    def add_question(self, question):
        '''add questions to the exam'''
        self.questions.append(question)
    
    def administer(self):
        '''admin all the exam's questions'''
        score = 0
        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1
        # print(float(score / len(self.questions)) * 100)
        score = (float(score) / len(self.questions)) * 100
        if score > 50:
            return ('passed')
        else:
            return ('failed')

class StudentExam:
    '''store a student, an exam and the student's score for that exam.'''
    def __init__(self, student, exam):
        self.student = student
        self.exam = exam
        self.score = None

    def take_test(self):
        '''administers the exam and assigns 
        the actual score to the StudentExam instance.'''
        self.score = self.exam.administer()

        # print("Your score is {:.2f} percent.".format(self.score))

        # print(f'Your score is {self.score} percent.')
        print(f'You have {self.score}.')

def example():
    '''creates an exam, adds a few Qs to the exam, creates a student etc.'''
    exam = Exam('midterm')

    set_q = Question('A','1')
    exam.add_question(set_q)

    set_q2 = Question('B','2')
    exam.add_question(set_q2)
    
    # print(exam.questions)
    student = Student('K','M','394 dfs drive')

    # k_midterm = StudentExam(student,exam)

    # k_midterm.take_test()

    # or
    StudentExam(student,exam).take_test()
    
example()