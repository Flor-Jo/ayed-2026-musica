| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | dataset de la cátedra | lista no vacía, sin traceback | pasa | Listado completo ok |
| P02 | E1 | Elegir un ítem inexistente (Opción 2) | id = 99 | mensaje claro, el menú sigue | pasa | Captura error sin caerse |
| P03 | E2 | Operación recursiva sobre un ítem con cadena | id = 2 | imprime la cadena [8, 1] | pasa | Resuelto con recursión |
| P04 | E2 | Operación recursiva sobre un ítem sin derivados | id = 3 | solo la lista vacía [] (caso base) | pasa | Caso base ok |
| P05 | E2 | Ver el detalle de un ítem que existe (Opción 2) | id = 1 | Muestra los datos de "Toxic" | pasa | Atributos correctos |
| P06 | E2 | Elegir una opción de menú inválida | input = "abc" | Muestra "Opción inválida", vuelve al menú | pasa | Menú permanece activo |
| P07 | E2 | Enviar input vacío en el menú principal | apretar Enter | No explota, vuelve al menú | pasa | Strip maneja vacío |
| P08 | E2 | Ingresar un texto cuando pide un ID | input = "uno" | Muestra error de número, el menú sigue | pasa | ValueError atrapado |
| P10 | E2 | Salir del programa de forma segura | input = "0" | Imprime "Chau." y el programa termina | pasa | Salida limpia |
| P11 | E3 | Agregar a la colección principal hasta el tope | equipo de 6 / equivalente | el séptimo falla con excepción propia | pasa | ColeccionLlenaError ok |
| P12 | E3 | Desapilar historial vacío | pila vacía | excepción propia, menú sigue | pasa | PilaVaciaError ok |
| P13 | E3 | Desencolar cola vacía | cola vacía | excepción propia, menú sigue | pasa | ColaVaciaError ok |
| P14 | E3 | Listar colección con el iterador | 2+ ítems | el orden coincide con las inserciones | pasa | Iterador de lista enlazada ok |
| P15 | E4 | Búsqueda lineal de un nombre que existe | "Toxic" (o título existente) | lo encuentra y muestra resumen | pasa | Búsqueda propia sin .index() |
| P16 | E4 | Búsqueda lineal de un nombre que no existe | "CancionInexistente" | "Canción no encontrada", sin traceback | pasa | Manejo sin excepción |
| P17 | E4 | Búsqueda binaria con catálogo desordenado | Catálogo sin ordenar | avisa o reordena; no da un falso hit | pasa | Reordena por título automáticamente y avisa |
| P18 | E4 | Ordenar por un criterio y después por otro | 1) Título 2) Duración | el orden cambia correctamente | pasa | Selección e inserción probados |
| P19 | E5 | Guardar CSV, salir, volver a entrar | - | los datos siguen | no corrido | Previsto para E5 |
| P20 | E5 | Guardar binario y modificar un registro por id | - | al recargar, ese campo cambió | no corrido | Previsto para E5 |
| P21 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido | no corrido | Previsto para E5 | 
