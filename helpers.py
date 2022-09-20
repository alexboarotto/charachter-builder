import bpy

class helpers():    

    @staticmethod
    def uniform_scale_objects(scale = 1):
        for obj in bpy.data.objects:
            if obj.parent is None:
                obj.scale = (obj.scale.x*scale, obj.scale.y*scale, obj.scale.z*scale)

                    
        
            

        