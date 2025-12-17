@echo off
echo ========================================
echo    Sistema Festival de Cine - API
echo ========================================
echo.
echo Iniciando API FastAPI en puerto 8000...
echo.
cd /d "%~dp0webApiRestFul"
python main.py
pause
