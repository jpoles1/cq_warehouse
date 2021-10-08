import cadquery as cq
from cq_warehouse.fastener import SocketHeadCapScrew

height = 60.0
width = 80.0
thickness = 10.0
diameter = 22.0
padding = 12.0

# make the screw
screw = SocketHeadCapScrew(screw_type="iso4762", size="M2-0.4", length=16, simple=False)
# make the assembly
pillow_block = cq.Assembly(None, name="pillow_block")
# make the base
base = (
    cq.Workplane("XY")
    .box(height, width, thickness)
    .faces(">Z")
    .workplane()
    .hole(diameter)
    .faces(">Z")
    .workplane()
    .rect(height - padding, width - padding, forConstruction=True)
    .vertices()
    .clearanceHole(fastener=screw, baseAssembly=pillow_block)
    .edges("|Z")
    .fillet(2.0)
)
pillow_block.add(base, name="base", color=cq.Color(162 / 255, 138 / 255, 255 / 255))
# Render the assembly
show_object(pillow_block)