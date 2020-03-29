import csv


def generateNextRowOfCrew():

	with open('imdbData/title.crew.tsv') as crew:
		
		reader = csv.reader(crew, delimiter='\t')

		for row in reader:
			yield row


def generateNextRowOfBasics():

	with open('imdbData/title.basics.tsv') as basics:

		reader = csv.reader(basics, delimiter='\t')

		for row in reader:
			yield row



def main():

	generatorForDirectors = generateNextRowOfCrew()
	generatorForBasics = generateNextRowOfBasics()


	#skip headers
	directors_row = next(generatorForDirectors)
	basics_row = next(generatorForBasics)

	f = open('output1.1.txt', 'a')
	f.write('primaryTitle\tDirectors\n')

	while True:
		try:

			# Get next value from Generator objects

			directors_row = next(generatorForDirectors)
			basics_row = next(generatorForBasics)

			print(directors_row)
			print(basics_row)


			list_of_directors = directors_row[1].split(",")

			if(len(list_of_directors)>1):

				#write the output
				directors_to_write = directors_row[1]
				movie_name = basics_row[2]

				#Files are closed when Python exits, but 
				#file output is usually buffered and if there is no newline,
				#pending output will not be flushed to the file system.

				str_to_write = movie_name +  '\t' +directors_to_write +'\n'

				f.write(str_to_write)
			
		except StopIteration:
			f.close()
			break

  

if __name__== "__main__":
  main()