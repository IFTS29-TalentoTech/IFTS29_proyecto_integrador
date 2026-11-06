# Genera el 2° TP integrador de Emprendedurismo (Unidades 4 a 6) en .docx editable.
# Uso: python build_tp2.py   (escribe junto a este archivo)
from pathlib import Path
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = Path(__file__).with_name("TP2 - Emprendedurismo - Unidades 4 a 6.docx")
AZUL = RGBColor(0x1F, 0x3A, 0x5F)

doc = Document()
sec = doc.sections[0]
sec.left_margin = sec.right_margin = Cm(2.2)
sec.top_margin = sec.bottom_margin = Cm(2.0)

st = doc.styles["Normal"]
st.font.name = "Calibri"
st.font.size = Pt(11)
st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
st.paragraph_format.space_after = Pt(6)
st.paragraph_format.line_spacing = 1.1
for name, size in (("Heading 1", 16), ("Heading 2", 13), ("Heading 3", 11.5)):
    h = doc.styles[name]
    h.font.name = "Calibri"
    h.font.size = Pt(size)
    h.font.bold = True
    h.font.color.rgb = AZUL
    h.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    h.paragraph_format.space_before = Pt(14 if name == "Heading 1" else 10)
    h.paragraph_format.space_after = Pt(4)


def shade(cell, hex_):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_)
    tcPr.append(shd)


def runs(p, text):
    """Texto con **negrita** inline."""
    for i, part in enumerate(text.split("**")):
        if part:
            r = p.add_run(part)
            r.bold = i % 2 == 1
    return p


def P(text, style=None, italic=False, align=None):
    p = doc.add_paragraph(style=style)
    runs(p, text)
    if italic:
        for r in p.runs:
            r.italic = True
    if align:
        p.alignment = align
    return p


def B(text):
    return P(text, style="List Bullet")


def H(text, level=1):
    return doc.add_heading(text, level=level)


def table(rows, widths, header=True, size=10):
    t = doc.add_table(rows=len(rows), cols=len(rows[0]))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, row in enumerate(rows):
        for j, txt in enumerate(row):
            c = t.cell(i, j)
            c.width = Cm(widths[j])
            c.text = ""
            p = c.paragraphs[0]
            p.paragraph_format.space_after = Pt(2)
            runs(p, txt)
            for r in p.runs:
                r.font.size = Pt(size)
                if header and i == 0:
                    r.bold = True
            if header and i == 0:
                shade(c, "DCE6F1")
    doc.add_paragraph()
    return t


# ---------------------------------------------------------------- Portada
t = doc.add_paragraph()
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = t.add_run("Seminario de Emprendedorismo")
r.bold = True
r.font.size = Pt(20)
r.font.color.rgb = AZUL
t = doc.add_paragraph()
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = t.add_run("2.° Trabajo Práctico Integrador — Evaluación: Unidades 4 a 6")
r.font.size = Pt(14)

P("**Grupo número:** [completar] (en Gestión de Proyectos: Comisión E, Equipo 08)")
P("**Integrantes y comisión:** completar la comisión de cada integrante en Emprendedurismo.")
table([
    ["Integrante", "Rol en el proyecto", "Comisión"],
    ["Santiago Cuda", "DevOps", "[completar]"],
    ["Adrián Madroñal", "QA", "[completar]"],
    ["Martín Juan", "Product Owner", "[completar]"],
    ["Nicolás Rolón", "Backend", "[completar]"],
    ["Gastón Zampar", "Frontend", "[completar]"],
], [6, 6, 4])

P("**Proyecto:** plataforma institucional y panel de administración para el IFTS N.° 2 DE 20 (Tecnicatura Superior en "
  "Emprendimientos Gastronómicos), el mismo proyecto del TP N.° 1 y de Gestión de Proyectos. El equipo desarrolla la "
  "solución como Software Factory (Talento Tech, IFTS N.° 29).")

# ---------------------------------------------------------------- Pregunta 1
H("Pregunta 1. Modelo Canvas")

P("**Idea, propuesta y modelo.** La idea inicial era “modernizar una página”. La propuesta, ya con problema, cliente y "
  "valor, es una plataforma que el propio instituto puede mantener actualizada sin saber programar. El modelo de negocio "
  "explica cómo esa propuesta funciona en la realidad: quién la usa y quién decide, cómo llega, qué se necesita para "
  "sostenerla y cómo se financia. El lienzo siguiente resume los nueve bloques; luego se fundamenta cada uno.")

