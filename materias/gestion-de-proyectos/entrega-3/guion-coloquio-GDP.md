# Guion del coloquio — Gestión de Proyectos

**Equipo 08 · Comisión E · Talento Tech** — Proyecto: modernización del sitio institucional del IFTS N°2.

## Qué pide la consigna (y cómo lo leemos)

- **Se presenta el Proyecto, no el TP.** Es una presentación empresaria a un cliente: sin "en la sección 7.3 de nuestro trabajo", sin hablar de la cátedra ni de la nota.
- Video grupal de **5 a 10 min** (objetivo: **8:30**, así hay margen para no pasarse). Máximo **1 o 2 slides por punto**.
- Cuatro puntos, en este orden: **(a)** visión general y problema, **(b)** propuesta de valor e indicadores de éxito (arrancar con *elevator pitch*), **(c)** riesgos y mitigación (con plan para cada riesgo), **(d)** costos: presupuesto "venta" y qué servicios y productos obtiene el cliente.
- Entrega: **9 al 15/11** en el foro del grupo. Nos co-evalúa el Equipo 01, con la rúbrica de **claridad, relevancia y precisión** (precisión = gráficos y datos que apoyen lo que se dice). Cada punto tiene que estar completo, no solo mencionado.

## Plan general

| # | Bloque | Slides | Quién | Tiempo | Acumulado |
|---|---|---|---|---|---|
| 0 | Apertura y presentación | 1 (portada) | Martín | 0:20 | 0:20 |
| a | Visión general y problema | 2 | Martín | 1:40 | 2:00 |
| b | Elevator pitch, propuesta de valor e indicadores | 2 | Gastón | 1:50 | 3:50 |
| c | Riesgos y mitigación | 2 | Nicolás y Adrián | 2:20 | 6:10 |
| d | Costos y presupuesto de venta | 2 | Santiago | 1:50 | 8:00 |
| 5 | Cierre y próximos pasos | 1 | Martín | 0:30 | 8:30 |

Total: 10 slides. Los reparto por rol (PO, frontend, backend, QA, DevOps); se pueden cambiar mientras cada uno hable de algo que conoce. Los textos están pensados a ~130 palabras por minuto.

---

## 0. Apertura (0:20) — Martín · Slide 1: portada

> **Slide:** logo Talento Tech + logo IFTS N°2, título "Un sitio que forma parte de la formación", los cinco nombres y roles.

"Buenas, somos Talento Tech: Santiago, Adrián, Nicolás, Gastón y yo, Martín. Hace dos meses el IFTS N°2 nos contó qué necesita de su sitio web. Hoy les mostramos qué entendimos, cómo lo resolvemos, qué puede salir mal y cuánto vale."

---

## a. Visión general del proyecto (1:40) — Martín

### Slide 2 — El problema
> **Slide:** captura del Google Sites actual con tres marcas rojas: "contenido 2021–2026 mezclado", "sin panel", "sin contacto". A la derecha, la frase del instituto: *"No formamos chefs. Formamos empresarios gastronómicos."*

"El IFTS N°2 forma empresarios gastronómicos. Pero su sitio hoy está en Google Sites y no está a la altura de esa identidad: mezcla contenido de 2021 a 2026, un estudiante no sabe cuál es el horario vigente, no hay ningún medio de contacto, y lo que se publica en Instagram y Facebook no se conecta con la web.

Además, quienes lo mantienen son docentes, no técnicos. Hoy cargar una novedad es una tarea que se posterga, y el sitio queda desactualizado."

### Slide 3 — Qué vamos a construir
> **Slide:** diagrama simple en dos bloques: **Sitio público** (Inicio, Institucional, La carrera, Estudiantes, Ingreso, Novedades, Contacto) y **Panel de administración** (novedades, horarios, archivo, avisos, usuarios). Debajo, tres íconos: SIU Guaraní · Aulas Virtuales · Mi Argentina.

"Proponemos una plataforma propia, con dos partes. Un sitio público moderno, rápido y adaptado a celulares. Y un panel de administración, para que el propio instituto cargue y edite contenido sin tocar código.

Tres ideas ordenan todo. Primero, separamos el contenido que casi no cambia, como el plan de carrera, del que cambia seguido, como horarios y novedades. Segundo, **el contenido vencido se archiva automáticamente, nunca se borra**: fue un pedido explícito del instituto. Tercero, de Instagram y Facebook se publica lo que el instituto elige, no todo: el criterio editorial sigue siendo humano.

Y suma accesos directos a los sistemas que los estudiantes ya usan y un formulario de contacto, que hoy no existe."

---

## b. Propuesta de valor e indicadores de éxito (1:50) — Gastón

