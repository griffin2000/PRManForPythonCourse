import prman

prman.Init()
ri = prman.Ri()
ri.Begin(ri.RENDER)

ri.Display("sphere.tiff","tiff","rgb")
ri.Projection("perspective")

ri.WorldBegin()
ri.Translate(0,0,2)
ri.Sphere(1,-1,1,360)
ri.WorldEnd()

ri.End()
