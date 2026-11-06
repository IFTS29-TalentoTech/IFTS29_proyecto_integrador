# Diagramas listos para pegar en Lucidchart

Cada archivo `.mmd` es un diagrama Mermaid para una página propia del documento de Lucidchart del equipo. Los 20 se validaron con Mermaid 12 (el mismo motor que usa la app para sus PDF).

## Cómo pegar un diagrama

1. En el documento de Lucid, creá una página nueva y ponele el título de la tabla de abajo.
2. Menú de formas: **Importar > Diagrama como código** (o el botón `+` > *Diagrama como código*). Elegí **Mermaid**.
3. Pegá el contenido del `.mmd` y aceptá.
4. Si algún estilo no se respeta (colores, líneas punteadas), se corrige a mano con la paleta de abajo. La estructura y los textos siempre llegan.

No se tocó nada del documento existente: las páginas nuevas se agregan **después** de las que ya tenga.

## Qué pegar en cada página

### Producto IFTS N°2 (paleta tierra del Figma vigente, 18/10/2026)

| Página | Título sugerido | Archivo | Origen en el repo | Qué cambió |
|---|---|---|---|---|
| 1 | Mapa del sitio público | `01-sitio-publico-mapa.mmd` | `entrega-2/diagramas/09a` | Páginas reales de la app (Inscripciones separada de Ingreso, contacto dentro de Institucional); se quitaron Galería y Plantel docente, que no están construidos |
| 2 | Mapa del panel | `02-panel-mapa.mmd` | `09b` | Áreas reales del panel y los tres roles (ADMIN, BEDELIA, EDITOR) |
| 3 | Arquitectura: capas | `03-arquitectura-capas.mmd` | reemplaza `07-componentes` | Next.js 15 + Express 5 + Prisma. La Etapa 2 decía JWT; la app usa sesión por cookie con el hash del token en base |
| 4 | Servicios configurables | `04-servicios-configurables.mmd` | `docs/ARQUITECTURA.md` de la app | Nuevo: almacenamiento, correo e Instagram intercambiables y configurables desde el panel |
| 5 | Despliegue | `05-despliegue.mmd` | `08-despliegue` | Hosting y despliegue marcados como **a definir** (la CI solo verifica, no despliega) |
| 6 | Modelo de datos 1/3: usuarios, contenidos y avisos | `06-er-contenidos-usuarios.mmd` | reemplaza `06a-er-contenidos` | Sale de `prisma/schema.prisma` |
| 7 | Modelo de datos 2/3: ciclos, horarios y archivo | `07-er-academico-documentos.mmd` | reemplaza `06b-er-academico` | Sale del schema; el plan de estudios, docentes y materias como tablas ya no existen |
| 8 | Modelo de datos 3/3: configuración y contacto | `08-er-configuracion-contacto.mmd` | nuevo | Entidades sueltas del schema (sin relaciones) |
| 9 | Clases del dominio | `09-clases-dominio.mmd` | reemplaza `02a` y `02b` | Mismo modelo que el schema, con las operaciones reales |
| 10 | Secuencia: vinculación con Instagram | `10-secuencia-vinculacion-redes.mmd` | `03a` | Endpoints y estados reales (`/social/sync`, `/posts/:id/approve`, DETECTED/LINKED) |
| 11 | Secuencia: formulario de contacto | `11-secuencia-contacto.mmd` | `03b` | Campo señuelo, límite de frecuencia, consentimiento y `mailSent` |
| 12 | Actividad: carga y publicación | `12-actividad-carga-publicacion.mmd` | `04a` | Estados DRAFT / SCHEDULED / PUBLISHED |
| 13 | Actividad: vigencia | `13-actividad-vigencia.mmd` | `04b` | La vigencia se calcula al consultar; lo vencido se conserva |
| 14 | Estados de Publication | `14-estados-publicacion.mmd` | `05a` | ARCHIVADA ya no existe: es PAUSED. Archivar documentos es otra cosa (Document ARCHIVED) |
| 15 | Estados de SocialPost | `15-estados-publicacion-social.mmd` | `05b` | Nombres en inglés y la vuelta a DETECTED al eliminar la publicación |

### Talento Tech (azul `#24507F`, sin paleta del cliente)

| Página | Título sugerido | Archivo | Origen en el repo |
|---|---|---|---|
| 16 | Decisión D-001: desarrollo a medida | `16-talento-tech-decision-001.mmd` | `proyecto/diagramas/decision-001-desarrollo-a-medida.mmd` (recolorado de verde a azul) |
| 17 | ITIL 4: cadena de valor | `17-talento-tech-itil-cadena-de-valor.mmd` | bloque Mermaid de `entrega-3/itil-4-aplicado.md` |
| 18 | Cronograma (Gantt) | `18-talento-tech-gantt.mmd` | `gestion-de-proyectos/entrega-2/diagramas/gantt.mmd` (sin cambios) |
| 19 | Red CPM 1/2 (actividades A a I) | `19-talento-tech-red-cpm-1-de-2.mmd` | `red-cpm.mmd`, primera mitad |
| 20 | Red CPM 2/2 (actividades G a P) | `20-talento-tech-red-cpm-2-de-2.mmd` | `red-cpm.mmd`, segunda mitad |

## Paleta del Figma vigente

| Uso | Color |
|---|---|
| Principal | `#8D775F` |
| Acento | `#6F5142` |
| Base | `#F6F6F3` |
| Acento 2 (relleno suave) | `#E0DFD5` |
| Acento 3 (texto y raíz) | `#291711` |
| Texto secundario | `#6E7271` |
| Éxito | `#556B3F` sobre `#E8EDE4` |
| Advertencia | `#B77A3A` sobre `#F7E9D6` |
| Error o pendiente | `#7A3A32` sobre `#F3DCDC` |

## Notas

- **Gantt (página 18):** la importación de Mermaid de Lucid puede no aceptar `gantt`. Si lo rechaza, usá el PNG o SVG que ya está en `materias/gestion-de-proyectos/entrega-2/diagramas/` como imagen en esa página.
- **Estados de Publication (página 14):** la vigencia (`visibleFrom` y `visibleUntil`) no es un estado: se calcula al consultar. Una publicación SCHEDULED se muestra sola cuando llega su fecha de inicio. Se puede eliminar a mano, con confirmación, si está en DRAFT, PAUSED o ya venció.
- **Autores:** `authorId` en Publication y Notice es un texto simple en el schema, sin clave foránea a User; por eso no hay línea entre ellos en el modelo de datos.
- **Diagramas de la Etapa 2 que no se llevan:** casos de uso (01) no tiene archivo `.mmd`, solo existe en Draw.io. Los `.mmd` originales de `entrega-2/diagramas/` no se modificaron: la Etapa 2 ya se entregó y no se reentrega.
- **Si cambia el schema** (`../ifts2-plataforma/prisma/schema.prisma`), hay que revisar las páginas 6, 7, 8 y 9.
