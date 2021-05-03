import random
import math
import numpy as npy
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from numpy.random import rand
 
def simulated_annealing(sampleList,matrix):
    """Peforms simulated annealing to find a solution"""
    initial_temp = 10000
    final_temp = 1
    alpha = 1
    
    current_temp = initial_temp
 
    # Start by initializing the current state with the initial state
    current_list = sampleList
    solution = current_list
    nextList = []
    count = 1
 
    while current_temp > final_temp:
        #print(current_temp)
 
        nextList = solution.copy()
        bsolution = batching(solution)
 
        swap_random(nextList)
        bnextList = batching(nextList)
 
        # Check if neighbor is best so far
        distance_diff = get_distance_total(bsolution,matrix,True) - get_distance_total(bnextList,matrix,True)
        acceptance = math.exp(-distance_diff/current_temp)
        # if the new solution is better, accept it or accept it with a probability of e^(-cost/temp)
        if distance_diff > 0:
            solution = nextList
        elif acceptance < rand():
            solution = nextList
 
        # decrement the temperature
        current_temp -= alpha
        print("Temperature: ", current_temp, "Distance: ", distance_diff)
        count += 1
        print(count)
        
    return solution
 
def swap_random(seq):
    idx = range(len(seq))
    i1, i2 = random.sample(idx, 2)
    seq[i1], seq[i2] = seq[i2], seq[i1]
 
def batching(list):
    batchedList = []
    x = 0
    y = len(list)
    for i in range (x,y,5):
        x = i
        batchedList.append(list[x:x+5])
 
    batchedList2 = []
    blist = []
    for i in range(len(batchedList)):
        for j in batchedList[i]:
            if j not in blist:
                blist.append(j)
        batchedList2.append(blist)
        blist = []
 
    return batchedList2
        
 
def find(element, matrix):
    #find array index(coordinate [y,x]) for element(item)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                return (i, j)
 
def get_distance(coord1, coord2):
    #find horizontal(x) and vertical(y) distance between two elements
    x = 0
    y1 = clean_coord(coord1[0])
    y2 = clean_coord(coord2[0])
    y = abs(y2 - y1)
    if coord1[1] < 6 and coord2[1] < 6 :
        x = coord1[1] + coord2[1]
    elif coord1[1] >= 6 and coord2[1] >= 6 :
        x1 = 11 - coord1[1]
        x2 = 11 - coord2[1]
        x = x1 + x2
    else :
        if coord1[1] < 6:
            x1 = coord1[1]
        elif coord1[1] >= 6: 
            x1 = 11 - coord1[1]
        if coord2[1] < 6:
            x2 = coord2[1]
        elif coord2[1] >= 6:
            x2 = 11 - coord2[1] 
        if x1 < x2:
            x = x1 + (11 - x2)
        elif x2 < x1:
            x = x2 + (11 - x1)
        if x1 == x2:
            x = 0
    
    return (x,y)
 
def clean_coord(coord):
    #determine the location of 'x' for a certain number
    if coord == 1 or coord == 3:
        coord = 2
    elif coord == 4 or coord == 6:
        coord = 5
    elif coord == 7 or coord == 9:
        coord = 8
    elif coord == 10 or coord == 12:
        coord = 11
    elif coord == 13 or coord == 15:
        coord = 14
    return coord
 
def get_distance_total(elist,matrix,batch):
    total_distance = 0
    #if unbatched
    if batch == False:
        for i in range(len(elist)):
            c1 = (0,0)
            c2 = find(elist[i],whmatrix)
            d = get_distance(c1,c2)
            total_distance += (d[0]+d[1])
 
    #batched list
    else:
        for i in range(len(elist)):
            for j in range(len(elist[i])):
                if j == 0:
                    c1 = (0,0)
                    c2 = find(elist[i][j],whmatrix)
                    d = get_distance(c1,c2)
                    total_distance += (d[0]+d[1])
                else:
                    c1 = c2
                    c2 = find(elist[i][j],whmatrix)
                    d = get_distance(c1,c2)
                    total_distance += (d[0]+d[1])
 
    return total_distance
 
