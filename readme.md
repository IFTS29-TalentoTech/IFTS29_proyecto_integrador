# Proyecto Integrador — Talento Tech × IFTS N°2

Repositorio de trabajo del equipo **Talento Tech** (IFTS N°29, Tecnicatura Superior en Desarrollo de Software, 2° cuatrimestre 2026). Un único proyecto —modernizar el sitio institucional del **IFTS N°2 DE 20** (Tec. Sup. en Emprendimientos Gastronómicos)— alimenta los trabajos prácticos de varias materias. El contexto del proyecto vive una sola vez en `proyecto/`; cada materia tiene su carpeta con consigna y entregas.

**Equipo:** Santiago Cuda (DevOps) · Adrián Madroñal (QA) · Martín Juan (Product Owner) · Nicolás Rolón (Backend) · Gastón Zampar (Frontend).
**Sitio de presentación del equipo:** talento-tech-group.vercel.app

## Enlaces

- **Figma (MVP visual y panel de administración):** https://www.figma.com/design/aRnoXCbNpkCFkHPH0En5B5/IFTS-N%25C2%25B0-2-%25E2%2580%2594-MVP-visual-y-panel-de-administraci%25C3%25B3n?node-id=0-1&p=f — 13 pantallas de escritorio, ~25 modales y 7 móviles (actualizado 18/10/2026; detalle en `proyecto/context.md` §5). Los PNG de `entrega-2/wireframes/` son de la versión anterior (verde). Se lee con el conector de Figma (cuenta zamparg; plan Starter = 20 llamadas/mes, usar con cuidado).

## Estructura

```
.
├── readme.md                  Este archivo (índice + estado). CLAUDE.md lo importa.
├── agents/                    Agentes/personas de IA reutilizables
│   └── agente-gestion-proyecto.md   Asesor de gestión (OKR, KPI, SMART, riesgos, WBS)
├── proyecto/                  FUENTE DE VERDAD compartida por todas las materias
│   ├── context.md             Cliente, estado del sitio, requerimientos, restricciones, cronograma  ← leer primero
│   ├── decisiones.md          Bitácora de decisiones (D-001: desarrollo a medida, NO WordPress; etc.) + diagramas/
│   ├── propuesta-para-cliente.md   Resumen ejecutivo orientado al cliente
│   ├── notes.md               Notas crudas de la reunión de relevamiento
│   ├── Meeting Transcription.pdf   Transcripción reunión 04/09/2026
├── cliente/ifts2/             Material del cliente y consigna general: logos, plan de carrera, links a vincular, PROYECTO INTEGRADOR IFTS 2 2026.docx, minuta 30/06
├── referencias/               Normativa y estilo: Ley de Pasantías, Práctica Profesionalizante (Ministerio), Manual de Estilo GCABA
└── materias/
    ├── ppiv-proyecto-integrador/     Práctica Profesionalizante IV
    │   ├── consigna/          Etapa 2 (PDF + resumen del docente)
    │   ├── entrega-1/         Etapa 1 (PDF), sitio HTML interactivo, estructura de contenido
    │   ├── entrega-2/         Etapa 2 armada: etapa-2-documento.md (fuente) → "Etapa 2 - Proyecto Integrador.pdf",
    │   │                      diagramas/ (.mmd editables + .svg/.png), presentacion-guion.md, wireframes/ (PNG de Figma),
    │   │                      build.py (regenera HTML y PDF), prompt-lovable-maqueta.md
    │   ├── entrega-3/         ETAPA 3: paquete de especificaciones para que un agente en otro repo genere el MVP
    │   │                      (README.md, AGENTS.md, especificaciones/00..09, prisma/schema.prisma, design-tokens.json)
    │   └── material/          ITIL 4, Modelado de Sistemas, Vicente y Ayala cap. 7
    ├── gestion-de-proyectos/
    │   ├── consigna/          Propuesta de TP integrador + rúbrica
    │   ├── entrega-1/         Parte 1 (docx + pdf de trabajo, y PDF "Comisión E Equipo 08")
    │   └── entrega-2/         Parte 2: parte-2.md + build_gdp.py + cpm.py (CPM/PERT) → PDF, diagramas/ (Gantt, red CPM)
    └── emprendedorismo/
        ├── consigna/          1° TP integrador (Unidades 1 a 3)
        ├── entrega-1/         trabajo-practico-integrador.md
        ├── entrega-2/         (vacía)
        └── material/          Lecturas y clases (Unidades 1–3, Running Lean, etc.)
```

Convención: `materias/<materia>/{consigna, entrega-N, material}`. Todo lo compartido entre materias va en `proyecto/`, **nunca se duplica** dentro de una materia: se enlaza.

## Estado de las entregas

