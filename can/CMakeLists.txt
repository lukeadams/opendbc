

# # Build packer and parser
# lenv = envCython.Clone()
# lenv["LINKFLAGS"] += [libdbc[0].get_labspath()]
# lenv.Program('parser_pyx.so', 'parser_pyx.pyx')
# lenv.Program('packer_pyx.so', 'packer_pyx.pyx')


# parser
add_cython_target(opendbc-parser-pyx
    parser_pyx.pyx CXX PY3
)
add_library(opendbc-parser-pyx ${opendbc-parser-pyx})
target_link_libraries(opendbc-parser-pyx Python::Python opendbc-libdbc)
target_include_directories(opendbc-parser-pyx PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

# packer 
add_cython_target(opendbc-packer-pyx
    packer_pyx.pyx CXX PY3
)
add_library(opendbc-packer-pyx ${opendbc-packer-pyx})
target_link_libraries(opendbc-packer-pyx Python::Python opendbc-libdbc)
target_include_directories(opendbc-packer-pyx PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

