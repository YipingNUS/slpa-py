#!/usr/bin/python

import numpy
#import slpa
import time
import random 

def main():
    """test slpa, randomly generate a graph

    Attributes:
        FILE_LOCATION: the location of the file to store the graph
        N: number of nodes in the graph
        LAMDA: I assume poisson distribution of the degrees of nodes.
               This is the lamda variable of the distribution        

        iteration: the number of iterations to run slpa
        threshhold: r => [0,1], if the probability is less than r,
                    remove it during post processing

    """
    FILE_LOCATION = 'input_graph.txt'
    N = 1000000  #total 1,000,000 nodes
    LAMDA = 200  #average degree set to 200

    ITERATION = 20
    THRESHHOLD = 0.1

    #perform poisson sampling
    start_time = time.time()
    
    f = open(FILE_LOCATION,"w+")

    f.write("%d\n" % N)  #write the number of nodes in first line
    f.write("%d\n" % LAMDA) #write lamda in second line

    degrees = numpy.random.poisson(LAMDA, N)

    for i in range(N):
        #generate an array of size degrees[i] of random integers
        if degrees[i] > N:
            degrees[i] = N 
        #neighbors = numpy.random.randint(N,size=degrees[i])
        neighbors = random.sample(range(N), degrees[i])
        f.write("%s\n" % ' '.join(str(neighbor) for neighbor in neighbors))
    # End of loop

    f.close()

    end_time = time.time()
    print("Elapsed time was %g seconds" % (end_time - start_time))
# End of main().

if __name__ == "__main__":
    main()
