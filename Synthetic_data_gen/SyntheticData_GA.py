import numpy as np
import random
import math
import pandas as pd
import matplotlib.pyplot as plt

#elements will contain value of bitcoin trade data
Number_of_elements_in_gen=30
Data=pd.read_csv("Bitcoin_Data.csv")
#downloading sample data over the last three months
#30 random values shall be sampled over the dataset obtained to make an interval of one month

Data=Data['Price'].tolist() # Add code to generate list from excel file using pandas here

#removing the commas in the list to enable conversion of string to int
count=0
for element in Data:
    element=element.replace(',',"")
    element=float(element)
    Data[count]=element
    count+=1

##function for creating a base generation here
##Base gen will contain 500 parent datasets only for now
def MakeParentSet(Base_Generation):
    Base_Generation=random.sample(Data,Number_of_elements_in_gen)
    #print(Base_Generation)
    return Base_Generation

#decide what the fitness factor will be      
def Find_Fitness_factor(Generation):
    Fitness_factors=[]
    #print(max(Generation))
    maximum=round(max(Generation))
    minimum=round(min(Generation))
    ##can generate a range of values we and process data based on this
    #creating range set using max and min values
    range_list=[]
    for i in range (minimum,maximum+1,25):       #will work if our data is spread out over a large range of integers
        range_list.append(i)
    set_range_counts= pd.cut(Generation, range_list).value_counts()    ###set the ranges properly based on data
    set_range_counts=set_range_counts.tolist()
    Fitness_factors=set_range_counts
    #fitness factor will be the number of occurances of the range of values based on previous data
    if(len(range_list)!=(len(Fitness_factors))):
        Fitness_factors.append(1)
    return (range_list,Fitness_factors)

#use the fitness fators to create new generation
def Make_new_Generation(Previous_Generation):
    (range_list,Fitness_factors)=Find_Fitness_factor(Previous_Generation)
    Dominant_element = range_list[Fitness_factors.index(max(Fitness_factors))]
    New_gen=random.choices(range_list, weights=Fitness_factors, k=Number_of_elements_in_gen-2)
    for i in range(2):
        New_gen.append(Dominant_element)
    #5 elements are being carried forward from prevous generation as they were dominant
    #This new gen is not continuous. So, we will have to make it nearly continuous

    #considering_mutation
    maximum=round(max(Previous_Generation))
    minimum=round(min(Previous_Generation))
    mutation_value=Consider_mutation(maximum,minimum)
    random_pos=np.random.randint(0,30)
    New_gen[random_pos]=mutation_value

    return New_gen

def Consider_mutation(maximum,minimum):
    mutation_value=np.random.randint(minimum,maximum)
    return mutation_value

def Make_Gaussian_distribution(Generation):
    Generation.sort()
    print(Generation)
    j=0
    Gauss_Gen=[]
    for i in (Generation):
        if(j%2==0):
            Gauss_Gen.append(i)
        j+=1
    for i in reversed(Generation):
        if(j%2==0):
            Gauss_Gen.append(i)
        j+=1
    #print(Gauss_Gen)
    return(Gauss_Gen)

def Make_next_month_dates():
    September=[]
    for i in range(30):
        September.append(str(i))
    return September

def Plot_Graph(month,Next_gen):
    plt.plot(month,Next_gen)
    # naming the x axis
    plt.xlabel('Dates')
    # naming the y axis
    plt.ylabel('Values')
    plt.show()

def Main():
    Base_Generation=[]      #creating empty list

    #creating the first generation of elements
    Base_Generation=MakeParentSet(Base_Generation)
    print("Base Gen: ", end=" ")
    print(Base_Generation)

    Next_gen=Make_new_Generation(Base_Generation)
    print("Next Gen: ", end=" ")
    print(Next_gen)
    
    September=Make_next_month_dates()
    Plot_Graph(September,Next_gen)

    Next_gen_Gauss=Make_Gaussian_distribution(Next_gen)
    #print(Next_gen)

    Plot_Graph(September,Next_gen_Gauss)
    
    

if __name__=='__main__':
    Main()

   



