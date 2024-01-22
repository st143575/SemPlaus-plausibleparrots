"""
Event detection on pep augmented processed.
"""

import json
import pandas as pd
from glen import event_detection


# Create a list of sentences from pep dataset for train/dev/test splits, respectively.
# (1) pep train
pep_train_processed_augmented = pd.read_csv('./input/pep_train_processed.csv')
sentences_pep_train = pep_train_processed_augmented['text']
print(f"Pep train has {len(sentences_pep_train)} sentences.\n")

# (2) pep dev
pep_dev_processed_augmented = pd.read_csv('./input/pep_dev_processed.csv')
sentences_pep_dev = pep_dev_processed_augmented['text']
print(f"Pep dev has {len(sentences_pep_dev)} sentences.\n")

# (3) pep test
pep_test_processed_augmented = pd.read_csv('./input/pep_test_processed.csv')
sentences_pep_test = pep_test_processed_augmented['text']
print(f"Pep test has {len(sentences_pep_test)} sentences.\n")


def predict(sentence_list, model_ckpts_dir='model_ckpts/', bs_TI=64, bs_TC=64, bs_TR=4, k=10):
    result = event_detection(sentence_list, model_ckpts_dir, bs_TI=bs_TI, bs_TC=bs_TC, bs_TR=bs_TR, k=k)
    return result

# Run event detection for each split.
result_pep_train = predict(sentences_pep_train)
result_pep_dev = predict(sentences_pep_dev)
result_pep_test = predict(sentences_pep_test)

# Add the ED result to the dataframe as a new column.
pep_train_processed_augmented['event_type'] = result_pep_train
pep_dev_processed_augmented['event_type'] = result_pep_dev
pep_test_processed_augmented['event_type'] = result_pep_test

# Write the results.
pep_train_processed_augmented.to_csv('./output/ed_pep_train_output.csv', index=False)
pep_dev_processed_augmented.to_csv('./output/ed_pep_dev_output.csv', index=False)
pep_test_processed_augmented.to_csv('./output/ed_pep_test_output.csv', index=False)
