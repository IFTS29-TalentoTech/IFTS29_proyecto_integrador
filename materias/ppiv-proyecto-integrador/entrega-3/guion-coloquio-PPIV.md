# Guion del coloquio — Práctica Profesionalizante IV

**Equipo Talento Tech** — Plataforma web del IFTS N°2. Fuente: `consigna/Lineamientos Coloquio.pdf`. Los datos técnicos salen de la aplicación real (`../ifts2-plataforma`, rama `main`) y de su `docs/entrega/Evidencias-de-pruebas.md`.

## Qué pide la consigna

- Video grupal asincrónico. **Máximo 5 minutos por integrante** (5 integrantes = hasta 25 min). **Todos presentes, con cámara encendida**; audio y video de buena calidad. Se puede grabar con Meet, Zoom u OBS (confirmar con el docente si Teams también vale; el resto de la consigna no lo menciona).
- **Contenido, en este orden:**
  1. **Interfaz y funcionamiento:** la aplicación en ejecución, los principales flujos y pantallas, el **CRUD completo y las validaciones** (campos vacíos, confirmaciones, mensajes).
  2. **Lógica, código y base de datos:** arquitectura y módulos principales; base de datos (estructura, tablas, relaciones); **una o dos pruebas unitarias y una de integración, mostrando su ejecución y resultados**; validaciones, manejo de errores y conexiones.
  3. **Cierre:** reflexión sobre el trabajo del grupo, las mejoras y el aprendizaje.
- **Se evalúa:** claridad y solidez técnica, demostración del sistema completo, **coherencia entre interfaz, código y base de datos**, participación equilibrada y organización.

Esto es una **demostración técnica**, no una presentación a un cliente. Las slides son de apoyo: la mayor parte del tiempo se ve la aplicación, el código y la terminal.

## Reparto y tiempos

| # | Quién | Bloque | Slides | Tiempo | Qué se ve en pantalla |
|---|---|---|---|---|---|
| 1 | Martín (PO) | Apertura, problema, roles y sitio público | 1–3 | 3:30 | Slides y sitio público en `localhost:3000` |
| 2 | Gastón (Frontend) | Panel: flujos, CRUD y validaciones | 4 | 4:30 | Panel en vivo |
| 3 | Nicolás (Backend) | Arquitectura, **stack y por qué lo elegimos**, validaciones y errores | 5–7 | 4:45 | Slides y código en el editor |
| 4 | Santiago (DevOps) | Base de datos, migraciones e instalación | 8 | 4:00 | DER, `schema.prisma`, terminal y la base |
| 5 | Adrián (QA) | Pruebas unitarias e integración, en ejecución | 9–11 | 4:30 | Terminal con Vitest y Supertest |
| 6 | Todos | Cierre y reflexión | 12 | 1:30 | Slide de cierre |
| | | **Total** | 12 | **22:45** | |

Quedan más de 2 minutos de margen sobre el máximo de 25. Si alguien se pasa de 5 minutos, recortar en la edición la parte menos importante de su demo.

**Pasaje de palabra:** cada bloque cierra con una frase que presenta al siguiente ("Gastón, te cedo la palabra para ver cómo trabaja el personal del instituto"). Mostrar el nombre y el rol de cada uno en pantalla al comenzar su parte.

---

## 1. Martín — Apertura, problema, roles y sitio público (3:30)

### Slide 1 · Portada (0:30)
> **Slide:** título, nombres, roles y qué explica cada uno.

"Buenas, somos el equipo Talento Tech. Les mostramos la plataforma web que construimos para el IFTS N°2, la Tecnicatura en Emprendimientos Gastronómicos. Vamos a ver cómo se usa, cómo está hecha por dentro, la base de datos y las pruebas. Yo soy Martín, Product Owner; me acompañan Gastón en el frontend, Nicolás en el backend, Santiago en infraestructura y base de datos, y Adrián en calidad."

### Slide 2 · Problema y solución (0:45)
> **Slide:** a la izquierda el problema (Google Sites desactualizado, sin panel, contenido de 2021 a 2026 mezclado, sin contacto); a la derecha la solución (sitio público + panel + base de datos propia).

