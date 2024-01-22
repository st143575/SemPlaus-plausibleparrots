The labels for this dataset are based on 

#### MACE Silver Aggregations 
The folder ```mace_aggregations```: contains the following files and information.

The file ```aggregated_predictions.tsv```: encompasses:
- event: the event target as presented to human annotators
- original_label: the original label based on dataset construction as described in §3 in the paper; events can be either plausible ('plausible') or implausible ('implausible')
- multi-class_prediction: predicted multi-class labels using MACE (Hovy et al., 2013) using standard parameters; labels range from 1 to 5 with 1 denoting implausibility, 5 referring to plausibility, and ratings of 3 used for filtering out invalid submissions
- binary_prediction: predicted binary labels using the MACE implementation by Hovy et al., 2013 using standard parameters; 0 denotes implausibility and 1 denotes plausibility

For binary labels, MACE binary predictions are used. 
For the multi-class setup, MACE multi-class predictions are used.

For further details on the raw annotations, please refer to the README in the directory ```raw-annotations```.