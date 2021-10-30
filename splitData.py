from sklearn.model_selection import train_test_split

def splitData(features, labels, config):
    return train_test_split(
        features,
        labels,
        test_size=config['testPct'],
        random_state=0)