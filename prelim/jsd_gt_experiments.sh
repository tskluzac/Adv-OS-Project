# run experiments
#source bin/activate

#echo "Running jsd experiments with file data/extension"
#python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 1 --rand-bytes 256 --out data/ext1gram256.csv
#python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 1 --rand-bytes 512 --out data/ext1gram512.csv
#python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 1 --rand-bytes 1024 --out data/ext1gram1024.csv
#python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 2 --rand-bytes 256 --out data/ext2gram256.csv
#python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 2 --rand-bytes 512 --out data/ext2gram512.csv
#python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 2 --rand-bytes 1024 --out data/ext2gram1024.csv

echo "Running jsd experiments with ground truth"
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 1 --rand-bytes 256 --out data/gt1gram256.csv --reader naivetruth.csv
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 1 --rand-bytes 512 --out data/gt1gram512.csv --reader naivetruth.csv
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 1 --rand-bytes 1024 --out data/gt1gram1024.csv --reader naivetruth.csv
