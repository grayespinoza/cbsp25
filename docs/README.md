# Cal-Bridge Summer Program

## Usage

### MSS
> [!IMPORTANT]
> MSS currently does not support Wayland, use X11 when running this script.

Setup Virtual Environment
```shell
cd src/
python -m venv mss
source mss/bin/activate
pip install opencv-python mss
```

Use Script
```shell
cd src/
source mss/bin/activate
python mss/screenshot.py
```

Exit Virtual Environment
```shell
deactivate
```
