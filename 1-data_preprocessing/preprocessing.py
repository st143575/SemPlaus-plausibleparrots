import os
import pandas as pd
from tqdm import tqdm
from argparse import ArgumentParser


DATA_PATH = "/mount/studenten/semantic-plausibility/datasets/"


def create_sentence_from_triple(input_path:str, output_path:str, dataset_name:str):
    """
    Concatenate the subject (s), verb (v) and object (o) of an (s,v,o)-event triple to a natural language sentence.
    The first letter of the subject will be capitalized. After s, v, o are concatenated, a full stop '.' will be 
    appended to the end of the object.

    For example, the event triple (tortoise, brings, limb) will become "Tortoise brings limb."
    
    Args:
        input_path:str    The path for the raw dataset of (s,v,o)-triples, e.g.,
                          /mount/studenten/semantic-plausibility/datasets/pap/train-dev-test-split/binary/
        output_path:str   The path for the data created for event extraction, e.g.,
                          /mount/studenten/arbeitsdaten-studenten1/semantic-plausibility/plausible-parrots/data_preprocessing/output/
        dataset_name:str  Name of the dataset, e.g. 'pap', 'pep'.
        
    Precondition:
        File names end with '.csv'.
        
    Run:
        python preprocessing.py -i /mount/studenten/semantic-plausibility/datasets/pap/train-dev-test-split/binary/ -o /mount/studenten/arbeitsdaten-studenten1/semantic-plausibility/plausible-parrots/data_preprocessing/output/ -dn pap
        python preprocessing.py -i /mount/studenten/semantic-plausibility/datasets/pep-3k/train-dev-test-split/ -o /mount/studenten/arbeitsdaten-studenten1/semantic-plausibility/plausible-parrots/data_preprocessing/output/ -dn pep
    """
    
    for subdir, dirs, files in os.walk(input_path):
        for file in files:
            fn = subdir + file
            
            # Validate the precondition.
            assert fn.endswith(".csv")
    
            # Load the input data to a dataframe.
            df = pd.read_csv(fn, sep=',')
            
            for i, row in tqdm(df.iterrows()):
                text = row['text']
                sentence = text[0].upper() + text[1:] + "."
                df.at[i, 'text'] = sentence
                
            # Get dataset split name ('train'/'dev'/'test').
            split_name = fn.split('/')[-1].split('.csv')[0]
            print(split_name)
            
            df.to_csv(f'./output/{dataset_name}_{split_name}_processed.csv', index=False)
            
            
parser = ArgumentParser()
parser.add_argument('-i', '--input_dir', help='path to the input data folder')
parser.add_argument('-o', '--output_dir', help='path to the output data folder')
parser.add_argument('-dn', '--dataset_name', help="name of the dataset, e.g. 'pap', 'pep'")

args = parser.parse_args()

create_sentence_from_triple(input_path=args.input_dir, output_path=args.output_dir, dataset_name=args.dataset_name)            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            