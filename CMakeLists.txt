project(opendbc)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/cmake/")

# # Generate service header
# # TODO: make this into an actual target to enable propagation of the include dir
# add_custom_command(OUTPUT services.h
#     DEPENDS services.py service_list.yaml
#     COMMAND python3 "${CMAKE_CURRENT_SOURCE_DIR}/services.py" > "services.h"
#     WORKING_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}"
# )


# Import('env', 'envCython', 'cereal')

# import os
# from opendbc.can.process_dbc import process

# dbcs = []
# for x in sorted(os.listdir('../')):
#   if x.endswith(".dbc"):
#     def compile_dbc(target, source, env):
#       process(source[0].path, target[0].path)
#     in_fn = [os.path.join('../', x), 'dbc_template.cc']
#     out_fn = os.path.join('dbc_out', x.replace(".dbc", ".cc"))
#     dbc = env.Command(out_fn, in_fn, compile_dbc)
#     dbcs.append(dbc)

# libdbc = env.SharedLibrary('libdbc', ["dbc.cc", "parser.cc", "packer.cc", "common.cc"]+dbcs, LIBS=["capnp", "kj"])

# Loop through and generate dbc defs
set(DBC_GENDIR "${CMAKE_CURRENT_BINARY_DIR}/dbc-out")
file(MAKE_DIRECTORY ${DBC_GENDIR})
file(GLOB SRC_DBCS dbcs/*.dbc)
foreach(CURR_DBC ${SRC_DBCS})
    get_filename_component(CURR_DBC_NAME ${CURR_DBC}  NAME_WLE)
    set(CURR_DBC_OUTPUT "${DBC_GENDIR}/${CURR_DBC_NAME}.cc")
    list(APPEND SRC_DBCS_OUT ${CURR_DBC_OUTPUT})

    add_custom_command(OUTPUT ${CURR_DBC_OUTPUT}
        COMMAND python3 -B can/process_dbc.py "${CURR_DBC}" "${CURR_DBC_OUTPUT}"
        WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
    )
endforeach(CURR_DBC)

add_library(opendbc-libdbc SHARED
    can/common.cc
    can/dbc.cc
    can/packer.cc
    can/parser.cc
    ${SRC_DBCS_OUT}
)
target_link_libraries(opendbc-libdbc cereal-objects)
target_include_directories(opendbc-libdbc PRIVATE ./can)

add_subdirectory(can)
