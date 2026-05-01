import maya.cmds as cmds

def prep_scene_for_export():
    """
    Herramienta básica de limpieza de pipeline.
    Realiza: Freeze Transformations, Delete History, y limpieza de nodos.
    """
    # 1. Obtener selección
    selection = cmds.ls(selection=True, dag=True, type='mesh')
    
    if not selection:
        cmds.warning("No hay meshes seleccionados para procesar.")
        return

    for obj in selection:
        # 2. Freeze Transformations
        cmds.makeIdentity(obj, apply=True, t=1, r=1, s=1, n=0)
        
        # 3. Delete History
        cmds.delete(obj, ch=True)
        
        # 4. Center Pivot
        cmds.xform(obj, cp=True)
        
        print(f"Procesado: {obj}")

    # 5. Limpieza general de la escena (Optimización)
    cmds.ogSkins() # Eliminar skins vacíos si existen
    print("Limpieza de pipeline completada con éxito.")

if __name__ == "__main__":
    prep_scene_for_export()