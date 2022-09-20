import bpy
import re
import os
from bpy_extras.io_utils import ImportHelper

from .helpers import helpers
from .auto_rigger import autorigger

SCALE = 5

class SelectDir(bpy.types.Operator, ImportHelper):

    """Select Directory"""
    bl_idname = "ch_builder.select_dir"
    bl_label = "Select Folder"
    bl_options = {'REGISTER'}

    filename_ext = "."
    use_filter_folder = True

    # Define this to tell 'fileselect_add' that we want a directoy
    directory = bpy.props.StringProperty(
        name="Folder Path",
        description="Directory containing character data"
        # subtype='DIR_PATH' is not needed to specify the selection mode.
        # But this will be anyway a directory path.
        )

    def import_items(self, folder_path):
        if not folder_path:
            return

        fbx_files = []

        for base, dirs, files in os.walk(folder_path, topdown=False):
            fbx_files.extend([ base+'\\'+fi for fi in files if fi.endswith(".fbx") ])

        for fbx in fbx_files:
            bpy.ops.import_scene.fbx(filepath=fbx)
        
    def execute(self, context):
        root_path = self.properties.filepath

        # remove current objects in scene
        for obj in bpy.data.objects:
            bpy.data.objects.remove(obj, do_unlink=True)

        # import files from folder to scene
        self.import_items(root_path)

        # attach all objects to armature with automatic weights 
        # (scales meshes up for high poly meshes because blender's auto weight system works with blender units
        #  so verts that are too close together can cause problems)
        helpers.uniform_scale_objects(SCALE)
        autorigger.attach_to_armature()
        helpers.uniform_scale_objects(1/SCALE)

        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        # Tells Blender to hang on for the slow user input
        return {'RUNNING_MODAL'}

def register():
    bpy.utils.register_class(SelectDir)


def unregister():
    bpy.utils.unregister_class(SelectDir)
