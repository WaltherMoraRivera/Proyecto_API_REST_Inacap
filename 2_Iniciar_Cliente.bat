@echo off
echo ========================================
echo  Sistema Festival de Cine - Cliente
echo ========================================
echo.
echo Asegurese de que la API este corriendo!
echo (Ejecute primero 1_Iniciar_API.bat)
echo.
timeout /t 3
echo Iniciando cliente PyQt6...
echo.
cd /d "%~dp0pyqt6"
python main.py
pause
