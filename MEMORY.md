# Long-Term Memory

## Operación y comportamiento

- [Modo conciso default](memory/modo-conciso-default.md) — Sergio aprobó 4 optimizaciones de tokens 2026-05-28: respuestas terse en lookups/altas rutinarias, mantener detalle solo en análisis profundos
- [Economía tokens Soporte](memory/economia-tokens-soporte.md) — Todos los agentes Soporte (grupos+directo) responden mínimo de tokens; directiva en 12 workspaces AGENTS.md (no main). Sergio 2026-10-01
- [Herramientas locales token-saver](memory/local-tools-token-saver.md) — `jq` + `exiftool` instalados 2026-06-03; usarlos antes de meter JSON/metadata crudo al contexto
- [Normalización nombres estación](memory/normalizacion-nombres-estacion.md) — Todos los grupos: relacionar alias hablados (t2, terminal 2, cancun…) al código canónico Mongo (MEXT2, CUN…) antes de buscar/escribir
- [Mintaka workflow](memory/mintaka-workflow.md) — Sillero escanea pase de abordar del pax (NO pulsera al pax). Pulsera NFC es identificador del operador
- [Expediente: foto siempre](memory/expediente-colaborador-foto.md) — Todo expediente de colaborador incluye la foto de perfil adjunta (GridFS `fotoPerfil` ObjectId → `fs.files`)
- [Sergio objetivo dirección](memory/sergio-objetivo-direccion.md) — Meta de carrera: dirección/subdirección; todo KRYX es evidencia ejecutiva de control operativo. Priorizar lo presentable a un director

## Workflows y pipelines

- [Limpiar posiciones guardia](memory/guardia-posiciones-limpiar.md) — `update_many activa:false` en `guardia_asignaciones`; libera coords+operadores de todas las posiciones; primera ejecución 2026-10-13 (55 docs)
- [Reporte carga aerolínea-estación](memory/reporte-carga-aerolinea-estacion.md) — Metodología validada para defender carga laboral vs métrica "menos servicios" (caso DL/MEXT2 abril 2026)
- [Reporte cierre al director](memory/reporte-cierre-director.md) — Plantilla aprobada 2026-08-25: Resumen + Cuestionamientos + Pendientes; distingue abiertas vs resueltas; va al correo de Pepe
- [Reporte solo operación](memory/reporte-solo-operacion.md) — Reporte diario NO lleva config/plomería interna (JIDs, coordinadores, registros vacíos); scrub en script + REGLA DE ALCANCE en prompt del cron
- [Reportes de Operación histórico (correo→BD)](memory/reportes-operacion-ingest.md) — reporte_ingest.py recupera "Reporte de Operacion" del correo → colección `reportes_operacion` + `incidencias`; backfill Sep 2026 (29 reportes, 44 inc)
- [Tally Alta Coordinador](memory/tally-alta-coordinador.md) — Form self-service onboarding roster/allowlist. Link tally.so/r/6807JB; scripts en ~/.kryx; jalar altas con tally_fetch_submissions.py
- [Support Pressure sidecar](memory/support-pressure-sidecar.md) — Sidecar T2 proactivo (support_pressure.py): detecta mala operación en Mongo (A1 auto-chequeo, A2 nudge preventivo de cierre). Fase 1 (2026-10-01): presión al DM del REP dueño
- [Follow-up seguimiento a reps](memory/followup-seguimiento-reps.md) — Pipeline T3 matutino 9am (followup_digest/ask): pregunta a cada rep por lo reportado ayer cruzado vs BD; borrador a Sergio, Fase 1. 2026-10-01
- [Agente estacion-rep + Minuta Operativa Nacional](memory/agente-estacion-rep-minuta.md) — Agente read-only scopeado por estación (piloto Javier/GDL 2026-09-29); pipeline minuta nocturna 6 estaciones → correo director. LECCIÓN: nunca pipear `message send` por grep

## Gateway y plomería

- [Gateway crash-loop x Telegram](memory/gateway-crash-loop-telegram.md) — health-monitor reinicia gateway a 120s si canal no conecta; poller Telegram duplicado → bucle. Fix: disable + drenar 60s + arrancar UNO
- [Gateway launchd orphan fix](memory/gateway-launchd-orphan-fix.md) — EX_CONFIG loop = plist corrupto (sed en XML). Fix: restaurar plist + unload/load. Nunca sed en XML. Watchdog → NVM binary 2026.7.1
- [Gateway launchd loop EX_CONFIG 78 (dir logs root)](memory/gateway-launchd-root-log-dir.md) — ~/Library/Logs/openclaw root-owned → launchd no escribe StdOut → respawn loop 69k. Fix: logs del plist a ruta escribible. Causa distinta a [[gateway-launchd-orphan-fix]]
- [Agentes modo degradado → restart gateway](memory/agentes-degradado-exec-restart.md) — "Sistema de consulta fuera" con Mongo arriba = tool de shell no cargado. Fix: restart gateway con binario NVM 2026.7.1 (NUNCA el beta del PATH)
- [main→Sonnet + heartbeat 120m](memory/main-sonnet-heartbeat-120m.md) — Recorte cuota 2026-10-06: main a Sonnet (Opus on-demand), heartbeat 30m→120m; NO vaciar HEARTBEAT.md (rompe lectura de respuestas de reps)
- [Optimizaciones tokens Oct 2026](memory/token-optimizations-oct2026.md) — requireMention en coordinacion/nacional, sesiones wiped, compact_coordinacion OFF, minuta_remind 10→4/día, heartbeat 240→480m, Ollama+nomic-embed autostart vía launchd

## Presentaciones

- [Sistema presentaciones HTML animadas](memory/presentaciones-html-sistema.md) — Stack completo estilo Orión: Three.js + CSS puro, layouts, animaciones, contadores, tablero flap, SCENES array. Ref: orion-valor-servicio.onrender.com

## Referencia técnica (leer bajo demanda, NO en cada turno)

- [KRYX Systems Reference](memory/kryx-systems-reference.md) — Bitácora completa de infra: launchd jobs, Mongo `orion_estaciones` (colecciones/campos/creds), canal WhatsApp, crons, reporte incidencias. Consultar cuando se necesite detalle de scripts, rutas o config de sistemas.

## Identidad

Identidad KRYX asignada y aceptada 2026-05-08 por Sergio (sergio.guillen.pacheco@gmail.com). Persona fijada en `IDENTITY.md`/`SOUL.md` — mantener coherencia. Decisiones sin titubeo en acciones internas; luz verde explícita para externas.
