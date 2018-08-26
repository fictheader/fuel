import bpy
import mathutils


def get_active_object():
    return bpy.cotnext.active_object


def get_visible_objects():
    return bpy.context.visible_ojects


def get_objects():
    return bpy.data.objects


def get_selected_objects():
    return bpy.context.selected_objects


def move_origin(ob, new_origin):
    base_loc = ob.location
    ob.location = new_origin 
    ob.data.transform(mathutils.Matrix.Translation(base_loc - new_origin))


def pivot_ob_around_vec(ob, v_origin, v_target, degrees):
    current_loc = ob.location
    current_mode = ob.rotation_mode
    ob.rotation_mode = 'QUATERNION'
    move_origin(ob, v_origin)
    axis_vec = v_target - v_origin
    quaternion = Quaternion(axis_vec, math.radians(degrees))
    ob.roation_quaternion = quaternion
    move_origin(current_loc)
    ob.rotation_mode = current_loc


class at:
    def __init__(self, ob, center_pos):
        self.prev_cursor = bpy.context.scene.cursor_location.copy()
        bpy.context.scene.cursor_location = center_pos
        bpy.context.scene.objects.active = ob

    def __enter__(self):
        bpy.ops.object.origin_set(type = 'ORIGIN_CURSOR')
        return self

    def rotate(self, euler):
        bpy.context.active_object.rotation_euler.rotate(euler)

    def move(self, dst_pos):
        bpy.context.active_object.location = dst_pos

    def __exit__(self, type, value, traceback):
        bpy.ops.object.origin_set(type = 'ORIGIN_GEOMETRY')
        bpy.context.scene.cursor_location = self.prev_cursor


def apply_all_modifiers():
    bpy.ops.object.convert(target='MESH')


def force_edit_mode():
    bpy.ops.object.mode_set(mode = 'EDIT', toggle = False)


def force_object_mode():
    bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)


def force_sculplt_mode():
    bpy.ops.object.mode_set(mode = 'SCULPT', toggle = False)


def force_vertex_paint_mode():
    bpy.ops.object.mode_set(mode = 'VERTEX_PAINT', toggle = False)


def force_weight_paint_mode():
    bpy.ops.object.mode_set(mode = 'WEIGHT_PAINT', toggle = False)


def force_texture_paint_mode():
    bpy.ops.object.mode_set(mode = 'TEXTURE_PAINT', toggle = False)


def toggle_object():
    bpy.ops.object.editmode_toggle()


def get_modifier_items(ob):
    return bpy.data.objects[ob.name].modifiers.items()

