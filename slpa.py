#!/usr/bin/env python
import numpy

class Slpa:
    """Identify overlapping nodes and overlapping communities in social networks

    Attributes:
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
        self.documents = documents
        self.V = V
    #end of __init__ 

    def configure(self, iteration):
        """Set parameters for tuning

        Args:
            iteration: int; maximum number of iterations of Gibbs sampling
            TODO: more parameters
        """
        self.iteration = iteration
    #end of configure

    def inference_gibbs_sampling(self, K, alpha, beta):
        """Performs Gibbs Sampling 
           
           Select initial state ? Repeat a large number of times: 
               1. Select an element 
               2. Update conditional on other elements. 
        
        Args:
            K: int. # of topics
            alpha: float. symmetric prior parameter on document--topic associations
            beta: symmetric prior parameter on topic--term associations

        Refer to pseudo code in figure 9
        """
        self.K = K
        self.alpha = [alpha] * K
        self.beta = [beta] * V

        #initialize the state of the Markov chain
        self.initialize_state()

        for i in range(self.iteration):
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
 
    def sample_full_conditional(m, n)
        """calculate the full conditional distribution for a word token with index i=(m,n)

        Args:
            m: m(th) document
            n: n(th) word

        Refer to formula (78) in paper
        """
        pseudo_prob_topic_dist = (count_term_topic[:, documents[m][n]] + 

        

    #end of sample_full_conditional

    def get_theta   
        """calculated theta based on document_topic and alpha
        refer to formula (82)
        """
    #end of get_theta

    def get_phi
        """calculated phi based on word_topic and beta
        refer to formula (81)
        """        
    #end of get_phi

    

#end of LdaGibbsSampler class
