import prman

prman.Init()
ri = prman.Ri()
ri.Begin(ri.RENDER)

ri.Display("polygon.tiff","tiff","rgb")
ri.Projection("perspective")

ri.WorldBegin()
ri.Translate(0,0,3)
ri.Rotate(45,0,1,0)

#Vertex count for each polygon
nverts = [4, 4, 4, 4, 4, 4]
#Indices describing polygons
indices = [0, 1, 3, 2, 2, 3, 5, 4, 4, 5, 7, 6, 6, 7, 1, 0, 1, 7, 5, 3, 6, 0, 2, 4]
#Vertex data
position = [-1.0, -1.0, 1.0, 1.0, -1.0, 1.0, -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0, 1.0, -1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0]
normal = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0]
texCoordS = [0.375, 0.625, 0.625, 0.375, 0.375, 0.625, 0.625, 0.375, 0.375, 0.625, 0.625, 0.375, 0.375, 0.625, 0.625, 0.375, 0.625, 0.875, 0.875, 0.625, 0.125, 0.375, 0.375, 0.125]
texCoordT = [0, 0, 0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.75, 0.75, 0.75, 1, 1, 0, 0, 0.25, 0.25, 0, 0, 0.25, 0.25]
vertexData = {ri.P: position, "facevarying normal N": normal, "facevarying float s": texCoordS, "facevarying float t": texCoordT}

ri.PointsPolygons(nverts,indices,vertexData)

ri.WorldEnd()

ri.End()
