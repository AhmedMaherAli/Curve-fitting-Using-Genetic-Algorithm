import random
from individual import Individual
import matplotlib.pyplot as plt

POP_SIZE = 30
GEN_MAX = 1500



def produce_starting_population(c,size):
    return [Individual(c) for _ in range(size)]

def mutate(indi,cur_generation,max_generation):
    
    for i in range(0,len(indi.values),1):
        gen=indi.values[i]
        r1=random.uniform(-2,2)
        if r1<=0.5:
            v=gen-2
        else:
            v=gen-2
        v0=((1-cur_generation)/max_generation)
        r2=(random.uniform(0,1)) ** v0
        

        indi.values[i]=v*(1-r2)

def fitness(individual, points):
    fit = 0

    for point in points:
        x=point.x
        actual_y=point.y
        calculated_y = 0

        power=0
        for coefficient in individual.values:
            # For each coefficient
            calculated_y += (coefficient * (x ** power))
            power+=1
        mse = (actual_y  - calculated_y ) ** 2
        fit += mse

    fit/=len(individual.values)
    return fit



def Reproduction(pop,cur_generation,max_generation,equation_degre,points):
    iniParentsProb = 0.2                                #number of parents will be initialy taken from the population
    mutation_chance = 0.08
    parent_lottery = 0.05

    parent_length = int(iniParentsProb*len(pop))
    parents = []                       #de 34an a3ml elitism b copy el best chrosomes
    nonparents = []

    for i in range(0,parent_length,1):
        parents.append(pop[i])

    for i in range(parent_length,len(pop),1):
        nonparents.append(pop[i])
        
    for np in nonparents:           #34an admn el diversity w keda
        if parent_lottery > random.random():
            parents.append(np)

    for p in parents:
        if mutation_chance > random.random():
            mutate(p,cur_generation,max_generation)
        p.fit=fitness(p,points)

    children = []
    desired_length = len(pop) - len(parents)
    
    while len(children) < desired_length :
        
        male = pop[random.randint(0,len(parents)-1)]
        
        female = pop[random.randint(0,len(parents)-1)]        
        
        crossOverPoint=random.randint(0,len(pop[0].values)-1)
        
        child=Individual(equation_degre)
        for i in range (0,crossOverPoint,1):
            child.values[i]=male.values[i]
        for i in range(crossOverPoint,len(child.values),1):
            child.values[i]=female.values[i]     # hena el arkam 0/1 bs fa echta m4 m7tag order1 crossover w keda nos mn hena 3la nos mn hena
        
        if mutation_chance > random.random():
            mutate(child,cur_generation,max_generation)
        child.fit=fitness(child,points)
        children.append(child)

    parents.extend(children)        #extend m4 append 34an dol 2 lists w keda
    return parents

class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y


def main():
    f=open("G:\\Genetics\\Assignment 2\\Assignment 2\\input-2.txt", "r")
    i=1
    if f.mode=="r":
            
        testCases=int(f.readline())
        print(testCases)
        print()
        for T in range(1,testCases+1,1):
            POINTS=[]

            line = f.readline()
            l = line.rstrip('\n').split(' ')

            number_of_point=int(l[0])
            equation_degre=int(l[1])
            print(number_of_point)
            print(equation_degre)
            print()
            for i in range(0,number_of_point):
                line=f.readline()
                l=line.rstrip('\n').split(' ')
                x=float(l[0])
                y=float(l[1])
                print(x,y)
                POINTS.append(Point(x,y))
            
            population = produce_starting_population(equation_degre,POP_SIZE)
            
            for i in range(0,len(population),1):
                population[i].fit=fitness(population[i],POINTS)
           
            
            for g in range(0,GEN_MAX):                
                population = sorted(population, key=lambda x: fitness(x,POINTS))
                population = Reproduction(population,g,GEN_MAX,equation_degre,POINTS)

            
            xs=[p.x for p in POINTS]
            ys=[p.y for p in POINTS]
            yps=[]
            v=0
            for p in POINTS:
                power=0
                for cof in population[0].values:
                    v+=(cof*(p.x ** power))
                    power+=1
                
                yps.append(v)
            
            
            plt.plot(xs,ys,color='blue')
            plt.show()
            plt.plot(xs,yps,color='red')
            plt.show()
            print(population[0].fit)
            print(population[0].values)
            
            
            
            
            
            
            
if __name__ == "__main__":
    main()
