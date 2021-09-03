#!/usr/bin/env python


file="./Mus_musculus.GRCm39.dna.primary_assembly.ens104.STAR_2.7.9a1Aligned.out.sam"


#I want this python program to open a sam file and then look at every line, 
#then tell me if the bitwise is flag & 4 !=true 


#usr/bin/time -v 

unmapped_count=0
mapped_count=0

i=0
with open (file, "r") as fh:
    for line in fh:
        if line.startswith("@")==False:
            line=line.strip('\n').split("\t")
            flag=int(line[1])
            i+=1
            if((flag & 4) != 4) and ((flag & 256) !=256):
                #print("mapped",flag)
                mapped_count+=1
            elif ((flag & 256) !=256):
                unmapped_count+=1
#            if i==500:
#                break 
#print("loop broken")
print("mapped read total",mapped_count)
print("unmapped read total",unmapped_count)






