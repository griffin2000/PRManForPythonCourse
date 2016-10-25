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

ri.AreaLightSource("PxrAreaLight", {"string shape":"sphere", "float intensity":0.5})
ri.Translate(0,0,4)


d=2.0

ri.AttributeBegin()
ri.Translate(-d,-d,0)
ri.Bxdf("PxrDiffuse","red",{"color diffuseColor":[ 1.0, 0.0, 0.0]})
ri.Sphere(1,-1,1,360)
ri.AttributeEnd()

ri.AttributeBegin()
ri.Translate(+d,-d,0)
ri.Bxdf("PxrDiffuse","green",{"color diffuseColor":[ 0.0, 1.0, 0.0]})
ri.Sphere(1,-1,1,360)
ri.AttributeEnd()

ri.AttributeBegin()
ri.Translate(0,+d,0)
ri.Bxdf("PxrDiffuse","blue",{"color diffuseColor":[ 0.0, 0.0, 1.0]})
ri.Sphere(1,-1,1,360)
ri.AttributeEnd()

ri.AttributeBegin()
ri.Translate(0,0,-4)
ri.Bxdf("PxrDisney", "chrome", {"color baseColor": [1, 1, 1],
                                "float roughness": 0.2} )
nverts = [4, 4, 4, 4, 4, 4]
#Indices describing polygons
indices = [0, 1, 3, 2, 2, 3, 5, 4, 4, 5, 7, 6, 6, 7, 1, 0, 1, 7, 5, 3, 6, 0, 2, 4]
#Vertex data
bs=6.0
position = [-bs, -bs, bs, bs, -bs, bs, -bs, bs, bs, bs, bs, bs, -bs, bs, -bs, bs, bs, -bs, -bs, -bs, -bs, bs, -bs, -bs]
normal = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0]
texCoordS = [0.375, 0.625, 0.625, 0.375, 0.375, 0.625, 0.625, 0.375, 0.375, 0.625, 0.625, 0.375, 0.375, 0.625, 0.625, 0.375, 0.625, 0.875, 0.875, 0.625, 0.125, 0.375, 0.375, 0.125]
texCoordT = [0, 0, 0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.75, 0.75, 0.75, 1, 1, 0, 0, 0.25, 0.25, 0, 0, 0.25, 0.25]
vertexData = {ri.P: position, "facevarying normal N": normal, "facevarying float s": texCoordS, "facevarying float t": texCoordT}

ri.PointsPolygons(nverts,indices,vertexData)
ri.AttributeEnd()



ri.AttributeEnd()

ri.WorldEnd()

ri.End()
