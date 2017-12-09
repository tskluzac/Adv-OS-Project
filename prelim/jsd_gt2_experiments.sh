echo "Running jsd experiments with ground truth  - n = 2"
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 2 --rand-bytes 256 --out data/gt2gram256.csv --reader naivetruth.csv
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 2 --rand-bytes 512 --out data/gt2gram512.csv --reader naivetruth.csv
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 2 --rand-bytes 1024 --out data/gt2gram1024.csv --reader naivetruth.csv