### Slide 4 — Elevator pitch (primeros ~30 s, sin leer, mirando a cámara)
> **Slide:** una sola frase grande, fondo con la paleta tierra del Figma. Sin más texto.

"Imaginen que la coordinadora de una carrera quiere avisar que cambió una mesa de examen. Hoy tiene que pedirle a alguien que sepa de sitios web. Con nuestra plataforma lo hace ella misma, en un minuto, desde el celular, y el aviso aparece en el sitio. Cuando la fecha pasa, desaparece solo, queda archivado y no se pierde nada. Un sitio que el instituto mantiene con sus propias manos, siempre vigente, sin costo mensual y sin depender de un tercero."

*(Ajustar con un ejemplo real que dé el cliente, por ejemplo la Mateada Patria o la Jornada de Gastronomía.)*

### Slide 5 — Valor para el instituto e indicadores de éxito
> **Slide:** izquierda, 4 beneficios con ícono. Derecha, tabla de 4 indicadores con su meta.

| Valor | Para quién |
|---|---|
| Sitio que refleja la identidad del instituto | Comunidad e ingresantes |
| Autonomía: panel simple, sin depender de un desarrollador | Matías, María y los docentes |
| Información siempre vigente, con archivo histórico | Estudiantes |
| Costo operativo cero | El instituto |

| Indicador de éxito | Meta |
|---|---|
| Secciones institucionales completas y validadas por el cliente | En la DEMO de la semana 6 *(cumplido)* |
| Panel que permite cargar novedades, horarios y galería sin tocar código | En la versión funcional de la semana 13 |
| Contenido académico visible solo del cuatrimestre en curso | 100 %, sin información obsoleta |
| Publicación desde redes con selección editorial, probada con un caso real | Antes de la entrega final |

"¿Cómo van a saber que funcionó? Con cuatro indicadores. Las secciones institucionales validadas por ustedes, que ya hicimos en la demo de la semana 6. Un panel con el que cargan novedades, horarios y galería sin ayuda. Cero información vencida visible. Y una publicación real de Instagram en el sitio. Sumamos tres medidas de calidad: que cualquier persona pueda usar el sitio, incluidas las que tienen alguna discapacidad; que cargue rápido en un celular; y que lo probemos de forma automática para detectar fallas antes de que las vean ustedes."

---

## c. Riesgos y mitigación (2:20) — Nicolás (c1) y Adrián (c2)

### Slide 6 — Mapa de riesgos (Nicolás, 1:10)
> **Slide:** matriz 3×3 de probabilidad e impacto con los 12 riesgos (R1 a R12) ubicados; los de exposición alta (6 a 9) en rojo.

"Identificamos doce riesgos y a cada uno le pusimos probabilidad, impacto, responsable y dos planes: uno para prevenirlo y otro por si ocurre igual. Estos son los de exposición alta.

El mayor es técnico. **Retraso en el servidor**: la planificación nos da una probabilidad de llegar a la versión funcional en la semana 13 del 36 %, y del 86 % en la semana 14. Es un hito ajustado y lo decimos de frente. Prevención: definir primero cómo se comunican el sitio y el servidor, y avanzar el frente visual con datos de prueba. Si pasa, entregamos una primera versión con novedades, horarios, archivo y acceso, y el resto entra una semana después.

Segundo: **Instagram**. La conexión con Instagram puede cambiar o el permiso vencer. Prevención: una prueba temprana y mantener esa parte separada del resto del sitio. Si falla, se cargan las publicaciones a mano desde el panel y el sitio sigue funcionando."

### Slide 7 — Mitigación y contingencia (Adrián, 1:10)
> **Slide:** tabla de 4 filas (R3, R4/R5, R8, R12): Riesgo → Qué hacemos para evitarlo → Qué hacemos si ocurre.

"Los demás riesgos son sobre todo de personas y de reglas.

**Cambios de diseño:** ya pasó, el instituto rechazó la paleta verde en la demo. Por eso los colores viven en un solo lugar: cambiarlos lleva minutos, no un rediseño. **Alcance que crece:** todo pedido nuevo pasa por Martín y se prioriza; lo que no es esencial queda para la próxima cohorte. **Datos personales y fotos de estudiantes:** publicamos solo con consentimiento, según la Ley 25.326, y si hay una queja se retira de inmediato. **Que el panel no se use:** panel simple, capacitación con casos prácticos y acompañamiento las primeras semanas.

El registro se revisa todos los meses, y ningún riesgo se borra: queda como aprendizaje."

---

## d. Costos del proyecto (1:50) — Santiago

### Slide 8 — Qué recibe el instituto
> **Slide:** lista de entregables con ícono (productos y servicios), todos con la etiqueta "incluido".