"El instituto tenía un sitio en Google Sites, abandonado, con contenido de varios años mezclado y sin forma de actualizarlo sin ayuda. Construimos un sitio institucional y un panel de gestión pensado para personal que no es técnico. Cuatro ideas gobiernan el sistema: nada se borra solo, lo vencido se oculta y se archiva; la vigencia se calcula al consultar; nada de las redes llega al sitio sin aprobación humana; y el sitio sigue funcionando aunque fallen Instagram, el correo o el almacenamiento."

### Slide 3 · Quién usa qué (0:30)
> **Slide:** cinco tarjetas: Público · Superadmin (crea roles y permisos) · Administración · Bedelía (avisos, horarios, llamados, archivo) · Comunicación (publicaciones y moderación de Instagram).

"Hay cinco tipos de usuario. El público no inicia sesión. Dentro del panel, el superadministrador crea roles y elige qué puede hacer cada uno; administración gestiona contenido y usuarios, bedelía carga avisos, horarios y archivo, y comunicación modera las publicaciones de Instagram. Los roles se guardan en la base, así que se pueden crear nuevos sin tocar código."

### Demo · Sitio público (2:00) — *compartir pantalla*
Recorrido en `http://localhost:3000`:
1. **Inicio**: identidad visual con la paleta que el cliente aprobó.
2. **Estudiantes**: avisos vigentes, horarios y llamados a examen **solo del ciclo en curso**. Decir que lo vencido no se ve acá, pero tampoco se borró.
3. **Novedades**: publicaciones aprobadas por el instituto.
4. **Institucional → contacto**: mostrar el formulario y que exige el **consentimiento** (si se intenta enviar vacío, aparece el mensaje).
5. Achicar la ventana (390 px) para mostrar que se adapta al celular.

"Este sitio lee todo de la base de datos. Cuando Bedelía cargue un aviso, lo vamos a ver aparecer acá. Gastón, te cedo la palabra."

---

## 2. Gastón — El panel: flujos, CRUD y validaciones (4:30)

> **Slide 4** acompaña los primeros 20 segundos (tabla CRUD y las cuatro reglas); el resto es en vivo en `localhost:3000/panel`.

"Soy Gastón, del frontend. Ahora vemos cómo trabaja el personal del instituto. Lo que van a ver son las cuatro operaciones, crear, leer, actualizar y eliminar, con las reglas que las protegen."

### Demo (4:00)
| Paso | Qué hacer | Qué decir |
|---|---|---|
| 1 | **Login** como `bedelia@ifts2.local`. Probar primero una clave incorrecta. | "Mensaje claro y límite de intentos para evitar fuerza bruta." |
| 2 | **Resumen** (pantalla principal del panel) y menú lateral. | "Lo que cada rol ve depende de sus permisos." |
| 3 | **Avisos → Nuevo aviso. Create con campos vacíos**: dejar el título vacío y poner una fecha de fin anterior al inicio. | "Los mensajes aparecen bajo cada campo: «El título es obligatorio.» y «La fecha de fin debe ser posterior a la fecha de inicio.». No se guarda nada." |
| 4 | **Completar y Publicar aviso** → diálogo **Sí, publicar**. Abrir el sitio público en otra pestaña (**Estudiantes**) y mostrar que el aviso ya está. | "**Create y Read**: el aviso se guardó en la base y se ve en el sitio." |
| 5 | **Editar** el aviso → **Guardar cambios** → confirmar. | "**Update**." |
| 6 | Mostrar que un aviso **vigente no ofrece «Eliminar»**: **Pausar** primero. | "La regla: solo se elimina lo no vigente." |
| 7 | **Eliminar** → diálogo «¿Eliminar…?». Primero **Cancelar** (no cambia nada); después **Sí, eliminar**. | "**Delete**, con confirmación. Es el mismo diálogo para todas las bajas." |
| 8 | **Administrar usuarios y roles** (como ADMIN): crear un usuario con un **correo que ya existe**. Mostrar «Ya existe un usuario con ese correo». Después **Desactivar** otro usuario. | "No se repiten correos. Los usuarios no se borran, se desactivan, para conservar la auditoría." |
| 9 | (Si hay tiempo) **Publicaciones → Instagram**: moderar una publicación detectada. | "Modo demostración: Instagram real no está conectado todavía." |

