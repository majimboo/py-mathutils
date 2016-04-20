
Blender-Mathutils
*****************


Overview
========

This module originated from Blender (the opens-source 3d package),
where it has been used for some years in production as a utility module for use in areas including animation,
games and mesh manipulation.

This differs from ``numpy`` in that it is computer graphics focused,
combining Matrix and Vector types with rotation classes which is very useful
for use with animation or anywhere ``Euler`` and ``Quaternion`` values are used frequently.

This project is mainly a build system around the actively maintained ``mathutils`` code in
Blender to allow non Blender related projects to make use of it.

A link to the Blender repository is used so the source never gets out of sync.


``mathutils`` at a glance
=========================

- ``mathutils`` module, with classes: ``Matrix``, ``Vector``, ``Quaternion``, ``Euler`` and ``Color``.
- ``mathutils.geometry`` module for useful functions such as
  ``intersect_ray_tri``, ``intersect_line_line`` and ``area_tri``.
- Supports operations you'd expect, slicing, multiplication, comparison, division addition where applicable.
- Supports swizzle style access on vectors: `v.xyz, v.zy, v.xxyz...` etc.


Important Details
=================

- Python 3 only
- Written in portable C
- Extensible...

  | mathutils types can be sub-classed from python.
  | C/C++ code can have mathutils objects synchronize with internal data using callbacks, or wrap the data directly.
- Documentation here

  | http://www.blender.org/documentation/blender_python_api_current/mathutils.html
- GPLv2 or later since this is apart of the Blender project.


Building
========

To build on unix like systems...

.. code-block:: sh

   git clone https://gitlab.com/ideasman42/blender-mathutils.git
   cd blender-mathutils

To build you can choose between pythons distutils or CMake.

**distutils:**

.. code-block:: sh

   python setup.py build
   sudo python setup.py install

**CMake:**

.. code-block:: sh

   cmake .
   make
   sudo make install

