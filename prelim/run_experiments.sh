# run experiments
source bin/activate

echo "Running svc experiments with ground truth"
python3 main.py /home/tskluzac/pub8/ svc head --split 0.5 --out gt.csv
python3 main.py /home/tskluzac/pub8/ svc rand --split 0.5 --out gt.csv
python3 main.py /home/tskluzac/pub8/ svc randhead --split 0.5 --head-bytes 256 --rand-bytes 256 --out gt.csv

echo "Running logit experiments ground truth"
python3 main.py /home/tskluzac/pub8/ logit head --out gt.csv
python3 main.py /home/tskluzac/pub8/ logit rand --out gt.csv
python3 main.py /home/tskluzac/pub8/ logit randhead --head-bytes 256 --rand-bytes 256 --out gt.csv

echo "Running rf experiments ground truth"
python3 main.py /home/tskluzac/pub8/ rf head --out gt.csv
python3 main.py /home/tskluzac/pub8/ rf rand --out gt.csv
python3 main.py /home/tskluzac/pub8/ rf randhead --head-bytes 256 --rand-bytes 256 --out gt.csv

echo "Running jsd experiments with file extension"
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 1 --rand-bytes 256 --out ext1gram256.csv
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 1 --rand-bytes 512 --out ext1gram512.csv
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 1 --rand-bytes 1024 --out ext1gram1024.csv
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 2 --rand-bytes 256 --out ext2gram256.csv
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 2 --rand-bytes 512 --out ext2gram512.csv
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 2 --rand-bytes 1024 --out ext2gram1024.csv

echo "Running jsd experiments with file extension"
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 1 --rand-bytes 256 --out gt1gram256.csv --reader naivetruth.csv
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 1 --rand-bytes 512 --out gt1gram512.csv --reader naivetruth.csv
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 1 --rand-bytes 1024 --out gt1gram1024.csv --reader naivetruth.csv
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 2 --rand-bytes 256 --out gt2gram256.csv --reader naivetruth.csv
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 2 --rand-bytes 512 --out gt2gram512.csv --reader naivetruth.csv
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 2 --rand-bytes 1024 --out gt2gram1024.csv --reader naivetruth.csv
