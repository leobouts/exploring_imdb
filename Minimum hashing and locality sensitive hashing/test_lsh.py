from jaccardSimilarity import get_J_Similarity
from minhash import minHash, signatureSimilarity
from lsh import local_sensitive_hashing
from load import load_movies_to_dicts
import matplotlib.pyplot as plt

path = r"/Users/leonidas/Desktop/Algorithms for big data/assignment1/ratings.csv"
userList, movieMap, movieList = load_movies_to_dicts(path)
movie_count = len(movieList.keys())
user_count = len(userList.keys())


def get_labels(s, movie_limit):
    labels = []
    for i in range(movie_limit):
        for j in range(movie_limit):
            if j > i:
                m1 = list(movieList)[i]
                m2 = list(movieList)[j]
                js = get_J_Similarity(movieList[m1], movieList[m2])

                if js >= s:
                    labels.append([m1, m2, True])
                else:
                    labels.append([m1, m2, False])
    return labels


# getScores
def get_lsh_scores(labels, sig_num, movie_limit):
    true_positives = 0
    true_negatives = 0
    false_positives = 0
    false_negatives = 0

    SIG = minHash(sig_num, userList, movieMap, movieList)

    scores = {}
    for band_num in [3,5,6,10]: # Testing values of band numbers
        pairs = local_sensitive_hashing(SIG, sig_num, band_num, movieList, movie_limit)
        for i in labels:
            tmp = (i[0], i[1])
            if tmp in pairs:
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

        if band_num == 3: ##### NEED TO CHANGE
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

        print("FOR b = ", band_num)
        print("PRECISION: ", precision)
        print("RECALL: ", recall)
        print("F1 SCORE: ", f1)

    return scores


scores = get_lsh_scores(get_labels(0.25, 100), 30, 100)

plt.figure()

for i, key in enumerate(scores):
    
    plt.subplot(2, 3, i+1)
    plt.plot([3,5,6,10], scores[key])
    plt.xticks([3,5,6,10])

    plt.xlabel("bands")
    plt.ylabel(key)
    plt.grid(True)

plt.show()