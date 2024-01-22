# Ultra Fine-grained Entity Typing (UFET)
We use CASENT for UFET. Please follow the instructions in their official [GitHub repo](https://github.com/yanlinf/CASENT).

## Usage
Create and activate a conda environment.
```bash
conda create -n casent python=3.10
conda activate casent
```

Clone the CASENT repository and specify the paths.
```bash
git clone https://github.com/yanlinf/CASENT.git
cd CASENT
mkdir Experiments
cd Experiments
mv ../../predict_2.py ./
mv ../../requirements_et.txt ./
```

Install dependencies and CASENT.
```bash
conda install pip --no-cache-dir
pip install -r requirements_et.txt --no-cache-dir
```

### Predict
```bash
python predict_2.py -i ./input/ -o ./output_2/ -m wikidata
```
