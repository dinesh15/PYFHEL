# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license.

FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG        e2239ee6043f73722e7aa812a459f54a28552929 # 1.11.0
)
FetchContent_GetProperties(googletest)

if(NOT googletest_POPULATED)
    FetchContent_Populate(googletest)

    set(BUILD_GMOCK OFF CACHE BOOL "" FORCE)
    set(INSTALL_GTEST OFF CACHE BOOL "" FORCE)
    set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
    mark_as_advanced(BUILD_GMOCK)
    mark_as_advanced(INSTALL_GTEST)
    mark_as_advanced(FETCHCONTENT_SOURCE_DIR_GOOGLETEST)
    mark_as_advanced(FETCHCONTENT_UPDATES_DISCONNECTED_GOOGLETEST)

    add_subdirectory(
        ${googletest_SOURCE_DIR}
        ${THIRDPARTY_BINARY_DIR}/googletest-src
        EXCLUDE_FROM_ALL)
endif()
