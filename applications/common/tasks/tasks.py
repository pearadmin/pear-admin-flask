import datetime

task_list = ['task2', 'task3', 'task4']


def task2(a, b):
    print(f'定时任务_1_{a},{b},{datetime.datetime.now()}')


def task3(a, b):
    print(f'定时任务_2_{a}{b}{datetime.datetime.now()}')


def task4(a, b):
    print(f'定时任务_4_{a}{b}{datetime.datetime.now()}')
