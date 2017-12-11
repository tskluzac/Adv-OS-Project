# run experiments
#source bin/activate

echo "Running jsd experiments 1/2 with file data/extension"
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 1 --rand-bytes 200 --out data/ext1gram200.csv
echo "Running jsd experiments 2/2 with file data/extension"
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 2 --rand-bytes 200 --out data/ext2gram200.csv

echo "Running jsd experiments 1/2 with file data/extension"
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 1 --rand-bytes 200 --out data/gt1gram200.csv --reader naivetruth.csv
echo "Running jsd experiments 2/2 with file data/extension"
python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 2 --rand-bytes 200 --out data/gt2gram200.csv --reader naivetruth.csv

#echo "Running svc experiments with ground truth"
#python3 main.py /home/tskluzac/pub8/ svc head --split 0.5 --out data/gt.csv --reader naivetruth.csv
#python3 main.py /home/tskluzac/pub8/ svc rand --split 0.5 --out data/gt.csv --reader naivetruth.csv
#python3 main.py /home/tskluzac/pub8/ svc randhead --split 0.5 --head-bytes 256 --rand-bytes 256 --out data/gt.csv --reader naivetruth.csv

#echo "Running logit experiments ground truth"
#python3 main.py /home/tskluzac/pub8/ logit head --out data/gt.csv --reader naivetruth.csv
#python3 main.py /home/tskluzac/pub8/ logit rand --out data/gt.csv --reader naivetruth.csv
#python3 main.py /home/tskluzac/pub8/ logit randhead --head-bytes 256 --rand-bytes 256 --out data/gt.csv --reader naivetruth.csv

#echo "Running rf experiments ground truth"
#python3 main.py /home/tskluzac/pub8/ rf head --out data/gt.csv --reader naivetruth.csv
#python3 main.py /home/tskluzac/pub8/ rf rand --out data/gt.csv --reader naivetruth.csv
#python3 main.py /home/tskluzac/pub8/ rf randhead --head-bytes 256 --rand-bytes 256 --out data/gt.csv --reader naivetruth.csv

#echo "Running jsd experiments with file data/extension"
#python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 1 --rand-bytes 256 --out data/ext1gram256.csv
#python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 1 --rand-bytes 512 --out data/ext1gram512.csv
#python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 1 --rand-bytes 1024 --out data/ext1gram1024.csv
#python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 2 --rand-bytes 256 --out data/ext2gram256.csv
#python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 2 --rand-bytes 512 --out data/ext2gram512.csv
#python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 2 --rand-bytes 1024 --out data/ext2gram1024.csv

#echo "Running jsd experiments with ground truth"
#python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 1 --rand-bytes 256 --out data/gt1gram256.csv --reader naivetruth.csv
#python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 1 --rand-bytes 512 --out data/gt1gram512.csv --reader naivetruth.csv
#python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 1 --rand-bytes 1024 --out data/gt1gram1024.csv --reader naivetruth.csv
#python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 2 --rand-bytes 256 --out data/gt2gram256.csv --reader naivetruth.csv
#python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 2 --rand-bytes 512 --out data/gt2gram512.csv --reader naivetruth.csv
#python3 main.py /home/tskluzac/pub8/ jsd randngram --ngram 2 --rand-bytes 1024 --out data/gt2gram1024.csv --reader naivetruth.csv
