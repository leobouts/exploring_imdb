import textwrap
import random

# We have here the LSH and the functions that it uses

def local_sensitive_hashing(signatures,sig_num, b, movieList, movie_limit):
    r = sig_num // b
    hf = create_random_hash_function()
    lsh_sig = prepare_signatures(signatures, r, movieList)
    pairs = []

    for band in range(b):
        buckets = {}
        for i, movie in enumerate(lsh_sig):
            if i == movie_limit - 1:  # STOPS AT 20 FIRST MOVIES
                break
            tmp = hf(int(lsh_sig[movie][band]))
            if tmp not in buckets.keys():
                buckets[tmp] = []
            buckets[tmp].append(movie)
        
        for key in buckets:
            if len(buckets[key]) > 1:
                pairs = updatePairs(buckets[key], pairs)
        
    return pairs


def create_random_hash_function(p=2**33-355, m=2**32-1):
    a = random.randint(1,p-1)
    b = random.randint(0, p-1)
    return lambda x: 1 + (((a * x + b) % p) % m)


def prepare_signatures(sig, r, movieList):
    sig = dict(zip(movieList.keys(), [convert_signature_to_string(sig[m]) for m in sig]))
    
    return split_signatures(r, sig)


def convert_signature_to_string(signature):
    output = ""
    for i in signature:
        if i < 10:
            output += "0"
        output += str(i)

    return output


def split_signatures(r, input):
    output = {}
    for i in input:
        # wrap is a nice function that splits the
        # initial string to a list of r-character words
        output[i] = textwrap.wrap(input[i], r)
    
    return output


def updatePairs(new_pairs, old_pairs):
    tmp = []
    for i in new_pairs:
        for j in new_pairs:
            if i < j:
                tmp.append((i,j))
    
    return list(set(tmp).union(set(old_pairs)))