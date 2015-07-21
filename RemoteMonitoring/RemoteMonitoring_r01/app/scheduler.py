__author__ = 'Index'


'''A scheduler for running the monitoring controllers at a consistent interval. Experimenting with a few solutions'''

import sched, time
import controllerMangoInitialstate


class scheduleManager():

    def __init__(self, name):
        self.schedy=sched.scheduler(time.time, time.sleep)
        self.name=name

    def addTask(self, func, *arg):
        self.schedy.enter(10, 1, func, arg)
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


def main():

    MyScheduleManager=scheduleManager('myScheduleManager')
    MISController=controllerMangoInitialstate.MangoInitialStateController("MISController")
#    Task_LogData=task('task_logData', func=MISController.logDataToIS, args='pp717')

#    MyScheduleManager.addTask(Task_LogData.taskFunc(), arg='pp717')

    while True:
        print "pre-run: %s" % MyScheduleManager.checkQueue()
        MyScheduleManager.addTask(MISController.logDataToIS, 'pp717')
        print "[+] Runnin dat task"

        print time.time()
        MyScheduleManager.run()

        print "post run: %s " % MyScheduleManager.checkQueue()
        print "[+] Been got dat task runned!"



if __name__=='__main__':
    main()