# 🚀 GUÍA DE EJECUCIÓN - Sistema de Gestión de Festival de Cine

## ✅ Estado Actual del Sistema

### API FastAPI (Backend)
- **Estado**: ✅ CORRIENDO
- **URL**: http://localhost:8000
- **Documentación Swagger**: http://localhost:8000/docs
- **Puerto**: 8000

### Base de Datos Oracle
- **Estado**: ⚠️ PENDIENTE CONFIGURACIÓN
- **Conexión configurada**: Sí (basedatos699_medium)
- **Tablas creadas**: Pendiente de verificación

### Cliente PyQt6
- **Estado**: ✅ LISTO PARA EJECUTAR
- **Archivo principal**: pyqt6/main.py

---

## 📋 Pasos para Usar el Sistema

### 1. API FastAPI (Ya está corriendo)

La API ya está ejecutándose en segundo plano. Puedes acceder a:

- **Documentación interactiva**: http://localhost:8000/docs
- **API alternativa**: http://localhost:8000/redoc
- **Endpoint raíz**: http://localhost:8000/

### 2. Verificar Base de Datos

#### Opción A: Si tienes Oracle configurado

```powershell
# Ejecutar scripts SQL en orden (desde SQL*Plus o SQL Developer)
sqlplus admin/Zayrus189918143@basedatos699_medium

# Luego ejecutar en orden:
@webApiRestFul\sql\01_create_tables.sql
@webApiRestFul\sql\02_create_audit_tables.sql
@webApiRestFul\sql\03_create_triggers.sql
@webApiRestFul\sql\04_create_stored_procedures_crud.sql
@webApiRestFul\sql\05_create_stored_procedures_auth.sql
@webApiRestFul\sql\06_create_stored_procedures_transactions.sql
@webApiRestFul\sql\07_insert_sample_data.sql
```

#### Opción B: Verificar que ya están creadas

La API intentará conectarse automáticamente cuando se haga una petición.

### 3. Ejecutar Cliente PyQt6

```powershell
cd pyqt6
python main.py
```

**Credenciales de prueba**:
- Usuario: `admin`
- Contraseña: `admin123`

---

## 🔧 Probar la API (Sin Cliente PyQt6)

### Usando Swagger UI (Recomendado)

1. Abrir http://localhost:8000/docs
2. Ir a la sección **Autenticación**
3. Click en `POST /auth/login`
4. Click en "Try it out"
5. Ingresar:
   ```json
   {
     "username": "admin",
     "password": "admin123"
   }
   ```
6. Click en "Execute"
7. Copiar el `access_token` de la respuesta
8. Click en "Authorize" (candado arriba a la derecha)
9. Pegar el token: `Bearer <token_copiado>`
10. Ahora puede probar los endpoints de películas

### Usando PowerShell/cURL

```powershell
# 1. Login
$response = Invoke-RestMethod -Uri "http://localhost:8000/auth/login" -Method Post -ContentType "application/json" -Body '{"username":"admin","password":"admin123"}'
$token = $response.access_token

# 2. Listar películas
$headers = @{
    "Authorization" = "Bearer $token"
}
Invoke-RestMethod -Uri "http://localhost:8000/peliculas/" -Headers $headers
```

---

## 🎯 Endpoints Disponibles

### Autenticación (No requiere token)
- `POST /auth/login` - Iniciar sesión
- `POST /auth/register` - Registrar usuario

### Películas (Requiere token)
- `GET /peliculas/` - Listar todas
- `GET /peliculas/{id}` - Obtener por ID
- `POST /peliculas/` - Crear nueva
- `PUT /peliculas/{id}` - Actualizar
- `DELETE /peliculas/{id}` - Eliminar (solo admin)

### Salud del sistema
- `GET /` - Info de la API
- `GET /health` - Estado del servidor

---

## ⚠️ Notas Importantes

### Si la base de datos no está configurada aún:

La API se ejecuta pero los endpoints fallarán con error de conexión. Para solucionar:

1. **Opción 1**: Ejecutar los scripts SQL en Oracle
2. **Opción 2**: Modificar temporalmente para usar datos en memoria (mock)

### Archivos de configuración:

- **API**: `webApiRestFul/config/settings.json`
- **PyQt6**: `pyqt6/config/settings.json`

Ambos ya están configurados con:
- Usuario: admin
- DSN: basedatos699_medium
- Wallet: C:\Users\Walther\Desktop\INACAP\Progra_de_Objetos\proyectoPyQt6\Wallet

---

## 📱 Usar el Sistema Completo

### Flujo Normal:

1. ✅ **API corriendo** (Ya está activa)
2. ⚠️ **Base de datos configurada** (Verificar)
3. ▶️ **Ejecutar cliente PyQt6**:
   ```powershell
   cd pyqt6
   python main.py
   ```
4. 🔐 **Login** con admin/admin123
5. 📋 **Gestionar películas** desde la interfaz gráfica

---

## 🐛 Troubleshooting

### Error: "Connection refused"
- Verificar que la API esté corriendo en http://localhost:8000
- Verificar el puerto en `pyqt6/config/settings.json`

### Error: "ORA-xxxxx" (Oracle)
- Verificar credenciales en `config/settings.json`
- Verificar que Oracle esté corriendo
- Ejecutar scripts SQL si las tablas no existen

### Error: "Token inválido"
- El token expira en 60 minutos
- Cerrar sesión y volver a iniciar

---

## 📊 Estructura de Datos

### Usuario de Prueba (después de ejecutar SQL):
- Username: `admin`
- Password: `admin123` (hash en BD)
- Rol: `admin`

### Películas de Ejemplo:
- El Viaje (Chile)
- Sueños del Mar (Argentina)
- Luz en la Oscuridad (Perú)
- Camino al Futuro (Chile)
- Risas Eternas (México)

---

## 🎉 ¡Sistema Listo!

La API está **corriendo correctamente**. Solo falta:

1. Verificar que las tablas de Oracle estén creadas
2. Ejecutar el cliente PyQt6
3. ¡Disfrutar del sistema!

Para detener la API:
```
Ctrl+C en la terminal donde está corriendo
```
