cmake_minimum_required(VERSION 2.6)

#find_package(Eigen2 REQUIRED)
#if(EIGEN2_FOUND)
#  INCLUDE_DIRECTORIES(${EIGEN2_INCLUDE_DIR})
#endif(EIGEN2_FOUND)
#if (CMAKE_COMPILER_IS_GNUCXX)
   #set ( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O2")
   #add_definitions ( "-DNDEBUG" )
#endif (CMAKE_COMPILER_IS_GNUCXX)

#set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O0 -ggdb")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3")

set(EIGEN2_INCLUDE_DIR "/usr/local/include/eigen3")
INCLUDE_DIRECTORIES(${EIGEN3_INCLUDE_DIR})

# Build a library to be imported as a python module.
set(WRAP_PYTHON TRUE CACHE BOOL "Build Python Wrapper")
if(WRAP_PYTHON)
	LINK_LIBRARIES(boost_python)
	INCLUDE_DIRECTORIES("/usr/include/python2.7")
	LINK_DIRECTORIES("/usr/lib/python2.7")
	ADD_LIBRARY(_FooClass SHARED example_wrapper.cpp)
	SET_TARGET_PROPERTIES(_FooClass PROPERTIES PREFIX "")	
#TARGET_LINK_LIBRARIES(_l1solver_e1x1 ${OPENCV_LIBRARIES})
endif(WRAP_PYTHON)