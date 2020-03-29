import random
from operator import itemgetter
from hashFunction import create_random_hash_functions
from hashFunction import hash_function

# INPUT:  positive integer K
# OUTPUT: a random permutation of the list [1,2,3,...,K]
def create_random_permutations(K=50, n = 10):

    a_list, b_list = create_random_hash_functions(n)
    
    random_permutations = []
    for i in range(len(a_list)):
        tmp_hash_list = []
        tmp_sorted_hash_list = []
        tmp_random_permutation = []

        for j in range(K):
            h_j = int(hash_function(j, a_list[i], b_list[i], K+1))
            tmp_hash_list.append((j, h_j))
        
        tmp_sorted_hash_list = sorted(tmp_hash_list, key=itemgetter(1))

        for j in range(len(tmp_sorted_hash_list)):
            tmp_random_permutation.append(1 + tmp_sorted_hash_list[j][0])
        
        random_permutations.append(tmp_random_permutation)
    
    return random_permutations


