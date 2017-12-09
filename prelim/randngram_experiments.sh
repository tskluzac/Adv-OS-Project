python3 main.py /home/tskluzac/pub8/ svc randngram --out data/gt.csv --reader naivetruth.csv
python3 main.py /home/tskluzac/pub8/ logit randngram --out data/gt.csv --reader naivetruth.csv
python3 main.py /home/tskluzac/pub8/ rf randngram --out data/gt.csv --reader naivetruth.csv

python3 main.py /home/tskluzac/pub8/ svc randngram --ngram 1 --rand-bytes 256 --out data/ext.csv
python3 main.py /home/tskluzac/pub8/ logit randngram --ngram 1 --rand-bytes 256 --out data/ext.csv
python3 main.py /home/tskluzac/pub8/ rf randngram --ngram 1 --rand-bytes 256 --out data/ext.csv
