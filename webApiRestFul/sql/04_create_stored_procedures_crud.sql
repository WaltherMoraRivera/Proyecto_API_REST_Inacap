-- ===========================================
-- STORED PROCEDURES - CRUD PELICULA
-- ===========================================

-- Procedimiento: Crear película
CREATE OR REPLACE PROCEDURE sp_crear_pelicula (
    p_titulo IN VARCHAR2,
    p_pais_origen IN VARCHAR2,
    p_director IN VARCHAR2,
    p_duracion_minutos IN NUMBER,
    p_genero IN VARCHAR2 DEFAULT 'Drama',
    p_clasificacion IN VARCHAR2 DEFAULT 'TE',
    p_sinopsis IN VARCHAR2 DEFAULT 'Sin sinopsis disponible',
    p_id_pelicula OUT NUMBER
) AS
BEGIN
    INSERT INTO pelicula (
        titulo, pais_origen, director, duracion_minutos,
        genero, clasificacion, sinopsis
    ) VALUES (
        p_titulo, p_pais_origen, p_director, p_duracion_minutos,
        p_genero, p_clasificacion, p_sinopsis
    ) RETURNING id_pelicula INTO p_id_pelicula;
    
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

-- Procedimiento: Leer película por ID
CREATE OR REPLACE PROCEDURE sp_leer_pelicula (
    p_id_pelicula IN NUMBER,
    p_cursor OUT SYS_REFCURSOR
) AS
BEGIN
    OPEN p_cursor FOR
        SELECT id_pelicula, titulo, pais_origen, director, 
               duracion_minutos, genero, clasificacion, sinopsis
        FROM pelicula
        WHERE id_pelicula = p_id_pelicula;
END;
/

-- Procedimiento: Listar todas las películas
CREATE OR REPLACE PROCEDURE sp_listar_peliculas (
    p_cursor OUT SYS_REFCURSOR
) AS
BEGIN
    OPEN p_cursor FOR
        SELECT id_pelicula, titulo, pais_origen, director,
               duracion_minutos, genero, clasificacion, sinopsis
        FROM pelicula
        ORDER BY id_pelicula;
END;
/

-- Procedimiento: Actualizar película
CREATE OR REPLACE PROCEDURE sp_actualizar_pelicula (
    p_id_pelicula IN NUMBER,
    p_titulo IN VARCHAR2,
    p_pais_origen IN VARCHAR2,
    p_director IN VARCHAR2,
    p_duracion_minutos IN NUMBER,
    p_genero IN VARCHAR2,
    p_clasificacion IN VARCHAR2,
    p_sinopsis IN VARCHAR2
) AS
BEGIN
    UPDATE pelicula
    SET titulo = p_titulo,
        pais_origen = p_pais_origen,
        director = p_director,
        duracion_minutos = p_duracion_minutos,
        genero = p_genero,
        clasificacion = p_clasificacion,
        sinopsis = p_sinopsis
    WHERE id_pelicula = p_id_pelicula;
    
    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'Película no encontrada');
    END IF;
    
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

-- Procedimiento: Eliminar película
CREATE OR REPLACE PROCEDURE sp_eliminar_pelicula (
    p_id_pelicula IN NUMBER
) AS
BEGIN
    DELETE FROM pelicula WHERE id_pelicula = p_id_pelicula;
    
    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'Película no encontrada');
    END IF;
    
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

-- ===========================================
-- STORED PROCEDURES - CRUD FUNCION
-- ===========================================

-- Procedimiento: Crear función
CREATE OR REPLACE PROCEDURE sp_crear_funcion (
    p_fecha IN DATE,
    p_hora IN VARCHAR2,
    p_precio_entrada IN NUMBER,
    p_estado_funcion IN VARCHAR2 DEFAULT 'Programada',
    p_observaciones IN VARCHAR2 DEFAULT 'Sin observaciones',
    p_id_sede IN NUMBER,
    p_id_funcion OUT NUMBER
) AS
BEGIN
    INSERT INTO funcion (
        fecha, hora, precio_entrada, estado_funcion,
        observaciones, id_sede
    ) VALUES (
        p_fecha, p_hora, p_precio_entrada, p_estado_funcion,
        p_observaciones, p_id_sede
    ) RETURNING id_funcion INTO p_id_funcion;
    
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

-- Procedimiento: Leer función por ID
CREATE OR REPLACE PROCEDURE sp_leer_funcion (
    p_id_funcion IN NUMBER,
    p_cursor OUT SYS_REFCURSOR
) AS
BEGIN
    OPEN p_cursor FOR
        SELECT id_funcion, fecha, hora, precio_entrada,
               estado_funcion, observaciones, id_sede
        FROM funcion
        WHERE id_funcion = p_id_funcion;
