# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | dataset de la cátedra | lista no vacía, sin traceback | no corrido | |
| P02 | E1 | Elegir un ítem inexistente (Opción 2) | id = 99 | mensaje claro, el menú sigue | no corrido | |
| P03 | E2 | Operación recursiva sobre un ítem con cadena | id = 2 | imprime la cadena [8, 1] | no corrido | |
| P04 | E2 | Operación recursiva sobre un ítem sin derivados | id = 3 | solo la lista vacía [] (caso base) | no corrido | |
| P05 | E2 | Ver el detalle de un ítem que existe (Opción 2) | id = 1 | Muestra los datos de "Toxic" | no corrido | |
| P06 | E2 | Elegir una opción de menú inválida | input = "abc" | Muestra "Opción inválida", vuelve al menú | no corrido | |
| P07 | E2 | Enviar input vacío en el menú principal | apretar Enter | No explota, vuelve al menú | no corrido | |
| P08 | E2 | Ingresar un texto cuando pide un ID | input = "uno" | Muestra error de número, el menú sigue | no corrido | |
| P10 | E2 | Salir del programa de forma segura | input = "0" | Imprime "Chau." y el programa termina | no corrido | |
| P11 | E3 | Agregar a la colección principal hasta el tope | equipo de 6 / equivalente | el séptimo falla con excepción propia | no corrido | |
| P12 | E3 | Desapilar historial vacío | pila vacía | excepción propia, menú sigue | no corrido | |
| P13 | E3 | Desencolar cola vacía | cola vacía | excepción propia, menú sigue | no corrido | |
| P14 | E3 | Listar colección con el iterador | 2+ ítems | el orden coincide con las inserciones | no corrido | |
| P15 | E4 | Búsqueda lineal de un nombre que existe | | lo encuentra | no corrido | |
| P16 | E4 | Búsqueda lineal de un nombre que no existe | | no encontrado, sin traceback | no corrido | |
| P17 | E4 | Búsqueda binaria con catálogo desordenado | | avisa o reordena; no da un falso hit | no corrido | |
| P18 | E4 | Ordenar por un criterio y después por otro | | el orden cambia | no corrido | |
| P19 | E5 | Guardar CSV, salir, volver a entrar | | los datos siguen | no corrido | |
| P20 | E5 | Guardar binario y modificar un registro por id | | al recargar, ese campo cambió | no corrido | |
| P21 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido | no corrido | |