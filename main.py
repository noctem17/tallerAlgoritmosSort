"""Punto de entrada del programa. Antes de correr esto, hay que haber
corrido herramientas/generar_numeros.py al menos una vez."""

from controller.controlador_pruebas import ejecutar_pruebas
from view.vista_resultados import guardar_csv, graficar_resultados

if __name__ == "__main__":
    resultados = ejecutar_pruebas()

    if resultados:
        guardar_csv(resultados)
        graficar_resultados(resultados)
    else:
        print("No hubo resultados. Revisa que los archivos numeros_N.txt existan en datos/.")