#!/usr/bin/python
#k = dom, m = het, n = rec
#Return probability that offspring is dom or het
#easier to do 1 minus the probability offspring is rec
dom = float(raw_input("k = "))
het = float(raw_input("m = "))
rec = float(raw_input("n = "))

total = dom + het + rec

#prob two recessive mate
rec_rec = (rec/total) * ((rec - 1)/(total - 1))
#prob two heterozygous mate
het_het = (het/total) * ((het - 1)/(total - 1))
#prob one recessive and one heterozygous mate
het_rec = (het/total) * (rec/(total - 1)) + (rec/total * (het/(total - 1)))

#probability offspring is recessive is the sum of probability of each possiblity 
prob = rec_rec + (het_het * 1/4) + (het_rec * 1/2)
print "The probability an offspring has a dominant allele is %s" % (1 - prob)