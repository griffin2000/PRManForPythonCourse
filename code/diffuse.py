import prman

prman.Init()
ri = prman.Ri()
ri.Begin(ri.RENDER)
ri.Quantize("rgba", 255, 0, 255, 0.5)
ri.Exposure(1,1) 

ri.Hider("raytrace", {"int incremental":1, "int maxsamples":100, "int minsamples": 25})
ri.Integrator("PxrPathTracer", "ffo",
                   {"int numLightSamples": 4, "int numBxdfSamples": 4,
                    "int numIndirectSamples": 4, "int allowCaustics": 1})

ri.Display("Diffuse","windows","rgb")
ri.Projection("perspective")

ri.WorldBegin()


ri.AttributeBegin()

ri.Translate(0,0,4)
ri.AreaLightSource("PxrAreaLight", {"string shape":"sphere", "float intensity":4.0})

ri.AttributeBegin()
ri.Translate(-1,-1,0)
ri.Bxdf("PxrDiffuse","red",{"color diffuseColor":[ 1.0, 0.0, 0.0]})
ri.Sphere(1,-1,1,360)
ri.AttributeEnd()

ri.AttributeBegin()
ri.Translate(+1,-1,0)
ri.Bxdf("PxrDiffuse","green",{"color diffuseColor":[ 0.0, 1.0, 0.0]})
ri.Sphere(1,-1,1,360)
ri.AttributeEnd()

ri.AttributeBegin()
ri.Translate(0,+1,0)
ri.Bxdf("PxrDiffuse","blue",{"color diffuseColor":[ 0.0, 0.0, 1.0]})
ri.Sphere(1,-1,1,360)
ri.AttributeEnd()




ri.AttributeEnd()

ri.WorldEnd()

ri.End()
