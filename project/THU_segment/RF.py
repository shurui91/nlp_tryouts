__author__ = 'qing'
import sys
from sklearn.ensemble import RandomForestClassifier
from util import extract_features
from util import extract_testfeatures
from util import preprocess_data
from util import preprocess_testdata
from sklearn.metrics import accuracy_score


def run(input_file, test_file, k):
    clf = RandomForestClassifier(n_estimators=k)
    df = preprocess_data(input_file)
    X, label_dict, dict = extract_features(df)
    r, c = X.shape
    dft = preprocess_testdata(test_file)
    Xt, yt = extract_testfeatures(dft, label_dict, dict)
    clf.fit(X[:,0:c-1], X[:,c-1])
    z = clf.predict(Xt)
    print(accuracy_score(yt, z))


def tune_rf(input_file, test_file):
    for k in range(90, 110, 2):
        print('k = ' + str(k))
        run(input_file, test_file, k)


if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')
    #run("output/training_data_stanford.csv", "output/test_data_stanford.csv", 100)
    #run("training_set/training_data_thu.csv", "testset/test_data_thu.csv", 100)
    tune_rf("training_set/training_data_thu.csv", "testset/test_data_thu.csv")