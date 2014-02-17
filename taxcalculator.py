'''Small Calculator for Canadians to calculate their income tax in 2014'''
import os

federal_tax_buckets = [(43953, 0.15), (43954, 0.22), (48363, 0.26)]
federal_tax_max = 0.29
ontario_tax_buckets = [(40120, 0.0505), (20122, 0.0915), (433848, 0.1116)]
ontario_tax_max = 0.1316

def compute_tax(income, bucket, tax_max):
	total_tax = 0.0
	counted_income = income
	bucket_index = 0
	while True:
		if bucket_index == len(bucket):
			total_tax += counted_income * tax_max
			break;
		if bucket[bucket_index][0] > counted_income:
			total_tax += counted_income * bucket[bucket_index][1]
			break;
		counted_income -= bucket[bucket_index][0]
		total_tax += bucket[bucket_index][0] * bucket[bucket_index][1]
		bucket_index += 1

	return total_tax

print "please enter your annual income: "
income = float(raw_input().strip())
federal_tax = compute_tax(income, federal_tax_buckets, federal_tax_max)
ontario_tax = compute_tax(income, ontario_tax_buckets, ontario_tax_max)
total_tax = federal_tax + ontario_tax
print "Your 2014 income tax would be:"
print "  Federal Tax --- $"+str(federal_tax)
print "  Ontario Tax --- $"+str(ontario_tax)
print "  Total --------- $"+str(total_tax)
print ""
print "That means your pre-tax monthly income is: " + str(income/12.0)
print "That means your after-tax monthly income is: " + str((income-total_tax)/12.0)






	
