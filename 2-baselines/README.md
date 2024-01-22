# Baselines
## Zero-shot Inference with RoBERTa
Run RoBERTa for zero-shot inference.
### Usage
Run the code in `baseline_zeroshot.ipynb`
### Results
<div  align="center">    
<img src="./img/eval_scores_pap_baseline_zeroshot.png" width="45%"/>
<img src="./img/eval_scores_pep_baseline_zeroshot.png" width="45%"/>
</div>

## Fine-tune RoBERTa on (s,v,o)-Events
Fine-tune RoBERTa on the augmented, preprocessed (s,v,o)-events, without injecting event type and entity type knowledge.
### Usage
Run the code in `baseline_finetune_3.ipynb`
### Results
<div  align="center">    
<img src="./img/eval_scores_pap_baseline_ft_ckpt-1842.png" width="45%"/>
<img src="./img/eval_scores_pep_baseline_ft_ckpt-1842.png" width="45%"/>
</div>
