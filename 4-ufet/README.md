# Ultra Fine-grained Entity Typing (UFET)
We use CASENT for UFET. Please follow the instructions in their official [GitHub repo](https://github.com/yanlinf/CASENT).

## Usage
### Virtual Environment
Create and activate a conda environment.
```bash
conda create -n casent python=3.10
conda activate casent
git clone https://github.com/yanlinf/CASENT.git
cd CASENT
```

Install pip in the conda env.
```bash
conda install pip
```

### Installation
Make sure you have the following dependencies installed.
- Python 3.11.5
  - Everything in requirements_et.txt by running
    ```bash
    pip install -r requirements_et.txt --no-cache-dir
    ```
    
### Predict
