# Gesture mapper

# Installation Instructions

1. Clone the git repo:
```bash
git clone git@github.com:kshitijaucharmal/GestureMapper.git
cd GestureMapper
```

2. Checkout to new branch
```bash
git checkout -b branchname
```

3. Setup python env
```bash
python -m venv .

source bin/activate # <-- on Mac/linux
source Scripts/activate  # <-- on windows

pip install -r requirements.txt
```

## Usage

1. Start training
```
python src # Ctrl-C to quit
```

2. Record:
```bash
python src/record.py
```
- Enter a label for data to record (peace, palm etc.)
- Hold r to record

3. Test after collecting data
- First train.
- Same Steps as record, but gestures without holding r will show detected gesture

