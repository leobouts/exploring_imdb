from randomPermutation import create_random_permutations

def minHash(sig_count, userList, movieMap, movieList):

    user_count = len(userList.keys())
    movie_count = len(movieList.keys())
    permutations = create_random_permutations(user_count, sig_count)
    SIG = {}

    # Initialize signatures to 'infinity'
    for i in range(1, movie_count + 1):
        SIG[i] = []
        for j in range(sig_count):
            SIG[i].append(user_count + 10)

    # Scan users
    for user in userList.keys():
        # Scan movies
        for movie in movieList.keys():
            # Check if the user has seen this movie
            if user in movieList[movie]:
                # Scan permutations
                for i in range(sig_count):
                    # Map movieIndex in permutationIndex
                    permutation_index = permutations[i].index(user)
                    
                    if permutation_index < SIG[movieMap[movie]][i]:
                        SIG[movieMap[movie]][i] = permutation_index
    
    return SIG

def signatureSimilarity(movieId1, movieId2, n, movieMap, SIG):

    index1 = movieMap[movieId1]
    index2 = movieMap[movieId2]

    count = 0
    for i in range(n):
        if SIG[index1][i] == SIG[index2][i]:
            count += 1
    
    return count / n