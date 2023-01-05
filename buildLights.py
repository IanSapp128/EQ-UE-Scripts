import unreal

multiplier = 21

with open("PATH TO LIGHTS .txt") as f:
    for line in f:
        if line.startswith("#"):
            continue
        else:
            trimLine = line.split(",")
            posX = float(trimLine[0]) * multiplier
            posY = float(trimLine[1]) * -multiplier
            posZ = float(trimLine[2]) * multiplier
            radius = float(trimLine[3]) * multiplier
            colorR = float(trimLine[4])
            colorG = float(trimLine[5])
            colorB = float(trimLine[6])

            obj = unreal.PointLight()

            actor_location = unreal.Vector(posX,posY,posZ)
            actor_rotation = unreal.Rotator(0,0,0)
            spawned_actor = unreal.EditorLevelLibrary.spawn_actor_from_object(obj, actor_location, actor_rotation)
            lightComp = spawned_actor.light_component
            linearColor = unreal.LinearColor(colorR, colorG, colorB, 1.0)
            color = linearColor.quantize()
            lightComp.set_editor_property("attenuation_radius", radius)
            lightComp.set_editor_property("light_color", color)
            lightComp.set_editor_property("cast_shadows", False)