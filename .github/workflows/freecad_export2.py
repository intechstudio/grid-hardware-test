import FreeCAD

import Part


import os 
if os.path.isdir("temp"):
  print("Directory already exists")
else:
  os.mkdir("temp")

App.openDocument("Mechanical/Design/PCBA-ENDLESSPOT/PCBA-ENDLESSPOT.FCStd")

objs = App.ActiveDocument.Objects
for obj in objs:
  sono=App.ActiveDocument.getObject(obj.Name)

  if sono.TypeId == "App::Part":
    print(obj.Label, obj.Name, "STEP")
    sono.Shape.exportStep("temp/"+obj.Label+".step")
    __objs__=[]
    __objs__.append(App.ActiveDocument.getObject(obj.Name))
    print(__objs__)
    import ImportGui
    ImportGui.export(__objs__,"temp/"+obj.Label+"2.step")