Cierre del bloque: "Todo lo que hicimos quedó guardado. Nicolás te cuenta qué pasa por debajo cuando apreto un botón."

---

## 3. Nicolás — Arquitectura, validaciones y errores (4:00)

### Slide 5 · Arquitectura (1:15)
> **Slide:** diagrama de capas: Navegador → Web (Next.js 15, sitio público y panel) → API (Express 5) → PostgreSQL 17 con Prisma; a un costado `packages/shared` y los servicios externos.

"Soy Nicolás, del backend. Es un monorepo con tres partes. La web es Next.js: el sitio público se renderiza en el servidor con caché de 60 segundos y el panel exige sesión. La API es Express con TypeScript, y la base es PostgreSQL con Prisma. Entre los dos hay un paquete compartido, `packages/shared`, con los esquemas de validación, los permisos por rol y las reglas de vigencia: una sola fuente para el navegador y la API.

La API se organiza en módulos, uno por carpeta: avisos, publicaciones, documentos, horarios, llamados, usuarios, auditoría, integraciones y otros. Cada módulo exporta su ruta y se monta solo. Los servicios externos, como almacenamiento, correo e Instagram, están detrás de una interfaz: cambiar de proveedor es cambiar configuración, no código."

*Mostrar en el editor:* `apps/api/src/modules/notices/index.ts` (rutas) y `apps/api/src/routes.ts` (autodescubrimiento de módulos).

### Slide 6 · Stack y por qué lo elegimos (1:30)
> **Slide:** tabla con pieza, tecnología y motivo.

"¿Por qué estas tecnologías? Primero, **TypeScript en todo**: el mismo lenguaje en la web, la API y el paquete compartido, y muchos errores aparecen al compilar, no cuando el usuario los encuentra. Segundo, **Next.js** para el sitio: renderiza en el servidor y guarda en caché, y eso lo hace rápido en celulares, que es donde lo van a abrir los estudiantes; el panel usa las mismas rutas protegidas. Con **Radix y Tailwind** logramos teclado y foco accesibles, y los colores quedan en un solo lugar: cuando el instituto rechazó la paleta verde, cambiamos un archivo. La API es **Express**, simple, separada y fácil de probar. Y la base es **PostgreSQL con Prisma**: nuestros datos tienen relaciones y reglas, como que un ciclo tenga horarios y llamados, y una base relacional las hace cumplir; Prisma da migraciones versionadas y tipos generados, y todo es gratuito, que era una restricción del cliente. Elegimos desarrollo a medida y descartamos un CMS: la cátedra lo pidió y nos da control de las reglas, como el archivo de lo vencido. Lo que dejamos afuera: no hay permisos por registro ni jerarquías complejas, porque un instituto con pocos usuarios tiene que poder administrarlos."

*Mostrar en el editor:* `package.json` raíz (scripts) y `pnpm-workspace.yaml`.

### Slide 7 · Una petición, validaciones y errores (2:00)
> **Slide:** el recorrido de una petición (origen → sesión → permiso → validación → módulo → base → auditoría) y un ejemplo de error.

"Cuando se crea un aviso, la petición pasa por capas. Primero la seguridad: verificación de origen, sesión guardada en la base y límite de frecuencia. Después los permisos: la matriz del paquete compartido dice si ese rol puede crear avisos. Después la validación con zod: el mismo esquema que usa el formulario, así que el mensaje es el mismo. Recién ahí el módulo escribe en la base y deja un registro de auditoría con quién y cuándo.

Los errores salen todos con el mismo formato, Problem Details, con un mensaje en español que la pantalla muestra tal cual. Por ejemplo, si se intenta eliminar un aviso vigente, la API responde 409: «No se puede eliminar un aviso vigente. Pausalo o esperá a que venza.» Las contraseñas se guardan con hash argon2 y los secretos del cliente, como el token de Instagram, cifrados con AES-256. Santiago te muestra dónde se guarda todo esto."

*Mostrar en el editor:* `packages/shared/src/schemas.ts` (esquema `noticeCreateInput`), `apps/api/src/middleware/error-handler.ts`.

---

## 4. Santiago — Base de datos, migraciones e instalación (4:00)

### Slide 8 · Base de datos (1:30)
> **Slide:** las 19 tablas en 4 áreas (Acceso y auditoría · Académico · Publicaciones y redes · Sitio) y las relaciones principales.

