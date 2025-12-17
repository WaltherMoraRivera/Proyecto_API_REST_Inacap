# 🚀 INICIO RÁPIDO - Sistema Festival de Cine

## ⚡ Solución al Error de Conexión

El error que viste ocurre cuando el cliente PyQt6 intenta conectarse a la API pero esta no está corriendo.

### ✅ SOLUCIÓN:

Debes mantener **DOS aplicaciones corriendo simultáneamente**:

1. **API FastAPI** (Backend) - Puerto 8000
2. **Cliente PyQt6** (Frontend) - Interfaz gráfica

---

## 📋 Forma 1: Usando Scripts Batch (RECOMENDADO)

### Paso 1: Iniciar la API
```
Doble click en: 1_Iniciar_API.bat
```
- Se abrirá una ventana negra
- Verás: "Uvicorn running on http://0.0.0.0:8000"
- **NO CIERRES ESTA VENTANA**

### Paso 2: Iniciar el Cliente
```
Doble click en: 2_Iniciar_Cliente.bat
```
- Se abrirá la ventana de login
- Ingresa: usuario=`admin`, password=`admin123`
- ¡Listo!

---

## 📋 Forma 2: Usando PowerShell Manual

### Terminal 1 - API (dejar corriendo)
```powershell
cd "c:\Users\Walther\Desktop\INACAP\Progra_de_Objetos\Proyecto API\Proyecto_API_Rest_Inacap\webApiRestFul"
python main.py
```
**⚠️ NO CERRAR - Debe quedar corriendo**

### Terminal 2 - Cliente (nueva terminal)
```powershell
cd "c:\Users\Walther\Desktop\INACAP\Progra_de_Objetos\Proyecto API\Proyecto_API_Rest_Inacap\pyqt6"
python main.py
```

---

## 🔍 Verificar que la API esté corriendo

Antes de ejecutar el cliente, verificar en navegador:
- http://localhost:8000 - Debe mostrar JSON con info de la API
- http://localhost:8000/docs - Debe mostrar Swagger UI

Si no funcionan, la API no está corriendo.

---

## 🔐 Credenciales

- **Usuario**: admin
- **Contraseña**: admin123

---

## 🐛 Troubleshooting

### Error: "Max retries exceeded"
➡️ **Causa**: La API no está corriendo
➡️ **Solución**: Ejecutar `1_Iniciar_API.bat` primero

### Error: "Connection refused" o "10061"
➡️ **Causa**: Puerto 8000 no está escuchando
➡️ **Solución**: Reiniciar la API

### Error: "Usuario no existe"
➡️ **Causa**: Las tablas de BD no están creadas
➡️ **Solución**: Ejecutar scripts SQL primero

---

## 📊 Arquitectura

```
Cliente PyQt6  ─────HTTP────►  API FastAPI  ─────SQL────►  Oracle DB
 (puerto N/A)                   (puerto 8000)              (basedatos699)
```

**Ambos deben estar corriendo simultáneamente**

---

## ✅ Checklist de Ejecución

- [ ] API corriendo (Terminal 1 o 1_Iniciar_API.bat)
- [ ] Ver "Uvicorn running on http://0.0.0.0:8000"
- [ ] Abrir http://localhost:8000 en navegador (debe responder)
- [ ] Ejecutar cliente PyQt6 (Terminal 2 o 2_Iniciar_Cliente.bat)
- [ ] Login con admin/admin123
- [ ] ¡Usar el sistema!

---

## 🎯 Estado Actual

✅ API configurada correctamente
✅ Cliente PyQt6 configurado
✅ Archivos batch creados
⚠️ Base de datos Oracle (verificar tablas)

**La API está corriendo AHORA en tu terminal**
**El cliente está listo para ejecutarse**
