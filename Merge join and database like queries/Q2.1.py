import csv
import time
from operator import itemgetter

reader = csv.reader(open("imdbData/title.ratings.tsv"), delimiter="\t")


rating_0 = 0
rating_1 = 0
rating_2 = 0
rating_3 = 0
rating_4 = 0
rating_5 = 0
rating_6 = 0
rating_7 = 0
rating_8 = 0
rating_9 = 0

listOf0 = []
listOf1 = []
listOf2 = []
listOf3 = []
listOf4 = []
listOf5 = []
listOf6 = []
listOf7 = []
listOf8 = []
listOf9 = []

first_line = True

#starting time for  sorting
start_time = time.time()
sorted_file = sorted(reader, key=itemgetter(1),reverse=True)

for line in sorted_file:
	#skip header
	if first_line:
		first_line = False
		continue

	avg_rating = float(line[1])

	if(avg_rating<=1):
		rating_0 +=1
	elif(avg_rating<=2):
		rating_1 +=1
	elif(avg_rating<=3):
		rating_2 +=1
	elif(avg_rating<=4):
		rating_3 +=1
	elif(avg_rating<=5):
		rating_4 +=1
	elif(avg_rating<=6):
		rating_5 +=1
	elif(avg_rating<=7):
		rating_6 +=1
	elif(avg_rating<=8):
		rating_7 +=1
	elif(avg_rating<=9):
		rating_8 +=1
	else:
		rating_9 +=1

time_sorted = time.time() - start_time



print('0.1-1.0:',rating_0)
print('1.1-2.0:',rating_1)
print('2.1-3.0:',rating_2)
print('3.1-4.0:',rating_3)
print('4.1-5.0:',rating_4)
print('5.1-6.0:',rating_5)
print('6.1-7.0:',rating_6)
print('7.1-8.0:',rating_7)
print('8.1-9.0:',rating_8)
print('9.1-10.0:',rating_9)
print('time in seconds for sorting and counting:',time_sorted)


#re-read file

reader = csv.reader(open("imdbData/title.ratings.tsv"), delimiter="\t")

#skip header again
first_line = True

start_time = time.time()

#reader is not sorted
for line in reader:
	
	#skip header
	if first_line:
		first_line = False
		continue

	avg_rating = float(line[1])

	if(avg_rating<=1):
		listOf0.append(line)
	elif(avg_rating<=2):
		listOf1.append(line)
	elif(avg_rating<=3):
		listOf2.append(line)
	elif(avg_rating<=4):
		listOf3.append(line)
	elif(avg_rating<=5):
		listOf4.append(line)
	elif(avg_rating<=6):
		listOf5.append(line)
	elif(avg_rating<=7):
		listOf6.append(line)
	elif(avg_rating<=8):
		listOf7.append(line)
	elif(avg_rating<=9):
		listOf8.append(line)
	else:
		listOf9.append(line)


print('0.1-1.0:',len(listOf0))
print('1.1-2.0:',len(listOf1))
print('2.1-3.0:',len(listOf2))
print('3.1-4.0:',len(listOf3))
print('4.1-5.0:',len(listOf4))
print('5.1-6.0:',len(listOf5))
print('6.1-7.0:',len(listOf6))
print('7.1-8.0:',len(listOf7))
print('8.1-9.0:',len(listOf8))
print('9.1-10.0:',len(listOf9))

time_hashed = time.time() - start_time

print('time in seconds for bucketing the unsorted and getting the length:',time_hashed)



    