from jaccardSimilarity import get_J_Similarity
from minhash import minHash, signatureSimilarity
from load import load_movies_to_dicts
import matplotlib.pyplot as plt

####################
# CHANGE THIS PATH #
####################

path = r"/Users/leonidas/Desktop/Algorithms for big data/assignment1/ratings.csv"
userList, movieMap, movieList = load_movies_to_dicts(path)
movie_count = len(movieList.keys())
user_count = len(userList.keys())


def get_labels(s, movie_limit):
    labels = []
    for i in range(movie_limit):
        for j in range(movie_limit):
            # We just calculate the upper triangle of the matrix to
            # be more efficient (there is symmetry between the pairs)
            if j > i: 
                m1 = list(movieList)[i]
                m2 = list(movieList)[j]
                js = get_J_Similarity(movieList[m1], movieList[m2])

                if js >= s:
                    labels.append([m1, m2, True])
                else:
                    labels.append([m1, m2, False])
    return labels


def get_min_hash_scores(labels, sig_num):
    true_positives = 0
    true_negatives = 0
    false_positives = 0
    false_negatives = 0

    SIG = minHash(sig_num, userList, movieMap, movieList)

    scores = {}
    for n in range(5,31,5): # Testing values of n first signatures
        for i in labels:
            sim = signatureSimilarity(i[0], i[1], n, movieMap, SIG)

            if sim >= 0.25:
                if i[2]:
                    true_positives += 1
                else:
                    false_positives += 1
            else:
                if i[2]:
                    false_negatives += 1
                else:
                    true_negatives += 1

        precision = true_positives / (true_positives + false_positives)
        recall = true_positives / (true_positives + false_negatives)
        f1 = 2 * recall * precision / (recall + precision)

        if n == 5:
            scores["precision"] = []
            scores["recall"] = []
            scores["f1"] = []
            # scores["tp"] = []
            scores["fp"] = []
            scores["fn"] = []
            # scores["tn"] = []

        scores["precision"].append(precision)
        scores["recall"].append(recall)
        scores["f1"].append(f1)
        # scores["tp"].append(true_positives)
        scores["fp"].append(false_positives) 
        scores["fn"].append(false_negatives)
        # scores["tn"].append(true_negatives)

        print("FOR n` = ", n)
        print("PRECISION: ", precision)
        print("RECALL: ", recall)
        print("F1 SCORE: ", f1)
    
    return scores


scores = get_min_hash_scores(get_labels(0.25, 100), 40)

plt.figure()

for i, key in enumerate(scores):
    #print(scores[key])
    
    plt.subplot(2, 3, i+1)
    plt.plot([5, 10, 15, 20, 25, 30], scores[key])
    plt.xticks([5, 10, 15, 20, 25, 30])
    plt.xlabel("n`")
    plt.ylabel(key)
    plt.grid(True)
    #plt.title(key)
    #break
plt.show()