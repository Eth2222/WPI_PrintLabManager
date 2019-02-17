from datetime import timedelta

class printJob:
    #TODO will need a helper function to parse 22:33 into a time delta, 
    #actually will need a pretty good time parser
    #it will work as text for now, needs to be put in a gform as string anyways
    def __init__(self, date, time, name, email, weight, duration, queueName):
        self.date = date
        self.time = time
        self.name = name
        self.email = email
        self.weight = weight
        self.duration = duration
        self.queueName = queueName
        #dict{'date':self.date, 'time':self.time,'name':self.name,'email':self.email,'weight':self.weight,'duration':self.duration,'queuename':self.queueName}

#look into __json__ function of python. its interesting
#may want to store as json the whole time

# update --cannot serialize 'sets' which this is apparently


