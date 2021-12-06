CD ..
CALL python -m venv venv
CALL venv\Scripts\activate
CALL pip install playwright pyinstaller pyyaml
SET PLAYWRIGHT_BROWSERS_PATH=0
CALL playwright install chromium
PAUSE
