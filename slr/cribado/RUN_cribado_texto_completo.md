# Cribado de texto completo — hoja de ejecución (opción 2: extractos + Claude y Codex en paralelo)

Todo se ejecuta desde `slr/cribado`. Ambos ejecutores se reparten el trabajo solos (`scripts/ft_coord.py`):
Claude toma los informes desde el principio de la cola, Codex desde el final; A y B de un mismo informe
siempre los hace el mismo modelo. Se pueden ejecutar **a la vez** y **reanudar** tantas veces como haga falta.

## Claude (tu plan Pro; Sonnet en modo headless)
```
python scripts/run_ft_cli.py --jobs 8
```
- Si se alcanza el límite de uso, se detiene solo. Cuando se reinicie la cuota, vuelve a ejecutar el mismo comando.

## Codex (tu plan de Codex)
1. Abre Codex en la raíz del repositorio y pega:
   > Read `slr/cribado/HANDOFF_codex_ft.md` (v2) and do step 1 only (excerpt calibration), then stop and report the table.
2. Si la tabla muestra **8/8 o 7/8 en «include-vs-not»**, dile: «continue» (paso 2).
   Si muestra menos, no continúes con Codex y avísame.

## Si Codex dice «pending calls: 0» pero aún quedan informes
Libera los informes que Claude reservó y no empezó (los que tienen decisión parcial siguen con Claude):
```
python scripts/ft_coord.py release claude
```

## Seguimiento
- Avance: `python -c "import sys; sys.path.insert(0,'scripts'); import ft_coord, json; d=ft_coord.decided(); print(len(d), 'de 862 llamadas decididas')"`
- Cuando llegue a **862 de 862**, avísame: hago la fusión, el desempate (Opus), la segunda lectura de E6 y tu hoja de revisión.

## Qué cambió (para la sección de métodos)
- Los informes sin decisión previa se cribaron con un **extracto** (páginas de título, resumen, introducción/contribuciones y sección experimental), calibrado frente al texto completo en 8 informes (`calibracion_extractos.py`).
- Revisores A/B del Nivel 1: Claude Sonnet (headless) y GPT (Codex) según el informe; ambos revisores de un informe, siempre el mismo modelo. Registro por informe en `sr_work/runs/` y `claims/`.
