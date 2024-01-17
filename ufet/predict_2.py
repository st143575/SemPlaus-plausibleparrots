import os
import torch
import pandas as pd
import dill as pickle
from tqdm import tqdm
from typing import Optional, Union
from argparse import ArgumentParser

from casent.entity_typing_t5 import T5ForEntityTypingPredictor
from casent.entity_typing_t5 import T5ForWikidataEntityTypingPredictor


PATH = '/mount/studenten/arbeitsdaten-studenten1/semantic-plausibility/plausible-parrots/'
CACHE_DIR = PATH + 'cache/'
ED_PATH = PATH + 'event_extraction/glen/ED/'

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def get_svo(evt_sentence:str):
    """
    Get the subject (s), verb (v) and object (o) from an event sentence, e.g. 'County receives hour.'.
    Remove the full stop '.' from the object.
    """
    
    s, v, o = evt_sentence.split(' ')
    o = o[:-1]
    return s, v, o

def add_special_tokens(evt_sentence:str):
    """
    For an event sentence, add the special tokens <M> and </M> that indicate the span of an entity mention 
    to each of s and o, respectively, and return the two sentences, each with s and o marked with the special tokens.
    """
    
    s, v, o = get_svo(evt_sentence)
    s_m = "<M> " + s + " </M>"
    o_m = "<M> " + o + " </M> ."
    evt_sent_1 = " ".join([s_m, v, o + "."])
    evt_sent_2 = " ".join([s, v, o_m])
    return [evt_sent_1, evt_sent_2]

def preprocess_data(ed_result):
    sentences = ed_result['text']
    sentences_marked = []
#     sentences = ed_result['sentence'].to_list()
    for sent in sentences:
        sentences_marked.append(add_special_tokens(sent))
    return sentences_marked



def entity_typing(input_file, mode:Optional[Union['ufet', 'wikidata']], device=device):
    """
    Entity typing for the subjects and objects of the event sentences.
    """
    
    ed_result = pd.read_csv(input_file)
    sentences_marked = preprocess_data(ed_result)
#     print(sentences_marked)
    
    if mode == 'ufet':
        predictor_ufet = T5ForEntityTypingPredictor.from_pretrained('yanlinf/casent-large', cache_dir=CACHE_DIR)
        predictor_ufet.to(device)
        output_ufet = dict()
        for i, sents in tqdm(enumerate(sentences_marked)):
            sentence = ed_result.iloc[i]['text']
            output_ufet[sentence] = predictor_ufet.predict_raw(sents)
        return output_ufet
    
    elif mode == 'wikidata':
        predictor_wikidata = T5ForWikidataEntityTypingPredictor.from_pretrained(
            'yanlinf/casent-large', 
            ontology_path='../ontology_data/ontology_expanded.json', 
            cache_dir=CACHE_DIR,
        )
        predictor_wikidata.to(device)
        
        subject_types = []
        object_types = []
        for i, sents in tqdm(enumerate(sentences_marked)):
            sentence = ed_result.iloc[i]['text']
            #print("SENT:", sentence)
            so_types = predictor_wikidata.predict_raw(sents)
            #print("SO_TYPES:", so_types)
            stypes = so_types[0].wd_types
            stypes = [{'wd_qid': stype.wd_qid, 'wd_label': stype.wd_label, 'description': stype.description} for stype in stypes]
            otypes = so_types[1].wd_types
            otypes = [{'wd_qid': otype.wd_qid, 'wd_label': otype.wd_label, 'description': otype.description} for otype in otypes]
            #print("STYPES:", stypes)
            #print("OTYPES:", otypes)
            subject_types.append(stypes)
            object_types.append(otypes)
        #return subject_types, object_types
        # Add the two columns 'subject_types' and 'object_types' to ed_result as the entity typing result.
        ed_result['subject_types'] = subject_types
        ed_result['object_types'] = object_types
        return ed_result
            
    else:
        raise ValueError("Invalid mode! Mode can be either 'ufet' or 'wikidata'!")
    
    
def predict(input_path:str, output_path:str, mode:Optional[Union['ufet', 'wikidata']]):
    """
    Run predict.py:
    python predict_2.py -i /mount/studenten/arbeitsdaten-studenten1/semantic-plausibility/plausible-parrots/3-event_extraction/glen/ED/output/ -o ./output_2/ -m wikidata
    """
    
    def _create_output_file_name(input_file:str, mode:Optional[Union['ufet', 'wikidata']]):
        fn = input_file.split('/')[-1]
        fn = fn.split('.')[0]
        fn = fn.split('_')
        fn = '_'.join([fn[1], fn[2]])
        fn = f"et_{fn}_{mode}.csv"
        return fn
    
    for root, dirs, files in os.walk(input_path):
        for file in files:
            if file.endswith('.csv'):
                print(file)
                fp = root + file
                output_fn = _create_output_file_name(fp, mode=mode)
                et_result = entity_typing(fp, mode=mode)
                et_result.to_csv(output_path+output_fn, index=False)
                
    
    
    
parser = ArgumentParser()
parser.add_argument('-i', '--input_dir', type=str, help='path to the input data folder')
parser.add_argument('-o', '--output_dir', type=str, help='path to the output data folder')
parser.add_argument('-m', '--mode', type=str, help="the type set used for entity typing, can be either 'ufet' or 'wikidata'")

args = parser.parse_args()

# Print statements to check the values of the arguments.
print("Input Directory:", args.input_dir)
print("Output Directory:", args.output_dir)
print("Mode:", args.mode)

predict(input_path=args.input_dir, output_path=args.output_dir, mode=args.mode)
