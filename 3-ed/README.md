# Event Detection

We use CEDAR trained on the GLEN benchmark. Please follow the instructions in their official [GitHub repo](https://github.com/ZQS1943/GLEN).

## Usage

### Virtual Environment
Create and activate a conda environment.
```bash
conda create -n glen python=3.11
conda activate glen
```

Install pip in the conda env.
```bash
conda install pip
```

### Installation
Run
```bash
pip install -r requirements_ed.txt --no-cache-dir
```
    
### Predict
For Pap, run ```bash
    python ed_pap_2.py
    ```
    
For Pep, run ```bash
    python ed_pep_2.py
    ```
