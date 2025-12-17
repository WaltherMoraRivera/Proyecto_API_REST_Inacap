-- ===========================================
-- FIX: Actualizar password del usuario admin
-- Este script actualiza la contraseña hasheada
-- ===========================================

-- Actualizar contraseña de admin (admin123 hasheado)
UPDATE usuario 
SET password_hash = '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9'
WHERE username = 'admin';

-- Actualizar contraseña de usuario1 (user123 hasheado)
UPDATE usuario 
SET password_hash = 'f03881a88c6e39135f0ecc60efd609131b36a9d4a57a3e8b80ab7ad8ab5d1e13'
WHERE username = 'usuario1';

COMMIT;

-- Verificar que se actualizó correctamente
SELECT username, password_hash, nombre_completo, rol 
FROM usuario 
WHERE username IN ('admin', 'usuario1');
