# 🗄️ CONFIGURACIÓN DE BASE DE DATOS ORACLE

## 🚨 ERROR ACTUAL

```
ORA-06550: PLS-00905: object ADMIN.SP_LOGIN is invalid
```

**Causa**: Los stored procedures y tablas no existen en la base de datos Oracle.

**Solución**: Ejecutar los scripts SQL para crear la estructura de la base de datos.

---

## ✅ OPCIÓN 1: Ejecutar con Script Batch (RECOMENDADO)

### Paso único:
```
Doble click en: EJECUTAR_SCRIPTS_SQL.bat
```

Este script ejecutará automáticamente los 7 archivos SQL en orden:
1. ✅ Tablas principales (PELICULA, FUNCION, USUARIO, etc.)
2. ✅ Tablas de auditoría (bitácoras)
3. ✅ Triggers para auditoría automática
4. ✅ Stored Procedures CRUD
5. ✅ Stored Procedures de autenticación (SP_LOGIN, SP_REGISTER)
6. ✅ Stored Procedures de transacciones
7. ✅ Datos de prueba (usuario admin/admin123)

---

## ✅ OPCIÓN 2: Ejecutar Manualmente con SQL*Plus

### Requisitos:
- Oracle Instant Client instalado
- SQL*Plus disponible en PATH
- Wallet configurado en: `C:\Users\Walther\Desktop\INACAP\Progra_de_Objetos\proyectoPyQt6\Wallet`

### Comandos:

```powershell
cd "c:\Users\Walther\Desktop\INACAP\Progra_de_Objetos\Proyecto API\Proyecto_API_Rest_Inacap\webApiRestFul\sql"

# Ejecutar cada script en orden
sqlplus admin/Zayrus189918143@basedatos699_medium @01_create_tables.sql
sqlplus admin/Zayrus189918143@basedatos699_medium @02_create_audit_tables.sql
sqlplus admin/Zayrus189918143@basedatos699_medium @03_create_triggers.sql
sqlplus admin/Zayrus189918143@basedatos699_medium @04_create_stored_procedures_crud.sql
sqlplus admin/Zayrus189918143@basedatos699_medium @05_create_stored_procedures_auth.sql
sqlplus admin/Zayrus189918143@basedatos699_medium @06_create_stored_procedures_transactions.sql
sqlplus admin/Zayrus189918143@basedatos699_medium @07_insert_sample_data.sql
```

---

## ✅ OPCIÓN 3: Usando SQL Developer (Interfaz Gráfica)

### Pasos:

1. **Abrir Oracle SQL Developer**

2. **Crear Conexión:**
   - Connection Name: `Festival_Cine`
   - Usuario: `admin`
   - Contraseña: `Zayrus189918143`
   - Connection Type: `Cloud Wallet`
   - Configuration File: `C:\Users\Walther\Desktop\INACAP\Progra_de_Objetos\proyectoPyQt6\Wallet\Wallet_basedatos699.zip`
   - Service: `basedatos699_medium`

3. **Conectar** (botón Test Connection → Connect)

4. **Ejecutar Scripts:**
   - File → Open → Seleccionar `01_create_tables.sql`
   - Presionar F5 (Run Script)
   - Repetir con los archivos 02 al 07 EN ORDEN

---

## 📋 Archivos SQL y su Propósito

| Archivo | Descripción | Objetos Creados |
|---------|-------------|-----------------|
| `01_create_tables.sql` | Tablas principales | PELICULA, FUNCION, USUARIO, SALA, etc. (11 tablas) |
| `02_create_audit_tables.sql` | Tablas de bitácora | BITACORA_PELICULA, BITACORA_FUNCION, etc. (5 tablas) |
| `03_create_triggers.sql` | Triggers de auditoría | 15 triggers para INSERT/UPDATE/DELETE |
| `04_create_stored_procedures_crud.sql` | Procedimientos CRUD | SP_INSERTAR_PELICULA, SP_ACTUALIZAR_PELICULA, etc. |
| `05_create_stored_procedures_auth.sql` | Procedimientos auth | **SP_LOGIN**, SP_REGISTER, SP_CAMBIAR_PASSWORD |
| `06_create_stored_procedures_transactions.sql` | Procedimientos transacciones | SP_CREAR_FUNCION_CON_VENTA, etc. |
| `07_insert_sample_data.sql` | Datos de prueba | Usuario admin, películas, salas, funciones |

---

## 🔐 Credenciales de Conexión

```
Usuario:    admin
Contraseña: Zayrus189918143
DSN:        basedatos699_medium
Wallet:     C:\Users\Walther\Desktop\INACAP\Progra_de_Objetos\proyectoPyQt6\Wallet
```

---

## ✅ Verificar que se Creó Correctamente

Después de ejecutar los scripts, verifica con:

```sql
-- Ver todas las tablas
SELECT table_name FROM user_tables ORDER BY table_name;

-- Ver stored procedures
SELECT object_name FROM user_procedures WHERE object_type = 'PROCEDURE' ORDER BY object_name;

-- Ver triggers
SELECT trigger_name FROM user_triggers ORDER BY trigger_name;

-- Verificar usuario admin
SELECT * FROM USUARIO WHERE usuario = 'admin';
```

Deberías ver:
- ✅ 16 tablas (11 principales + 5 bitácoras)
- ✅ ~15 stored procedures
- ✅ 15 triggers
- ✅ 1 usuario admin con rol 'admin'

---

## 🎯 Después de Ejecutar los Scripts

Una vez completada la creación de la base de datos:

1. ✅ **Reiniciar la API** (si estaba corriendo)
   ```
   1_Iniciar_API.bat
   ```

2. ✅ **Ejecutar el Cliente PyQt6**
   ```
   2_Iniciar_Cliente.bat
   ```

3. ✅ **Login exitoso** con:
   - Usuario: `admin`
   - Contraseña: `admin123`

---

## 🐛 Troubleshooting

### Error: "SP_LOGIN is invalid"
➡️ No ejecutaste el script `05_create_stored_procedures_auth.sql`

### Error: "Table or view does not exist"
➡️ No ejecutaste el script `01_create_tables.sql`

### Error: "TNS:could not resolve the connect identifier"
➡️ Verifica que el Wallet esté en la ruta correcta y TNS_ADMIN esté configurado

### Error: "ORA-01017: invalid username/password"
➡️ Verifica las credenciales: admin/Zayrus189918143

---

## 📝 Notas Importantes

- ⚠️ Los scripts son **idempotentes parcialmente**: algunos objetos tienen `DROP ... IF EXISTS`, otros no
- ⚠️ Si ejecutas dos veces, puede haber errores de "object already exists" (es normal, puedes ignorarlos)
- ⚠️ El orden de ejecución **ES CRÍTICO**: las tablas deben existir antes que los triggers y procedures
- ✅ El script 07 inserta el usuario admin con password hasheado correctamente