# Lienzo visual 5 columnas x 3 filas con celdas combinadas
cv = doc.add_table(rows=3, cols=5)
cv.style = "Table Grid"
cv.alignment = WD_TABLE_ALIGNMENT.CENTER
W = Cm(3.3)
for row in cv.rows:
    for c in row.cells:
        c.width = W
# columnas: 0 socios | 1 actividades/recursos | 2 propuesta | 3 relación/canales | 4 segmentos
cv.cell(0, 0).merge(cv.cell(1, 0))
cv.cell(0, 2).merge(cv.cell(1, 2))
cv.cell(0, 4).merge(cv.cell(1, 4))
cv.cell(2, 0).merge(cv.cell(2, 2))
cv.cell(2, 3).merge(cv.cell(2, 4))

blocks = {
    (0, 0): ("Socios clave", ["IFTS N.° 29 y cátedra", "GCABA / Ministerio de Educación (.edu.ar, SIU, Aulas Virtuales, Mi Argentina)", "Meta (API de Instagram)", "Hosting, base de datos y almacenamiento en planes gratuitos"], "EAF1DD"),
    (0, 1): ("Actividades clave", ["Relevamiento y validación", "Diseño y desarrollo", "Pruebas y despliegue", "Capacitación y soporte"], "EAF1DD"),
    (1, 1): ("Recursos clave", ["Equipo de 5 roles", "Código y documentación", "Prototipo en Figma", "Plataforma desplegada"], "EAF1DD"),
    (0, 2): ("Propuesta de valor", ["Un sitio institucional que el propio equipo del instituto actualiza sin depender de terceros", "Información vigente, nada se pierde (archivo)", "Redes seleccionadas por criterio editorial", "Costo cero de operación para el cliente"], "FFF2CC"),
    (0, 3): ("Relación con clientes", ["Acompañamiento personal", "Co-creación con prototipos", "Manual y capacitación", "Soporte por correo"], "FCE4D6"),
    (1, 3): ("Canales", ["Demostración con el caso real", "Contacto directo y alianzas institucionales", "Sitio y redes del equipo", "Repositorio público"], "FCE4D6"),
    (0, 4): ("Segmentos de clientes", ["**Decisor:** conducción del instituto", "**Usuarios administradores:** docentes y bedelía", "**Usuarios finales:** alumnos, aspirantes, egresados", "**Réplica:** otros IFTS y escuelas"], "FCE4D6"),
    (2, 0): ("Estructura de costos", ["Horas del equipo (costo principal)", "Infraestructura según tráfico", "Dominio", "Soporte y capacitación", "Difusión mínima"], "F2DCDB"),
    (2, 3): ("Fuentes de ingresos", ["Desarrollo sin cobro para el IFTS N.° 2 (práctica profesionalizante)", "Mantenimiento anual opcional", "Implementación para otras instituciones", "Capacitación y horas de evolución"], "F2DCDB"),
}
for (i, j), (title, items, color) in blocks.items():
    c = cv.cell(i, j)
    shade(c, color)
    c.text = ""
    p = c.paragraphs[0]
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(title)
    r.bold = True
    r.font.size = Pt(9.5)
    for it in items:
        q = c.add_paragraph()
        q.paragraph_format.space_after = Pt(1)
        runs(q, "• " + it)
        for rr in q.runs:
            rr.font.size = Pt(8.5)
doc.add_paragraph()

H("1.1. Propuesta de valor", 2)
P("**Qué es y qué problema resuelve.** El sitio actual del IFTS N.° 2 está en Google Sites, sin administración "
  "efectiva: mezcla horarios y mesas de examen de 2021 a 2026, usa archivos incrustados, no tiene formulario de "
  "contacto y no se vincula con las redes. El problema no es solo estético: la información importante pierde vigencia "
  "y las consultas de alumnos recaen informalmente sobre pocas personas. La propuesta es una plataforma pública con un "
  "panel de gestión propio.")
P("**Beneficio concreto.** Los administradores (docentes sin formación técnica) publican avisos, cargan grillas de "
  "horarios y llamados a examen y eligen qué publicaciones de Instagram se muestran, con vigencia definida; lo vencido "
  "se archiva y se puede restaurar, nunca se borra por error. Los alumnos y aspirantes encuentran en un solo lugar lo "
  "vigente y los accesos a SIU Guaraní, Aulas Virtuales y Mi Argentina.")
