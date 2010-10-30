###MADE BY RISHI RAWAT
### SATURDAY, SEP 11, 2010




import numpy;import random; import networkx as nx; import matplotlib.pyplot as plt

class bear:
    bearlist = []   #all bears stay on the bearlist for ever, even if they die
    bearnum = 0  #bearnum is a counter for the number of bears that have lived in the population; each bear that goes throught the population is given a number one higher than the one before it 
    bearpop = 0  #bearpop is number of bears currently alive
    pmale = .5
    def __init__(self, name, male = False, alive = True,father = "unknown",mother = "unknown"):
        self.name = name
        self.age = 0
        self.beforerep = 5  # years before reproducing, newborn bears must wait 5 yrs
        self.lifespan = round(numpy.random.normal(35,5)) # lifespan on a normal distribution
        self.ismale = male #ismale is a true/false depending on gender
        self.alive = alive #by default, bears are born alive
        bear.bearlist.append(self) 
        self.father = father
        self.mother = mother
        bear.bearnum += 1
        self.children = []
        bear.bearpop += 1
        # Above, change lifespan to random distrobution

    def __add__(self,mother):
        gender = True
        if ((numpy.random.binomial(1,bear.pmale)) == 0):
            gender = False
        
        #bearname = "cub_%s_%s" % (self.name, mother.name)
        bearname = str(bear.bearnum) + str(gender)
        newbear = bear(bearname,gender,True, self, mother)

        self.children.append(newbear)
        mother.children.append(newbear)
        
        self.beforerep = 5
        mother.beforerep = 5
        
        




    
def newyear():
    for everybear in bear.bearlist:
        if everybear.alive is True:
            everybear.age +=1
            everybear.beforerep = everybear.beforerep - 1
        



def mating():
    eligiblemales=[]
    eligiblefemales=[]
    for eachbear in bear.bearlist:
        if (eachbear.alive is True) and (eachbear.age >= eachbear.lifespan):
            eachbear.alive = False
            bear.bearpop -=1
        #####
        ##### IF A BEAR'S AGE IS EQUAL TO HIS LIFESPAN, IT DIES HERE AND POPULATION DECREASES BY 1
        #####            
    for eachbear in bear.bearlist:
        if (eachbear.ismale is True) and (eachbear.beforerep <= 0) and (eachbear.alive is True):
            eligiblemales.append(eachbear)
    for eachbear in bear.bearlist:
        if (eachbear.ismale is False) and (eachbear.beforerep <= 0) and (eachbear.alive is True):
            eligiblefemales.append(eachbear)

    for males in eligiblemales:
        try:
            num = random.randint(0,len(eligiblefemales))
            f = eligiblefemales[num]
            if (males.mother is not f.mother) or (males.father is not f.father) and (males.age - f.age <= 10):
                males + f
                #must remove the female now:
                del eligiblefemales[num]
        except: #when elibiblefemales is empty
            pass
        finally:
            pass
    newyear()


############Timing functions/initilization
def start():
    bear.bearlist = []
    bear.bearnum = 0
    bear.bearpop = 0
    Adam = bear("Adam",True,True,"m","d"); Eve = bear("Eve",False,True,"ms","dd"); Mary = bear("Mary",False,True,"msd","dgg");
def five():
    mating();mating();mating();mating();mating();
def twfive():
    five();five();five();five();five()
def hundfif():
    twfive();twfive();twfive();twfive();twfive();twfive()


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#ANSWERS TO THE QUESTIONS:
#
#
#
#
#
#

#a.)
    #I am defining a function(avgborn) that will look at the average number of
    #births over "sample" different bear populations

    #>>> avgborn(100,10)
    #1212.8


def avgborn(numberofyears,sample):
    total = 0.0
    for each in xrange(sample):
        
        start()
        for each in xrange(numberofyears):
            mating()
        total += bear.bearnum-3
    average = float(total)/sample
    return average











    #A modification of the program gives the number of bears alive at the end of
    # a number of years. Due to the ammount of time it was taking my computer to get
    #through 150 yrs, I used a sample = 4
##
##      >>> avgalive(150,4)
##      66060.5


def avgalive(numberofyears,sample):
    total = 0.0
    for each in xrange(sample):
        
        start()
        for each in xrange(numberofyears):
            mating()
            #print bear.bearpop
        total += bear.bearpop
    average = float(total)/sample
    return average
    










#B.)The program below takes the number of years a population needs to live, a given
#number of samples(over which to assess a probability) and the probability of a cub being a male
# it will count the number of times the population survives for the number of years. if the population survives
#atleast 90% of the time, it will let the use know
#otherwise, it will incrementally adjust the probability until the population survives atleast 90% of the time.
#finally it will return this probability

#e.g.

##>>> avgends(150,15,.2)
##with a 0.340000 probability for males, there's atleast a 10 percent chance the pop will make it 150yrs, sample size = 15


def avgends(numberofyears,sample,probmale):
    total = 0.0
    bear.pmale = probmale
    for each in xrange(sample):
        
        start()
        for each in xrange(numberofyears):
            mating()
            if bear.bearpop ==0:
                total += 1
                break
            
    average =  (float(total)/float(sample))
    
    if average <= .10:
       print "with a %f probability for males, there's atleast a 10 percent chance the pop will make it 150yrs, sample size = %i"\
             %(probmale, sample)
    else:
       newprob = float(probmale) + .01
       avgends(numberofyears,sample,newprob)







##########Graphing assume in: ipython -pylab, assume already began the bear population

def graph_indiv_history(bearnumber):
    mybear = bear.bearlist[bearnumber]
  
    bearhist = nx.Graph()
    bearstoconsider = [mybear]
    bearhist.add_node(mybear.name)  
    for each in bearstoconsider:
        print each.name
        try:
            bearhist.add_node(each.mother.name);
            bearhist.add_node(each.father.name);
            bearhist.add_edge(each.name, each.mother.name)
            bearhist.add_edge(each.name, each.father.name)
            bearstoconsider.append(each.mother)
            bearstoconsider.append(each.father)

            #for every in each.children:
            #    bearstoconsider.append(every)
        except:
            pass
        finally:
            pass   
    nx.draw(bearhist)

    


def graphing_entire_history():
    
 #   import matplotlib.pyplot as plt
    beargraph = nx.Graph()
    bear.bearlist.pop(0); bear.bearlist.pop(0); bear.bearlist.pop(0)
    for each in bear.bearlist:
        beargraph.add_node(each.name);
    for each in bear.bearlist:
        beargraph.add_edge(each.name, each.mother.name);
        beargraph.add_edge(each.name, each.father.name);
    nx.draw(beargraph)




































##
##
##Other useful functions:
##    
##
##def colony(years,prob_male):
##    start()
##    year = 0
##    for each in xrange(years):
##        mating()
##        year += 1
##        print "year %i: %i bears have lived in the colony, %i have died, %i are currently living" \
##              % (year, bear.bearnum, (bear.bearnum - bear.bearpop), bear.bearpop)
##