"Soy Santiago, de infraestructura. La base es PostgreSQL 17, con 19 tablas, que el DER divide en cuatro áreas. Acceso y auditoría: `User`, `Session`, `AuditLog` y las de roles, `Role` y `RolePermission`; un usuario tiene un rol, cada rol tiene sus permisos, y cada usuario tiene muchas sesiones y registros de auditoría. Académico: `AcademicTerm`, o ciclo lectivo, `Schedule`, `ExamCall`, `Notice` y `Document`; un ciclo tiene muchos horarios y muchos llamados, y un documento puede estar adjunto a un aviso, un horario o un llamado. Publicaciones y redes: `Publication`, `SocialPost`, `Category` y las integraciones. Y el sitio: ajustes, secciones de contenido, enlaces y mensajes de contacto."

### Demo (2:30) — *compartir pantalla*
1. Abrir `prisma/schema.prisma` y mostrar el modelo `Notice` (campos, enum de estado, relación con `User` y `Category`) y los índices únicos.
2. Abrir el DER (`docs/entrega/diagramas/der-academico.png`).
3. **Coherencia interfaz-base:** abrir Prisma Studio (`pnpm exec prisma studio`) o `psql` y mostrar la fila del aviso que Gastón creó (título, estado, fechas, autor) y su registro en `AuditLog` (`notice.create`).
4. Terminal: `pnpm db:up` (Docker con PostgreSQL), `pnpm db:migrate` (migraciones versionadas) y `pnpm db:seed` (datos de demostración).
5. Mencionar: dos semillas (`demo` y `prod`); el CI en GitHub Actions; el `.zip` generado con `pnpm package` sin secretos; y que la instalación se probó en un directorio limpio siguiendo solo el PDF.

"¿Por qué esta base y estas herramientas? Elegimos PostgreSQL porque los datos están relacionados y tienen reglas de integridad; Prisma para que el esquema quede versionado en migraciones y el código tenga tipos generados; y Docker para que la base sea igual en todas las máquinas, sin instalar nada. La base se crea desde cero con tres comandos y cualquier docente puede levantarla con la documentación. Adrián, ahora sí: ¿cómo sabemos que todo esto funciona?"

---

## 5. Adrián — Pruebas unitarias y de integración (4:30)

### Slide 9 · Pruebas unitarias (1:30)
> **Slide:** UT-1 (vigencia) y UT-2 (validación zod) con el código y el resultado.

"Soy Adrián, de calidad. Usamos tres herramientas, cada una para su nivel: **Vitest** para las pruebas unitarias, **Supertest** para probar la API como lo haría un cliente, contra una base PostgreSQL real, y **Cypress** para recorrer la interfaz como lo haría una persona, con una revisión de accesibilidad. Probar contra la base real, y no contra un doble, nos da confianza en que lo que pasa en las pruebas pasa en producción. Una prueba unitaria verifica una función de forma aislada. Elegimos las que protegen las reglas centrales del producto. La primera, `isNoticeVisible`: un aviso es visible solo si está activo y dentro de sus fechas; probamos vigente, vencido, pausado, futuro y el borde del último día, que incluye hasta las 23:59 de Buenos Aires. La segunda, el esquema de validación: rechaza un título vacío y una fecha de fin anterior al inicio, con mensajes claros."

### Demo en terminal (1:30)
```bash
pnpm --filter @ifts2/shared exec vitest run test/visibility.test.ts --reporter=verbose
pnpm --filter @ifts2/shared exec vitest run test/schemas-permissions.test.ts --reporter=verbose
```
Resultados esperados: UT-1 **5 de 5**; UT-2 **11 de 11**. Mostrar el archivo de prueba con el código al lado de la salida.

### Slide 10 · Prueba de integración (1:15)
> **Slide:** los 5 pasos de INT-1.

"La prueba de integración recorre varias capas juntas: crea un aviso por la API, comprueba que la fila existe en PostgreSQL con el usuario autor, que quedó registrada la auditoría y que el aviso aparece en el sitio público."

