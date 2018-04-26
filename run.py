#!/usr/bin/env python

"""First MNE BIDS app.

Example usage:

$ ./run.py --inputdir ./BIDS-examples/ds000248 --subject_id 01
--outputdir ./evoked/

"""

# Authors: Mainak Jas <mainak.jas@telecom-paristech.fr>
#
# License: BSD (3-clause)

import os
import glob
import argparse
import os.path as op

import mne
import numpy as np

parser = argparse.ArgumentParser(description='Read BIDS compatible data.')
parser.add_argument('--inputdir', type=str, help='Path to BIDS study folder')
parser.add_argument('--subject_id', type=str, help='Subject label')
parser.add_argument('--outputdir', type=str, help='Path to output folder')
args = parser.parse_args()

pattern = op.join(args.inputdir, 'sub-' + args.subject_id, 'meg', '*_meg.fif')
raw_fnames = glob.glob(pattern)

# just work on one file
raw = mne.io.read_raw_fif(raw_fnames[0])

events = mne.find_events(raw, stim_channel='STI 014')

print('Number of events:', len(events))
print('Unique event codes:', np.unique(events[:, 2]))

epochs = mne.Epochs(raw, events, event_id=None, tmin=-0.1, tmax=1,
                    baseline=(None, 0), preload=True)

if not op.exists(args.outputdir):
    os.mkdir(args.outputdir)
epochs.average().save(op.join(args.outputdir, 'evoked.fif'))

