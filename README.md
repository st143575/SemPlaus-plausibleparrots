# SemPlaus-plausibleparrots
Modeling Semantic Plausibility WS23/24.

## Usage

### Virtual Environment
Create and activate a conda environment.
```bash
conda create -n <environment_name>
conda activate <environment_name>
```

Install pip in the conda env.
```bash
conda install pip
```

### Installation
Make sure you have the following dependencies installed.
- Python 3.11.7
  - Everything in requirements.txt by running
    ```bash
    pip install -r requirements.txt
    ```
    
### Data Analysis
Please follow the instructions in `./0-preliminary_study/` for data analysis.

### Data Preprocessing and Data Augmentation
Please follow the instructions in `./1-data_preprocessing` for data preprocessing and augmentation.

### Baselines
We evaluate two baseline systems on our task: (1) zero-shot inference; and (2) fine-tuning on the sentences preprocessed and augmented from the original (s,v,o)-event triples.
To run the baselines, please follow the instructions in `./2-baselines/`.

### Event Detection
TBD

### Ultra Fine-grained Entity Typing
TBD

### Dataset Construction
We construct the datasets for our system using the templates specifically designed for (1) injecting both event and entity type knowledge (evt+ent), (2) injecting only event type knowledge (evt), and (3) injecting only entity types knowledge (ent), respectively. Please follow the instructions in `./5-dataset_construction/`.

### Fine-tune and Evaluate Our System
We fine-tune and evaluate our system with the knowledge-enhanced datasets.
Please follow the instructions in `./6-finetune_and_eval/`.
