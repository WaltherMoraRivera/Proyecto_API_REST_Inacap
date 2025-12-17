-- ===========================================
-- STORED PROCEDURES - AUTENTICACIÓN Y USUARIOS
-- ===========================================

-- Procedimiento: Crear usuario (con hash de contraseña)
CREATE OR REPLACE PROCEDURE sp_crear_usuario (
    p_username IN VARCHAR2,
    p_password_hash IN VARCHAR2,
    p_nombre_completo IN VARCHAR2,
    p_email IN VARCHAR2,
    p_rol IN VARCHAR2 DEFAULT 'usuario',
    p_id_usuario OUT NUMBER
) AS
BEGIN
    INSERT INTO usuario (
        username, password_hash, nombre_completo,
        email, rol, activo
    ) VALUES (
        p_username, p_password_hash, p_nombre_completo,
        p_email, p_rol, 1
    ) RETURNING id_usuario INTO p_id_usuario;
    
    COMMIT;
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
        ROLLBACK;
        RAISE_APPLICATION_ERROR(-20010, 'El username o email ya existe');
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

-- Procedimiento: Login (verificar credenciales)
CREATE OR REPLACE PROCEDURE sp_login (
    p_username IN VARCHAR2,
    p_password_hash IN VARCHAR2,
    p_id_usuario OUT NUMBER,
    p_nombre_completo OUT VARCHAR2,
    p_email OUT VARCHAR2,
    p_rol OUT VARCHAR2,
    p_resultado OUT VARCHAR2
) AS
    v_stored_hash VARCHAR2(255);
    v_activo NUMBER;
BEGIN
    -- Buscar usuario
    SELECT id_usuario, password_hash, nombre_completo, email, rol, activo
    INTO p_id_usuario, v_stored_hash, p_nombre_completo, p_email, p_rol, v_activo
    FROM usuario
    WHERE username = p_username;
    
    -- Verificar si está activo
    IF v_activo = 0 THEN
        p_resultado := 'USUARIO_INACTIVO';
        
        -- Registrar intento fallido en bitácora
        INSERT INTO bitacora_usuario (
            id_usuario, username, operacion, resultado, mensaje
        ) VALUES (
            p_id_usuario, p_username, 'FAILED_LOGIN', 'FALLIDO', 'Usuario inactivo'
        );
        COMMIT;
        RETURN;
    END IF;
    
    -- Verificar contraseña
    IF v_stored_hash = p_password_hash THEN
        -- Login exitoso
        p_resultado := 'EXITOSO';
        
        -- Actualizar último acceso
        UPDATE usuario
        SET ultimo_acceso = SYSDATE
        WHERE id_usuario = p_id_usuario;
        
        -- Registrar login exitoso en bitácora
        INSERT INTO bitacora_usuario (
            id_usuario, username, operacion, resultado, mensaje
        ) VALUES (
            p_id_usuario, p_username, 'LOGIN', 'EXITOSO', 'Login exitoso'
        );
        
        COMMIT;
    ELSE
        -- Contraseña incorrecta
        p_resultado := 'PASSWORD_INCORRECTO';
        
        -- Registrar intento fallido en bitácora
        INSERT INTO bitacora_usuario (
            id_usuario, username, operacion, resultado, mensaje
        ) VALUES (
            p_id_usuario, p_username, 'FAILED_LOGIN', 'FALLIDO', 'Contraseña incorrecta'
        );
        COMMIT;
    END IF;
    
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        -- Usuario no existe
        p_resultado := 'USUARIO_NO_EXISTE';
        p_id_usuario := NULL;
        
        -- Registrar intento fallido en bitácora
        INSERT INTO bitacora_usuario (
            id_usuario, username, operacion, resultado, mensaje
        ) VALUES (
            0, p_username, 'FAILED_LOGIN', 'FALLIDO', 'Usuario no existe'
        );
        COMMIT;
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

-- Procedimiento: Logout (registrar cierre de sesión)
CREATE OR REPLACE PROCEDURE sp_logout (
    p_id_usuario IN NUMBER,
    p_username IN VARCHAR2
) AS
BEGIN
    INSERT INTO bitacora_usuario (
        id_usuario, username, operacion, resultado, mensaje
    ) VALUES (
        p_id_usuario, p_username, 'LOGOUT', 'EXITOSO', 'Logout exitoso'
    );
    
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

-- Procedimiento: Cambiar contraseña
CREATE OR REPLACE PROCEDURE sp_cambiar_password (
    p_id_usuario IN NUMBER,
    p_password_hash_actual IN VARCHAR2,
    p_password_hash_nuevo IN VARCHAR2,
    p_resultado OUT VARCHAR2
) AS
    v_stored_hash VARCHAR2(255);
BEGIN
    -- Verificar contraseña actual
    SELECT password_hash
    INTO v_stored_hash
    FROM usuario
    WHERE id_usuario = p_id_usuario;
    
    IF v_stored_hash = p_password_hash_actual THEN
        -- Actualizar contraseña
        UPDATE usuario
        SET password_hash = p_password_hash_nuevo
        WHERE id_usuario = p_id_usuario;
        
        p_resultado := 'EXITOSO';
        COMMIT;
    ELSE
        p_resultado := 'PASSWORD_ACTUAL_INCORRECTO';
        ROLLBACK;
    END IF;
    
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        p_resultado := 'USUARIO_NO_ENCONTRADO';
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

-- Procedimiento: Activar/Desactivar usuario
CREATE OR REPLACE PROCEDURE sp_activar_desactivar_usuario (
    p_id_usuario IN NUMBER,
    p_activo IN NUMBER
) AS
BEGIN
    UPDATE usuario
    SET activo = p_activo
    WHERE id_usuario = p_id_usuario;
    
    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(-20011, 'Usuario no encontrado');
    END IF;
    
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

-- Procedimiento: Listar usuarios
CREATE OR REPLACE PROCEDURE sp_listar_usuarios (
    p_cursor OUT SYS_REFCURSOR
) AS
BEGIN
    OPEN p_cursor FOR
        SELECT id_usuario, username, nombre_completo, email,
               rol, activo, fecha_creacion, ultimo_acceso
        FROM usuario
        ORDER BY id_usuario;
END;
/

COMMIT;
