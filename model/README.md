# Model Weights

The trained model isn't committed to this repo directly — it's excluded in `.gitignore` since `.keras` files are large.

## Download

- **bone_break_classifier.keras** — [Download from Releases](https://github.com/i0nlyaziz/Bone-Fracture-Classification-System/releases/download/v1.0/bone_break_classifier.keras)

## Using the model

1. Download `bone_break_classifier.keras` from the link above and place it in this `model/` folder.
2. `main.py` loads it directly with `tf.keras.models.load_model('model/bone_break_classifier.keras')` — no conversion step is required.
3. Update the path in `main.py` if you place the file somewhere other than `model/`.