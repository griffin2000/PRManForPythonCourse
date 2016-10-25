import prman

prman.Init()
ri = prman.Ri()
ri.Begin(ri.RENDER)


for frame in range(0, 10):
    xTranslation = (frame*0.1)-0.5
    ri.FrameBegin(frame)
    ri.Display("sphere.%0.3d.tiff"%frame, "tiff", "rgb")
    ri.Projection("perspective")
    ri.WorldBegin()
    ri.Translate(xTranslation,0,2)
    ri.Sphere(1,-1,1,360)
    ri.WorldEnd()
    ri.FrameEnd()

ri.End()
