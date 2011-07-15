from distutils.core import setup, Extension

include_dirs = [
    "src/stubs",
    "src/blenlib",
    ]

source_files = [
    "src/stubs/stubs.c",

    "src/blenlib/intern/math_base.c",
    "src/blenlib/intern/math_base_inline.c",
    "src/blenlib/intern/math_color.c",
    "src/blenlib/intern/math_geom.c",
    "src/blenlib/intern/math_geom_inline.c",
    "src/blenlib/intern/math_matrix.c",
    "src/blenlib/intern/math_rotation.c",
    "src/blenlib/intern/math_vector.c",
    "src/blenlib/intern/math_vector_inline.c",

    "src/mathutils/mathutils.c",
    "src/mathutils/mathutils_Color.c",
    "src/mathutils/mathutils_Euler.c",
    "src/mathutils/mathutils_Matrix.c",
    "src/mathutils/mathutils_Quaternion.c",
    "src/mathutils/mathutils_Vector.c",
    "src/mathutils/mathutils_geometry.c",
    ]


setup(name="mathutils",
      version="2.58a",
      maintainer="Campbell Barton",
      maintainer_email="ideasman42@gmail.com",
      url="http://code.google.com/p/blender-mathutils",
      ext_modules=[Extension("mathutils",
                             source_files,
                             include_dirs=include_dirs,
                             define_macros=[("MATH_STANDALONE", None)]
                             )
                  ],
     )
