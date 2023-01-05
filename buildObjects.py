import unreal

multiplier = 21

with open("PATH TO OBJECTS .txt") as f:
    for line in f:
        if line.startswith("#"):
            continue
        else:
            trimLine = line.split(",")
            modelName = trimLine[0]
            posX = float(trimLine[1]) * multiplier
            posY = float(trimLine[2]) * -multiplier
            posZ = float(trimLine[3]) * multiplier
            rotX = float(trimLine[4])
            rotY = float(trimLine[5]) 
            rotZ = float(trimLine[6]) * -1
            scaleX = float(trimLine[7]) * multiplier
            scaleY = float(trimLine[8]) * multiplier
            scaleZ = float(trimLine[9]) * multiplier
            obj = unreal.load_asset(f'/Game/firiona/Objects/{modelName}.{modelName}')
            actor_location = unreal.Vector(posX,posY,posZ)
            actor_rotation = unreal.Rotator(rotX,rotY,rotZ)
            scale = unreal.Vector(scaleX,scaleY,scaleZ)
            spawned_actor = unreal.EditorLevelLibrary.spawn_actor_from_object(obj, actor_location, actor_rotation)
            try:
                spawned_actor.set_actor_relative_scale3d(scale)
            except:
                pass