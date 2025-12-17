-- ===========================================
-- TRIGGERS DE AUDITORÍA
-- Registran automáticamente cambios en las tablas
-- ===========================================

-- Trigger para PELICULA - INSERT
CREATE OR REPLACE TRIGGER trg_pelicula_insert
AFTER INSERT ON pelicula
FOR EACH ROW
BEGIN
    INSERT INTO bitacora_pelicula (
        id_pelicula, operacion, titulo_nuevo, director_nuevo, 
        duracion_nueva, usuario
    ) VALUES (
        :NEW.id_pelicula, 'INSERT', :NEW.titulo, :NEW.director, 
        :NEW.duracion_minutos, USER
    );
END;
/

-- Trigger para PELICULA - UPDATE
CREATE OR REPLACE TRIGGER trg_pelicula_update
AFTER UPDATE ON pelicula
FOR EACH ROW
BEGIN
    INSERT INTO bitacora_pelicula (
        id_pelicula, operacion, 
        titulo_anterior, titulo_nuevo,
        director_anterior, director_nuevo,
        duracion_anterior, duracion_nueva,
        usuario
    ) VALUES (
        :NEW.id_pelicula, 'UPDATE',
        :OLD.titulo, :NEW.titulo,
        :OLD.director, :NEW.director,
        :OLD.duracion_minutos, :NEW.duracion_minutos,
        USER
    );
END;
/

-- Trigger para PELICULA - DELETE
CREATE OR REPLACE TRIGGER trg_pelicula_delete
AFTER DELETE ON pelicula
FOR EACH ROW
BEGIN
    INSERT INTO bitacora_pelicula (
        id_pelicula, operacion, titulo_anterior, director_anterior,
        duracion_anterior, usuario
    ) VALUES (
        :OLD.id_pelicula, 'DELETE', :OLD.titulo, :OLD.director,
        :OLD.duracion_minutos, USER
    );
END;
/

-- Trigger para FUNCION - INSERT
CREATE OR REPLACE TRIGGER trg_funcion_insert
AFTER INSERT ON funcion
FOR EACH ROW
BEGIN
    INSERT INTO bitacora_funcion (
        id_funcion, operacion, fecha_nueva, precio_nuevo,
        estado_nuevo, usuario
    ) VALUES (
        :NEW.id_funcion, 'INSERT', :NEW.fecha, :NEW.precio_entrada,
        :NEW.estado_funcion, USER
    );
END;
/

-- Trigger para FUNCION - UPDATE
CREATE OR REPLACE TRIGGER trg_funcion_update
AFTER UPDATE ON funcion
FOR EACH ROW
BEGIN
    INSERT INTO bitacora_funcion (
        id_funcion, operacion,
        fecha_anterior, fecha_nueva,
        precio_anterior, precio_nuevo,
        estado_anterior, estado_nuevo,
        usuario
    ) VALUES (
        :NEW.id_funcion, 'UPDATE',
        :OLD.fecha, :NEW.fecha,
        :OLD.precio_entrada, :NEW.precio_entrada,
        :OLD.estado_funcion, :NEW.estado_funcion,
        USER
    );
END;
/

-- Trigger para FUNCION - DELETE
CREATE OR REPLACE TRIGGER trg_funcion_delete
AFTER DELETE ON funcion
FOR EACH ROW
BEGIN
    INSERT INTO bitacora_funcion (
        id_funcion, operacion, fecha_anterior, precio_anterior,
        estado_anterior, usuario
    ) VALUES (
        :OLD.id_funcion, 'DELETE', :OLD.fecha, :OLD.precio_entrada,
        :OLD.estado_funcion, USER
    );
END;
/

-- Trigger para ASISTENCIA - INSERT
CREATE OR REPLACE TRIGGER trg_asistencia_insert
AFTER INSERT ON asistencia
FOR EACH ROW
BEGIN
    INSERT INTO bitacora_asistencia (
        id_funcion, id_asistente, operacion, 
        entradas_nuevo, metodo_pago_nuevo, usuario
    ) VALUES (
        :NEW.id_funcion, :NEW.id_asistente, 'INSERT',
        :NEW.entradas, :NEW.metodo_pago, USER
    );
END;
/

-- Trigger para ASISTENCIA - UPDATE
CREATE OR REPLACE TRIGGER trg_asistencia_update
AFTER UPDATE ON asistencia
FOR EACH ROW
BEGIN
    INSERT INTO bitacora_asistencia (
        id_funcion, id_asistente, operacion,
        entradas_anterior, entradas_nuevo,
        metodo_pago_anterior, metodo_pago_nuevo,
        usuario
    ) VALUES (
        :NEW.id_funcion, :NEW.id_asistente, 'UPDATE',
        :OLD.entradas, :NEW.entradas,
        :OLD.metodo_pago, :NEW.metodo_pago,
        USER
    );
END;
/

-- Trigger para ASISTENCIA - DELETE
CREATE OR REPLACE TRIGGER trg_asistencia_delete
AFTER DELETE ON asistencia
FOR EACH ROW
BEGIN
    INSERT INTO bitacora_asistencia (
        id_funcion, id_asistente, operacion,
        entradas_anterior, metodo_pago_anterior, usuario
    ) VALUES (
        :OLD.id_funcion, :OLD.id_asistente, 'DELETE',
        :OLD.entradas, :OLD.metodo_pago, USER
    );
END;
/

-- Trigger para EVALUACION - INSERT
CREATE OR REPLACE TRIGGER trg_evaluacion_insert
AFTER INSERT ON evaluacion
FOR EACH ROW
BEGIN
    INSERT INTO bitacora_evaluacion (
        id_jurado, id_pelicula, operacion,
        puntuacion_nueva, comentario_nuevo, usuario
    ) VALUES (
        :NEW.id_jurado, :NEW.id_pelicula, 'INSERT',
        :NEW.puntuacion, :NEW.comentario, USER
    );
END;
/

-- Trigger para EVALUACION - UPDATE
CREATE OR REPLACE TRIGGER trg_evaluacion_update
AFTER UPDATE ON evaluacion
FOR EACH ROW
BEGIN
    INSERT INTO bitacora_evaluacion (
        id_jurado, id_pelicula, operacion,
        puntuacion_anterior, puntuacion_nueva,
        comentario_anterior, comentario_nuevo,
        usuario
    ) VALUES (
        :NEW.id_jurado, :NEW.id_pelicula, 'UPDATE',
        :OLD.puntuacion, :NEW.puntuacion,
        :OLD.comentario, :NEW.comentario,
        USER
    );
END;
/

-- Trigger para EVALUACION - DELETE
CREATE OR REPLACE TRIGGER trg_evaluacion_delete
AFTER DELETE ON evaluacion
FOR EACH ROW
BEGIN
    INSERT INTO bitacora_evaluacion (
        id_jurado, id_pelicula, operacion,
        puntuacion_anterior, comentario_anterior, usuario
    ) VALUES (
        :OLD.id_jurado, :OLD.id_pelicula, 'DELETE',
        :OLD.puntuacion, :OLD.comentario, USER
    );
END;
/

-- Trigger para USUARIO - Actualizar último acceso
CREATE OR REPLACE TRIGGER trg_usuario_update_acceso
BEFORE UPDATE OF ultimo_acceso ON usuario
FOR EACH ROW
BEGIN
    :NEW.ultimo_acceso := SYSDATE;
END;
/

COMMIT;
