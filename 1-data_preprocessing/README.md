# Data Preprocessing and Data Augmentation
We preprocess the data by concatenating the subject, verb and object of each (s,v,o)-event triple, uppercasing the first character of the subject and adding a full stop "." at the end of the object.
To mitigate the label imbalance issue in the Pap dataset, we perform data augmentation by sampling implausible examples from the multiclass data.

- For data preprocessing, run `python ./preprocessing.py`
- For data augmentation on Pap, run the code in `./data_augmentation/data_augmentation.ipynb`
