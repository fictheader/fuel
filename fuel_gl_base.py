import bpy

#MAIN
def rect_range_check_2d(*args):
    def _rect_ragne_check_2d_1(cursor_loc, top_left, bottom_right):

        x_1, y_1 = top_left[0], top_left[1]
        x_2, y_2 = bottom_right[0], bottom_right[1]

        if x_1 <= cursor_loc[0] <= x_2 and y_1 >= cursor_loc[1] >= y_2:
            return True
        else:
            return False


    def _rect_ragne_check_2d_2(cursor_loc, center_loc, width, height):
        
        c_x, c_y = center_loc[0], center_loc[1]
        x_1, y_1 = c_x - width/2, c_y - height/2
        x_2, y_2 = c_x + width/2, c_y + height/2
        
        if x_1 <= cursor_loc[0] <= x_2 and y_1 >= cursor_loc[1] >= y_2:
            return True
        else:
            return False

    if len(*args) == 3:
        _rect_ragne_check_2d_1(*args)
    else:
        _rect_ragne_check_2d_2(*args)

