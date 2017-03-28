from os import path
import argparse
import pickle
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

import config


parser = argparse.ArgumentParser()
parser.add_argument('--naverage', type=int, help='number of periods over which to average', default=50)
args = parser.parse_args()

columns = [
    'Discriminator loss',
    'Prob real',
    'Prob fake (before G update)',
    'Prob fake (after G update)',
]

# read pickled loss history
with open(path.join(config.path_outputs, 'loss_history.pkl'), 'rb') as f:
    loss_history = pickle.load(f)

# smooth loss curves via moving average
epochs = 25  # TODO: read this dynamically
losses = np.array(loss_history)
ma = np.vstack(
    [np.convolve(series, np.ones(args.naverage) / args.naverage)
     for series in losses.T]).T[args.naverage - 1:-args.naverage, :]
x = np.linspace(1, epochs, ma.shape[0])
xnew = np.linspace(x.min(), x.max(), epochs)
smoothed = np.vstack([spline(x, s, xnew) for s in ma.T]).T

fig, ax = plt.subplots()
for i, series in enumerate(smoothed.T):
    ax.plot(xnew, series, label=columns[i])

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.2, box.width, box.height * 0.9])
legend = ax.legend(loc='lower center', ncol=2, bbox_to_anchor=[0.5, -0.32], shadow=True)
ax.set_xlabel('Iteration')
fig.savefig(path.join(config.path_base, 'WGAN_loss_history.png'))
