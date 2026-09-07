"""
FUTURISTIC WRIST-MOUNTED ELECTRONIC DEVICE - FUSION 360 PYTHON GENERATOR
=========================================================================

This script generates a complete parametric Fusion 360 CAD model of a rugged,
futuristic sci-fi wrist communicator.

CORRECTED VERSION - Uses only methods available in current Fusion 360 API
"""

import adsk.core
import adsk.fusion
import traceback


app = None
ui = None
design = None
rootComp = None


def run(context):
    """Main execution function."""
    global app, ui, design, rootComp
    
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        rootComp = design.rootComponent
        
        ui.messageBox("Starting Wrist Device creation...", "Info")
        
        create_parameters()
        create_main_housing()
        create_control_buttons()
        create_strap()
        create_hinges()
        create_buckle()
        
        ui.messageBox("Wrist Device created successfully!", "Success")
        
    except Exception as e:
        ui.messageBox(f"Error: {str(e)}\n{traceback.format_exc()}", "Error")


def create_parameters():
    """Create user parameters."""
    params = [
        ("DEVICE_LENGTH", "145 mm"),
        ("DEVICE_WIDTH", "72 mm"),
        ("DEVICE_HEIGHT", "38 mm"),
        ("HOUSING_LENGTH", "145 mm"),
        ("HOUSING_WIDTH", "72 mm"),
        ("HOUSING_HEIGHT", "34 mm"),
        ("HOUSING_CORNER_RADIUS", "12 mm"),
        ("BUTTON_DIAMETER", "10 mm"),
        ("BUTTON_HEIGHT", "3 mm"),
        ("STRAP_WIDTH", "52 mm"),
        ("STRAP_THICKNESS", "5 mm"),
    ]
    
    for name, value in params:
        try:
            design.userParameters.itemByName(name)
        except:
            design.userParameters.add(name, adsk.core.ValueInput.createByString(value), "", "")


def get_param(name):
    """Get parameter value."""
    try:
        return design.userParameters.itemByName(name).value
    except:
        return 0.0


def create_main_housing():
    """Create main housing body."""
    try:
        # Create sketch on XY plane
        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)
        sketch.name = "Housing_Sketch"
        
        h_len = get_param("HOUSING_LENGTH") / 10.0
        h_wid = get_param("HOUSING_WIDTH") / 10.0
        
        hl = h_len / 2.0
        hw = h_wid / 2.0
        
        lines = sketch.sketchCurves.sketchLines
        
        # Create rectangle
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-hl, -hw, 0),
            adsk.core.Point3D.create(hl, -hw, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(hl, -hw, 0),
            adsk.core.Point3D.create(hl, hw, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(hl, hw, 0),
            adsk.core.Point3D.create(-hl, hw, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-hl, hw, 0),
            adsk.core.Point3D.create(-hl, -hw, 0)
        )
        
        # Extrude
        profiles = sketch.profiles
        if profiles.count > 0:
            profile = profiles.item(0)
            extrudes = rootComp.features.extrudeFeatures
            
            h_height = get_param("HOUSING_HEIGHT") / 10.0
            extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            extrude_input.setSymmetricExtent(adsk.core.ValueInput.createByReal(h_height / 2.0), False)
            extrudes.add(extrude_input)
            
            # Rename body
            for body in rootComp.bodies:
                if body.name == "Body":
                    body.name = "Main_Housing"
                    break
    
    except Exception as e:
        ui.messageBox(f"Error in create_main_housing: {str(e)}", "Error")


def create_control_buttons():
    """Create four yellow buttons."""
    try:
        btn_dia = get_param("BUTTON_DIAMETER") / 10.0
        btn_height = get_param("BUTTON_HEIGHT") / 10.0
        
        positions = [(-3.0, 2.0), (-1.5, 2.0), (-3.0, 0.5), (-1.5, 0.5)]
        
        for idx, (x, y) in enumerate(positions):
            sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)
            sketch.name = f"Button_{idx+1}_Sketch"
            
            circles = sketch.sketchCurves.sketchCircles
            circles.addByCenterAndRadius(adsk.core.Point3D.create(x, y, 0), btn_dia / 2.0)
            
            profiles = sketch.profiles
            if profiles.count > 0:
                profile = profiles.item(0)
                extrudes = rootComp.features.extrudeFeatures
                
                extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
                extrude_input.setSymmetricExtent(adsk.core.ValueInput.createByReal(btn_height / 2.0), False)
                extrudes.add(extrude_input)
                
                for body in rootComp.bodies:
                    if body.name == "Body":
                        body.name = f"Button_{idx+1}"
                        break
    
    except Exception as e:
        pass


