import prman

prman.Init()
ri = prman.Ri()
ri.Begin(ri.RENDER)

ri.Display("translation.tiff","tiff","rgb")
ri.Projection("perspective")

ri.WorldBegin()

ri.AttributeBegin()
ri.Translate(0,0,4)

ri.TransformBegin()
ri.Translate(-1,-1,0)
ri.Sphere(1,-1,1,360)
ri.TransformEnd()

ri.TransformBegin()
ri.Translate(+1,-1,0)
ri.Sphere(1,-1,1,360)
ri.TransformEnd()

ri.TransformBegin()
ri.Translate(0,+1,0)
ri.Sphere(1,-1,1,360)
ri.TransformEnd()

ri.AttributeEnd()

ri.WorldEnd()

ri.End()
