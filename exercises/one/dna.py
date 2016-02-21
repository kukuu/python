#A geneticist needs your help identifying if 
#a dna sequence exists in a larger strand of dna.
# A DNA sequence consists of a sequence of A, T, G, and Cs.
 #write a program that takes a DNA sequence from the user and
 # confirms ‘Found’ or ‘Not Found’ depending on whether the input is
  #contained in the target DNA strand. Use dna.py

#DNA strand: ATTGCGCCTTATGCTTAACC

#As a challenge extend this program to check that the input is
#correct.

DNASTRAND = "ATTGCGCCTTATGCTTAACC"
DNASTRAND = str(DNASTRAND)

#do a validation check on the length

#length = len(DNASTRAND)
#for char in DNASTRAND
   # if char not in 'ATGC'
        #print('Hi your DNA is a valid one') 


DNASTRAND = input("Please enter your DNA sequence :")

if  not 'A' in DNASTRAND or 'T' in DNASTRAND or 'G' in DNASTRAND:
	print('Please enter a valid sequence')

if   'A' in DNASTRAND or 'T' in DNASTRAND or 'G' in DNASTRAND:
	print('Hi your DNA is a valid one')

