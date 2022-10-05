import bpy

class autorigger():

    def find_armature():
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                return obj
        return None

    @classmethod
    def attach_to_armature(self):
        armature = self.find_armature()

        for obj in bpy.data.objects:
            if obj.parent is None and obj is not armature:
                obj.select_set(True)
                armature.select_set(True)
                bpy.ops.object.parent_set(type = 'ARMATURE_AUTO')
                bpy.ops.object.select_all(action='DESELECT')
