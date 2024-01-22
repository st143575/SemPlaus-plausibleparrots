# Event Detection

We use CEDAR trained on the GLEN benchmark. Please follow the instructions in their official [GitHub repo](https://github.com/ZQS1943/GLEN).

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
- Python 3.11.5
  - Everything in requirements_ed.txt by running
    ```bash
    pip install -r requirements_ed.txt
    ```
    
### Predict
For Pap, run ```bash
    python ed_pap_2.py
    ```
    
For Pep, run ```bash
    python ed_pep_2.py
    ```
