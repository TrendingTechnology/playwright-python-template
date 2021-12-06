CD ..
CALL venv\Scripts\activate
SET PLAYWRIGHT_BROWSERS_PATH=0
FOR /F %%i IN ('python -c "import yaml; CONFIG = yaml.load(open('config.yml'), Loader=yaml.SafeLoader); print(CONFIG['start_page'])"') DO SET START_PAGE=%%i
CALL playwright codegen %START_PAGE%
PAUSE
