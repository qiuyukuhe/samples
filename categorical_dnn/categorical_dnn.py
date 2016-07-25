import pandas as pd
import tensorflow as tf
import tensorflow.contrib.learn as tflearn
from sklearn import metrics
from sklearn.cross_validation import train_test_split
import os.path
import numpy as np


class CategoricalDNN:
    '''
        This class only works with categorical data and if the data range is static.
        It assumes that the last column of the data is the `label` or `class` to train for.
    '''

    def __init__(self, file_name, columns, training_size, learning_rate, iterations):

        # Check to see if the parameters are valid
        if os.path.isfile(file_name):
            self._file_name = file_name
            self._columns = columns
            self._training_size = training_size
            self._learning_rate = learning_rate
            self._iterations = iterations

            # All looks good, let's load it into a matrix
            self._load_csv()

            # Randomize the dataset and split according to the parameter
            self._shuffle_split()

        else:
            raise IOError('Could not find file: %s.' % file_name)

    def _convert_categorical_nominal(self, df, column_no):
        return pd.Categorical.from_array(df[df.columns[column_no]]).codes

    def _load_csv(self):

        # Loading CSV into the system using Pandas
        self._input_map = []
        self._raw_data = pd.read_csv(self._file_name, sep=',', skipinitialspace=True)
        self._datadim = len(self._raw_data.columns)

        # Find uniques in the last column aka. `label` or `class`
        self._classes = self._raw_data[self._raw_data.columns[self._datadim - 1]].unique()

        # Create a map of all unique values by columns
        for i in range(self._datadim):
            self._raw_data[self._raw_data.columns[i]] = \
                self._convert_categorical_nominal(self._raw_data, i)

    def _shuffle_split(self):
        self._raw_data.iloc[np.random.permutation(len(self._raw_data))]
        self._testdata, self._traindata = train_test_split(self._raw_data, test_size=self._training_size)

        # TF Learn / TensorFlow only takes int32 / int64 at the moment as oppose to int8
        self._train_label = [int(row) for row in self._traindata[self._raw_data.columns[self._datadim - 1]]]
        self._test_label = [int(row) for row in self._testdata[self._raw_data.columns[self._datadim - 1]]]

    def train(self):

        # The rule: my own rule aka. own intuition
        hidden_Layers = [self._datadim - 1,
                         ((self._datadim - 1) + len(self._classes)) / 2,
                         len(self._classes)]

        classifier = tflearn.DNNClassifier(hidden_units=hidden_Layers,
                                           n_classes=len(self._classes),
                                           activation_fn=tf.nn.relu)

        classifier.learning_rate = self._learning_rate

        classifier.fit(self._traindata, self._train_label, steps=self._iterations)
        score = metrics.accuracy_score(self._test_label, classifier.predict(self._testdata))
        print 'Accuracy on test dataset: %f' % score
        score = metrics.accuracy_score(self._train_label, classifier.predict(self._traindata))
        print 'Accuracy on training dataset: %f' % score

    def data_insights(self):

        # Quick snapshot of the data on the console.
        print '\nShape: {}\n'.format(self._raw_data.shape)
        print 'Data types:'
        self._raw_data.info()
        print '\nTop 5 rows: \n{}'.format(self._raw_data.head())
        print '\nData statistics: \n{}'.format(self._raw_data.describe().T)
        print '-\n'
