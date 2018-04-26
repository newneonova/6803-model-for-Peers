import cobra
import cobra.test
import os
from os.path import join

model = cobra.io.read_sbml_model('mmc12.xml')
cobra.io.save_json_model(model,'mmc12.json')
