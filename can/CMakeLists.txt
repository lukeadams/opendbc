
# parser
add_cython_target(parser_pyx
    parser_pyx.pyx CXX PY3
)
add_library(parser_pyx MODULE ${parser_pyx})
target_link_libraries(parser_pyx Python::Python opendbc-libdbc)
target_include_directories(parser_pyx PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})
set_target_properties(parser_pyx PROPERTIES PREFIX "")


# packer 
add_cython_target(packer_pyx
    packer_pyx.pyx CXX PY3
)
add_library(packer_pyx MODULE ${packer_pyx})
target_link_libraries(packer_pyx Python::Python opendbc-libdbc)
target_include_directories(packer_pyx PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})
set_target_properties(packer_pyx PROPERTIES PREFIX "")
