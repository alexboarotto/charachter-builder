import bpy

class helpers():    

    @staticmethod
    def uniform_scale_objects(scale = 1):
        for obj in bpy.data.objects:
            if obj.parent is None:
                bpy.context.scene.cursor.location = (0.0, 0.0, 0.0)
                bpy.ops.object.origin_set(type = 'ORIGIN_CURSOR')
                obj.scale = (obj.scale.x*scale, obj.scale.y*scale, obj.scale.z*scale)

                    
        
            

        