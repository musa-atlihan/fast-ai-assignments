# The code in this file is implemented by me, it is different from the file used in the lessons.

import numpy as np

def submit2redux(test_batches, preds, file_name='subm_full.csv'):
    """Prepare the predictions for to submit to Kaggle
    
    Submitting to Kaggle cats and dogs redux competitions.
    
    Args:
        test_batches: Batches of test set.
        preds: prediction array for the test set (not the labels, probabilities).
    """
    
    file_names = test_batches.filenames
    # get isdog plus clip for 0. and 1.
    isdog = np.clip(preds[:,1], 0.02, 0.98)
    # ids
    ids = [int(f[10:f.find('.')]) for f in file_names]
    # stack
    subm = np.stack([ids,isdog], axis=1)
    # order
    ordered = subm[subm[:,0].argsort()]
    # save
    np.savetxt('data/' + file_name, ordered, fmt='%d,%.5f', header='id,label', comments='')
    print('File saved as ./data/' + file_name + '.')