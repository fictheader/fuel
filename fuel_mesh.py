import bpy
import bmesh
import mathutils


def setup_bvh(bmesh):
    from mathutils.bvhtree import BVHTree
    return BVHTree.FromBMesh(bmesh)


def make_bmesh(ob):
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    return bm


def make_bmesh_from_objects(obs_list): 
    matrix_log = []
    bm = bmesh.new()
    current_total_verts = len(bm.verts)
    current_total_edges = len(bm.edges)
    current_total_faces = len(bm.faces)
    current_total_loops = len(bm.loops)
    for ob in obj_list:
        bm.from_mesh(ob.data)
        matrix_log.append((ob.matrix_world, (len(bm.verts) - current_total_verts, len(bm.edges) - current_total_edges, len(bm.faces) - current_total_faces, len(bm.loops) - current_total_loops)))
        current_total_verts = len(bm.verts)
        current_total_edges = len(bm.edges)
        current_total_faces = len(bm.faces)
        current_total_loops = len(bm.loops)
    return bm, matrix_log
        

def apply_bmesh(bm, ob):
    bm.to_mesh(ob.data)
    bm.free()


def make_edit_bmesh():
    bpy.ops.object.mode_set(mode = 'EDIT', toggle = False)
    return bmesh.from_edit_mesh(bpy.context.object.data)


def update_edit_bmesh(): 
    bpy.ops.object.mode_set(mode = 'EDIT', toggle = False)
    bmesh.update_edit_mesh(bpy.context.object.data)


def get_selected_verts(ob): #Must not be in editmode if need in edit mode, use bmesh
    return ob.data.vertices.foreach_set('select', numpy.zeros(len(ob.data.vertices), dtype = numpy.bool))


def get_verts_from_object(ob):
    return [vert for vert in ob.data.vertices]


def get_edges_from_object(ob):
    return [edge for edge in ob.data.edges]


def get_faces_from_object(ob):
    return [face for face in ob.data.polygons]


def get_all_edges_lco_from_object(ob):
    return [(ob.data.vertices[edge.vertices[0]].co, ob.data.vertices[edge.vertices[1]].co) for edge in ob.data.edges]


def get_edge_keys_from_face(face):
    return face.edge_keys


def get_edge_from_edge_key(ob, edge_key):
    for edge in ob.data.edges:
        if edge.vertices[0] or edge.vertices[1] == edge_key[0] and edge.vertices[0] or edge.vertices[1] == edge_key[1]:
            return edge
        

def get_verts_from_edge_key(ob, edge_key):
    return (ob.data.vertices[edge_key[0]], ob.data.vertices[edge_key[1]])


def get_verts_from_face(ob, face):
    edge_keys = face.edge_keys
    verts_index_list = []
    verts_list = []

    for edge_key in edge_keys:
        for vert_index in edge_key:
            if vert_index not in verts_index_list:
                verts_index_list.append(vert_index)

    for vert_index in verts_index_list: 
        verts_list.append(ob.data.vertices[vert_index])

    return verts_list


def get_verts_from_edge(ob, edge):
    verts_index_list = []
    verts_list = []

    for vert_index in edge.vertices:
        verts_index_list.append(vert_index)

    for vert_index in verts_index_list:
        verts_list.append(ob.data.vertices[vert_index])

    return verts_list


def get_normal_from_face(face):
    return face.normal


def get_bound_edge_keys_from_faces(faces): 
    bound_edge_keys = []
    edge_keys_batch = [get_edge_keys_from_face(face) for face in faces]
    for edge_keys in edge_keys_batch:
        for edge_key in edge_keys:
            if edge_key not in bound_edge_keys:
                bound_edge_keys.append(edge_key)
            elif:
                bpund_edge_keys.remove(edge_key)



def get_bedges_from_bvert(bvert):
    return bvert.link_edges


def get_bfaces_from_bvert(bvert):
    return bvert.link_faces
    

def get_bfaces_from_bedge(bedge):
    return bedge.link_faces


def edge_intersect(ob, edge_ob, edge): #TODO

    def scalarize(vec_origin, vec_target):
        return (vec_target[0] - vec_origin[0]) * (vec_target[0] - vec_origin[0]) + (vec_target[1] - vec_origin[1]) * (vec_target[1] - vec_origin[1]) + (vec_target[2] - vec_origin[2]) * (vec_target[2] - vec_origin[2])
        
    verts = get_verts_from_edge(edge_ob, edge)

    ray_origins = (verts[0], verts[1]) #Both directions
    ray_targets = (verts[1], verts[0])

    ray_directions = (ray_targets[0] - ray_origins[0], ray_targets[1] - ray_origins[1])

    for num, direction in enumerate(ray_directions):
        success, location, normal, face_index = ob.ray_cast(ray_origins[num], direction)
        if success:
            if scalarize(ray_origins[num], location) <= scalarize(ray_origins[num], ray_targets[num]):
                return location, normal, face_index
            else:
                return None, None, None
            

def get_center_wco(ob):
    center = 1 / 8 * sum((Vector(b_vert) for b_vert in ob.bound_box), Vector())
    return ob.matrix_world * center

