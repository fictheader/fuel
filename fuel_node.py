import bpy

def get_textures():
    return bpy.data.textures


def get_texture_nodetree(texture):
    return texture.node_tree


def get_texture_nodes(node_tree):
    return node_tree.nodes


def get_texture_nodetree_type(node_tree):
    return node_tree.type


def get_texture_nodetree_name(node_tree):
    return node_tree.name