if __name__ == '__main__':
    whmatrix = [['x','x','x','x','x','x','x','x','x','x','x','x'],#0
        ['x','1','2','3','4','5','6','7','8','9','10','x'],#1
        ['x','x','x','x','x','x','x','x','x','x','x','x'],#2
        ['x','20','19','18','17','16','15','14','13','12','11','x'],#3
        ['x','21','22','23','24','25','26','27','28','29','30','x'],#4
        ['x','x','x','x','x','x','x','x','x','x','x','x'],#5
        ['x','40','39','38','37','36','35','34','33','32','31','x'],#6
        ['x','41','42','43','44','45','46','47','48','49','50','x'],#7
        ['x','x','x','x','x','x','x','x','x','x','x','x'],#8
        ['x','60','59','58','57','56','55','54','53','52','51','x'],#9
        ['x','61','62','63','64','65','66','67','68','69','70','x'],#10
        ['x','x','x','x','x','x','x','x','x','x','x','x'],#11
        ['x','80','79','78','77','76','75','74','73','72','71','x'],#12
        ['x','81','82','83','84','85','86','87','88','89','90','x'],#13
        ['x','x','x','x','x','x','x','x','x','x','x','x'],#14
        ['x','100','99','98','97','96','95','94','93','92','91','x'],#15
        ['x','x','x','x','x','x','x','x','x','x','x','x']]#16
 
    sampleList100 = ['80', '54', '68', '54', '99', '52', '1', '76', '1', '18', '79', '38', '46', '27', '41', '58', '77', '59', '99', '49', '67', '91', '96', '81', '63', '12', '30', '10', '74', '88', '51', '100', '40', '87', '23', '40', '99', '73', '49', '11', '10', '22', '80', '11', '51', '46', '19', '41', '6', '13', '42', '69', '96', '80', '2', '71', '55', '55', '97', '89', '21', '18', '66', '64', '27', '73', '91', '93', '20', '27', '6', '72', '7', '61', '82', '39', '58', '36', '39', '33', '26', '91', '43', '74', '74', '95', '34', '73', '8', '10', '34', '54', '89', '36', '65', '44', '52', '73', '84', '95']
    sampleList20 = sampleList100[:20]
    sampleList50 = sampleList100[:50]
    # generate list with random numbers
    # for i in range(0,100):
    #     n = random.randint(1,100)
    #     sampleList.append(str(n))
    # print(sampleList)
 
    # p1 = random.randrange(1,100)
    # p2 = random.randrange(1,100)
    # c1 = find(str(p1),whmatrix)
    # c2 = find(str(p2),whmatrix)
    
    # d = get_distance(c1,c2)
    # print (p1," and ",p2)
    # print(d)
    # print("distance = ",d[0] + d[1])
    
    batchedList = batching(sampleList100)
    batchedList20 = batching(sampleList20)
    batchedList50 = batching(sampleList50)
 
    #sort list order by asc then batch
    ascList = list(set(sampleList100))
    ascList = [int(i) for i in ascList]
    ascList.sort(reverse=False)
    ascList = [str(i) for i in ascList]
    ascList = batching(ascList)
 
    ascList20 = list(set(sampleList20))
    ascList20 = [int(i) for i in ascList20]
    ascList20.sort(reverse=False)
    ascList20 = [str(i) for i in ascList20]
    ascList20 = batching(ascList20)
 
    ascList50 = list(set(sampleList50))
    ascList50 = [int(i) for i in ascList50]
    ascList50.sort(reverse=False)
    ascList50 = [str(i) for i in ascList50]
    ascList50 = batching(ascList50)
 
    simAnneal100 = simulated_annealing(sampleList100,whmatrix)
    simAnneal100 = batching(simAnneal100)
    simAnneal50 = simulated_annealing(sampleList50,whmatrix)
    simAnneal50 = batching(simAnneal50)
    simAnneal20 = simulated_annealing(sampleList20,whmatrix)
    simAnneal20 = batching(simAnneal20)
 
    t1_100 = get_distance_total(sampleList100,whmatrix,False)
    t1_20 = get_distance_total(sampleList20,whmatrix,False)
    t1_50 = get_distance_total(sampleList50,whmatrix,False)
    t2_100 = get_distance_total(batchedList,whmatrix,True)
    t2_20 = get_distance_total(batchedList20,whmatrix,True)
    t2_50 = get_distance_total(batchedList50,whmatrix,True)
    t3_100 = get_distance_total(ascList,whmatrix,True)
    t3_20 = get_distance_total(ascList20,whmatrix,True)
    t3_50 = get_distance_total(ascList50,whmatrix,True)
    t4_100 = get_distance_total(simAnneal100,whmatrix,True)
    t4_20 = get_distance_total(simAnneal20,whmatrix,True)
    t4_50 = get_distance_total(simAnneal50,whmatrix,True)
 
    plt.figure(1)
    objects = ('Unbatched','Batched FCFS','Simulated Annealing','Sort Batched')
    y_pos = npy.arange(len(objects))
    performance = [t1_100,t2_100,t4_100,t3_100]
 
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(fontsize=8)
    plt.ylabel('Distance')
    plt.title('Difference between Lists for 100 objects')
 
    plt.figure(2)
    X = ['Unbatched','Batched FCFS','Simulated Annealing','Sort Batched']
    a = [t1_20,t2_20,t4_20,t3_20]
    b = [t1_50,t2_50,t4_50,t3_50]
    c = [t1_100,t2_100,t4_100,t3_100]
    
    X_axis = npy.arange(len(X))
    
    plt.bar(X_axis - 0.2, a, 0.2, label = '20')
    plt.bar(X_axis , b, 0.2, label = '50')
    plt.bar(X_axis + 0.2, c, 0.2, label = '100')
    
    plt.xticks(X_axis, X)
    plt.xticks(fontsize=8)
    plt.xlabel("Batching Method")
    plt.ylabel("Distance")
    plt.title("Overall Comparison of Batching Methods with Different List Size ")
    plt.legend(title = "List Size")
    plt.show()
    
    print("Performance Comparison for List of 100:\n","Unbatched|\t", "Batched FCFS|\t", "Simulated Annealing|\t", "Sort Batched|\n", t1_100, "m\t\t",t2_100,"m\t\t",t4_100,"m\t\t\t",t3_100, "m\n" )
    print("Overview:")
    print("Distance for list of 20:\n","Unbatched|\t", "Batched FCFS|\t", "Simulated Annealing|\t", "Sort Batched|\n", t1_20, "m\t\t",t2_20,"m\t\t",t4_20,"m\t\t\t",t3_20, "m\n"  )
    print("Distance for list of 50:\n","Unbatched|\t", "Batched FCFS|\t", "Simulated Annealing|\t", "Sort Batched|\n", t1_50, "m\t\t",t2_50,"m\t\t",t4_50,"m\t\t\t",t3_50, "m\n"  )
    print("Distance for list of 100:\n","Unbatched|\t", "Batched FCFS|\t", "Simulated Annealing|\t", "Sort Batched|\n", t1_100, "m\t\t",t2_100,"m\t\t",t4_100,"m\t\t\t",t3_100, "m"  )
