# EQ-UE-Scripts
A few scripts I made to bring Everquest Zone objects and lights into the Unreal editor quickly.
I used a program called [Lantern Extractor](https://github.com/LanternEQ/LanternExtractor) that will export all of the information from an Everquest Zone.
Along with the individual zone assets it also exports several text files with location information for objects, lights, and I believe even sounds.

To use this script, you have to [enable Python in the Unreal editor](https://docs.unrealengine.com/4.27/en-US/ProductionPipelines/ScriptingAndAutomation/Python/). Edit the script to point to the text file related to the script (so for the light script, point to the light text file)
This script also has a multiplier setting. What I did was import the zone into the Unreal Editor and then change the scale to what I believed was the best size for my project. That scale number should be set to the multiplier in the script. 
I set my zone to a scale of 21 and that's why 21 is the default in the script. Feel free to change based on your own zone scaling. 
This will make sure the lights and props are the right size and in the right place.