P("**Por qué elegirla frente a otras alternativas.** Frente a mantener Google Sites o contratar un CMS genérico, la "
  "plataforma está hecha a la medida del funcionamiento del instituto (contenido estanco vs. dinámico, selección "
  "editorial, roles de Rectoría y Bedelía), no cuesta nada de operar mientras alcance la infraestructura gratuita y "
  "viene con capacitación y acompañamiento del equipo que la construyó. Como indica la Unidad 4, nadie compra líneas "
  "de código: se elige la solución al problema que se ahorra. Y encaja con la frase ancla del cliente (“no formamos "
  "chefs, formamos empresarios gastronómicos”): un instituto que forma emprendedores necesita una comunicación a la "
  "altura.")

H("1.2. Segmentos de clientes", 2)
P("Quien usa la solución no es quien decide, por lo que se distinguen roles:")
table([
    ["Rol", "Quiénes", "Qué necesitan"],
    ["**Decisor / cliente**", "Rectoría del IFTS N.° 2 (Cecilia) y asesoría pedagógica; supervisión del GCABA para el dominio", "Comunicar con confianza la identidad institucional; aprobar alcance y contenidos"],
    ["**Usuarios administradores**", "Matías Peláez, María del Carmen Canobi y Bedelía Académica", "Cargar y archivar contenido en pocos pasos, sin conocimientos técnicos"],
    ["**Usuarios finales**", "Alumnos, egresados y aspirantes (150 a 200 en cada ingreso; picos estimados de 300 a 400 concurrentes)", "Encontrar horarios, mesas, inscripciones y trámites desde el celular"],
    ["**Segmento de réplica**", "Otros IFTS, escuelas técnicas y organismos públicos con sitios desactualizados y sin presupuesto", "La misma solución adaptada, con bajo costo y acompañamiento"],
], [3.8, 6.4, 6.4])
P("Es un modelo con varios actores: el valor lo perciben los usuarios finales, lo opera el personal administrativo y "
  "lo valida quien conduce la institución; cada uno requiere un mensaje y un canal distintos.")

H("1.3. Canales", 2)
B("**Cómo se da a conocer:** demostración del caso real del IFTS N.° 2 (el prototipo y la plataforma funcionando), "
  "presentación del equipo en su sitio y redes profesionales, y recomendación entre instituciones.")
B("**Cómo se comercializa:** contacto directo con autoridades de otros institutos, acuerdos de alcance simples y "
  "propuestas a medida; en el caso actual, la propia modalidad de la cátedra.")
B("**Cómo se entrega:** como aplicación web desplegada en línea (modelo de servicio, no instalación en el instituto), "
  "con manual de usuario, manual técnico y capacitación inicial. El código queda disponible en un repositorio.")

H("1.4. Relación con los clientes", 2)
P("Se combina **asistencia personal** en la etapa de implementación (reuniones, validación de prototipos, pruebas "
  "con tareas reales como cargar una novedad o archivar un evento) con **autoservicio** cotidiano: el panel y su manual "
  "permiten operar sin intervención. Esta lógica sigue la distinción de la Unidad 4 entre soporte automatizado y "
  "personalizado: como los administradores no son técnicos, el vínculo debe ser cercano al inicio y reducirse a medida "
  "que ganan autonomía. El soporte posterior se canaliza por correo y, si hay contrato, con tiempos de respuesta acordados.")

H("1.5. Fuentes de ingresos", 2)
P("El IFTS N.° 2 no tiene presupuesto para servicios digitales (su caja chica se destina a materia prima para las "
  "prácticas), por lo que el ingreso no puede basarse en cobrarle el desarrollo. Las alternativas evaluadas son:")
B("**Pago único** por implementación: no es viable con este cliente; sí con instituciones que dispongan de presupuesto "
  "(el equipo estimó en Gestión de Proyectos un precio muy inferior si se reutiliza el modelo, a validar).")
B("**Suscripción o contrato de mantenimiento anual opcional** (soporte, correcciones y mejoras): es el ingreso "
  "recurrente más razonable para software a medida; la estimación de Gestión de Proyectos es de USD 1.800 por año.")
B("**Pago por servicios:** capacitación, carga inicial de contenidos y paquetes de horas de evolución.")
B("**Licencias:** descartadas como fuente de ingreso. El código se publica con licencia abierta (MIT), decisión "
  "coherente con un cliente público y un proyecto educativo; lo que se vende es el servicio, no el código.")
