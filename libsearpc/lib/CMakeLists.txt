cmake_minimum_required(VERSION 3.20)

set(SEARPC_VERSION_MAJOR 3)
set(SEARPC_VERSION_MINOR 2)
set(SEARPC_VERSION_PATCH 0)
set(SEARPC_VERSION_STRING ${SEARPC_VERSION_MAJOR}.${SEARPC_VERSION_MINOR}.${SEARPC_VERSION_PATCH})

option(BUILD_SHARED "Build as shared library" OFF)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(SOURCES searpc-client.c searpc-server.c searpc-utils.c searpc-named-pipe-transport.c)

add_library(searpc_static STATIC ${SOURCES})
if(BUILD_SHARED)
add_library(searpc SHARED ${SOURCES})
endif()

add_definitions(-DG_LOG_DOMAIN="Searpc")

IF (APPLE)
SET_TARGET_PROPERTIES(searpc PROPERTIES LINK_FLAGS
"-undefined dynamic_lookup -flat_namespace")
ENDIF (APPLE)

file(GLOB_RECURSE HDRS *.h)

set_target_properties(searpc 
PROPERTIES VERSION ${SEARPC_VERSION_STRING} 
PUBLIC_HEADER "${HDRS}")

set_target_properties(searpc_static 
PROPERTIES OUTPUT_NAME searpc)

install(TARGETS searpc)

target_link_libraries(searpc PRIVATE ${CONAN_LIBS})