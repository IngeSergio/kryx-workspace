# Política de acceso a MongoDB de Sergio

_Establecida 2026-05-09 por solicitud explícita de Sergio: "déjala abierta pero protegida para evitar movimientos ajenos a lo que yo te solicite."_

## Cluster

- Host: `orion-mongodb-b899a789.mongo.ondigitalocean.com` (DigitalOcean managed)
- Usuario: `doadmin` (privilegios de admin — esto es exactamente por qué hay protocolo)
- URI guardada en: `~/.kryx/mongo_uri` (chmod 600)
- Cliente: `~/.kryx/venv/bin/python` con `pymongo`
- Audit log: `~/.kryx/mongo_audit.log` (append-only, chmod 600)

## Reglas binding

### 1. Iniciativa cero

NO me conecto a la BD por exploración propia, curiosidad, "vamos a ver qué hay", ni preparación anticipada. Cada conexión responde a una solicitud explícita de Sergio en la conversación activa. Si Sergio no me lo pidió en la sesión actual, no toco la BD.

### 2. Scope estricto

Si Sergio pide "trae al colaborador 2421" → eso ejecuto. NO añado de mi cuenta:
- Listar otras colecciones
- Hacer counts globales
- Explorar campos adicionales
- Probar queries relacionadas

Excepción: si genuinamente necesito un `find_one()` para descubrir el schema antes de cumplir su solicitud, lo hago y lo declaro en el audit. Mínimo viable, no más.

### 3. Operaciones prohibidas sin autorización doblemente explícita

Estas operaciones requieren que Sergio las nombre por su efecto, no solo por intención:

- `update_many` — debe decir "actualiza todos los X" y yo confirmo cuántos antes
- `delete_one` / `delete_many` — debe decir "borra"
- `drop_collection` / `drop_database` — banneadas en script. Si las pide, edito el script en su presencia.
- `bulk_write` con operaciones destructivas — mismo trato que delete_many

### 4. Protocolo de write

Cada operación de escritura sigue:

1. `find_one()` con el filtro exacto → muestro estado actual
2. Confirmo conmigo mismo que el filtro matchea solo lo intended (count si hay duda)
3. Aplico `update_one` (nunca `update_many` salvo regla 3)
4. `find_one()` de nuevo → muestro estado posterior
5. Reporto a Sergio con before / after / matched / modified

### 5. Audit log

Cada conexión y cada operación escribe una línea en `~/.kryx/mongo_audit.log` con:

```
[ISO timestamp] [op_type] [db.coll] [filter] [change|n/a] [matched/modified|read_count]
```

Sergio puede `cat ~/.kryx/mongo_audit.log` en cualquier momento para auditar. Si encuentra una línea sin solicitud correspondiente en el chat, eso es un breach de mi parte.

### 6. Sin caching de credenciales

NO copio el contenido de `~/.kryx/mongo_uri` a memoria persistente, dreams, ni mensajes. NO lo escribo en logs propios. NO lo guardo en variables exportadas a env globales.

### 7. Cierre limpio

Cada operación abre, ejecuta, cierra (`client.close()`). No mantengo conexiones colgadas entre turnos.

## Si esta política se quiebra

Si Sergio detecta una entrada en el audit log que no corresponde a una solicitud suya:

1. Es un fallo grave de mi parte
2. Le aviso de inmediato lo que pasó y por qué
3. Reviso este archivo y refuerzo la regla quebrada

## Cómo refrescar memoria

Antes de cualquier operación de BD, releer este archivo si han pasado más de unas pocas vueltas en la conversación o si la sesión es nueva.
