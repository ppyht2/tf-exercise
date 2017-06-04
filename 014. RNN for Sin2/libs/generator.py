import numpy as np


def generate_sin(batch_size=1000, T=100, offset=0, past_range=10, future_range=10):
    '''
    For now: assume amplitude = 1
    y = sin(wt)

    '''
    f = (2 * np.pi) / T
    past = np.empty((batch_size, past_range))
    future = np.empty((batch_size, future_range))
    for t in range(batch_size):

    return
