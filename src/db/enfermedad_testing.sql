-- Insertar datos en la tabla sintoma
INSERT INTO sintoma (id_sintoma, nombre, descripcion) VALUES
(1, 'Cansancio', 'Sensación de falta de energía o fatiga'),
(2, 'Dificultad para respirar', 'Sensación de falta de aire o ahogo'),
(3, 'Dolor de cabeza', 'Molestia o presión en la cabeza'),
(4, 'Dolor de garganta', 'Molestia o ardor al tragar o hablar'),
(5, 'Dolor torácico', 'Dolor localizado en el pecho'),
(6, 'Fatiga', 'Cansancio físico o mental extremo'),
(7, 'Hambre constante', 'Sensación persistente de necesidad de comer'),
(8, 'Náuseas', 'Sensación de querer vomitar'),
(9, 'Palpitaciones', 'Sensación de latidos cardíacos rápidos o fuertes'),
(10, 'Tos seca', 'Tos sin expulsión de flema'),
(11, 'Tos con flema', 'Tos acompañada de moco o secreciones respiratorias'),
(12, 'Visión borrosa', 'Dificultad para ver con claridad'),
(13, 'Zumbido de oídos', 'Sensación de pitido constante o intermitente en los oídos');

-- Insertar datos en la tabla signo
INSERT INTO signo (id_signo, nombre, descripcion) VALUES
(1, 'Amígdalas inflamadas', 'Aumento de tamaño de las amígdalas'),
(2, 'Cianosis', 'Coloración azulada de piel o mucosas por falta de oxígeno'),
(3, 'Enrojecimiento faríngeo', 'Color rojo en la garganta debido a inflamación'),
(4, 'Estertores pulmonares', 'Ruidos anormales al auscultar los pulmones'),
(5, 'Fiebre', 'Elevación de la temperatura corporal'),
(6, 'Glucemia elevada', 'Nivel alto de azúcar en sangre'),
(7, 'Lengua depapilada', 'Pérdida de las papilas gustativas'),
(8, 'Leucocitosis', 'Aumento de glóbulos blancos en sangre'),
(9, 'Palidez', 'Disminución del color normal de la piel'),
(10, 'Presión arterial elevada', 'Valores de tensión arterial por encima de lo normal'),
(11, 'Rubor facial', 'Enrojecimiento de la cara'),
(12, 'Sibilancias auscultadas', 'Sonido agudo durante la respiración'),
(13, 'Taquicardia', 'Frecuencia cardíaca acelerada');

-- Insertar datos en la tabla enfermedad
INSERT INTO enfermedad (id_enfermedad, nombre, descripcion) VALUES
(1, 'Gripe', 'Infección viral que afecta las vías respiratorias superiores.'),
(2, 'COVID-19', 'Enfermedad causada por el coronavirus SARS-CoV-2.'),
(3, 'Neumonía', 'Infección pulmonar que inflama los sacos aéreos.'),
(4, 'Bronquitis', 'Inflamación de los bronquios, generalmente por infección viral.'),
(5, 'Faringitis', 'Inflamación de la faringe, comúnmente causada por virus o bacterias.'),
(6, 'Diabetes Mellitus tipo 2', 'Trastorno metabólico caracterizado por hiperglucemia crónica.'),
(7, 'Hipertensión arterial', 'Aumento persistente de la presión sanguínea.'),
(8, 'Amigdalitis', 'Inflamación de las amígdalas, a menudo causada por infecciones.'),
(9, 'Asma', 'Enfermedad crónica de las vías respiratorias con episodios de obstrucción.'),
(10, 'Otitis media', 'Infección o inflamación del oído medio.');

INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES
(1, 1), (1, 2), (1, 4),
(2, 1), (2, 2), (2, 5), (2, 7),
(3, 1), (3, 2), (3, 6),
(4, 2), (4, 4), (4, 6),
(5, 2), (5, 4), (5, 5),
(6, 3), (6, 8), (6, 10),
(7, 3), (7, 9),
(8, 2), (8, 4), (8, 5),
(9, 2), (9, 6), (9, 7),
(10, 5), (10, 8);

INSERT INTO enfermedad_signo (id_enfermedad, id_signo) VALUES
(1, 1), (1, 3),
(2, 1), (2, 4), (2, 5),
(3, 4), (3, 5),
(4, 2), (4, 4),
(5, 2),
(6, 6), (6, 7),
(7, 7), (7, 8),
(8, 2), (8, 3),
(9, 4), (9, 9),
(10, 10);
