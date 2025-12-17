-- ===========================================
-- DATOS DE PRUEBA
-- Inserts para poblar la base de datos
-- ===========================================

-- 1. Ciudad
INSERT INTO ciudad (nombre, region, pais) VALUES ('Santiago', 'Metropolitana', 'Chile');
INSERT INTO ciudad (nombre, region, pais) VALUES ('Valparaíso', 'Valparaíso', 'Chile');
INSERT INTO ciudad (nombre, region, pais) VALUES ('Concepción', 'Biobío', 'Chile');
INSERT INTO ciudad (nombre, region, pais) VALUES ('Buenos Aires', 'CABA', 'Argentina');
INSERT INTO ciudad (nombre, region, pais) VALUES ('Lima', 'Lima Metropolitana', 'Perú');

-- 2. Sede
INSERT INTO sede (nombre, direccion, capacidad_maxima, tipo_sede, id_ciudad) VALUES ('Cine Arte Alameda', 'Av. Libertador 123', 300, 'Cine convencional', 1);
INSERT INTO sede (nombre, direccion, capacidad_maxima, tipo_sede, id_ciudad) VALUES ('Teatro Municipal Valpo', 'Calle Bellavista 456', 500, 'Teatro', 2);
INSERT INTO sede (nombre, direccion, capacidad_maxima, tipo_sede, id_ciudad) VALUES ('Cine Biobío', 'Av. Los Carrera 789', 250, 'Cine independiente', 3);
INSERT INTO sede (nombre, direccion, capacidad_maxima, tipo_sede, id_ciudad) VALUES ('Cine Gaumont', 'Av. Rivadavia 321', 400, 'Cine histórico', 4);
INSERT INTO sede (nombre, direccion, capacidad_maxima, tipo_sede, id_ciudad) VALUES ('Cine UVK', 'Av. Benavides 654', 350, 'Cine comercial', 5);

-- 3. Pelicula
INSERT INTO pelicula (titulo, pais_origen, director, duracion_minutos, genero, clasificacion) VALUES ('El Viaje', 'Chile', 'Juan Pérez', 120, 'Drama', '+14');
INSERT INTO pelicula (titulo, pais_origen, director, duracion_minutos, genero, clasificacion) VALUES ('Sueños del Mar', 'Argentina', 'María López', 90, 'Romance', 'TE');
INSERT INTO pelicula (titulo, pais_origen, director, duracion_minutos, genero, clasificacion) VALUES ('Luz en la Oscuridad', 'Perú', 'Carlos Ramírez', 110, 'Suspenso', '+18');
INSERT INTO pelicula (titulo, pais_origen, director, duracion_minutos, genero, clasificacion) VALUES ('Camino al Futuro', 'Chile', 'Ana Torres', 100, 'Ciencia Ficción', '+7');
INSERT INTO pelicula (titulo, pais_origen, director, duracion_minutos, genero, clasificacion) VALUES ('Risas Eternas', 'México', 'Pedro Sánchez', 95, 'Comedia', 'TE');

-- 4. Funcion
INSERT INTO funcion (fecha, hora, precio_entrada, estado_funcion, id_sede) VALUES (SYSDATE, '18:00', 5000, 'Programada', 1);
INSERT INTO funcion (fecha, hora, precio_entrada, estado_funcion, id_sede) VALUES (SYSDATE + 1, '20:00', 6000, 'Programada', 2);
INSERT INTO funcion (fecha, hora, precio_entrada, estado_funcion, id_sede) VALUES (SYSDATE + 2, '19:30', 4500, 'Programada', 3);
INSERT INTO funcion (fecha, hora, precio_entrada, estado_funcion, id_sede) VALUES (SYSDATE + 3, '21:00', 7000, 'Programada', 4);
INSERT INTO funcion (fecha, hora, precio_entrada, estado_funcion, id_sede) VALUES (SYSDATE + 4, '17:00', 5500, 'Programada', 5);

-- 5. Proyeccion
INSERT INTO proyeccion (id_funcion, id_pelicula, orden_proyeccion) VALUES (1, 1, 1);
INSERT INTO proyeccion (id_funcion, id_pelicula, orden_proyeccion) VALUES (2, 2, 1);
INSERT INTO proyeccion (id_funcion, id_pelicula, orden_proyeccion) VALUES (3, 3, 1);
INSERT INTO proyeccion (id_funcion, id_pelicula, orden_proyeccion) VALUES (4, 4, 1);
INSERT INTO proyeccion (id_funcion, id_pelicula, orden_proyeccion) VALUES (5, 5, 1);

-- 6. Asistente
INSERT INTO asistente (nombre, correo, telefono, edad, ciudad_residencia, tipo_asistente) VALUES ('Pedro Gómez', 'pedro.gomez@mail.com', '9991111', 28, 'Santiago', 'General');
INSERT INTO asistente (nombre, correo, telefono, edad, ciudad_residencia, tipo_asistente) VALUES ('Laura Martínez', 'laura.martinez@mail.com', '9992222', 22, 'Valparaíso', 'Estudiante');
INSERT INTO asistente (nombre, correo, telefono, edad, ciudad_residencia, tipo_asistente) VALUES ('Carlos Ramírez', 'carlos.ramirez@mail.com', '9993333', 35, 'Concepción', 'Profesional');
INSERT INTO asistente (nombre, correo, telefono, edad, ciudad_residencia, tipo_asistente) VALUES ('Ana Torres', 'ana.torres@mail.com', '9994444', 30, 'Buenos Aires', 'Prensa');
INSERT INTO asistente (nombre, correo, telefono, edad, ciudad_residencia, tipo_asistente) VALUES ('Sofía Díaz', 'sofia.diaz@mail.com', '9995555', 26, 'Lima', 'General');