END;
/

-- Procedimiento: Listar todas las funciones
CREATE OR REPLACE PROCEDURE sp_listar_funciones (
    p_cursor OUT SYS_REFCURSOR
) AS
BEGIN
    OPEN p_cursor FOR
        SELECT id_funcion, fecha, hora, precio_entrada,
               estado_funcion, observaciones, id_sede
        FROM funcion
        ORDER BY fecha DESC, hora DESC;
END;
/

-- Procedimiento: Actualizar función
CREATE OR REPLACE PROCEDURE sp_actualizar_funcion (
    p_id_funcion IN NUMBER,
    p_fecha IN DATE,
    p_hora IN VARCHAR2,
    p_precio_entrada IN NUMBER,
    p_estado_funcion IN VARCHAR2,
    p_observaciones IN VARCHAR2,
    p_id_sede IN NUMBER
) AS
BEGIN
    UPDATE funcion
    SET fecha = p_fecha,
        hora = p_hora,
        precio_entrada = p_precio_entrada,
        estado_funcion = p_estado_funcion,
        observaciones = p_observaciones,
        id_sede = p_id_sede
    WHERE id_funcion = p_id_funcion;
    
    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(-20002, 'Función no encontrada');
    END IF;
    
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

-- Procedimiento: Eliminar función
CREATE OR REPLACE PROCEDURE sp_eliminar_funcion (
    p_id_funcion IN NUMBER
) AS
BEGIN
    DELETE FROM funcion WHERE id_funcion = p_id_funcion;
    
    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(-20002, 'Función no encontrada');
    END IF;
    
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

-- ===========================================
-- STORED PROCEDURES - CRUD ASISTENTE
-- ===========================================

-- Procedimiento: Crear asistente
CREATE OR REPLACE PROCEDURE sp_crear_asistente (
    p_nombre IN VARCHAR2,
    p_correo IN VARCHAR2,
    p_telefono IN VARCHAR2,
    p_edad IN NUMBER,
    p_ciudad_residencia IN VARCHAR2 DEFAULT 'No especificada',
    p_tipo_asistente IN VARCHAR2 DEFAULT 'General',
    p_id_asistente OUT NUMBER
) AS
BEGIN
    INSERT INTO asistente (
        nombre, correo, telefono, edad,
        ciudad_residencia, tipo_asistente
    ) VALUES (
        p_nombre, p_correo, p_telefono, p_edad,
        p_ciudad_residencia, p_tipo_asistente
    ) RETURNING id_asistente INTO p_id_asistente;
    
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

-- Procedimiento: Leer asistente por ID
CREATE OR REPLACE PROCEDURE sp_leer_asistente (
    p_id_asistente IN NUMBER,
    p_cursor OUT SYS_REFCURSOR
) AS
BEGIN
    OPEN p_cursor FOR
        SELECT id_asistente, nombre, correo, telefono, edad,
               ciudad_residencia, tipo_asistente
        FROM asistente
        WHERE id_asistente = p_id_asistente;
END;
/

-- Procedimiento: Listar todos los asistentes
CREATE OR REPLACE PROCEDURE sp_listar_asistentes (
    p_cursor OUT SYS_REFCURSOR
) AS
BEGIN
    OPEN p_cursor FOR
        SELECT id_asistente, nombre, correo, telefono, edad,
               ciudad_residencia, tipo_asistente
        FROM asistente
        ORDER BY nombre;
END;
/

-- Procedimiento: Actualizar asistente
CREATE OR REPLACE PROCEDURE sp_actualizar_asistente (
    p_id_asistente IN NUMBER,
    p_nombre IN VARCHAR2,
    p_correo IN VARCHAR2,
    p_telefono IN VARCHAR2,
    p_edad IN NUMBER,
    p_ciudad_residencia IN VARCHAR2,
    p_tipo_asistente IN VARCHAR2
) AS
BEGIN
    UPDATE asistente
    SET nombre = p_nombre,
        correo = p_correo,
        telefono = p_telefono,
        edad = p_edad,
        ciudad_residencia = p_ciudad_residencia,
        tipo_asistente = p_tipo_asistente
    WHERE id_asistente = p_id_asistente;
    
    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(-20003, 'Asistente no encontrado');
    END IF;
    
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

-- Procedimiento: Eliminar asistente
CREATE OR REPLACE PROCEDURE sp_eliminar_asistente (
    p_id_asistente IN NUMBER
) AS
BEGIN
    DELETE FROM asistente WHERE id_asistente = p_id_asistente;
    
    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(-20003, 'Asistente no encontrado');
    END IF;
    
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/

COMMIT;