| Materia | Entrega 1 | Entrega 2 |
|---|---|---|
| **PPIV – Proyecto integrador** | ✅ Hecha (Etapa 1: empresa Talento Tech, misión/visión, roles, relevamiento) | ✅ **Etapa 2 entregada**: `Etapa 2 - Proyecto Integrador.pdf` (52 págs., exportado de Google Docs; **es la versión oficial**). `etapa-2-documento.md` + `build.py` son el borrador previo y **quedaron desactualizados** respecto del PDF entregado (ver `proyecto/decisiones.md`). Links reales en la Tabla 13 del PDF (Drive, Lucidchart, Trello, GitHub, Canva). |
| **Gestión de Proyectos** | ✅ Hecha y **corregida por la cátedra: 84/100** (ver `entrega-1/corrección.txt`). A mejorar en la Parte 2: origen de los requerimientos (Negocio / Sistemas) y justificar Scrumban por flujo, iteración y control, **no** por "Scrum es para equipos grandes full-time". | 🟡 **Parte 2 armada (borrador, 8 págs.)**: `materias/gestion-de-proyectos/entrega-2/GDP_Comisión E_Equipo 08_TPI - Parte 2.pdf`. Incluye los 5 ítems (6 a 10), Gantt, CPM (fin en 16 semanas, ruta crítica A-D-F-G-J/K), PERT (13,25 sem esperadas; 36 % de cumplir la semana 13, 86 % la 14), 12 riesgos, licencia MIT, presupuesto USD 22.440 y punto de equilibrio, y el Anexo con el origen Negocio/Sistema de los requerimientos (corrección de la Parte 1). **Pendiente de revisión del equipo:** supuestos económicos (costos fijos USD 4.200/año, precios de los escenarios), fecha de la reunión de devolución y enlace a actas. |
| **Emprendedorismo** | ✅ Hecha (1° TP: perfil emprendedor, desarrollo profesional, oportunidad, FODA) | ❓ Consigna de la 2ª entrega **no está en el repo** (el material cubre Unidades 1–3). Agregarla en `materias/emprendedorismo/consigna/`. |

## Etapa 3 (MVP): especificaciones, no código

La consigna de la Etapa 3 (`materias/ppiv-proyecto-integrador/consigna/Etapa 3 - Desarrollo completo.pdf`) pide una aplicación funcional con base de datos y CRUD completo (incluido eliminar con confirmación), Manual Técnico, Manual de Usuario, 2-3 pruebas unitarias y 1-2 de integración documentadas, y un PDF con instrucciones de instalación. Entregables: repositorio, .zip, PDF, scripts de base y enlace desplegado. La aplicación no se desarrolla en este repositorio. `materias/ppiv-proyecto-integrador/entrega-3/` contiene el paquete de especificaciones, incluido el mapeo a la consigna en `10-entregables-etapa-3.md` (visión, requerimientos con criterios de aceptación, ADR técnicos, arquitectura, API, pantallas del Figma con nodos, pruebas, backlog por fases, datos reales y preguntas abiertas) para pasárselo a un agente en otro repositorio. Empezar por su `README.md` y `AGENTS.md`. Hosting, Instagram y roles están marcados como "a validar".

## Etapa 3: aplicación construida (repositorio aparte)

La aplicación se desarrolló en un repositorio separado, **local y sin remoto todavía**: `../ifts2-plataforma` (junto a este repositorio) (rama `main`). Estado al 30/10/2026:
- **Hecho y verificado:** sitio público (Inicio, Institucional con contacto, La carrera, Estudiantes, Ingreso, Inscripciones, Novedades) y panel (login, Resumen, Publicaciones y moderación de Instagram, Avisos, Mensajes, Horarios y llamados, Archivo, Configuración con usuarios, contenido, enlaces e integraciones). Instagram y correo se configuran desde el panel; colores y fuentes por variables CSS; comentarios y README pensados para otro grupo de estudiantes.
- **Pruebas:** 43 compartidas + 352 de API (Vitest/Supertest), 190 de Cypress, 33 verificaciones de flujos, carga con 400 usuarios virtuales (cumple en uso real; un proceso de Node satura a ~300-360 pedidos/s) y Lighthouse móvil ≥ 97 de rendimiento y ≥ 98 de accesibilidad.
- **Entregables de la cátedra:** `docs/entrega/IFTS2-Etapa-3-Documentacion.pdf` (85 págs.: Manual Técnico, Manual de Usuario, evidencias y CRUD) y `dist-entrega/ifts2-plataforma-<fecha>.zip` (`pnpm docs:pdf`, `pnpm package`). Instalación verificada en un directorio limpio.
- **Pendiente:** enlace a repositorio remoto y a la aplicación desplegada (hosting gratuito a definir por DevOps y validar para 300-400 concurrentes); prueba real con Instagram/Meta, SMTP y S3 (nunca probados con credenciales reales); datos del cliente (ubicación de materias por año, nombres distintos entre documentos, fechas y requisitos de ingreso); correcciones de diseño que pueda dar el cliente.

