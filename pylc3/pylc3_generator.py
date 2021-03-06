#!/usr/bin/python
from pygccxml import parser
from pygccxml import declarations
from pyplusplus import module_builder

# Create configuration for CastXML
xml_generator_config = parser.xml_generator_configuration_t(
                                    xml_generator_path='/usr/bin/castxml',
                                    xml_generator='castxml',
                                    compiler='gnu',
                                    compiler_path='/usr/bin/gcc',
                                    cflags='-std=c++11 -I../liblc3 -I../lc3test')

# List of all the C++ header of our library
header_collection = ["PyLC3.hpp"]

# Parses the source files and creates a module_builder object
builder = module_builder.module_builder_t(
                        header_collection,
                        xml_generator_path='/usr/bin/castxml',
                        xml_generator_config=xml_generator_config)

# Automatically detect properties and associated getters/setters
builder.classes().add_properties(exclude_accessors=True)
builder.calldefs(declarations.access_type_matcher_t('protected')).exclude()
builder.calldefs(declarations.access_type_matcher_t('private')).exclude()

# Define a name for the module
builder.build_code_creator(module_name="pylc3")

# Writes the C++ interface file
builder.write_module('PyLC3Gen.cpp')
