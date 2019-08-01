#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  MakePillow2019.py
#
#  Copyright 2018 Mac <Mac@HAFSTACKER>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#


bl_info = {
    "name": "Make Pillow",
    "description": "Make Pillow in blender with cloth sims and force fields",
    "author": "Mark C - Fourth Level Studios LTD",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "Spacebar",
    "warning": "2.8 Beta Release",
    "wiki_url": "http://example.com",
    "category": "Add Mesh" }

import bpy


class MakePillow(bpy.types.Operator):
    """Make Pillows The Easy Way"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "object.make_pillow"        # unique identifier for buttons and menu items to reference.
    bl_label = "Make Pillow"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def execute(self, context):        # execute() is called by blender when running the operator.

        # The original script
       scene = context.scene
       bpy.ops.object.effector_add(type='FORCE', enter_editmode=False, location=(0, 0, 0))
       bpy.ops.mesh.primitive_cube_add(location=(0.0, 0.0, 0.0), enter_editmode=True)
       bpy.ops.transform.resize(value=(1.0, 1.0, 0.2))
       bpy.ops.mesh.subdivide(quadcorner='INNERVERT')
       bpy.ops.mesh.subdivide()
       bpy.ops.mesh.subdivide()
       bpy.ops.object.modifier_add(type='SUBSURF')
       bpy.ops.object.modifier_apply(apply_as='DATA')
       bpy.ops.object.mode_set(mode='OBJECT', toggle=True)
       bpy.ops.object.shade_smooth()
       bpy.ops.object.modifier_add(type='CLOTH')
       bpy.context.object.modifiers["Cloth"].settings.effector_weights.gravity = 0
       bpy.data.objects['Field'].field.strength = 200
       bpy.context.object.modifiers["Cloth"].settings.mass = 0.3
       bpy.ops.screen.frame_jump(end=False)
       bpy.ops.screen.animation_play()

       return {'FINISHED'}            # this lets blender know the operator finished successfully.

def register():
    bpy.utils.register_class(MakePillow)


def unregister():
    bpy.utils.unregister_class(MakePillow)


# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
     register()
