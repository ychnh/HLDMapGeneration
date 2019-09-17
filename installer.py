import os
from os.path import dirname

OS = 'WIN'

# common/HyperLightDrifter/HyperLightDrifter.app/Contents/Resources
mod_dir = os.getcwd()
common_dir = dirname(os.getcwd())


if OS == 'MAC':
  
elif OS == 'WIN':
    rsc_path = os.path.join(common_dir,'HyperLightDrifter')


