# TP Integrador — AyED C2 2026

Repositorio del grupo para el Trabajo Práctico Integrador de Algoritmos y Estructuras de Datos (Cátedra Ambrossio - Bianco, Universidad Nacional Guillermo Brown).

---

## Integrantes

| Nombre | Mail | GitHub |
| --- | --- | --- |
| Florencia Luján Salinas | Florsalinas25@live.com | [@Flor-Jo](https://github.com/Flor-Jo) |
| Sebastián Aquino Frago | sebas.aquinofrago@gmail.com | [@Sebas_AF](https://github.com/Sebas_AF) |
| Florencia Soffiantini | fsoffiantini@gmail.com | [@fsoffian](https://github.com/fsoffian) |

---

## Tema Elegido: Biblioteca Musical

Modelado de un catálogo de temas de Pop de los 2000s orientado a objetos, con persistencia, TADs propios, funciones recursivas y algoritmos de búsqueda y ordenamiento manuales[cite: 1, 4].

---

## Estructura del Proyecto

```text
ayed-2026-musica/
├── README.md                  # Presentación general y estado de entregas
├── src/
│   ├── config.py              # Configuración general y tema activo
│   ├── main.py                # Interfaz de línea de comandos (CLI) y menú
│   ├── excepciones.py         # Excepciones propias del dominio y TADs
│   ├── dominio/
│   │   ├── cancion.py         # Clase entidad Cancion
│   │   ├── biblioteca.py      # Gestor del catálogo y lógica recursiva (E2)
│   │   └── playlist.py        # Colección con tope basada en ListaEnlazada (E3)
│   ├── tads/
│   │   ├── nodo.py            # Nodo de enlace simple
│   │   ├── lista_enlazada.py  # TAD Lista Enlazada con iterador
│   │   ├── pila.py            # TAD Pila (LIFO) para historial de consultas
│   │   └── cola.py            # TAD Cola (FIFO) para turnos de reproducción
│   └── algoritmos/            # Algoritmos propios implementados a mano (E4)
│       ├── busqueda.py        # Búsqueda lineal y búsqueda binaria
│       └── ordenamiento.py    # Selección (no estable) e inserción (estable)
├── docs/
│   ├── INFORME.md             # Informe técnico, justificación y complejidades (§5)
│   ├── PROTOCOLO_PRUEBAS.md   # Casos de prueba manuales ejecutados (P01 a P18)
│   └── DECLARACION_IA.md      # Registro formal de asistencia y herramientas
└── data/                      # Archivos de datos (E5)
