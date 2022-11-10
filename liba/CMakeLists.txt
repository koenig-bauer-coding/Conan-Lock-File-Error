# Author: Philipp Jeske <philipp.jeske@koenig-bauer.com>
# Copyright 2022 Koenig & Bauer Coding GmbH
#
# SPDX-License-Identifier: MIT

set(component LibA)

add_library(${component} "")
add_library(${PROJECT_NAME}::${component} ALIAS ${component})

add_subdirectory(include/liba)
add_subdirectory(src)

target_include_directories(${component}
   PUBLIC
      $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
      $<INSTALL_INTERFACE:include>
)

install(TARGETS ${component} EXPORT ${component}-targets
  COMPONENT ${component}
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
  INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

install(EXPORT ${component}-targets
  FILE "${PROJECT_NAME}-${component}-targets.cmake"
  NAMESPACE ${PROJECT_NAME}::
  DESTINATION ${CMAKE_INSTALL_LIBDIR}/liba/cmake
  COMPONENT ${component}
)

install(
  DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include
  COMPONENT ${component}
  DESTINATION ${CMAKE_INSTALL_PREFIX}
)