-- 7. Asistencia
INSERT INTO asistencia (id_funcion, id_asistente, entradas, metodo_pago) VALUES (1, 1, 2, 'Tarjeta');
INSERT INTO asistencia (id_funcion, id_asistente, entradas, metodo_pago) VALUES (2, 2, 1, 'Efectivo');
INSERT INTO asistencia (id_funcion, id_asistente, entradas, metodo_pago) VALUES (3, 3, 3, 'Transferencia');
INSERT INTO asistencia (id_funcion, id_asistente, entradas, metodo_pago) VALUES (4, 4, 1, 'Tarjeta');
INSERT INTO asistencia (id_funcion, id_asistente, entradas, metodo_pago) VALUES (5, 5, 2, 'Efectivo');

-- 8. Jurado
INSERT INTO jurado (nombre, correo, especialidad, pais_origen, experiencia_anos, tipo_jurado) VALUES ('Dr. Juan Herrera', 'juan.herrera@mail.com', 'Dirección', 'Chile', 10, 'Permanente');
INSERT INTO jurado (nombre, correo, especialidad, pais_origen, experiencia_anos, tipo_jurado) VALUES ('María Vega', 'maria.vega@mail.com', 'Actuación', 'Argentina', 8, 'Invitado');
INSERT INTO jurado (nombre, correo, especialidad, pais_origen, experiencia_anos, tipo_jurado) VALUES ('Ricardo Soto', 'ricardo.soto@mail.com', 'Guion', 'Perú', 12, 'Honorario');
INSERT INTO jurado (nombre, correo, especialidad, pais_origen, experiencia_anos, tipo_jurado) VALUES ('Diana Fuentes', 'diana.fuentes@mail.com', 'Fotografía', 'Chile', 15, 'Permanente');
INSERT INTO jurado (nombre, correo, especialidad, pais_origen, experiencia_anos, tipo_jurado) VALUES ('Fernando Ríos', 'fernando.rios@mail.com', 'Sonido', 'México', 20, 'Invitado');

-- 9. Participacion_Jurado
INSERT INTO participacion_jurado (id_jurado, id_funcion, rol_participacion) VALUES (1, 1, 'Evaluador');
INSERT INTO participacion_jurado (id_jurado, id_funcion, rol_participacion) VALUES (2, 2, 'Moderador');
INSERT INTO participacion_jurado (id_jurado, id_funcion, rol_participacion) VALUES (3, 3, 'Evaluador');
INSERT INTO participacion_jurado (id_jurado, id_funcion, rol_participacion) VALUES (4, 4, 'Invitado especial');
INSERT INTO participacion_jurado (id_jurado, id_funcion, rol_participacion) VALUES (5, 5, 'Evaluador');

-- 10. Evaluacion
INSERT INTO evaluacion (id_jurado, id_pelicula, puntuacion, comentario, categoria_evaluada) VALUES (1, 1, 9, 'Gran dirección', 'Direccion');
INSERT INTO evaluacion (id_jurado, id_pelicula, puntuacion, comentario, categoria_evaluada) VALUES (2, 2, 8, 'Buena actuación', 'Actuacion');
INSERT INTO evaluacion (id_jurado, id_pelicula, puntuacion, comentario, categoria_evaluada) VALUES (3, 3, 7, 'Historia interesante', 'Guion');
INSERT INTO evaluacion (id_jurado, id_pelicula, puntuacion, comentario, categoria_evaluada) VALUES (4, 4, 10, 'Fotografía impecable', 'Fotografia');
INSERT INTO evaluacion (id_jurado, id_pelicula, puntuacion, comentario, categoria_evaluada) VALUES (5, 5, 9, 'Excelente sonido', 'Sonido');

-- 11. Premiacion
INSERT INTO premiacion (id_pelicula, categoria, edicion, posicion, descripcion) VALUES (1, 'Mejor Dirección', 2025, 1, 'Premio a la mejor dirección');
INSERT INTO premiacion (id_pelicula, categoria, edicion, posicion, descripcion) VALUES (2, 'Mejor Actuación', 2025, 1, 'Premio a la mejor actuación');
INSERT INTO premiacion (id_pelicula, categoria, edicion, posicion, descripcion) VALUES (3, 'Mejor Guion', 2025, 1, 'Premio al mejor guion');
INSERT INTO premiacion (id_pelicula, categoria, edicion, posicion, descripcion) VALUES (4, 'Mejor Fotografía', 2025, 1, 'Premio a la mejor fotografía');
INSERT INTO premiacion (id_pelicula, categoria, edicion, posicion, descripcion) VALUES (5, 'Mejor Sonido', 2025, 1, 'Premio al mejor sonido');

-- 12. Usuario (contraseña: admin123 - en producción usar hash real)
INSERT INTO usuario (username, password_hash, nombre_completo, email, rol) 
VALUES ('admin', 'admin123', 'Administrador Sistema', 'admin@festival.cl', 'admin');

INSERT INTO usuario (username, password_hash, nombre_completo, email, rol) 
VALUES ('usuario1', 'user123', 'Usuario Prueba', 'usuario@festival.cl', 'usuario');

COMMIT;
