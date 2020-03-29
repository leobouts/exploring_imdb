import csv


def generateNextRowOfRatings():

	with open('imdbData/title.ratings.tsv') as ratings:
		
		reader = csv.reader(ratings, delimiter='\t')

		for row in reader:
			yield row


def generateNextRowOfBasics():

	with open('imdbData/title.basics.tsv') as basics:

		reader = csv.reader(basics, delimiter='\t')

		for row in reader:
			yield row



def main():

	generatorForRatings = generateNextRowOfRatings()
	generatorForBasics = generateNextRowOfBasics()

	#skip headers

	ratings_row = next(generatorForRatings)
	basics_row = next(generatorForBasics)

	#get first values
	
	ratings_row = next(generatorForRatings)
	basics_row = next(generatorForBasics)

	while True:
		try:

			if(ratings_row[0]==basics_row[0]):
				ratings_row = next(generatorForRatings)
			else:
				print(basics_row[2])
			
			basics_row = next(generatorForBasics)

		except StopIteration:
			break


  

if __name__== "__main__":
  main()