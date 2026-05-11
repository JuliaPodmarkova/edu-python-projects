import random
from os import remove


def lottery():
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    win = random.choice(tickets)
    return win
print('The ticket is win: ', lottery())

def twoDayLottery(firstDay, secondDay):
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(firstDay, secondDay)
    return win1,win2
win1, win2 = twoDayLottery('monday ', ' tusday')
print('win: ', win1, ' win: ', win2)

def test(a = 2, b = True):
    print(a, b)
test()
test(False, 'ok')
test([1, 2])
test(*[1, 2])
