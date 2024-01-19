# Baselines
## Zero-shot Inference with RoBERTa
### Results
<div  align="center">    
<img src="./img/eval_scores_pap_baseline_zeroshot.png" width="45%"/>
<img src="./img/eval_scores_pep_baseline_zeroshot.png" width="45%"/>
</div>
<div  align="center">    
<img src="./img/eval_scores_pap_baseline_ft_ckpt-1842.png" width="45%"/>
<img src="./img/eval_scores_pep_baseline_ft_ckpt-1842.png" width="45%"/>
</div>

### Evaluates Roberta in a zero-shot manner, we use this system as a baseline model.
### When running this script, remember to configure the data path with your directory.
## Finetuning with labelled data.ipynb
### We finedtuend Roberta with PAP and PEP-3k datasets
### When running this script, remember to configure the data path with your directory.
## Datasets
### The finetuning datasets can be found under datasets/preprocessed/baseline