P("En lo inmediato el retorno es profesional: un caso real para el portfolio y una referencia para captar nuevos "
  "clientes. Es una limitación honesta del modelo y se retoma en la Pregunta 3 (financiamiento).")

H("1.6. Recursos clave", 2)
B("**Humanos:** equipo de cinco integrantes con roles de producto, frontend, backend, QA y DevOps.")
B("**Intelectuales:** código fuente, documentación (Manual Técnico y de Usuario), prototipo en Figma, conocimiento "
  "del funcionamiento de los institutos y el criterio de contenido estanco vs. dinámico.")
B("**Tecnológicos:** aplicación desplegada, base de datos, almacenamiento de imágenes y documentos, correo, "
  "control de versiones y herramientas de gestión.")
B("**Relacionales:** acceso a los referentes del instituto y a la cátedra para validar.")

H("1.7. Actividades clave", 2)
B("Relevar necesidades y validar con los usuarios administradores (reuniones, prototipo, pruebas de uso).")
B("Diseñar y desarrollar el sitio, el panel y las integraciones, con pruebas y despliegue.")
B("Capacitar al instituto y documentar para que la operación no dependa del equipo.")
B("Brindar soporte y mantener la integración con servicios externos.")
B("Difundir el caso para generar nuevos clientes.")

H("1.8. Socios clave", 2)
B("**IFTS N.° 29 y su cátedra:** marco, mentoría y evaluación; permite trabajar el caso como práctica.")
B("**GCABA / Ministerio de Educación:** dominio .edu.ar y sistemas con los que se integra el sitio (SIU Guaraní, "
  "Aulas Virtuales, Mi Argentina).")
B("**Meta (Instagram/Facebook):** fuente del contenido que el instituto selecciona; sujeta a sus condiciones y APIs.")
B("**Proveedores de infraestructura:** hosting, base de datos, almacenamiento y correo en planes gratuitos; "
  "librerías y herramientas de código abierto.")
P("Hay dependencias reales (Meta, límites de los planes gratuitos); ninguna es propia, por lo que se documentan y se "
  "prevén alternativas.")

H("1.9. Estructura de costos", 2)
P("Solo se identifican los tipos de costo, sin cálculos (se trabajan en Gestión de Proyectos):")
B("**Fijos:** horas de trabajo del equipo (el costo principal, como señala la Unidad 4 para el software), "
  "herramientas de gestión y diseño.")
B("**Variables:** infraestructura y almacenamiento, que crecen con el tráfico y el volumen de imágenes; servicios de "
  "terceros si superan el plan gratuito.")
B("**Recurrentes menores:** dominio anual, soporte posterior y capacitación.")
B("**De comercialización:** material de presentación y difusión, mínimo.")

H("1.10. Coherencia del modelo como sistema", 2)
P("Según la Unidad 4, un modelo de negocio es un sistema de relaciones: cada decisión impacta en el resto. Acá la "
  "restricción central es que el cliente no puede pagar. Por eso el modelo ofrece valor sin costo de operación "
  "(infraestructura gratuita), lo que obliga a recursos y actividades livianas y a **autoservicio** en la relación con "
  "el cliente. Los ingresos pasan a depender de la **réplica** a otras instituciones y del **mantenimiento opcional**, "
  "lo que justifica una solución reutilizable, documentada y con licencia abierta. A su vez, la reputación del caso "
  "real alimenta los canales de difusión. Si el cliente pidiera más (más tráfico, más módulos), subirían los costos "
  "variables y habría que renegociar ingresos: el modelo es viable mientras alcance y capacidad se mantengan acotados.")

# ---------------------------------------------------------------- Pregunta 2
H("Pregunta 2. Estrategia de marketing y comunicación")

H("a. Público objetivo", 2)
P("El público al que se dirige la estrategia de difusión es el **personal directivo y administrativo de institutos de "
  "formación técnica superior (IFTS) y escuelas públicas de la Ciudad de Buenos Aires**, que son quienes deciden "
  "adoptar la solución. Se segmenta por criterios:")
B("**Geográfico:** CABA y Gran Buenos Aires, donde el equipo puede acompañar de forma presencial o remota.")
B("**Demográfico/organizacional:** instituciones públicas de educación técnica con presupuesto limitado.")
B("**Comportamiento:** instituciones que actualizan información con frecuencia (inscripciones, mesas de examen, "
  "eventos) y hoy lo hacen con un sitio gratuito abandonado o solo por redes.")
