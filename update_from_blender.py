#!/usr/bin/env python3

"""
This script simply copies required files from blender source dir.

run:

  rm -rf src/blenlib src/mathutils
  update_from_blender.py /src/blender

Assuming blenders code is in /src/blender
"""

import os
import sys
BLENDER_DIR = sys.argv[-1]
SOURCE_DIR = os.getcwd()

test_path = os.path.join(BLENDER_DIR, "source/blender/python/mathutils")
if not os.path.exists(test_path):
    print("Blender directory not given as argument: Can't find %r" % test_path)
    sys.exit(1)
del test_path


def update_source(files, files_dest, files_level):
    import shutil
    for f in files:
        f_src = os.path.join(BLENDER_DIR, f)
        f_dst = os.sep.join(f.split(os.sep)[files_level:])
        f_dst = os.path.join(SOURCE_DIR, files_dest, f_dst)
        print("%r -> %r" % (f_src, f_dst))

        os.makedirs(os.path.dirname(f_dst), exist_ok=True)
        shutil.copy2(f_src, f_dst)
        os.system("git add " + f_dst)


# strip "source/blender/python"
files_mathutils_level = 3
files_mathutils_dest = "src"
files_mathutils = (
    "source/blender/python/mathutils/mathutils.c",
    "source/blender/python/mathutils/mathutils.h",
    "source/blender/python/mathutils/mathutils_Color.c",
    "source/blender/python/mathutils/mathutils_Color.h",
    "source/blender/python/mathutils/mathutils_Euler.c",
    "source/blender/python/mathutils/mathutils_Euler.h",
    "source/blender/python/mathutils/mathutils_Matrix.c",
    "source/blender/python/mathutils/mathutils_Matrix.h",
    "source/blender/python/mathutils/mathutils_Quaternion.c",
    "source/blender/python/mathutils/mathutils_Quaternion.h",
    "source/blender/python/mathutils/mathutils_Vector.c",
    "source/blender/python/mathutils/mathutils_Vector.h",
    "source/blender/python/mathutils/mathutils_geometry.c",
    "source/blender/python/mathutils/mathutils_geometry.h",
    "source/blender/python/mathutils/mathutils_interpolate.c",
    "source/blender/python/mathutils/mathutils_interpolate.h",
    )


# strip "source/blender"
files_blenlib_level = 2
files_blenlib_dest = "src"
files_blenlib = (
    "source/blender/blenlib/BLI_compiler_attrs.h",
    "source/blender/blenlib/BLI_compiler_compat.h",
    "source/blender/blenlib/BLI_compiler_typecheck.h",
    "source/blender/blenlib/BLI_dynstr.h",
    "source/blender/blenlib/BLI_math.h",
    "source/blender/blenlib/BLI_math_base.h",
    "source/blender/blenlib/BLI_math_bits.h",
    "source/blender/blenlib/BLI_math_color.h",
    "source/blender/blenlib/BLI_math_color_blend.h",
    "source/blender/blenlib/BLI_math_geom.h",
    "source/blender/blenlib/BLI_math_inline.h",
    "source/blender/blenlib/BLI_math_interp.h",
    "source/blender/blenlib/BLI_math_matrix.h",
    "source/blender/blenlib/BLI_math_rotation.h",
    "source/blender/blenlib/BLI_math_solvers.h",
    "source/blender/blenlib/BLI_math_statistics.h",
    "source/blender/blenlib/BLI_math_vector.h",
    "source/blender/blenlib/BLI_strict_flags.h",
    "source/blender/blenlib/BLI_sys_types.h",
    "source/blender/blenlib/BLI_system.h",
    "source/blender/blenlib/BLI_utildefines.h",
    "source/blender/blenlib/intern/math_base.c",
    "source/blender/blenlib/intern/math_bits_inline.c",
    "source/blender/blenlib/intern/math_base_inline.c",
    "source/blender/blenlib/intern/math_color.c",
    "source/blender/blenlib/intern/math_color_blend_inline.c",
    "source/blender/blenlib/intern/math_color_inline.c",
    "source/blender/blenlib/intern/math_geom.c",
    "source/blender/blenlib/intern/math_geom_inline.c",
    "source/blender/blenlib/intern/math_interp.c",
    "source/blender/blenlib/intern/math_matrix.c",
    "source/blender/blenlib/intern/math_rotation.c",
    "source/blender/blenlib/intern/math_vector.c",
    "source/blender/blenlib/intern/math_vector_inline.c",
    )


# strip "source/blender/python"
files_pygeneric_level = 3
files_pygeneric_dest = "src"
files_pygeneric = (
    "source/blender/python/generic/py_capi_utils.c",
    "source/blender/python/generic/py_capi_utils.h",
    "source/blender/python/generic/python_utildefines.h",
    )


update_source(files_mathutils, files_mathutils_dest, files_mathutils_level)
update_source(files_blenlib, files_blenlib_dest, files_blenlib_level)
update_source(files_pygeneric, files_pygeneric_dest, files_pygeneric_level)

