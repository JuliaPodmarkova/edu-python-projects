def calc(line):
    operand1, operation, operand2 = line.split(' ')
    if operation == '+':
        print('Результат: ', (int(operand1) + int(operand2)))
    if operation == '-':
        print('Результат: ', (int(operand1) - int(operand2)))
    if operation == '*':
        print('Результат: ', (int(operand1) * int(operand2)))
    if operation == '/':
        print('Результат: ', (int(operand1) / int(operand2)))
    if operation == '%':
        print('Результат: ', (int(operand1) % int(operand2)))
    if operation == '//':
        print('Результат: ', (int(operand1) // int(operand2)))

cnt = 0

with open("data.txt", 'r') as file:
    for line in file:
        cnt += 1
        try:
            calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
               print('Error on line {} - do not have parameters to answer'.format(cnt))
            if 'int' in exc.args[0]:
                print('Error on line {} - can not chang parameters for int()'.format(cnt))
