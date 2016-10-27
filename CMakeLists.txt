
# avoid having empty buildtype
set(CMAKE_BUILD_TYPE_INIT Release)

set_property(DIRECTORY APPEND PROPERTY COMPILE_DEFINITIONS
	$<$<CONFIG:Debug>:DEBUG;_DEBUG>
	$<$<CONFIG:Release>:NDEBUG>
	$<$<CONFIG:MinSizeRel>:NDEBUG>
	$<$<CONFIG:RelWithDebInfo>:NDEBUG>
)

cmake_policy(SET CMP0003 NEW)
cmake_policy(SET CMP0005 NEW)

cmake_minimum_required(VERSION 2.8)

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/bin CACHE INTERNAL "" FORCE )
set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR}/lib CACHE INTERNAL "" FORCE )

# needed for python lib
if(CMAKE_COMPILER_IS_GNUCC)
	set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIC -funsigned-char")
endif()

if(MSVC)
	set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} /J")
endif()


# -----------------------------------------------------------------------------
# configure python

if(NOT DEFINED PYTHON_ROOT_DIR)
	execute_process(
		COMMAND python3 -c "from distutils.sysconfig import PREFIX; print(PREFIX)"
		OUTPUT_VARIABLE _prefix
		OUTPUT_STRIP_TRAILING_WHITESPACE
	)
	set(PYTHON_ROOT_DIR "${_prefix}" CACHE PATH INTERNAL)
	unset(_prefix)
endif()

if(NOT DEFINED PYTHON_SITE_PACKAGES)
	execute_process(
		COMMAND python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"
		OUTPUT_VARIABLE _site_packages
		OUTPUT_STRIP_TRAILING_WHITESPACE
	)
	set(PYTHON_SITE_PACKAGES "${_site_packages}" CACHE PATH INTERNAL)
	unset(_site_packages)
endif()

if(NOT DEFINED PYTHON_INCLUDE_DIR)
	execute_process(
		COMMAND python3 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc(plat_specific=1))"
		OUTPUT_VARIABLE _inc_dir
		OUTPUT_STRIP_TRAILING_WHITESPACE
	)
	set(PYTHON_INCLUDE_DIR "${_inc_dir}" CACHE PATH INTERNAL)
	unset(_inc_dir)
endif()

# set standard cmake/python names, uncached
set(PYTHON_INCLUDE_DIRS "${PYTHON_INCLUDE_DIR}")


# -----------------------------------------------------------------------------
# stubs

# needed so we don't attempt to do clever back-trace
# (not included in stand-alone version).
add_definitions(-DWITH_ASSERT_ABORT)

set(SRC
	src/stubs/stubs.c

	src/stubs/BLI_memarena.h
	src/stubs/MEM_guardedalloc.h
	src/stubs/MEM_sys_types.h
)

include_directories(
	src/stubs
)

add_library(stubs_lib ${SRC})

# -----------------------------------------------------------------------------
# blenlib

add_definitions(-DMATH_STANDALONE)

set(SRC
	src/blenlib/intern/math_base.c
	src/blenlib/intern/math_base_inline.c
	src/blenlib/intern/math_bits_inline.c
	src/blenlib/intern/math_color.c
	src/blenlib/intern/math_geom.c
	src/blenlib/intern/math_geom_inline.c
	src/blenlib/intern/math_matrix.c
	src/blenlib/intern/math_rotation.c
	src/blenlib/intern/math_vector.c
	src/blenlib/intern/math_vector_inline.c

	src/blenlib/BLI_compiler_attrs.h
	src/blenlib/BLI_compiler_compat.h
	src/blenlib/BLI_dynstr.h
	src/blenlib/BLI_math.h
	src/blenlib/BLI_math_base.h
	src/blenlib/BLI_math_bits.h
	src/blenlib/BLI_math_color.h
	src/blenlib/BLI_math_color_blend.h
	src/blenlib/BLI_math_geom.h
	src/blenlib/BLI_math_inline.h
	src/blenlib/BLI_math_interp.h
	src/blenlib/BLI_math_matrix.h
	src/blenlib/BLI_math_rotation.h
	src/blenlib/BLI_math_solvers.h
	src/blenlib/BLI_math_vector.h
	src/blenlib/BLI_strict_flags.h
	src/blenlib/BLI_sys_types.h
	src/blenlib/BLI_utildefines.h
)

include_directories(
	src/blenlib
)

include_directories(
    SYSTEM
	${PYTHON_INCLUDE_DIRS}
)

add_library(blenlib_lib ${SRC})


# -----------------------------------------------------------------------------
# mathutils

set(SRC
	src/mathutils/mathutils.c
	src/mathutils/mathutils_Color.c
	src/mathutils/mathutils_Euler.c
	src/mathutils/mathutils_Matrix.c
	src/mathutils/mathutils_Quaternion.c
	src/mathutils/mathutils_Vector.c
	src/mathutils/mathutils_geometry.c
	src/mathutils/mathutils_interpolate.c

	src/mathutils/mathutils.h
	src/mathutils/mathutils_Color.h
	src/mathutils/mathutils_Euler.h
	src/mathutils/mathutils_Matrix.h
	src/mathutils/mathutils_Quaternion.h
	src/mathutils/mathutils_Vector.h
	src/mathutils/mathutils_geometry.h
	src/mathutils/mathutils_interpolate.h

	src/generic/py_capi_utils.c
	src/generic/py_capi_utils.h
	src/generic/python_utildefines.h
)

include_directories(
	src/mathutils
)

# see stubs.c
if(CMAKE_COMPILER_IS_GNUCC)
	set_source_files_properties(${SRC}
		PROPERTIES
		COMPILE_FLAGS
		  "-DMEM_mallocN=_poison -DMEM_callocN=_poison -DMEM_freeN=_poison -DBLI_memarena_alloc=_poison"
	)
endif()


# -----------------------------------------------------------------------------
# python module

add_library(mathutils_module SHARED ${SRC})

set_target_properties(
	mathutils_module
	PROPERTIES
		PREFIX ""
		OUTPUT_NAME mathutils
		LINKER_LANGUAGE C
		LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
		RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin  # only needed on windows
)

if(WIN32)
	# python modules use this
	set_target_properties(
		mathutils_module
		PROPERTIES
		SUFFIX ".pyd"
	)	
endif()

# link
target_link_libraries(mathutils_module
	blenlib_lib
	stubs_lib
)

# -----------------------------------------------------------------------------
# installation

install(
	TARGETS mathutils_module
	LIBRARY
	DESTINATION
		"${PYTHON_SITE_PACKAGES}"
)
