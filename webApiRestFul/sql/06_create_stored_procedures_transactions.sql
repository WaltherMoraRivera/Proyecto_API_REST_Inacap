-- ===========================================
-- STORED PROCEDURES - TRANSACCIONES COMPLEJAS
-- Demuestran uso de COMMIT y ROLLBACK
-- ===========================================

-- Procedimiento: Registrar asistencia completa (transaccional)
-- Crea asistente si no existe y registra su asistencia a función
CREATE OR REPLACE PROCEDURE sp_registrar_asistencia_completa (
    p_nombre IN VARCHAR2,
    p_correo IN VARCHAR2,
    p_telefono IN VARCHAR2,
    p_edad IN NUMBER,
    p_id_funcion IN NUMBER,
    p_entradas IN NUMBER,
    p_metodo_pago IN VARCHAR2,
    p_id_asistente OUT NUMBER,
    p_resultado OUT VARCHAR2
) AS
    v_asistente_existe NUMBER;
BEGIN
    -- Verificar si el asistente ya existe por correo
    BEGIN
        SELECT id_asistente INTO p_id_asistente
        FROM asistente
        WHERE correo = p_correo;
        
        v_asistente_existe := 1;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            v_asistente_existe := 0;
    END;
    
    -- Si no existe, crear el asistente
    IF v_asistente_existe = 0 THEN
        INSERT INTO asistente (
            nombre, correo, telefono, edad
        ) VALUES (
            p_nombre, p_correo, p_telefono, p_edad
        ) RETURNING id_asistente INTO p_id_asistente;
    END IF;
    
    -- Registrar la asistencia
    INSERT INTO asistencia (
        id_funcion, id_asistente, entradas, metodo_pago
    ) VALUES (
        p_id_funcion, p_id_asistente, p_entradas, p_metodo_pago
    );
    
    p_resultado := 'EXITOSO';
    COMMIT;
    
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
        ROLLBACK;
        p_resultado := 'ERROR: Asistencia ya registrada';
    WHEN OTHERS THEN
        ROLLBACK;
        p_resultado := 'ERROR: ' || SQLERRM;
        RAISE;
END;
/

-- Procedimiento: Programar función con película (transaccional)
CREATE OR REPLACE PROCEDURE sp_programar_funcion_pelicula (
    p_fecha IN DATE,
    p_hora IN VARCHAR2,
    p_precio_entrada IN NUMBER,
    p_id_sede IN NUMBER,
    p_id_pelicula IN NUMBER,
    p_orden_proyeccion IN NUMBER DEFAULT 1,
    p_id_funcion OUT NUMBER,
    p_resultado OUT VARCHAR2
) AS
    v_capacidad NUMBER;
    v_pelicula_existe NUMBER;
BEGIN
    -- Verificar que la sede existe y obtener capacidad
    BEGIN
        SELECT capacidad_maxima INTO v_capacidad
        FROM sede
        WHERE id_sede = p_id_sede AND estado = 'Activa';
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            ROLLBACK;
            p_resultado := 'ERROR: Sede no existe o está inactiva';
            RETURN;
    END;
    
    -- Verificar que la película existe
    BEGIN
        SELECT COUNT(*) INTO v_pelicula_existe
        FROM pelicula
        WHERE id_pelicula = p_id_pelicula;
        
        IF v_pelicula_existe = 0 THEN
            ROLLBACK;
            p_resultado := 'ERROR: Película no existe';
            RETURN;
        END IF;
    END;
    
    -- Crear la función
    INSERT INTO funcion (
        fecha, hora, precio_entrada, estado_funcion, id_sede
    ) VALUES (
        p_fecha, p_hora, p_precio_entrada, 'Programada', p_id_sede
    ) RETURNING id_funcion INTO p_id_funcion;
    
    -- Crear la proyección
    INSERT INTO proyeccion (
        id_funcion, id_pelicula, orden_proyeccion
    ) VALUES (
        p_id_funcion, p_id_pelicula, p_orden_proyeccion
    );
    
    p_resultado := 'EXITOSO';
    COMMIT;
    
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        p_resultado := 'ERROR: ' || SQLERRM;
        RAISE;
END;
/

-- Procedimiento: Cancelar función y reembolsar (transaccional)
CREATE OR REPLACE PROCEDURE sp_cancelar_funcion_reembolso (
    p_id_funcion IN NUMBER,
    p_resultado OUT VARCHAR2
) AS
    v_asistencias NUMBER;
