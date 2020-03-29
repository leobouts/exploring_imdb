import csv


def generateNextRowOfEpisode():

	with open('imdbData/episode.sorted.tsv') as episode:
		
		reader = csv.reader(episode, delimiter='\t')

		for row in reader:
			yield row


def generateNextRowOfBasics():

	with open('imdbData/title.basics.tsv') as basics:

		reader = csv.reader(basics, delimiter='\t')

		for row in reader:
			yield row



def main():

	generatorForEpisodes = generateNextRowOfEpisode()
	generatorForBasics = generateNextRowOfBasics()

	#skip headers
	episodes_row = next(generatorForEpisodes)
	basics_row = next(generatorForBasics)



	f = open('output1.2.txt', 'w')
	f.write('primaryTitle\tParentTconst\tseasonNumber\n')

	
		
		#check if the episode matches the basics info
		# the episode file does not contain all of the titles
		# while the basics contain them all.

	while True:
		try:

			episodes_row = next(generatorForEpisodes)
			basics_row = next(generatorForBasics)

			while(episodes_row[3]!='1'):
				episodes_row = next(generatorForEpisodes)
			
			while(episodes_row[0]!=basics_row[0]):		
				basics_row = next(generatorForBasics)


			#write the output
			parentTconst = episodes_row[1]
			seasonNumber = episodes_row[3]
			movie_name = basics_row[2]

			#Files are closed when Python exits, but 
			#file output is usually buffered and if there is no newline,
			#pending output will not be flushed to the file system.

			str_to_write = movie_name+'\t'+parentTconst+'\t'+seasonNumber+'\n'

			print(str_to_write)

			f.write(str_to_write)

		except StopIteration:
			f.close()
			break


  

if __name__== "__main__":
  main()