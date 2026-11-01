import time
import sys

print("1. Iniciando medición...", flush=True)

try:
    from src.dominio.biblioteca import Biblioteca
    from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
    from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion
    print("2. Módulos importados correctamente.", flush=True)
except Exception as e:
    print(f"Error importando módulos: {e}", flush=True)
    sys.exit(1)

b = Biblioteca()
datos_orig = b.obtener_todas()
n1 = len(datos_orig)
datos_x10 = list(datos_orig) * 10
n2 = len(datos_x10)

print(f"3. Catálogo cargado: n1={n1}, n2={n2}", flush=True)

# 1. Búsqueda Lineal
t0 = time.perf_counter()
busqueda_lineal(datos_orig, "NoExiste", lambda c: c.titulo)
t1 = time.perf_counter()
print(f"Búsqueda lineal (n={n1}): {t1 - t0:.8f} s", flush=True)

t0 = time.perf_counter()
busqueda_lineal(datos_x10, "NoExiste", lambda c: c.titulo)
t1 = time.perf_counter()
print(f"Búsqueda lineal (n={n2}): {t1 - t0:.8f} s", flush=True)

# 2. Búsqueda Binaria (requiere ordenar primero)
copia_ord_1 = list(datos_orig)
ordenar_insercion(copia_ord_1, lambda c: c.titulo)
t0 = time.perf_counter()
busqueda_binaria(copia_ord_1, "NoExiste", lambda c: c.titulo)
t1 = time.perf_counter()
print(f"Búsqueda binaria (n={n1}): {t1 - t0:.8f} s", flush=True)

copia_ord_2 = list(datos_x10)
ordenar_insercion(copia_ord_2, lambda c: c.titulo)
t0 = time.perf_counter()
busqueda_binaria(copia_ord_2, "NoExiste", lambda c: c.titulo)
t1 = time.perf_counter()
print(f"Búsqueda binaria (n={n2}): {t1 - t0:.8f} s", flush=True)

# 3. Selección
copia_sel_1 = list(datos_orig)
t0 = time.perf_counter()
ordenar_seleccion(copia_sel_1, lambda c: c.titulo)
t1 = time.perf_counter()
print(f"Ordenar selección (n={n1}): {t1 - t0:.8f} s", flush=True)

copia_sel_2 = list(datos_x10)
t0 = time.perf_counter()
ordenar_seleccion(copia_sel_2, lambda c: c.titulo)
t1 = time.perf_counter()
print(f"Ordenar selección (n={n2}): {t1 - t0:.8f} s", flush=True)

# 4. Inserción
copia_ins_1 = list(datos_orig)
t0 = time.perf_counter()
ordenar_insercion(copia_ins_1, lambda c: c.titulo)
t1 = time.perf_counter()
print(f"Ordenar inserción (n={n1}): {t1 - t0:.8f} s", flush=True)

copia_ins_2 = list(datos_x10)
t0 = time.perf_counter()
ordenar_insercion(copia_ins_2, lambda c: c.titulo)
t1 = time.perf_counter()
print(f"Ordenar inserción (n={n2}): {t1 - t0:.8f} s", flush=True)

print("4. Medición finalizada con éxito.", flush=True)