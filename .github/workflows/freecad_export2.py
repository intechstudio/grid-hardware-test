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
  sono.ViewObject.show()

  # Ez kell ide
  FreeCADGui.updateGui()
  FreeCADGui.updateGui()
  FreeCADGui.updateGui()
  FreeCADGui.updateGui()
  FreeCADGui.updateGui()
  FreeCADGui.updateGui()

  if sono.TypeId == "PartDesign::Body":

    if "png" in export_list:
      print(obj.Label, obj.Name, "PNG")
      exportScreenshot(obj.Label, "temp/"+obj.Label+".png")

    if "step" in export_list:
      print(obj.Label, obj.Name, "STEP")

      sono.Shape.exportStep("temp/"+obj.Label+".step")

    if "stl" in export_list:
      print(obj.Label, obj.Name, "STL")
      sono.Shape.exportStl("temp/"+obj.Label+".stl")

  if sono.TypeId == "App::Part":
    print(obj.Label, obj.Name, "STEP")
    sono.Shape.exportStep("temp/"+obj.Label+".step")
    __objs__=[]
    __objs__.append(App.ActiveDocument.getObject(obj.Name))
    print(__objs__)
    import ImportGui
    ImportGui.export(__objs__,"temp/"+obj.Label+"2.step")

  elif sono.TypeId == "TechDraw::DrawPage":
    if "pdf" in export_list:
      print(obj.Label, obj.Name, "DRAW")
      TechDrawGui.export([sono],u"temp/"+obj.Label+".pdf")

  sono.ViewObject.hide()


hideAll()
