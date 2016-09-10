cmake_minimum_required(VERSION 2.8.11)
include(ExternalProject)

set(PROJECTNAME examples)
project(${PROJECTNAME})

# Copyright: (C) 2014 Walkman Consortium
# Authors: Enrico Mingo, Alessio Rocchi
# CopyPolicy: Released under the terms of the GNU GPL v2.0.

cmake_minimum_required(VERSION 2.8.12)
if(COMMAND cmake_policy)
    cmake_policy(SET CMP0003 OLD)
    cmake_policy(SET CMP0005 NEW)
    cmake_policy(SET CMP0017 NEW)
endif(COMMAND cmake_policy)
include(ExternalProject)
# PROJECT(OpenSoT)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake/Modules/")

# FIND_PACKAGE(Boost REQUIRED COMPONENTS filesystem)
# FIND_PACKAGE(iDynTree REQUIRED)
# FIND_PACKAGE(idynutils REQUIRED)
# FIND_PACKAGE(Klampt QUIET)
# FIND_PACKAGE(tf REQUIRED)
# FIND_PACKAGE(YARP REQUIRED)

# add include directories
# INCLUDE_DIRECTORIES(. include ${YARP_INCLUDE_DIRS} ${iDynTree_INCLUDE_DIRS})

# include_directories("${qpOASES_INCLUDE_DIRS}")

# ADD_EXECUTABLE(klampt_controller main.cpp)

ADD_LIBRARY(test_dany test_dany_code.c)
#                                       example_klampt_controller.h
#                                       src/KlamptController.cpp
#                                       include/KlamptController.h
#                                       include/utils.h)

# ADD_DEPENDENCIES(example_klampt_controller OpenSoT)
# ADD_DEPENDENCIES(klampt_controller example_klampt_controller)

# TARGET_LINK_LIBRARIES(test_dany PUBLIC OpenSoT ${idynutils_LIBRARIES} ${Boost_LIBRARIES})

# TARGET_LINK_LIBRARIES(test_dany_file         PUBLIC test_dany)

install(TARGETS test_dany DESTINATION lib)

find_package(SWIG)
if(SWIG_FOUND)
    include(UseSWIG)

    set_source_files_properties(Test_interface_dany.i PROPERTIES CPLUSPLUS ON)

    include_directories(. include)
    link_libraries(test_dany)

    set(CMAKE_SWIG_FLAGS "-Wall;-module;Exampletest_dany;-threads")

        set(OPENSOT_USES_PYTHON_VERSION "" CACHE STRING "Specify python version to use" )

        find_package(PythonInterp ${OPENSOT_USES_PYTHON_VERSION} REQUIRED)
        set(OPENSOT_USES_PYTHON_VERSION_ARGS)
        if(NOT OPENSOT_USES_PYTHON_VERSION)
          set (OPENSOT_USES_PYTHON_VERSION ${PYTHON_VERSION_STRING})
        endif()

        find_package(PythonLibs ${OPENSOT_USES_PYTHON_VERSION} EXACT)
        include_directories(${PYTHON_INCLUDE_PATH})
        link_libraries(${PYTHON_LIBRARY})

        set(target_name Exampletest_dany)

        swig_add_module(${target_name} python Test_interface_dany.i)
        set_target_properties(_${target_name} PROPERTIES OUTPUT_NAME "_Exampletest_dany")
        set_target_properties(_${target_name} PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib/python)

        # installation path is determined reliably on most platforms using distutils
        execute_process(COMMAND ${PYTHON_EXECUTABLE}
            -c "from distutils import sysconfig; print(sysconfig.get_python_lib(1,0,prefix=''))"
        OUTPUT_VARIABLE PYTHON_INSTDIR OUTPUT_STRIP_TRAILING_WHITESPACE )
        install(FILES ${CMAKE_CURRENT_BINARY_DIR}/test_dany.py DESTINATION ${PYTHON_INSTDIR} )
        install(TARGETS _${target_name} DESTINATION ${PYTHON_INSTDIR} )

endif(SWIG_FOUND)