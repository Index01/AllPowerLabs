__author__ = 'Index'


'''A scheduler for running the monitoring controllers at a consistent interval. Experimenting with a few solutions'''

import sched, time


class scheduleManager():

    def __init__(self, name):
        self.schedy=sched.scheduler(time.time, time.sleep)
        self.name=name

    def addTask(self, interval, func, *arg):
        self.schedy.enter(interval, 1, func, arg)
        print self.schedy.queue

        return

    def run(self):
        self.schedy.run()
        return


    def checkQueue(self):
        print self.schedy.queue

class task():

    '''Task object should have the same name as the object instance .func will be called on'''
    def __init__(self, name, func, args):
        self.name=name
        self.func=func
        self.args=args


    '''Function which will be called on the owning task object'''
    def taskFunc(self):
        func=self.func
        print "Func: % s" % func

        return func


    def returnFunc(self):


        return self.func


