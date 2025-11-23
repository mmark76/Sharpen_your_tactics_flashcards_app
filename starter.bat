@echo off
cd "%~dp0"

echo Starting local server on http://localhost:8000 ...
start "" http://localhost:8000/index.html

python -m http.server 8000
