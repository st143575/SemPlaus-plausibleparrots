# Data Analysis
The implementations of data analysis are saved as jupyter notebooks (.ipynb). In the statistical analysis, we analyze common data statistics for the four datasets Adept, Ellie, PaP and PeP-3k. For each data split (train, eval/dev, test) of each dataset, we analyze the following characteristics:

## Statistical Analysis
  - Number of examples
  - Number of each feature (given by column name, e.g., sentence1, sentence2, modifier etc. in Adept), with and without duplicates
  - Average length, minimal length, maximal length, variance, and standard deviation of textual features (e.g., sentence1 in Adept), tokenized using BERT tokenizer
  - Frequency and distribution of features with duplicated instances (e.g., modifiers, nouns and labels in Adept)

  Please check the following notebooks for details:
  
    - `./data_statistics/adept/datastatistic_adept_train.ipynb`
    - `./data_statistics/adept/datastatistic_adept_dev.ipynb`
    - `./data_statistics/adept/datastatistic_adept_test.ipynb`
    - `./data_statistics/ellie/datastatistic_ellie.ipynb`
    - `./data_statistics/pap/datastatistic_pap_train.ipynb`
    - `./data_statistics/pap/datastatistic_pap_val.ipynb`
    - `./data_statistics/pap/datastatistic_pap_test.ipynb`
    - `./data_statistics/pep-3k/datastatistic_pep3k_train.ipynb`
    - `./data_statistics/pep-3k/datastatistic_pep3k_dev.ipynb`
    - `./data_statistics/pep-3k/datastatistic_pep3k_test.ipynb`

## Linguistic Analysis
  - Stop words
  - N-grams
  - Part-Of-Speech (POS) tags
  - Wordcloud that illustrates the most frequent words associated with plausible label and implausible label, respectively.
  - Semantic similarities between words. This could help identify whether certain types of verbs or objects are more associated with plausible or implausible labels.

  Please check `./data_analysis_linguistic.ipynb` for details.

Note: The `PROJECT_PATH` in the notebooks is set to '<root_dir_of_this_repo>' which indicates the root path of this repo. After cloning it to your computer, please set it to '<path_to_this_repo>/SemPlaus-plausibleparrots/'.





