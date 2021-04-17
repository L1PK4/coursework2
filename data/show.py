import pickle
with open('data/data.pickle', 'rb') as f:
    print(pickle.load(f))