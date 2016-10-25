import prman

prman.Init()
ri = prman.Ri()
ri.Begin(ri.RENDER)

ri.Display("polygon.tiff","tiff","rgb")
ri.Projection("perspective")

ri.WorldBegin()
ri.Translate(0,0,2)
ri.Polygon({ri.P: [-0.5,-0.5,0, 0.5, -0.5, 0,    0.5, 0.5, 0,   -0.5, 0.5, 0]})

ri.WorldEnd()

ri.End()
