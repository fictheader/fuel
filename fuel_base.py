import bpy
import bpy_extras.view3d_utils
import sys
import os

#need rewrite

def override_context(area_name):
    for area in bpy.context.screen.areas:
        if area.type == area_name:
            override = bpy.context.copy()
            override['area'] = area
            return override


def print_to_console(txt):
    ovctx = override_context('CONSOLE')
    try:
        bpy.ops.console.scrollback_append(ovctx, text = str(txt), type = 'OUTPUT')

    except ValueError:
        pass


def get_region_window_size_context():
    for region in bpy.context.area.regions:
        if region.type == 'WINDOW':
            return region.width, region.height

    
def get_viewport_loc_context(): #TODO
    region = bpy.context.region
    rv3d = bpy.context.region_data
    width, height = get_region_window_size_context() 
    coord = (width/2, height/2)
    return bpy_extras.view3d_utils.region_2d_to_origin_3d(region, rv3d, coord)


def get_viewports_loc(screen_name):
    area_set = []
    rv3d_set = []
    region_set = []
    coord_set = []
    result = []

    for area in bpy.data.screens[screen_name].areas:
        if area.type == 'VIEW_3D':
            area_set.append(area)
            rv3d_set.append(area.spaces[0].region_3d)

    for area in area_set:
        for region in area.regions:
            if region.type == 'WINDOW':
                region_set.append(region)
                coord_set.append((region.width/2 , region.height/2))

    final_set = zip(region_set, rv3d_set, coord_set)
    
    for args in final_set:
        result.append(bpy_extras.view3d_utils.region_2d_to_origin_3d(*args))

    return result


def get_area_context():
    return bpy.context.area


def get_areas_context():
    return bpy.context.screen.areas


def get_screen_name_context():
    return bpy.context.screen.name


def get_screen(screen_name):
    return bpy.data.screens[screen_name]


def get_areas(screen_name):
    return get_screen(screen_name).areas


def get_area(screen_name, area_name):
    areas = get_areas(screen_name)
    for area in areas:
        if area.type == area_name:
            return area


def get_space_context(area_name):
    areas = bpy.context.screen.areas
    for area in areas:
        if area.type == area_name:
            for space in area.spaces:
                if space.type == area_name:
                    return space


def get_space(area_name, screen_name):
    areas = get_areas(screen_name) 
    for area in areas:
        if area.type == area_name:
            for space in area.spaces:
                if space.type == area_name:
                    return space


def get_view3d_space_context():
    areas = bpy.context.screen.areas
    for area in areas:
        if area.type == 'VIEW_3D':
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    return space


def get_view3d_space(screen_name):
    areas = get_areas(screen_name)
    for area in areas:
        if area.type == 'VIEW_3D':
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    return space


def get_regions_context(area_name):
    areas = bpy.context.screen.areas
    for area in areas:
        if area.type == area_name:
            return area.regions


def get_regions(area_name, screen_name):
    areas = get_areas(screen_name)
    for area in areas:
        if area.type == area_name:
            return area.regions


def get_view3d_regions_context():
    areas = bpy.context.screen.areas
    for area in areas:
        if area.type == 'VIEW_3D':
            return area.regions


def get_view3d_regions(screen_name):
    areas = get_areas(screen_name)
    for area in areas:
        if area.type == 'VIEW_3D':
            return area.regions


def get_rv3d_context():
    areas = bpy.context.screen.areas
    for area in areas:
        if area.type == 'VIEW_3D':
            return area.spaces[0].region_3d


def get_rv3d(screen_name): 
    areas = get_areas(screen_name)
    for area in areas:
        if area.type == 'VIEW_3D':
            return area.spaces[0].region_3d


def get_addon_prefs():
    user_preferences = bpy.context.user_preferences
    return user_preferences.addons[__name__].preferences


def get_keymap_item(km, kmi_idname):
    for keymap_item in km.keymap_items:
        if keymap_item.idname == kmi_idname:
            return keymap_item
    return None
