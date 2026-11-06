# Guion del video para el cliente — Plataforma web del IFTS N°2

**Público:** el equipo del IFTS N°2 (Matías Peláez, María del Carmen Canobi y quienes validan el alcance): personas que **no son técnicas** y que van a usar el sistema. **Duración:** máximo 10 minutos (objetivo: **9:00**). **Formato:** demostración de la aplicación en ejecución, con una o dos slides de apoyo.

Este video **no explica cómo está hecho**. Muestra qué puede hacer cada persona del instituto y qué cambia en su trabajo. Sin palabras como API, base de datos, código ni CRUD: se dice "aviso", "panel", "archivo", "permiso".

## Idea del video

Seguimos **un día en el instituto**, de punta a punta, con las personas reales que lo van a usar:

1. Un aspirante o estudiante entra al **sitio** y encuentra lo que busca.
2. **Bedelía** carga un aviso y los horarios, y se ven en el sitio al instante.
3. **Comunicación** elige qué publicaciones de Instagram se muestran.
4. La **dirección** ordena la configuración y, con el **Superadministrador**, decide quién puede hacer qué.

Cada parte responde a algo que el instituto pidió en la reunión de relevamiento: un sitio a la altura de la carrera, que se mantenga sin ayuda técnica, siempre vigente, con lo vencido archivado y no borrado, y con el criterio editorial de redes en manos del instituto.

## Reparto y tiempos

| # | Quién | Bloque | Pantalla | Tiempo |
|---|---|---|---|---|
| 1 | Martín | Apertura: qué pidieron y qué van a ver | Slide 1 | 1:00 |
| 2 | Gastón | El sitio público, visto por un estudiante | Sitio | 1:50 |
| 3 | Adrián | Bedelía: avisos, horarios, llamados y archivo | Panel | 1:50 |
| 4 | Nicolás | Comunicación: Instagram y mensajes de contacto | Panel | 1:30 |
| 5 | Santiago | Dirección: configuración, usuarios y **roles y permisos** | Panel | 1:45 |
| 6 | Martín | Cierre: costo, próximos pasos y qué necesitamos | Slide 2 | 0:45 |
| | | **Total** | | **8:40** |

Quedan más de 80 segundos de margen. Todos con cámara encendida al presentarse; cada uno cede la palabra al siguiente por su nombre.

---

## 1. Martín — Apertura (1:00)

> **Slide 1:** "Lo que pidieron" a la izquierda en cinco renglones (los de abajo) y "Lo que van a ver" a la derecha: sitio público y panel de gestión.
> 1. Un sitio a la altura de la carrera. 2. Que lo mantengan ustedes, sin depender de nadie. 3. Información siempre vigente. 4. Lo vencido se archiva, no se borra. 5. Las redes, con el criterio del instituto.

"Buenas, somos el equipo Talento Tech. En la reunión del 4 de septiembre nos contaron qué necesitaban: un sitio que refleje lo que es la tecnicatura, que lo puedan mantener ustedes mismos, que muestre siempre lo vigente y que lo viejo se archive y no se pierda. Y que de las redes se publique solo lo que ustedes elijan.

Hoy les mostramos cómo quedó, con la aplicación funcionando. Vamos a seguir lo que pasa en un día en el instituto, y vamos a ver cómo cada persona entra y encuentra solo lo suyo. Gastón, empezamos por el sitio."

---

## 2. Gastón — El sitio público, visto por un estudiante (1:50)

*Compartir pantalla: sitio público, `http://localhost:3000` (o el enlace desplegado, si ya existe).*

| Paso | Qué mostrar | Qué decir |
|---|---|---|
| 1 | **Inicio** | "Esta es la cara del instituto. Usa la paleta de marrones que definimos con ustedes después de la demo." |
| 2 | **La carrera** | "Qué se estudia, el perfil del egresado, el plan." |
| 3 | **Ingreso** | "Acá entra un aspirante: convocatoria, requisitos y pasos." |
| 4 | **Estudiantes** | "Esta es la pantalla que más van a usar los alumnos. Avisos vigentes, horarios y mesas de examen **del ciclo actual**. Nada vencido, nada mezclado." |
| 5 | **Inscripciones** | "Los llamados a examen y el acceso directo a SIU Guaraní. También están Aulas Virtuales y Mi Argentina." |
| 6 | **Novedades** | "Lo que el instituto decide mostrar de sus redes." |
| 7 | **Institucional → contacto**: llenar el formulario | "Una consulta llega al correo del instituto. Pide el consentimiento para usar los datos." |
| 8 | Achicar la ventana (celular) | "Y todo se ve bien en el celular." |

