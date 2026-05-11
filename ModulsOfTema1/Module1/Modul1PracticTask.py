grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]];
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'};
student1 = len(grades[0]);
student2 = len(grades[1]);
student3 = len(grades[2]);
student4 = len(grades[3]);
student5 = len(grades[4]);
sumBallStudent1 = sum(grades[0]);
sumBallStudent2 = sum(grades[1]);
sumBallStudent3 = sum(grades[2]);
sumBallStudent4 = sum(grades[3]);
sumBallStudent5 = sum(grades[4]);
averageScoreStudent1 = round(sumBallStudent1 / student1, 2);
averageScoreStudent2 = round(sumBallStudent2 / student2, 2);
averageScoreStudent3 = round(sumBallStudent3 / student3, 2);
averageScoreStudent4 = round(sumBallStudent4 / student4, 2);
averageScoreStudent5 = round(sumBallStudent5 / student5, 2);
averageScoreStudents = [averageScoreStudent1, averageScoreStudent2, averageScoreStudent3, averageScoreStudent4, averageScoreStudent5];
studentsList = list(students);
studentsList.sort();
dictionary = dict(zip(studentsList, averageScoreStudents));
print(dictionary);