## Pendientes que surgen de la orientación del aula (PPIV)

- **Historias de usuario:** hechas en `materias/ppiv-proyecto-integrador/entrega-3/historias-de-usuario.md` (12, priorizadas). La Etapa 2 ya entregada no se modifica.
- **Entrega de avance** (≥ 2 módulos, video, portfolio): **no aplica**, decisión del equipo; se va directo a la Etapa 3.
- **Registro de horas reales por integrante:** alimenta el presupuesto final de Gestión de Proyectos (la Parte 2 estima 680 h).
- **ITIL 4** (materia: PPIV): borrador en `materias/ppiv-proyecto-integrador/entrega-3/itil-4-aplicado.md`; faltan las secciones `[completar]`, los tiempos de servicio con el cliente y confirmar fecha y formato con los docentes.
- **Coloquio final:** sin definir todavía.

## Hitos del proyecto con el cliente (fijados por la cátedra)

| Semana | Hito | Estado |
|---|---|---|
| 2 | Reunión 1: relevamiento (04/09/2026) | ✅ |
| 6 | Reunión 2: DEMO de diseño/prototipos y alcance definitivo | ⏳ |
| 13 | Reunión 3: versión funcional | ⏳ |

## Resumen del proyecto (detalle en `proyecto/context.md`)

- **Cliente:** IFTS N°2 (GCABA). Ancla de identidad: *"No formamos chefs. Formamos empresarios gastronómicos."*
- **Problema:** sitio en Google Sites abandonado, con contenido de 2021–2026 mezclado, sin panel, sin contacto, sin integración con redes.
- **Solución propuesta:** sitio público + panel de administración propio; contenido *estanco* vs *dinámico* (archivar, nunca borrar); selección editorial de posts de Instagram/Facebook (hashtag + rango de fechas); accesos a SIU Guaraní, Aulas Virtuales y Mi Argentina; formulario de contacto.
- **Restricciones:** presupuesto casi nulo (hosting/dominio gratuitos; .edu.ar a evaluar), administradores no técnicos (Matías Peláez, María del Carmen Canobi), 3 equipos compitiendo por el mismo cliente, desarrollo propio (sin CMS de terceros).
- **Marca del cliente (IFTS N°2):** el cliente rechazó la paleta verde; el **Figma vigente (18/10/2026)** usa tokens tierra: primary `#8D775F`, base `#F6F6F3`, accent `#6F5142`, accent-2 `#E0DFD5`, accent-3 `#291711`, font `#6E7271` + semánticos (ver `proyecto/context.md` §5), Inter y fotos reales. El PDF de Etapa 2 entregado describe la paleta verde anterior. El azul `#24507F` + Fraunces es de **Talento Tech**, no del cliente.

## Para agentes de IA

1. Antes de cualquier tarea, leer `proyecto/context.md`. Para trabajo de materia, leer además la `consigna/` correspondiente y la entrega 1 de esa materia (mantener coherencia de nombres, roles, objetivos y datos).
2. No inventar datos del cliente ni del equipo: salen de `proyecto/` y de las entregas hechas. Si falta algo, marcarlo como `[completar]`.
3. Entregas nuevas van en `materias/<materia>/entrega-N/`; si hay información nueva del cliente, actualizar `proyecto/context.md` (no la materia).
4. Respetar el formato exigido por cada consigna (APA en PPIV; máx. 10 págs. y nombre de archivo en GdP; conciso y fundamentado en Emprendedorismo).
5. Para gestión (OKR/KPI/SMART/riesgos) usar `agents/agente-gestion-proyecto.md`. Para comunicación escrita formal con el cliente, `referencias/Manual de Estilo del GCABA...pdf`.
6. Español rioplatense, tono profesional y directo.
7. Las consignas de `consigna/` tienen un `.txt` al lado del PDF (extraído con `pdftotext -layout`): leer ese. Para otros PDF/DOCX, extraer el texto en vez de asumir su contenido.

## Pendientes de orden

- Confirmar cuál de los dos PDF de GdP Parte 1 es el entregado (`GDP_Comisión E_Equipo 08_TPI - Parte 1.pdf` vs `GDP_ComisionX_TalentoTech_TPI-Parte1.pdf`) y descartar el otro.

- El PDF de Etapa 2 entregado conserva restos de edición para corregir si se reentrega: una nota editorial en 6.1 ("la oración siguiente es muy larga…"), la nota de la Tabla 2 que aún dice "alternativa WordPress quedó como plan B" (contradice D-001), fechas de minuta incoherentes (24/09 en 4.4, 26/09 en Referencias; la minuta del repo es del 30/06) y la frase del Anexo A sobre campos entre corchetes.
- La Etapa 2 **no se reentrega**; los restos de edición de arriba solo importan si se reutiliza ese texto en la Etapa 3.