B("**Psicográfico:** equipos que valoran la autonomía y la imagen institucional, pero no tienen personal técnico.")
P("**Por qué es relevante:** comparte con el IFTS N.° 2 el problema, la restricción de recursos y el perfil de "
  "administradores. Esto permite replicar lo aprendido con poco ajuste. Sigue la lógica de la Vaca Púrpura de "
  "Godin: en lugar de apuntar a “todas las organizaciones”, empezar por un nicho reducido donde la propuesta sea "
  "claramente valiosa y desde ahí crecer. Como público secundario, los alumnos y aspirantes del instituto, que validan "
  "la utilidad del sitio.")

H("b. Posicionamiento", 2)
P("Se destacará el aspecto **“tu equipo lo actualiza solo, sin saber programar, y nada se pierde”**: simplicidad de "
  "autogestión, archivo en lugar de borrado y curaduría editorial de redes. No se comunicará la tecnología (lenguajes, "
  "arquitectura), porque, según la Unidad 5, el cliente percibe el beneficio y no el detalle técnico. Los competidores "
  "reales son Google Sites, un CMS genérico (que exige conocimiento técnico) o contratar a un tercero, que implica "
  "costo y dependencia. Frente a ellos, el posicionamiento es: **hecha a la medida de un instituto, sin costo de "
  "operación y con acompañamiento de quienes la construyeron.**")

H("c. Canales y herramientas de comunicación", 2)
table([
    ["Canal", "Uso", "Por qué es adecuado"],
    ["**Demostración con el caso real**", "Mostrar el sitio y el panel funcionando, con una tarea concreta (cargar un aviso, archivar un evento)", "Los directivos deciden al ver el resultado; es la prueba más creíble y no cuesta"],
    ["**Contacto directo y alianzas**", "Reuniones con equipos directivos de otros IFTS, a través del propio IFTS N.° 2 y la supervisión", "La confianza institucional circula por recomendación; es el canal con mejor relación costo-resultado"],
    ["**Sitio web y redes profesionales del equipo**", "Publicar el caso, capturas, resultados y contacto", "Da visibilidad y credibilidad a quien busca referencias"],
], [4.2, 6.2, 6.2])
P("Estos canales se priorizan sobre la publicidad paga, que no se justifica con presupuesto casi nulo y con un público "
  "reducido y fácil de identificar.")

H("d. Mensaje de presentación", 2)
P("“Si el sitio de tu instituto está desactualizado y nadie tiene tiempo de mantenerlo, tenemos una solución simple: "
  "una plataforma donde tu equipo publica avisos, horarios y novedades sin saber programar, elige qué mostrar de "
  "Instagram y archiva lo vencido sin perder nada. La desarrollamos junto al IFTS N.° 2 y no te generará costos de "
  "infraestructura. Te mostramos cómo funciona en 15 minutos.”", italic=True)

# ---------------------------------------------------------------- Pregunta 3
H("Pregunta 3. Redes profesionales")

P("Según la Unidad 6, los emprendimientos crecen porque acceden a información, clientes, socios y oportunidades que "
  "circulan por redes, y el capital social suele pesar tanto como el financiero. El proyecto tiene capital humano "
  "(conocimientos del equipo) y un caso real, pero poco capital social fuera del círculo del IFTS N.° 2 y carece de "
  "capital financiero. Para ampliar sus posibilidades necesita, sobre todo, **relaciones** que lo conecten con nuevos "
  "clientes, con respaldo institucional y con recursos para sostenerse.")

