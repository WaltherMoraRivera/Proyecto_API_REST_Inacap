@echo off
echo ========================================
echo   FIX: Actualizar Password Admin
echo ========================================
echo.
echo Este script corrige el problema de password
echo actualizando el hash SHA-256 en la base de datos
echo.
echo Usuario: admin
echo Password: admin123
echo.
pause
echo.
echo Ejecutando script de actualizacion...
echo.

cd /d "%~dp0webApiRestFul\sql"

sqlplus -S admin/Zayrus189918143@basedatos699_medium @FIX_actualizar_password_admin.sql

echo.
echo ========================================
echo   PASSWORD ACTUALIZADO
echo ========================================
echo.
echo Ahora intenta hacer login nuevamente con:
echo Usuario: admin
echo Password: admin123
echo.
pause
