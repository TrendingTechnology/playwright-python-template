<div align="center">

# Playwright-python template 🍪

Template to quickly start your playwright-python project

[Getting started](#getting-started) •
[Demo](#demo) •
[Configuration](#configuration) 

</div>

## Getting started

1. Clone the repository:
```cmd
git clone https://github.com/constantbratu/playwright-python-template.git
cd playright-python-template
```

2. Set up the virtual environment:
```cmd
python -m venv venv
venv\Scripts\activate
pip install playwright pyinstaller pyyaml
```

3. Set up the environment variable and install chromium:
```cmd
SET PLAYWRIGHT_BROWSERS_PATH=0
playwright install chromium
```

4. Configure the project using the provided `config.yaml` file

5. Start recording the session using:
```
playwright codegen <start_page>
```

6. Copy the generated async code into `main.py`:

```python
async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(
        headless=CONFIG["headless"],
        executable_path=get_executable_path(),
        args=CONFIG["chromium_args"],
    )
    context = await browser.new_context(viewport=None)

    global page
    page = await context.new_page()
    page.set_default_timeout(CONFIG["default_timeout"])

    await page.goto(CONFIG["start_page"])
    
    # ---> GENERATED CODE GOES HERE <---

    await context.close()
    await browser.close()
```

7. Compile the project and bundle the chromium binary via `pyinstaller` using the provided spec file:
```
pyinstaller --noconfirm build.spec
```

To save time, 3 scripts have been added to the repository:

- `init_venv.bat` to set up the environment and download all the required files
- `codegen.bat` to start the recording session
- `build.bat` to compile the project

## Demo
...

## Configuration

Edit `config.yml` to change the project settings:

```yaml
start_page: https://www.google.com/  # <str> sets the initial page; changing this key will also affect `codegen.bat`

headless: false  # <bool> if the browser should run in headless mode
default_timeout: 5000  # <int> maximum time to wait for the page to load (in milliseconds)
chromium_args:  # <list[str]> list of chromium command line switches
    - --window-size=800,600
    - --user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36
```
A list of chromium command line switches can be found [here](https://peter.sh/experiments/chromium-command-line-switches/). Note that more options will also be added in the future.
