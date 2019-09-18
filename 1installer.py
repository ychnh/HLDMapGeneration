import os
import time
from os.path import dirname
from os.path import join
import util
from shutil import copyfile

OS = 'WIN'

def install():
  mod_dir = os.getcwd()
  common_dir = dirname(os.getcwd())
  rsc_installer = join(mod_dir,'rsc','installer','WIN_replace')
  
  def get_game_folder(common_dir):
    candidates = os.listdir(common_dir)
    candidates = [join(common_dir,cand) for cand in candidates]
    for cand in candidates:
      cand_content = os.listdir(cand)
      cand_content = [f.lower() for f in cand_content]
      if 'AMB_North.ogg'.lower() in cand_content:
        return cand
    raise Exception('Game Folder not found in the directory where the Mod Folder is.')
  
  
  
  if OS == 'MAC':
    #rsc_game common/HyperLightDrifter/HyperLightDrifter.app/Contents/Resources
    donothing=1
  elif OS == 'WIN':
    #rsc_game = os.path.join(common_dir,'HyperLightDrifter')
    rsc_game = get_game_folder(common_dir)
    print(rsc_game)
    replace_dir = join(rsc_installer,'WIN_replace')
    replace_pairs = [('rm_c_backertabletx.lvl','rm_C_BackerTabletX.lvl','central','Central')]
    replace_pairs += [('rm_in_01_brokenshallows.lvl','rm_IN_01_brokenshallows.lvl','intro','Intro')]
    copy_pairs = [('rm_wc_minilab_layer0_sketch.png','west','West')]
    copy_pairs += [('rm_wc_minilab_layer1_sketch.png','west','West')]
    copy_pairs += [('rm_wc_minilab_layer1_sketch_baked.png','west','West')]
    copy_pairs += [('rm_wc_minilab_layer1_sketch_invfloor_baked.png','west','West')]
    copy_pairs += [('rm_wc_minilab_layer2_sketch.png','west','West')]
    copy_pairs += [('phrases.txt', '', '')]
  
  for filename, filename_dest, rsc_dir_src, rsc_dir_dest in replace_pairs:
    file_src = join(rsc_installer,rsc_dir_src, filename)
    file_dest = join(rsc_game,rsc_dir_dest, filename_dest)
    util.replace_file(file_src, file_dest)
      
  for filename, rsc_dir_src, rsc_dir_dest in copy_pairs:
    
    file_src = join(rsc_installer,rsc_dir_src, filename)
    file_dest = join(rsc_game,rsc_dir_dest, filename)
    copyfile(file_src, file_dest)
  
  print('Installation Complete')  
  time.sleep(10)



try:
  install()
except Exception as ex:
  print(ex)
  time.sleep(100)