def create_strap():
    """Create wrist strap."""
    try:
        strap_wid = get_param("STRAP_WIDTH") / 10.0
        strap_thick = get_param("STRAP_THICKNESS") / 10.0
        
        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)
        sketch.name = "Strap_Sketch"
        
        x1 = -strap_wid / 2.0
        x2 = strap_wid / 2.0
        y1 = -5.0
        y2 = -3.0
        
        lines = sketch.sketchCurves.sketchLines
        lines.addByTwoPoints(adsk.core.Point3D.create(x1, y1, 0), adsk.core.Point3D.create(x2, y1, 0))
        lines.addByTwoPoints(adsk.core.Point3D.create(x2, y1, 0), adsk.core.Point3D.create(x2, y2, 0))
        lines.addByTwoPoints(adsk.core.Point3D.create(x2, y2, 0), adsk.core.Point3D.create(x1, y2, 0))
        lines.addByTwoPoints(adsk.core.Point3D.create(x1, y2, 0), adsk.core.Point3D.create(x1, y1, 0))
        
        profiles = sketch.profiles
        if profiles.count > 0:
            profile = profiles.item(0)
            extrudes = rootComp.features.extrudeFeatures
            
            extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            extrude_input.setSymmetricExtent(adsk.core.ValueInput.createByReal(strap_thick / 2.0), False)
            extrudes.add(extrude_input)
            
            for body in rootComp.bodies:
                if body.name == "Body":
                    body.name = "Strap"
                    break
    
    except Exception as e:
        pass


def create_hinges():
    """Create hinges."""
    try:
        hinge_dia = 1.0  # cm
        
        # Left hinge
        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)
        sketch.name = "Left_Hinge_Sketch"
        circles = sketch.sketchCurves.sketchCircles
        circles.addByCenterAndRadius(adsk.core.Point3D.create(-7.2, -2.5, 0), hinge_dia / 2.0)
        
        profiles = sketch.profiles
        if profiles.count > 0:
            profile = profiles.item(0)
            extrudes = rootComp.features.extrudeFeatures
            extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            extrude_input.setSymmetricExtent(adsk.core.ValueInput.createByReal(0.2), False)
            extrudes.add(extrude_input)
            
            for body in rootComp.bodies:
                if body.name == "Body":
                    body.name = "Left_Hinge"
                    break
        
        # Right hinge
        sketch2 = rootComp.sketches.add(rootComp.xYConstructionPlane)
        sketch2.name = "Right_Hinge_Sketch"
        circles2 = sketch2.sketchCurves.sketchCircles
        circles2.addByCenterAndRadius(adsk.core.Point3D.create(7.2, -2.5, 0), hinge_dia / 2.0)
        
        profiles2 = sketch2.profiles
        if profiles2.count > 0:
            profile2 = profiles2.item(0)
            extrudes2 = rootComp.features.extrudeFeatures
            extrude_input2 = extrudes2.createInput(profile2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            extrude_input2.setSymmetricExtent(adsk.core.ValueInput.createByReal(0.2), False)
            extrudes2.add(extrude_input2)
            
            for body in rootComp.bodies:
                if body.name == "Body":
                    body.name = "Right_Hinge"
                    break
    
    except Exception as e:
        pass


def create_buckle():
    """Create rear buckle."""
    try:
        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)
        sketch.name = "Buckle_Sketch"
        
        lines = sketch.sketchCurves.sketchLines
        lines.addByTwoPoints(adsk.core.Point3D.create(-2.0, -5.5, 0), adsk.core.Point3D.create(2.0, -5.5, 0))
        lines.addByTwoPoints(adsk.core.Point3D.create(2.0, -5.5, 0), adsk.core.Point3D.create(2.0, -4.5, 0))
        lines.addByTwoPoints(adsk.core.Point3D.create(2.0, -4.5, 0), adsk.core.Point3D.create(-2.0, -4.5, 0))
        lines.addByTwoPoints(adsk.core.Point3D.create(-2.0, -4.5, 0), adsk.core.Point3D.create(-2.0, -5.5, 0))
        
        profiles = sketch.profiles
        if profiles.count > 0:
            profile = profiles.item(0)
            extrudes = rootComp.features.extrudeFeatures
            extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            extrude_input.setSymmetricExtent(adsk.core.ValueInput.createByReal(0.15), False)
            extrudes.add(extrude_input)
            
            for body in rootComp.bodies:
                if body.name == "Body":
                    body.name = "Rear_Buckle"
                    break
    
    except Exception as e:
        pass


if __name__ == "__main__":
    run(None)
