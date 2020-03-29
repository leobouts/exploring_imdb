import csv
# This function scans the file one time, creates and returns 
# three dictionaries userList, movieMap, movieList


def load_movies_to_dicts(path):

	userList = {}
	movieMap = {}
	movieList = {}
	movie_counter = 1

	with open(path) as infile:
		csv_reader = csv.reader(infile, delimiter=',')
		count = 0
		
		for row in csv_reader:
			if count == 0:
				count += 1
				continue
			
			userId_tmp = int(row[0])
			movieId_tmp = int(row[1])

			if userId_tmp not in userList.keys():
				userList[userId_tmp] = []
			
			userList[userId_tmp].append(movieId_tmp)

			if movieId_tmp not in movieList.keys():
				movieList[movieId_tmp] = []
				movieMap[movieId_tmp] = movie_counter
				movie_counter += 1

			movieList[movieId_tmp].append(userId_tmp)


			count += 1
			
	return userList, movieMap, movieList