"Todo lo que ven acá lo carga el propio instituto desde el panel. Adrián, ¿cómo lo carga Bedelía?"

---

## 3. Adrián — Bedelía: avisos, horarios, llamados y archivo (1:50)

*Compartir pantalla: panel, ingresando como Bedelía.*

| Paso | Qué mostrar | Qué decir |
|---|---|---|
| 1 | **Ingreso al panel** y pantalla **Resumen** | "Cada persona entra con su usuario y ve solo lo que le corresponde." |
| 2 | **Avisos académicos → Nuevo aviso**: título, texto, destinatarios, fecha de vencimiento | "Un aviso se escribe como un correo. Si falta algo, el sistema lo dice claro y no guarda nada." Dejar el título vacío un segundo para mostrar el mensaje. |
| 3 | **Publicar** y mostrar el aviso en **Estudiantes** (otra pestaña) | "Y ya está en el sitio. Sin pedirle nada a nadie." |
| 4 | **Horarios y llamados**: mostrar un llamado, por ejemplo el turno extraordinario de diciembre | "Los horarios y mesas se cargan por archivo y quedan asociados al ciclo." |
| 5 | **Pausar** el aviso y **Eliminar** (ventana de confirmación; Cancelar y después confirmar) | "Si algo se publicó por error, se pausa. Y eliminar siempre pide confirmación." |
| 6 | **Archivo**: buscar un documento de años anteriores y **Restaurar** | "Lo vencido no se borra: queda guardado en el archivo y se puede volver a publicar." |

"Todo esto lo hace Bedelía. Las redes sociales las maneja otra persona. Nicolás."

---

## 4. Nicolás — Comunicación: Instagram y mensajes (1:30)

*Compartir pantalla: panel, ingresando como Comunicación.*

| Paso | Qué mostrar | Qué decir |
|---|---|---|
| 1 | **Publicaciones**: lista de publicaciones detectadas de Instagram (filtro **Instagram**, estado **Pendiente**) | "El sistema detecta lo que el instituto publica con la etiqueta acordada. **Nada llega al sitio sin que una persona lo apruebe.**" |
| 2 | **Aprobar** una: elegir sección, fecha hasta la que se muestra y confirmar que hay consentimiento si tiene fotos | "Se elige dónde aparece y hasta cuándo. Si hay fotos de estudiantes, hay que confirmar el consentimiento." |
| 3 | **Descartar** otra y mostrar que se recupera desde Descartadas | "Lo que no es relevante se descarta, y se puede recuperar." |
| 4 | **Nueva publicación** propia (borrador) | "También se pueden escribir novedades propias, sin pasar por Instagram." |
| 5 | **Mensajes**: ver la consulta enviada en el paso 7 del sitio | "Las consultas del sitio llegan acá, para que las responda quien corresponda." |

**Aclaración honesta, dicha en el video:** "La conexión real con la cuenta de Instagram del instituto la configuran ustedes desde el panel, con una guía paso a paso. En esta demostración trabajamos con publicaciones de ejemplo."

"Y ahora, cómo se organiza todo esto. Santiago."

---

## 5. Santiago — Dirección: configuración, usuarios y roles (1:45)

*Compartir pantalla: panel, ingresando como Superadministrador.*

