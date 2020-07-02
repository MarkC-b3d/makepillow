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
    "author": "Mark C, Oxervision",
    "version": (0, 0, 2),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh",
    "warning": "",
    "wiki_url": "https://github.com/blendedmarks/makepillow.py",
    "category": "Add Mesh" }

import bpy


class OBJECT_OT_MakePillow(bpy.types.Operator):
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
       bpy.ops.object.mode_set(mode='OBJECT', toggle=True)
       bpy.ops.object.modifier_apply(apply_as='DATA')
       bpy.ops.object.shade_smooth()
       bpy.ops.object.modifier_add(type='CLOTH')
       ##Cloth sim settings
       bpy.context.object.modifiers["Cloth"].settings.effector_weights.gravity = 0
       bpy.context.object.modifiers["Cloth"].settings.quality = 10
       bpy.context.object.modifiers["Cloth"].settings.time_scale = 2
       bpy.context.object.modifiers["Cloth"].settings.mass = 0.3
       bpy.context.object.modifiers["Cloth"].settings.air_damping = 0
       bpy.context.object.modifiers["Cloth"].settings.bending_model = 'LINEAR'
       bpy.context.object.modifiers["Cloth"].settings.tension_stiffness = 1
       bpy.context.object.modifiers["Cloth"].settings.shear_stiffness = 0
       bpy.context.object.modifiers["Cloth"].settings.bending_stiffness = 1
       bpy.context.object.modifiers["Cloth"].settings.tension_damping = 5
       bpy.context.object.modifiers["Cloth"].settings.shear_damping = 5
       bpy.context.object.modifiers["Cloth"].settings.bending_damping = 0.5
       bpy.context.object.modifiers["Cloth"].settings.use_pressure = True
       bpy.context.object.modifiers["Cloth"].settings.uniform_pressure_force = 0.5
       bpy.context.object.modifiers["Cloth"].collision_settings.use_collision = True
       bpy.context.object.modifiers["Cloth"].collision_settings.use_self_collision = True
       #Force field settings
       bpy.data.objects['Field'].field.strength = 200
       bpy.ops.screen.frame_jump(end=False)
       bpy.ops.screen.animation_play()

       return {'FINISHED'}            # this lets blender know the operator finished successfully.


def menu_func(self, context):
    self.layout.operator(OBJECT_OT_MakePillow.bl_idname,
                        text="Make Pillow", icon="MOD_CLOTH")


def register():
    bpy.utils.register_class(OBJECT_OT_MakePillow)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)



def unregister():
    bpy.utils.unregister_class(OBJECT_OT_MakePillow)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)



# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
     register()
