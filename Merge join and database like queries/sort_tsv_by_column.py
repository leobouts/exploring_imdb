import csv
from operator import itemgetter
reader = csv.reader(open("imdbData/title.episode.tsv"), delimiter="\t")

f = open('episode.sorted.tsv', 'w')

for line in sorted(reader, key=itemgetter(0)):

    str_to_write = line[0]+'\t'+line[1]+'\t'+line[2]+'\t'+line[3]+'\n'
    print(str_to_write)
    f.write(str_to_write)

f.close()
    