| Paso | Qué mostrar | Qué decir |
|---|---|---|
| 1 | **Configuración → período académico** (año y cuatrimestre) | "Con un cambio, todo el sitio pasa a mostrar el cuatrimestre nuevo." |
| 2 | **Datos institucionales y enlaces** (SIU, Aulas Virtuales, Mi Argentina, correo de contacto) | "Dirección, teléfono, correo y los accesos del sitio se editan acá." |
| 3 | **Usuarios**: crear un usuario y asignarle un rol; mostrar el aviso si el correo ya existe | "Cada persona tiene su usuario. Administración puede crear usuarios, también otros administradores. Lo que no puede es crear superadministradores ni darle a alguien más permisos de los que tiene." |
| 4 | **Roles y permisos** *(nuevo, solo Superadministrador)*: crear un rol, por ejemplo **Prensa**, y tildar solo lo que puede hacer (Publicaciones y Resumen) | "Hay roles ya armados, como Bedelía, Comunicación y Administración. Pero el instituto no queda atado a ellos: el **superadministrador** puede crear un rol nuevo, y también ajustar los que ya existen, eligiendo casilla por casilla exactamente qué puede hacer cada uno." |
| 5 | Asignar **Prensa** a un usuario, ingresar con ese usuario y mostrar que ve solo **Publicaciones y Resumen** | "La persona con este rol no ve ni puede usar nada más." |
| 6 | Volver al Superadministrador y mostrar el **registro de actividad** (quién creó el rol y cuándo) | "Todo queda registrado: quién hizo qué y cuándo." |

"Hay una sola regla de seguridad que vale la pena decir: siempre tiene que haber al menos un superadministrador, para que el sistema nunca quede sin nadie que pueda administrar los accesos. Martín, cerramos."

> **Importante:** el rol Superadministrador y la pantalla de Roles y permisos se desarrollan hoy (ver RF11 y ADR-18 en `especificaciones/`). Se graba este paso **solo si ya funciona**. Si no está listo, se reemplaza por una frase ("estamos terminando una pantalla para que el superadministrador cree roles y permisos a medida") y no se muestra nada que no exista.

---

## 6. Martín — Cierre (0:45)

> **Slide 2:** "Costo para el instituto: $0" · "Próximos pasos" (versión funcional, capacitación a los editores, manual de usuario) · "Qué necesitamos de ustedes" (lista).

"Para resumir: el sitio y el panel ya funcionan. La meta es que para el instituto el costo de funcionamiento sea cero, con servicios gratuitos; estamos terminando de definir dónde va a quedar publicado. Lo que sigue es la versión final, la capacitación a quienes van a cargar contenido y el manual de usuario.

Para terminar de ajustar el sistema, necesitamos de ustedes cinco cosas: la ubicación de las materias por año y las fechas y requisitos de ingreso; las etiquetas que van a usar en Instagram; cómo avanzar con el dominio .edu.ar; **quién va a ser la persona superadministradora** y qué roles necesitan además de los que ya vimos; y que nos digan qué cambiarían del diseño. Gracias."

---

## Qué evitar y qué decir con cuidado

- **Jerga:** no decir API, base de datos, token, CRUD, endpoint, build. Decir "el sistema", "el panel", "se guarda".
- **Prometer solo lo que está:** Instagram real, correo real y el sitio publicado en internet **todavía no están** (el sitio corre en una computadora del equipo). Decirlo una vez, con naturalidad, en el bloque de Nicolás y en el cierre.
- **Roles:** presentar los tres roles ya armados como *ejemplos* y los roles a medida como una posibilidad, no como un requisito. El cliente decide quién es superadministrador (pregunta Q22 en `09-preguntas-abiertas.md`).
- **Tono:** rioplatense, cercano y claro. Hablarle a "ustedes", al equipo del instituto.

## Antes de grabar

1. **Estado inicial:** base con la semilla de demostración, con un aviso vigente, uno vencido y publicaciones de Instagram de ejemplo detectadas. Un usuario por rol más uno **SUPERADMIN**, y un usuario de prueba sin rol asignado para el paso 5 del bloque de Santiago.
2. **Ensayo con cronómetro**, empezando de cero. Si se pasa de 9:30, recortar el paso 8 de Gastón y el paso 6 de Santiago.
3. **Datos del cliente:** usar los nombres reales de la carrera y del plantel solo si el instituto lo permitió; si no, datos de ejemplo.
4. **Formato:** Teams, como en los otros videos; todos con cámara encendida; mismo nivel de audio. Si se puede, subtítulos: el video va a ser visto por personas que no conocen los términos.
5. **Pendiente de decidir:** si el video lo ve el cliente por separado o también se presenta en una reunión; en ese caso conviene una pregunta abierta al final ("¿qué le sacarían o agregarían?").