H("a y b. Actores estratégicos, aporte y vínculo", 2)
table([
    ["Actor", "Aporte posible", "Cómo se establecería el vínculo"],
    ["**Autoridades y referentes del IFTS N.° 2** (Rectoría, asesoría pedagógica, Matías Peláez y María del Carmen Canobi)",
     "Es el cliente de referencia: valida la solución, brinda un testimonio y puede recomendarla a otros institutos",
     "Sostener la relación después de la entrega: capacitación, seguimiento del uso y una devolución final formal. Pedir una carta de recomendación y presentar resultados concretos (tiempo de actualización, consultas resueltas)"],
    ["**Supervisión y áreas del Ministerio de Educación del GCABA**",
     "Acceso a otros IFTS y escuelas (potenciales clientes), gestión del dominio .edu.ar y orientación sobre la integración con SIU, Aulas Virtuales y Mi Argentina",
     "Contacto formal a través del IFTS N.° 2, con una presentación breve del caso y de lo que se necesita. Aportar valor primero, por ejemplo con la documentación para el trámite del dominio"],
    ["**IFTS N.° 29 y su cátedra** (docentes de Desarrollo de Software)",
     "Mentoría técnica y profesional, espacios de difusión, acceso a futuras cohortes que podrían mantener o evolucionar la plataforma",
     "Mantener comunicación regular, presentar avances, usar el repositorio abierto como medio de traspaso y proponer continuidad del proyecto"],
    ["**Otros institutos y escuelas técnicas** (directivos, equipos administrativos)",
     "Nuevos clientes con necesidades similares; sus requerimientos mejoran el producto",
     "Presentación mediante demostración, a partir de recomendaciones del IFTS N.° 2 o de la supervisión. Ofrecer una prueba piloto acotada antes de cualquier compromiso"],
    ["**Comunidad profesional y proveedores tecnológicos** (comunidades de software abierto, eventos del sector, programadores y diseñadores freelance)",
     "Aprendizaje, solución de problemas técnicos (por ejemplo, límites de la API de Instagram), posibles colaboradores y primeros contactos laborales",
     "Participar en eventos y comunidades, publicar aprendizajes del proyecto y colaborar con aportes antes de pedir ayuda (reciprocidad)"],
], [4.6, 6, 6.4], size=9.5)

P("**Cómo se construye el vínculo (criterio común).** Siguiendo la lógica del networking de la Unidad 6, no se trata de "
  "“juntar contactos” sino de generar relaciones sostenidas por reciprocidad y valor: ofrecer primero (demostraciones, "
  "documentación, resultados) y pedir después (recomendaciones, presentaciones). Las redes deben construirse antes de "
  "necesitarlas, por lo que conviene empezar durante la entrega y no al buscar el segundo cliente.")

H("Marca profesional del equipo", 2)
P("La marca personal es la percepción que otros construyen sobre un profesional, no un logotipo ni una cuenta. "
  "Para el equipo, se apoya en cuatro componentes: **competencia** (una plataforma funcional con pruebas y manuales), "
  "**credibilidad** (cumplir los plazos con el cliente y no prometer capacidades sin validar), **diferenciación** "
  "(especialización en instituciones educativas y usuarios no técnicos) y **visibilidad** (portfolio, resultados y "
  "recomendaciones). Se evita confundir presencia digital con visibilidad profesional: lo importante no es publicar "
  "mucho, sino mostrar casos concretos y alineados con la propuesta de valor.")

H("Financiamiento para sostener el proyecto", 2)
P("El proyecto se financia hoy con **recursos propios** (bootstrapping): horas del equipo y herramientas gratuitas. "
  "Esto aporta independencia y control, pero implica recursos limitados, crecimiento lento y riesgo personal. Otras "
  "vías serían los **programas de apoyo a emprendedores** (capacitación, mentoría, subsidios o créditos, a explorar a "
  "través de la cátedra y organismos del GCABA) y los **ingresos del mantenimiento** de clientes que sí puedan pagar. "
  "El financiamiento colectivo no parece adecuado, ya que el producto es un servicio institucional con pocos "
  "clientes y no tiene un público masivo que lo respalde.")

P("**Conclusión.** Las tres formas de capital de la Unidad 6 se resumen así: el capital **humano** del equipo ya está "
  "presente, el **social** se construye con los actores anteriores y el **financiero** depende de transformar el caso "
  "del IFTS N.° 2 en clientes que paguen mantenimiento o implementación. La ausencia de cualquiera de los tres "
  "limita el crecimiento, por lo que la prioridad es consolidar la relación con el cliente de referencia y abrir "
  "el segundo cliente.")

H("Material consultado", 2)
for m in [
    "Unidad 4 — Modelo Canvas y Semana 7: Modelos de negocio y planificación (Seminario de Emprendedorismo).",
    "Unidad 5 — Estrategias de marketing y comunicación.",
    "Unidad 6 — Marca personal, redes profesionales y financiamiento.",
    "Osterwalder, A. y Pigneur, Y. El lienzo del modelo de negocio (Generación de modelos de negocio).",
    "La Segmentación de Mercado y Resumen de La Vaca Púrpura (Seth Godin).",
    "TP N.° 1 de Emprendedurismo y TP de Gestión de Proyectos (Partes 1 y 2) del mismo proyecto.",
]:
    B(m)

doc.save(OUT)
print("OK", OUT)
