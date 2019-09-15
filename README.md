# HLDMapGeneration
Hyper Light Drifter Modding

# Installation Guide
1. Replace original game contents with the files in the "Files to replace folder".
2. Place the mapgen.py and mapgenTemplate.txt into the directory with .exe file or the .app file.
3. Run the python script (and leave it running) and start a new game. Take the first elevator down in the tutorial to start the mod.
4. Collect healthpacks, gearbits, outfits, weapons to upgrade your character as you progress

# Notes
A new level is generated everytime you leave the map.
 Because I am not deallocating resources after they die, the game will get a bit laggy after 5-8 regeneration of the map. (On my crappy computer at least)
 Just restart the hyper light drifter game and it should be fine.

The game gets more difficult the more you play. If the game is getting too difficult, restart the python script. The difficulty will reset.

# Future
* UI Custom overlay
* https://github.com/dzen/pyosd
* Move to different planets after exiting game and starting new
* Generate planets randomly with GANs


# Goals 
* python 3 convert
* understand parameters and events
* rewrite random gen into localized
# Windows Installation
* http://www.python.org/download/windows/
