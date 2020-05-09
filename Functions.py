def get_scores():
    score1 = float(input('What is the score of first test?'))
    while score1 < 0:
        print('Error. Please enter a positive number.')
        score1 = float(input('What is the score of first test?'))
    score2 = float(input('What is the score of the second test?'))
    while score2 < 0:
        print('Error. Please enter a positive number.')
        score2 = float(input('What is the score of the second test?'))
    score3 = float(input('What is the score of the third test?'))
    while score3 < 0:
        print('Error. Please enter a positive number.')
        score3 = float(input('What is the score of the third test?'))
    return score1, score2, score3


def calculate_average(score1, score2, score3):
    total = score1 + score2 + score3
    average = total / 3
    return average


def assign_grade(average):
    if average >= 90:
        grade = 'A'
    else:
        if average >= 80:
            grade = 'B'
        else:
            if average >= 70:
                grade = 'C'
            else:
                if average >= 60:
                    grade = 'D'
                else:
                    grade = 'F'
    return grade


def show_results(grade, average):
    print('Grade\t', 'Average')
    print()
    print(grade, '\t', format(average, '.2f'), sep='')


def main():
    score1, score2, score3 = get_scores()

    average = calculate_average(score1, score2, score3)

    grade = assign_grade(average)

    show_results(grade, average)


main()


