"""This script translates all the community* files to format compatable for NMI

This script assume index starts from 0 and the numbering is continous
"""
import sys
import os

for filename in os.listdir("./"):  #list current dir
    if filename.startswith("community"):  #this is a gold standard file
        f = open(filename, "r")
        lines = f.readlines()
        f.close()
        
        community_list = []
        for i in range(len(lines)):
            community_list.append([])  #append empty list to the members
        for line in lines:
            components = line.strip().split("\t")
            if len(components) == 2:
                node = components[0]
                communities = [int(item) for item in components[1].split(" ")]
                for community in communities:
                    if community > len(community_list):
                        print ("%d --- %d".format(community, len(community_list)))
                    community_list[community].append(node) 

        f_out = open(filename.replace(".dat", ".out"), "w+")

        for community in community_list:
            if len(community) > 0:
                f_out.write(" ".join(community))
                f_out.write("\n")
        f.close()
                

