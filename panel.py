import bpy

class ImportPanel(bpy.types.Panel):
    bl_idname = "SCENE_PT_import"
    bl_label = ""
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="Import Folder")

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Draw import button
        layout.operator("ch_builder.select_dir", text = "Select Directory")


def register():
    bpy.utils.register_class(ImportPanel)

def unregister():
    bpy.utils.unregister_class(ImportPanel)