BEGIN
    -- Contar asistencias registradas
    SELECT COUNT(*) INTO v_asistencias
    FROM asistencia
    WHERE id_funcion = p_id_funcion;
    
    -- Eliminar todas las asistencias (simulación de reembolso)
    DELETE FROM asistencia
    WHERE id_funcion = p_id_funcion;
    
    -- Actualizar estado de la función a Cancelada
    UPDATE funcion
    SET estado_funcion = 'Cancelada',
        observaciones = 'Cancelada - ' || v_asistencias || ' asistencias reembolsadas'
    WHERE id_funcion = p_id_funcion;
    
    IF SQL%ROWCOUNT = 0 THEN
        ROLLBACK;
        p_resultado := 'ERROR: Función no encontrada';
        RETURN;
    END IF;
    
    p_resultado := 'EXITOSO: ' || v_asistencias || ' asistencias eliminadas';
    COMMIT;
    
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        p_resultado := 'ERROR: ' || SQLERRM;
        RAISE;
END;
/

-- Procedimiento: Evaluar película por jurado (transaccional)
CREATE OR REPLACE PROCEDURE sp_evaluar_pelicula_jurado (
    p_id_jurado IN NUMBER,
    p_id_pelicula IN NUMBER,
    p_puntuacion IN NUMBER,
    p_comentario IN VARCHAR2,
    p_categoria_evaluada IN VARCHAR2,
    p_resultado OUT VARCHAR2
) AS
    v_jurado_existe NUMBER;
    v_pelicula_existe NUMBER;
BEGIN
    -- Verificar que el jurado existe
    SELECT COUNT(*) INTO v_jurado_existe
    FROM jurado
    WHERE id_jurado = p_id_jurado;
    
    IF v_jurado_existe = 0 THEN
        ROLLBACK;
        p_resultado := 'ERROR: Jurado no existe';
        RETURN;
    END IF;
    
    -- Verificar que la película existe
    SELECT COUNT(*) INTO v_pelicula_existe
    FROM pelicula
    WHERE id_pelicula = p_id_pelicula;
    
    IF v_pelicula_existe = 0 THEN
        ROLLBACK;
        p_resultado := 'ERROR: Película no existe';
        RETURN;
    END IF;
    
    -- Insertar o actualizar evaluación
    BEGIN
        INSERT INTO evaluacion (
            id_jurado, id_pelicula, puntuacion,
            comentario, categoria_evaluada
        ) VALUES (
            p_id_jurado, p_id_pelicula, p_puntuacion,
            p_comentario, p_categoria_evaluada
        );
        p_resultado := 'EXITOSO: Evaluación creada';
    EXCEPTION
        WHEN DUP_VAL_ON_INDEX THEN
            -- Si ya existe, actualizar
            UPDATE evaluacion
            SET puntuacion = p_puntuacion,
                comentario = p_comentario,
                categoria_evaluada = p_categoria_evaluada,
                fecha_evaluacion = SYSDATE
            WHERE id_jurado = p_id_jurado
              AND id_pelicula = p_id_pelicula;
            p_resultado := 'EXITOSO: Evaluación actualizada';
    END;
    
    COMMIT;
    
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        p_resultado := 'ERROR: ' || SQLERRM;
        RAISE;
END;
/

-- Procedimiento: Premiar película (transaccional con validación)
CREATE OR REPLACE PROCEDURE sp_premiar_pelicula (
    p_id_pelicula IN NUMBER,
    p_categoria IN VARCHAR2,
    p_edicion IN NUMBER,
    p_posicion IN NUMBER,
    p_descripcion IN VARCHAR2,
    p_id_premio OUT NUMBER,
    p_resultado OUT VARCHAR2
) AS
    v_pelicula_existe NUMBER;
    v_premio_existe NUMBER;
BEGIN
    -- Verificar que la película existe
    SELECT COUNT(*) INTO v_pelicula_existe
    FROM pelicula
    WHERE id_pelicula = p_id_pelicula;
    
    IF v_pelicula_existe = 0 THEN
        ROLLBACK;
        p_resultado := 'ERROR: Película no existe';
        RETURN;
    END IF;
    
    -- Verificar si ya existe un premio para esa categoría, edición y posición
    SELECT COUNT(*) INTO v_premio_existe
    FROM premiacion
    WHERE categoria = p_categoria
      AND edicion = p_edicion
      AND posicion = p_posicion;
    
    IF v_premio_existe > 0 THEN
        ROLLBACK;
        p_resultado := 'ERROR: Ya existe un premio para esa categoría, edición y posición';
        RETURN;
    END IF;
    
    -- Crear el premio
    INSERT INTO premiacion (
        id_pelicula, categoria, edicion, posicion, descripcion
    ) VALUES (
        p_id_pelicula, p_categoria, p_edicion, p_posicion, p_descripcion
    ) RETURNING id_premio INTO p_id_premio;
    
    p_resultado := 'EXITOSO';
    COMMIT;
    
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        p_resultado := 'ERROR: ' || SQLERRM;
        RAISE;
END;
/

COMMIT;
