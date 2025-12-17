@echo off
echo ========================================
echo   EJECUTAR SCRIPTS SQL EN ORACLE
echo ========================================
echo.
echo IMPORTANTE: Este comando ejecutara todos los scripts SQL
echo en tu base de datos Oracle Autonomous.
echo.
echo Base de datos: basedatos699_medium
echo Usuario: admin
echo.
pause
echo.
echo Ejecutando scripts SQL...
echo.

cd /d "%~dp0webApiRestFul\sql"

echo [1/7] Creando tablas principales...
sqlplus -S admin/Zayrus189918143@basedatos699_medium @01_create_tables.sql

echo [2/7] Creando tablas de auditoria...
sqlplus -S admin/Zayrus189918143@basedatos699_medium @02_create_audit_tables.sql

echo [3/7] Creando triggers...
sqlplus -S admin/Zayrus189918143@basedatos699_medium @03_create_triggers.sql

echo [4/7] Creando stored procedures CRUD...
sqlplus -S admin/Zayrus189918143@basedatos699_medium @04_create_stored_procedures_crud.sql

echo [5/7] Creando stored procedures autenticacion...
sqlplus -S admin/Zayrus189918143@basedatos699_medium @05_create_stored_procedures_auth.sql

echo [6/7] Creando stored procedures transacciones...
sqlplus -S admin/Zayrus189918143@basedatos699_medium @06_create_stored_procedures_transactions.sql

echo [7/7] Insertando datos de prueba...
sqlplus -S admin/Zayrus189918143@basedatos699_medium @07_insert_sample_data.sql

echo.
echo ========================================
echo   SCRIPTS EJECUTADOS EXITOSAMENTE
echo ========================================
echo.
echo Ahora puedes ejecutar la API y el cliente.
echo.
pause
