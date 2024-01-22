"""
Event detection on pap augmented processed.
"""

import json
import pandas as pd
from glen import event_detection


# Create a list of sentences from pap dataset for train/dev/test splits, respectively.
# (1) pap train
pap_train_processed_augmented = pd.read_csv('./input/pap_train_processed_augmented.csv')
sentences_pap_train = pap_train_processed_augmented['text']
print(f"Pap train has {len(sentences_pap_train)} sentences.\n")

# (2) pap dev
pap_dev_processed_augmented = pd.read_csv('./input/pap_dev_processed_augmented.csv')
sentences_pap_dev = pap_dev_processed_augmented['text']
print(f"Pap dev has {len(sentences_pap_dev)} sentences.\n")

# (3) pap test
pap_test_processed_augmented = pd.read_csv('./input/pap_test_processed_augmented.csv')
sentences_pap_test = pap_test_processed_augmented['text']
print(f"Pap test has {len(sentences_pap_test)} sentences.\n")


def predict(sentence_list, model_ckpts_dir='model_ckpts/', bs_TI=64, bs_TC=64, bs_TR=4, k=10):
    result = event_detection(sentence_list, model_ckpts_dir, bs_TI=bs_TI, bs_TC=bs_TC, bs_TR=bs_TR, k=k)
    return result

# Run event detection for each split.
result_pap_train = predict(sentences_pap_train)
result_pap_dev = predict(sentences_pap_dev)
result_pap_test = predict(sentences_pap_test)

# Add the ED result to the dataframe as a new column.
pap_train_processed_augmented['event_type'] = result_pap_train
pap_dev_processed_augmented['event_type'] = result_pap_dev
pap_test_processed_augmented['event_type'] = result_pap_test

# Write the results.
pap_train_processed_augmented.to_csv('./output/ed_pap_train_output.csv', index=False)
pap_dev_processed_augmented.to_csv('./output/ed_pap_dev_output.csv', index=False)
pap_test_processed_augmented.to_csv('./output/ed_pap_test_output.csv', index=False)
