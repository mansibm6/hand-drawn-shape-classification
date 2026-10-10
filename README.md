# Hand-drawn shape classification

Trains a three-class CNN for circles, squares, and triangles using 28×28 RGB images.

## Setup and execution

Use Python 3.11 and a separate virtual environment for this project. Run commands from this folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python check_inputs.py
python -m jupyterlab
```

On Windows, activate with `.venv\Scripts\activate`. For notebooks, select this environment’s kernel and execute from the top in a fresh kernel. The first code cell exposes `INPUT_PATHS` where old machine-specific paths existed. `PROJECT_DATA_DIR` changes the base for those configured paths; remaining relative paths use the notebook working directory.

## Notebooks

- [Shape Classifier.ipynb](Shape%20Classifier.ipynb)

## Inputs

Supply these inputs yourself; no dataset is downloaded automatically:

- `data/train/`
- `data/validation/`
- `data/test/`

## Outputs

An in-memory model, training history, and predicted labels for test images.

## Implementation and limitations

Put class subdirectories under train and validation, and individual images under test. Validation now has its own directory rather than reusing training images. Prediction uses the training rescaling and argmax instead of requiring probabilities to equal exactly one.

Reusable model/analysis functions live in `experiment_shape_classifier.py`. Notebooks retain the experiment sequence, training, and visual narrative.

## Verification

The workspace regression suite checks source/notebook validity and selected behavior with bundled or synthetic inputs. Full experiment training and historical metric reproduction are not implied. See the workspace `REFACTOR_REPORT.md` for exact test coverage and unresolved runtime requirements.

## Original references

These links were retained from the original project notes; availability and licensing must be checked by the person obtaining the data.

- https://www.kaggle.com/cactus3/basicshapes
