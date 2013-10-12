#!/usr/bin/env python
import numpy

class Slpa:
    """Identify overlapping nodes and overlapping communities in social networks

    Attributes:
       N: number of nodes
       ITERATION: number of iterations
       THRESHHOLD: r => [0,1], if the probability is less than r,
                   remove it during post processing

       adjacency_list: int[N][K] for each node a list of its neighbours' id
       node_labels: [int]{id:count} first dimension is a list of all nodes
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
        
        self.N = int(lines.pop().strip()) 
        self.LAMDA = int(lines.pop().strip())  
 
        self.adjacency_list = []

        for line in lines:
            # get all the neighbors of the current node
            self.adjacency_list.append([int(i) for i in line.strip().split(" ")])     
        
    #end of __init__ 

    def perform_slpa(self, ITERATION):
        """Performs SLPA algorithm 
        
        Args:
            TERATION: number of iterations
        """
        self.ITERATION = ITERATION

        for i in range(self.ITERATION):
            for m in range(len(topic_assign)):  #for each document
                for n in range(len(topic_assign[m])):  #for each word
                    #decrement counts and sums
                    old_topic = topic_assign[m][n]
                    count_doc_topic[m][old_topic] -= 1
                    word_sum_topic[old_topic] -= 1
                    count_term_topic[document[m][n]][old_topic] -= 1

                    #perform full conditional inference
                    new_topic = sample_full_conditional(m,n)
                    topic_assign[m][n] = new_topic

                    count_doc_topic[m][new_topic] += 1
                    word_sum_topic[new_topic] += 1
                    count_term_topic[document[m][n]][new_topic] += 1
            
            #TODO: if converged and L sampling iterations since last read out then read out parameters        
    #end of gibbs_sampling

    def initialize_state(self):
        """ Initialisation: assignment topics to words, increment counts
           
        """
        for m in range(len(topic_assign)):  #for each document
            for n in range(len(topic_assign[m])):  #for each word
                # sample topic for the current word
                topic = numpy.random.multinomial(100,[1/K.]*K).argmax()
                topic_assign[m][n] = topic
                #increment counts
                count_doc_topic[m][topic] += 1
	        word_sum_topic[topic] += 1
                count_term_topic[document[m][n]][topic] += 1	

    #end of initialize_state

    def post_processing(self, THRESHHOLD):
        """performs post processing to remove the labels that are below the threshhold
           
        Args:
	    THRESHHOLD: r => [0,1], if the probability is less than r,
                        remove it during post processing
        """
        self.THRESHHOLD = THRESHHOLD
    #end of post_processing
    
 
#end of Slpa class
