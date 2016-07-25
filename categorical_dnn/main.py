from categorical_dnn import CategoricalDNN

# According to the CSV
COLUMNS = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']

LEARNING_RATE = 0.1
TRAINING_SIZE = 0.75 # 75%;
ITERATIONS = 1800

def main():

    dnn = CategoricalDNN('car-data.csv',
                         COLUMNS,
                         TRAINING_SIZE,
                         LEARNING_RATE,
                         ITERATIONS)
    dnn.data_insights()
    dnn.train()

if __name__ == "__main__":
    main()


