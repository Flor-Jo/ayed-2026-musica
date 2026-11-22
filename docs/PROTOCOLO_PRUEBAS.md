# Protocolo de Pruebas de Regresión — AyED C2 2026

Ejecución completa sobre el producto cerrado (`tag entrega-6`) desde la raíz del repositorio (`python -m src.main`), dividida según los módulos defendidos por cada integrante.

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Responsable (Defensa) | Notas |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo (Opción 1) | Catálogo base | Lista no vacía, sin traceback | pasa | Florencia Luján Salinas | Listado completo ok |
| P02 | E1 | Ver detalle de un ítem inexistente (Opción 2) | `id = 99` | Mensaje claro, el menú sigue activo | pasa | Florencia Luján Salinas | Captura error sin caerse |
| P03 | E2 | Operación recursiva sobre un ítem con cadena (Opción 5) | `id = 2` | Imprime la cadena `[8, 1]` | pasa | Florencia Luján Salinas | Resuelto con recursión |
| P04 | E2 | Operación recursiva sobre un ítem sin derivados (Opción 5) | `id = 3` | Devuelve la lista vacía `[]` (caso base) | pasa | Florencia Luján Salinas | Caso base ok |
| P05 | E3 | Llenar la colección principal hasta el tope (Opción 6b) | 6 canciones (tope = 5) | La sexta falla con excepción propia | pasa | Sebastián Aquino Frago | `ColeccionLlenaError` capturada |
| P06 | E3 | Desapilar historial vacío (Opción 7b) | Pila vacía | Excepción propia, menú sigue | pasa | Sebastián Aquino Frago | `PilaVaciaError` capturada |
| P07 | E3 | Desencolar cola vacía (Opción 8b) | Cola vacía | Excepción propia, menú sigue | pasa | Sebastián Aquino Frago | `ColaVaciaError` capturada |
| P08 | E3 | Listar colección con el iterador (Opción 6a) | 2+ ítems en playlist | El orden coincide con las inserciones | pasa | Sebastián Aquino Frago | `__iter__` de `ListaEnlazada` ok |
| P09 | E4 | Búsqueda lineal de un título que existe (Opción 3.1) | `"Toxic"` | Lo encuentra y muestra resumen | pasa | Florencia Soffiantini | Búsqueda propia sin `.index()` |
| P10 | E4 | Búsqueda lineal de un título que no existe (Opción 3.1) | `"CancionInexistente"` | "Canción no encontrada", sin traceback | pasa | Florencia Soffiantini | Manejo limpio |
| P11 | E4 | Búsqueda binaria con catálogo desordenado (Opción 3.2) | Catálogo sin ordenar | Avisa y reordena; no da un falso hit | pasa | Florencia Soffiantini | Reordena por título automáticamente |
| P12 | E4 | Ordenar por un criterio y después por otro (Opción 4) | 1) Título 2) Duración | El orden cambia correctamente | pasa | Florencia Soffiantini | Selección e Inserción probados |
| P13 | E5 | Guardar `.txt`, salir, volver a entrar y cargar (Opción 9a -> 0 -> 9b) | Catálogo modificado | Los datos persisten en disco | pasa | Sebastián Aquino Frago | Persistencia en `data/canciones.txt` ok |
| P14 | E5 | Guardar binario, modificar por ID y recargar (Opción 9c -> 9g -> 9d) | `id = 1` modificado | Al recargar desde `.bin`, el campo cambió | pasa | Florencia Luján Salinas | Acceso directo `seek(9 + pos * 84)` ok |
| P15 | E5 | Abrir archivo basura/corrupto (Opción 9b / 9d) | `README.md` como ruta | Excepción de archivo inválido sin traceback | pasa | Florencia Soffiantini | `ArchivoInvalidoError` capturada |
