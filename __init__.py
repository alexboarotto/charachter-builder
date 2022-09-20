from . import panel
from . import import_folder

bl_info = {
    "name": "Character Builder",
    "blender": (3, 0, 0),
    "category": "Import-Export",
    "support": "COMMUNITY",
}

def register():
    panel.register()
    import_folder.register()

def unregister():
    panel.unregister()
    import_folder.unregister()
