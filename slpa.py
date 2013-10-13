#!/usr/bin/env python
'''
Created on Oct 12, 2013

@author: yiping
'''

import numpy as np
import time

class Slpa:
    """Identify overlapping nodes and overlapping communities in social networks

    Attributes:
       N: number of nodes
       ITERATION: number of iterations
       THRESHHOLD: r => [0,1], if the probability is less than r,
                   remove it during post processing

       adjacency_list: int[N][K] for each node a list of its neighbours' id
       node_memory: [int]{id:count} first dimension is a list of all nodes
                    for each node we have a dictionary keeping the count 
                    of the labels it received 
        
    """    
 
    def __init__(self, input_file):
        """Initialize the instance with input data

        create adjacency_list after reading the input file

        Args:
            input_file: the file path to the input file
                        The file 
        """
        f = open(input_file, "r")
        lines = f.readlines()
        
        self.N = int(lines.pop(0).strip()) 
        self.LAMDA = int(lines.pop(0).strip())  

        print "N=%d" % self.N
        print "LAMDA=%d" % self.LAMDA
 
        self.adjacency_list = []
        self.node_memory = []        

        for line in lines:
            # get all the neighbors of the current node
            self.adjacency_list.append([int(i) for i in line.strip().split(" ")])

        print "self.adjacency_list has length %d" % len(self.adjacency_list)

        for i in range(self.N):     
            self.node_memory.append({i:1})  #append a dictionary containing single entry to node_memory

        print "self.node_memory has length %d" % len(self.node_memory)

    #end of __init__ 


    def perform_slpa(self, ITERATION):
        """Performs SLPA algorithm 
        
        Use multinomial sampling for speaker rule
        Use maximum vote for listener rule
        Args:
            TERATION: number of iterations
        """
        self.ITERATION = ITERATION

        for t in range(self.ITERATION):
              
            print "Performing %dth iteration" % t

            order = np.random.permutation(self.N)  # Nodes.ShuffleOrder()
            for i in order:  #for each node
                label_list = {}

                for j in self.adjacency_list[i]:  #for each neighbor of the listener
                    # select a label to propagate from speaker j to listener i
                    sum_label = sum(self.node_memory[j].itervalues())
                    label = self.node_memory[j].keys()[np.random.multinomial(1,[float(c)/sum_label for c in self.node_memory[j].values()]).argmax()]
                    if label not in label_list:
                        label_list[label] = 1
                    else:
			label_list[label] += 1
                
                #listener chose a received label to add to memory
                selected_label = max(label_list, key=label_list.get)
                #add the selected label to the memory
                if selected_label in self.node_memory[i]:
                    self.node_memory[i][selected_label] += 1
                else:
                    self.node_memory[i][selected_label] = 1
                                
    #end of perform_slpa

    def post_processing(self, THRESHHOLD):
        """performs post processing to remove the labels that are below the threshhold
           
        Args:
	    THRESHHOLD: r => [0,1], if the probability is less than r,
                        remove it during post processing
        """
        self.THRESHHOLD = THRESHHOLD
    #end of post_processing
    
 
#end of Slpa class

def main():
    slpa = Slpa("input_graph.txt")

    start_time = time.time()

    slpa.perform_slpa(20)  #perform slpa for 20 iterations

    end_time = time.time()
    print("Elapsed time for slpa was %g seconds" % (end_time - start_time))

    for mem in slpa.node_memory:
        print str(mem)
#end of main().

if __name__ == "__main__":
    main()

