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


	dict_years_sum = {}
	dict_years_counter = {}
	dict_years_result = {}

	while True:
		try:

			basics_row = next(generatorForBasics)
			ratings_row = next(generatorForRatings)

			year = basics_row[5]
			rating = float(ratings_row[1])

			#ignore NaN values and non valid years
			if(year=='\\N' or rating=='\\N' or int(year)>2020):
				continue
			else:

				#check if the year already exist, if not create the entry
				if year in dict_years_sum:
					dict_years_sum[year] += rating
					dict_years_counter[year] += 1

				else:
					dict_years_sum[year] = rating
					dict_years_counter[year] = 1

				#update gradually the statistics
				dict_years_result[year] = dict_years_sum[year] / dict_years_counter[year]

		except StopIteration:
			break


	for year in sorted(dict_years_sum.keys()):

		print('year:',year,' average rating:',dict_years_result[year])

if __name__== "__main__":
  main()