| Producto | Servicio |
|---|---|
| Sitio público responsive y accesible | Relevamiento y diseño validado con ustedes |
| Panel de administración con roles de usuario | Capacitación a los editores |
| Archivo automático de contenido vencido | Manual de usuario y documentación técnica |
| Integración con Instagram y Facebook por selección | Traspaso del código y mantenimiento inicial |
| Formulario de contacto y accesos a SIU, Aulas y Mi Argentina | Código bajo licencia abierta MIT |

"Lo que el instituto recibe es esto. Productos: el sitio, el panel, el archivo automático, la integración con redes y el contacto. Servicios: el relevamiento, la capacitación, los manuales y el traspaso completo del código, bajo licencia MIT, para que el instituto y futuras cohortes puedan modificarlo y reutilizarlo."

### Slide 9 — Presupuesto de venta
> **Slide:** gráfico de barras apiladas por fase (Análisis USD 2.100 · Diseño 3.300 · Desarrollo 8.400 · Pruebas 2.700 · Capacitación 1.200 · Manual y soporte 1.800 · Mantenimiento inicial 900), y a la derecha una cascada: **USD 20.400 mano de obra + USD 1.292 indirectos = USD 21.692 costo → +25 % = USD 27.115 valor de venta**, con "Costo para el IFTS N°2: USD 0".

"El proyecto son 680 horas de trabajo, a USD 30 la hora, que dan USD 20.400. Sumando los costos indirectos de la empresa, el costo total es de **USD 21.692**. Con una ganancia del 25 %, el **valor de venta de este servicio es de USD 27.115**.

Ahora, sabemos que el instituto no cuenta con ese presupuesto, y por eso el proyecto lo hacemos **sin cobro**: es nuestra práctica profesional. Hosting, base de datos, correo y todas las herramientas usan planes gratuitos, así que **para el instituto el costo es cero**. Solo podría sumar, si quiere, un dominio .com.ar de unos 8.500 pesos al año.

Y hay dos opciones para después: un contrato de mantenimiento de USD 1.800 al año, opcional. Y, para nosotros, reutilizar la plataforma en otras instituciones por unos USD 5.000, lo que nos permite sostener el servicio en el tiempo."

---

## 5. Cierre (0:30) — Martín · Slide 10

> **Slide:** línea de tiempo con los hitos (Reunión 1 ✅ · DEMO ✅ · Versión funcional, semana 13), y una frase de cierre con contacto del equipo y enlace al sitio.

"Para cerrar: ya relevamos, ya validamos el diseño con ustedes y estamos construyendo. Lo que sigue es la versión funcional y la capacitación a los editores. Les pedimos lo de siempre: los contenidos estancos confirmados, las etiquetas (hashtags) para Instagram y que nos digan cómo avanzar con el dominio. Gracias."

---

## Antes de grabar: pendientes y decisiones

1. **Consistencia con la Parte 2 entregada.** Todos los números de arriba salen del PDF "Parte 2 - v final" (680 h, USD 21.692, USD 27.115, 36 % y 86 %, 12 riesgos). Si alguien cambia un dato en la presentación, el video y el TP se contradicen.
2. **Supuestos económicos: confirmados** (son los del trabajo final entregado: USD 4.200 de costos fijos por año y USD 30 la hora).
3. **La aplicación se muestra andando**, de fondo mientras hablamos, compartiendo pantalla en Teams. Sugerencia: tener la app abierta en el sitio público (slides 2–3 y 5) y en el panel (slide 5 y 9), y recorrerla despacio, sin hablar de lo que se ve en pantalla en ese momento sino de lo que cuenta la slide.
4. **Fechas:** las que valen son las del trabajo entregado (cronograma del 28/08 al 18/12, el de Drive). En el video no se dicen fechas de inicio: se usa "semana 6" y "semana 13".
5. **Lenguaje de cliente: ajustado.** Se sacaron WCAG, Lighthouse, API, MVP y cobertura de pruebas del texto hablado. Si alguien dice "WIP", "CPM", "PERT" o "Scrumban", que sea con una frase de explicación. La metodología puede ir en una línea en la slide 7 ("trabajamos en ciclos de dos semanas con revisión del cliente").
6. **Grabación:** en Teams, como en la Etapa 2. Ponerse de acuerdo en el orden de los turnos y en pasar la palabra ("Gastón, te cedo la palabra"). Ensayar con cronómetro: si pasa de 9:30, recortar la slide 8 y la lista de indicadores.
7. **Herramienta:** Google Slides, con la paleta tierra del Figma (`#8D775F`, `#F6F6F3`, `#6F5142`).
