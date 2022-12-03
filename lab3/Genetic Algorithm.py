import random

class GeneticAlgoForTPS():
    def __init__(self,k,T,players,playersRuns,population):
        self.predictedRun=int(T)
        self.numberOfPlayers=int(k)
        self.players=players
        self.playersRuns=playersRuns
        self.population=population
        self.offSprings=[]
        self.newOffSpring=[]
        self.iteration=0
        
    def offSpringCromosomeCreator(self):
        if 1<=self.predictedRun or self.predictedRun<=1000 or 1<=self.numberOfPlayers or self.numberOfPlayers<=18:
            for j in range(len(self.population)):
                total_run=0
                count=0
                for i in self.population[j]:
                    if i=="0":
                        pass
                    else:
                        z=self.players[count]
                        total_run=total_run+ int(self.playersRuns[z])
                    count+=1
                if total_run==self.predictedRun:
                    print(self.players)
                    print(self.population[j])
                    return
                elif abs(total_run-int(T))<=10:
                    self.offSprings.append(self.population[j])
            self.singlePointCrossOver()
    

    def singlePointCrossOver(self):
        self.newOffSpring=[]
        rand=random.randint(0,self.numberOfPlayers-1)      #random index
        for i in range(len(self.offSprings)-1):
            #i=0
            old1=self.offSprings[i] #10111010
            for j in range(i+1,len(self.offSprings),1): 

                old2=self.offSprings[j] #11001111
                temp=old1[rand]  #0
                temp1=old2[rand]#1
                new1=old1[0:rand]+temp1+old1[rand+1:self.numberOfPlayers]
                new2=old2[0:rand]+temp+old2[rand+1:self.numberOfPlayers]
                self.newOffSpring.append(new1)
                self.newOffSpring.append(new2)
                
        self.offSprings=self.newOffSpring + self.population
        self.mutation()


    def mutation(self):
        a=[]
        rand=random.randint(0,self.numberOfPlayers-1)  #random index
        for i in self.offSprings:
            if i[rand]=="0":
                new=i[0:rand]+"1"+i[rand+1:self.numberOfPlayers]
            else:
                new=i[0:rand]+"0"+i[rand+1:self.numberOfPlayers]
            a.append(new)
        self.offSprings=self.offSprings+ a
        self.fitnessChecker()

    def fitnessChecker(self):
        a=True
        self.iteration+=1
        for j in range(len(self.offSprings)):
            total_run=0
            count=0
            for i in self.offSprings[j]:
                if i=="0":
                    pass
                else:
                    z=self.players[count]
                    total_run=total_run+ int(self.playersRuns[z])
                    count+=1
            if total_run==self.predictedRun:
                print(self.players)
                print(self.offSprings[j])
                a=False
                break
        if a:
            if self.iteration==2:
                  print(self.players)
                  print(-1)
            else:
                self.singlePointCrossOver()

    





f=open('input.txt','r')
x=f.read().split("\n")
players=[]
playersRuns={} 
for i in range(len(x)):
    y=x[i].split(" ")
    if i==0:
        k=y[0] #8
        T=y[1] #330
    else:
        players.append(y[0])
        playersRuns[y[0]]=y[1]
     
population=[]
for i in range(pow(2,int(k))):
    x=""
    for j in range(int(k)):
        x+=str(random.randint(0,1))
    if x not in population:
        population.append(x)

firstPrediction=GeneticAlgoForTPS(k,T,players,playersRuns,population)
firstPrediction.offSpringCromosomeCreator()



