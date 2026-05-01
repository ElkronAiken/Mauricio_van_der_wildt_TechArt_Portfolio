# 🛠️ Pipeline Prep Tool - Autodesk Maya

![Banner del Proyecto](.\Mauricio_van_der_wildt_TechArt_Portfolio\Auto_CleanUp&Prep_Tool)

Este repositorio contiene una herramienta de automatización diseñada para optimizar y estandarizar el flujo de trabajo en **Autodesk Maya**, enfocada en la preparación de assets antes de su exportación a motores de juego o entornos de renderizado.

## 🎯 Propósito
El objetivo principal es reducir el error humano y ahorrar tiempo al automatizar tareas repetitivas de limpieza. Esta herramienta asegura que todos los modelos cumplan con los estándares técnicos básicos, garantizando escenas "limpias" y listas para producción.

## ⚙️ Lenguajes Incluidos

El script se encuentra disponible en dos versiones para adaptarse a las necesidades del pipeline:

* 🐍 **Python (`maya_prep_tool.py`):** Recomendado para pipelines modernos por su versatilidad.
* 📜 **MEL (`maya_prep_tool.mel`):** Ideal para una integración nativa profunda con las funciones core de Maya.

## 📊 Resultados Esperados (Validación Técnica)

Al ejecutar la herramienta, podrás verificar los cambios en la interfaz de Maya:

1.  **Limpieza de Nodos:** El historial de construcción (*Construction History*) en el *Attribute Editor* se eliminará, dejando solo los nodos básicos de *Transform* y *Shape*.
2.  **Reset de Coordenadas:** Las transformaciones serán congeladas (*Freeze Transformations*). Los valores de *Translate* y *Rotate* volverán a `0`, y los de *Scale* a `1` en el *Channel Box*.
3.  **Ajuste de Pivote:** El punto de pivote se centrará automáticamente en la geometría del objeto, facilitando su manipulación y uso posterior en el motor.

## 🚀 Instrucciones de Uso

### Para Python:
1. Copia el contenido de `maya_prep_tool.py`.
2. En Maya, abre el **Script Editor** (Windows > General Editors > Script Editor).
3. Pega el código en una pestaña de **Python**.
4. Selecciona tus objetos en el viewport y presiona `Ctrl + Enter`.

### Para MEL:
1. Copia el contenido de `maya_prep_tool.mel`.
2. En el **Script Editor**, abre una pestaña de **MEL**.
3. Pega el código.
4. Selecciona tus objetos en el viewport y presiona `Ctrl + Enter`.

---
*Desarrollado para la certificación de TechArt - 2026.*