```bash
pnpm --filter @ifts2/api exec vitest run test/api/integracion-catedra.test.ts --reporter=verbose
```
Resultado esperado: **2 pruebas aprobadas** (INT-1 crear y ver en el sitio; INT-2 eliminar: 204 si está pausado, **409 si está vigente**). Mencionar que usa PostgreSQL real, sin dobles de la base, y que se reemplazan solo los servicios externos.

### Slide 11 · Resumen y límites (0:15)
> **Slide:** 395 pruebas unitarias y de API · 190 de Cypress · 33 flujos · Lighthouse móvil 97–99 de rendimiento y 98–100 de accesibilidad.

"En total son 395 pruebas unitarias y de API y 190 de interfaz con Cypress, todas aprobadas. Y decimos con claridad lo que no probamos: Instagram, SMTP y almacenamiento reales, y el despliegue."

---

## 6. Cierre y reflexión (1:30) — todos · Slide 12

> **Slide:** tres columnas: Lo que logramos · Lo que aprendimos · Lo que falta. Cada uno dice **una frase** (15 a 20 segundos).

Borrador, para que cada uno lo diga con sus palabras:
- **Martín:** "Pasamos de un pedido difuso a una plataforma que el instituto puede mantener solo. Validar el diseño con el cliente nos ahorró rehacer trabajo."
- **Gastón:** "Los colores y fuentes viven en un solo lugar. Cuando el cliente rechazó la paleta verde, el cambio fue de tokens, no de pantallas."
- **Nicolás:** "Compartir las reglas entre la web y la API evitó que dijeran cosas distintas."
- **Santiago:** "Con migraciones y semillas, cualquiera levanta el proyecto desde cero."
- **Adrián:** "Probar contra una base real encontró errores que un doble no hubiera mostrado."

"Para cerrar: queda pendiente el despliegue en un hosting y las pruebas con Instagram y el correo reales. Gracias."

---

## Antes de grabar

0. **Rol Superadministrador (se implementa hoy, ver ADR-18 y RF11 en las specs).** El guion y las slides ya lo mencionan (slide 3, base de 19 tablas con `Role` y `RolePermission`). Cuando esté hecho, **actualizar los números** que cambian: cantidad de tablas, de pruebas (hoy 395 unitarias y de API, 190 de Cypress, 33 flujos) y los usuarios de demostración (agregar uno SUPERADMIN). Si no llega a estar terminado y funcionando, **sacarlo del video** en lugar de mostrarlo a medias, y cambiar la slide 3 a "cuatro tipos de usuario".

1. **Entorno de la demo** (lo prepara quien comparte pantalla): `pnpm db:up`, `pnpm db:migrate`, `pnpm db:seed`, `pnpm dev`. Comprobar `http://localhost:4000/health` y `http://localhost:3000`. **No correr `pnpm db:reset` en medio de la grabación** (borra y resiembra).
2. **Un solo ensayo completo con cronómetro y con la base en el estado inicial.** La demo crea y elimina datos; conviene repetirla desde la semilla.
3. **Dos usuarios abiertos:** Bedelía (`bedelia@ifts2.local`, `Demo-2026-ifts2`) y Admin (`admin@ifts2.local`). Dos ventanas del navegador (panel y sitio público).
4. **Código abierto de antemano** en el editor, con letra grande: `notices/index.ts`, `routes.ts`, `schemas.ts`, `error-handler.ts`, `schema.prisma` y los dos archivos de prueba.
5. **Cada uno debe poder explicar el código de su parte.** Los evaluadores miran la solidez técnica: conviene leer los archivos que se muestran y ensayar las preguntas probables ("¿por qué zod compartido?", "¿qué pasa si falla Instagram?", "¿por qué no se borran los usuarios?").
6. **Ser honestos con los límites:** la aplicación corre en local (todavía no hay enlace desplegado ni repositorio remoto), y Instagram, SMTP y S3 no se probaron con credenciales reales. Decirlo una vez, en el cierre.
7. **Cámara encendida todo el video**, también durante las demos (usar la vista de Teams con la cámara en un costado, o mostrar la cámara en la intro de cada bloque). Mismo nivel de audio entre los cinco.
8. **Pendiente de decidir:** quién comparte pantalla en cada bloque (lo más simple es que cada uno comparta la suya con la aplicación levantada en su máquina, o que todos usen una sola máquina y pasen el control).
