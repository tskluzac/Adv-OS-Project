from scipy.stats import entropy
from numpy.linalg import norm
from sklearn.manifold import TSNE

def jsd(p, q):

    """
    Jensen-Shannon divergence between two vectors (representing
    probability distributions

    Taken from https://stackoverflow.com/questions/15880133/jensen-shannon-divergence/27432724
    """

    norm_p = p/norm(p, ord=1)
    norm_q = q/norm(q, ord=1)
    m = 0.5*(p+q)
    return 0.5*(entropy(p,m) + entropy(q,m))

def embed(reader):

    """
    embed the data from the reader into a 2d plane using JSD as the distance
    metric. reader's features should be ngrams
    """

    X = []

    for data in reader.data:

        x,_ = reader.feature.translate(data)
        X.append(x)

    sne = TSNE() # dim defaults to 2
    X_embed = sne.fit_transform(X)

    return X_embed
