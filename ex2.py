# Global variables. Feel free to play around with these
# but please return them to their original values before you submit.
# HINT: Your code should be using these values, if I change them (and I will)
# your output should change accordingly
a0_weight = 5
a1_weight = 7
a2_weight = 8
term_tests_weight = 20
exam_weight = 45
exercises_weight = 10
quizzes_weight = 5

a0_max_mark = 25
a1_max_mark = 50
a2_max_mark = 100
term_tests_max_mark = 50
exam_max_mark = 100
exercises_max_mark = 10
quizzes_max_mark = 5
exam_pass_mark = 40
overall_pass_mark = 50


def get_max(component_name):
    '''(str) -> float
    Given the name of a course component (component_name),
    return the maximum mark for that component. This is used to allow the GUI
    to display the "out of" text beside each input field.
    REQ: component_name must be one of: a0,a1,a2,exerises,midterm,exam
    >>> get_max('a0')
    25
    >>> get_max('exam')
    100
    REQ: component_name in {'a0', 'a1', 'a2', 'exercises', 'term tests',
    'quizzes', 'exam'}
    '''
    # DO NOT EDIT THIS FUNCTION. This function exists to allow the GUI access
    # to some of the global variables. You can safely ignore this function
    # for the purposes of E2.
    if (component_name == 'a0'):
        result = a0_max_mark
    elif (component_name == 'a1'):
        result = a1_max_mark
    elif (component_name == 'a2'):
        result = a2_max_mark
    elif (component_name == 'exercises'):
        result = exercises_max_mark
    elif (component_name == 'term tests'):
        result = term_tests_max_mark
    elif (component_name == 'quizzes'):
        result = quizzes_max_mark
    else:
        result = exam_max_mark

    return result


def percentage(raw_mark, max_mark):
    ''' (float, float) -> float
    Return the percentage mark on a piece of work that received a mark of
    raw_mark where the maximum possible mark of max_mark.
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: raw_max <= max_mark
    >>> percentage(15, 20)
    75.0
    >>> percentage(4.5, 4.5)
    100.0
    '''
    return raw_mark / max_mark * 100


def contribution(raw_mark, max_mark, weight):
    ''' (float, float, float) -> float
    Given a piece of work where the student earned raw_mark marks out of a
    maximum of max_marks marks possible, return the number of marks it
    contributes to the final course mark if this piece of work is worth weight
    marks in the course marking scheme.
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: weight >= 0
    >>> contribution(13.5, 15, 10)
    9.0
    '''
    return (raw_mark / max_mark) * weight


def term_work_mark(a0_mark, a1_mark, a2_mark, exercise_marks, quiz_marks,
                   test_marks):
    '''
    This function takes in marks from all assignments and calculates a weighted
    average for the course
    :param a0_mark: float
    :param a1_mark: float
    :param a2_mark: float
    :param exercise_marks: float
    :param quiz_marks: float
    :param test_marks: float
    :return: float
    >>> term_work_mark(25, 50, 100, 10, 5, 50)
    55.0
    >>> term_work_mark(20, 45, 70, 8, 4, 40)
    43.9
    '''
    mark = contribution(a0_mark, a0_max_mark, a0_weight) + \
        contribution(a1_mark, a1_max_mark, a1_weight) + \
        contribution(a2_mark, a2_max_mark, a2_weight) + \
        contribution(exercise_marks, exercises_max_mark, exercises_weight) + \
        contribution(quiz_marks, quizzes_max_mark, quizzes_weight) + \
        contribution(test_marks, term_tests_max_mark, term_tests_weight)
    return mark


def final_mark(a0_mark, a1_mark, a2_mark, exercise_marks, quiz_marks,
               test_marks, exam_mark):
    '''
    Get the final mark out of 100%
    :param a0_mark: float, x>=0
    :param a1_mark: float, x>=0
    :param a2_mark: float, x>=0
    :param exercise_marks: float, x>=0
    :param quiz_marks: float, x>=0
    :param test_marks: float, x>=0
    :param exam_mark: float, x>=0
    :return: float
    >>> final_mark(25, 50, 100, 10, 5, 50,100)
    100.0
    >>> final_mark(20, 45, 70, 8, 4, 40, 73)
    76.75
    '''
    term_mark = term_work_mark(a0_mark, a1_mark, a2_mark,
                               exercise_marks, quiz_marks, test_marks) + \
        contribution(exam_mark, exam_max_mark, exam_weight)
    return term_mark


def is_pass(a0_mark, a1_mark, a2_mark, exercise_marks, quiz_marks, test_marks,
            exam_mark):
    '''
    Takes in all marks for the given semester and returns whether the student
    has passed the course
    :param a0_mark:float, x>=0
    :param a1_mark:float, x>=0
    :param a2_mark:float, x>=0
    :param exercise_marks:float, x>=0
    :param quiz_marks:float, x>=0
    :param test_marks:float, x>=0
    :param exam_mark:float, x>=0
    :return: Boolean
    >>> is_pass(20, 45, 70, 8, 4, 40, 41)
    True
    >>> is_pass(20, 45, 70, 8, 4, 40, 39)
    False
    >>> is_pass(10, 21, 12, 2, 1, 15, 23)
    False
    '''
    if (exam_mark >= exam_pass_mark and
            final_mark(a0_mark, a1_mark, a2_mark, exercise_marks, quiz_marks,
                       test_marks, exam_mark) >= overall_pass_mark):
        return True
    else:
        return False
