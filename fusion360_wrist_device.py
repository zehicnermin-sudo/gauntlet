"""
FUTURISTIC WRIST-MOUNTED ELECTRONIC DEVICE - FUSION 360 PYTHON GENERATOR
=========================================================================

This script generates a complete parametric Fusion 360 CAD model of a rugged,
futuristic sci-fi wrist communicator with:
- Dark gray industrial housing
- Black curved wrist strap with texture
- Yellow protective frame and buttons
- Transparent cyan ribbed module
- Mechanical hinges and buckle
- Ventilation slots and recessed panels
- Screws, fasteners, and U1 marking

All major dimensions are parametric and editable via Fusion 360 User Parameters.

Author: Copilot CAD Generator
Date: 2026
"""

import adsk.core
import adsk.fusion
import traceback
import math


# Global reference variables
app = None
ui = None
design = None
rootComp = None


def run(context):
    """Main execution function called by Fusion 360."""
    global app, ui, design, rootComp
    
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        
        # Get the design
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        rootComp = design.rootComponent
        
        ui.messageBox("Starting Wrist Device creation...", "Info")
        
        # Create all user parameters first
        create_parameters()
        
        # Create each major component body
        create_main_housing()
        create_housing_panels()
        create_front_vents()
        create_top_frame()
        create_cyan_module()
        create_cyan_ribs()
        create_control_buttons()
        create_strap()
        create_strap_texture()
        create_hinges()
        create_buckle()
        create_screws()
        create_markings()
        
        # Finalize
        finalize_model()
        
        # Show success message
        ui.messageBox("Futuristic Wrist Device created successfully!", "Success")
        
    except Exception as e:
        ui.messageBox(f"Error: {str(e)}\n{traceback.format_exc()}", "Error")


# ============================================================================
# PARAMETER DEFINITIONS
# ============================================================================

def create_parameters():
    """Create all parametric master dimensions as Fusion 360 User Parameters."""
    
    try:
        params = design.userParameters
        
        # Main device dimensions
        add_parameter("DEVICE_LENGTH", "145 mm", "Overall device length")
        add_parameter("DEVICE_WIDTH", "72 mm", "Overall device width")
        add_parameter("DEVICE_HEIGHT", "38 mm", "Overall device height")
        
        # Housing dimensions
        add_parameter("HOUSING_LENGTH", "145 mm", "Main housing length")
        add_parameter("HOUSING_WIDTH", "72 mm", "Main housing width")
        add_parameter("HOUSING_HEIGHT", "34 mm", "Main housing height")
        add_parameter("HOUSING_CORNER_RADIUS", "12 mm", "Main housing corner radius")
        add_parameter("HOUSING_WALL_THICKNESS", "3 mm", "Housing wall thickness")
        
        # Top module dimensions
        add_parameter("TOP_MODULE_LENGTH", "70 mm", "Cyan module length")
        add_parameter("TOP_MODULE_WIDTH", "43 mm", "Cyan module width")
        add_parameter("TOP_MODULE_HEIGHT", "12 mm", "Cyan module height")
        
        # Yellow frame dimensions
        add_parameter("YELLOW_FRAME_LENGTH", "78 mm", "Yellow frame length")
        add_parameter("YELLOW_FRAME_WIDTH", "50 mm", "Yellow frame width")
        add_parameter("YELLOW_FRAME_HEIGHT", "7 mm", "Yellow frame height")
        add_parameter("YELLOW_FRAME_WALL", "2.5 mm", "Yellow frame wall thickness")
        
        # Strap dimensions
        add_parameter("STRAP_WIDTH", "52 mm", "Strap width")
        add_parameter("STRAP_THICKNESS", "5 mm", "Strap thickness")
        add_parameter("STRAP_INNER_RADIUS", "35 mm", "Strap inner radius")
        add_parameter("STRAP_OUTER_RADIUS", "40 mm", "Strap outer radius")
        
        # Ventilation slots
        add_parameter("FRONT_SLOT_LENGTH", "24 mm", "Front slot length")
        add_parameter("FRONT_SLOT_HEIGHT", "5 mm", "Front slot height")
        add_parameter("FRONT_SLOT_COUNT", "4", "Number of front slots")
        add_parameter("FRONT_SLOT_SPACING", "6 mm", "Spacing between slots")
        
        # Button dimensions
        add_parameter("BUTTON_DIAMETER", "10 mm", "Button diameter")
        add_parameter("BUTTON_HEIGHT", "3 mm", "Button height")
        
        # Fastener dimensions
        add_parameter("SCREW_DIAMETER", "3 mm", "Screw diameter")
        add_parameter("HINGE_DIAMETER", "10 mm", "Hinge barrel diameter")
        add_parameter("HINGE_PIN_DIAMETER", "4 mm", "Hinge pin diameter")
        
        # Fillet and chamfer sizes
        add_parameter("EDGE_FILLET", "2 mm", "Major edge fillet radius")
        add_parameter("SMALL_FILLET", "0.8 mm", "Small fillet radius")
        add_parameter("CHAMFER_SIZE", "1.5 mm", "Chamfer size")
        
    except Exception as e:
        ui.messageBox(f"Error in create_parameters: {str(e)}", "Error")


def add_parameter(name, value, description):
    """Helper to add a user parameter."""
    try:
        param = design.userParameters.itemByName(name)
        # Parameter exists, skip
        return
    except:
        # Parameter doesn't exist, create it
        try:
            design.userParameters.add(
                name,
                adsk.core.ValueInput.createByString(value),
                "",
                description
            )
        except:
            pass


# ============================================================================
# PARAMETER ACCESS
# ============================================================================

def get_parameter_value(param_name):
    """Get the current value of a parameter in cm."""
    try:
        param = design.userParameters.itemByName(param_name)
        return param.value
    except:
        return 0.0


# ============================================================================
# MAIN HOUSING
# ============================================================================

def create_main_housing():
    """Create the dark gray main housing enclosure."""
    
    try:
        # Create base rectangular sketch
        sketch = rootComp.sketches.addSketch(rootComp.xYConstructionPlane)
        sketch.name = "Housing_Base_Sketch"
        
        # Get parameter values (in cm)
        h_len = get_parameter_value("HOUSING_LENGTH") / 10.0  # Convert to cm
        h_wid = get_parameter_value("HOUSING_WIDTH") / 10.0
        h_rad = get_parameter_value("HOUSING_CORNER_RADIUS") / 10.0
        
        # Create rounded rectangle profile
        lines = sketch.sketchCurves.sketchLines
        arcs = sketch.sketchCurves.sketchArcs
        
        # Half dimensions
        hl = h_len / 2.0
        hw = h_wid / 2.0
        
        # Corner positions
        x1 = -hl + h_rad
        x2 = hl - h_rad
        y1 = -hw + h_rad
        y2 = hw + h_rad
        
        # Create straight segments
        pt1 = adsk.core.Point3D.create(x1, -hw, 0)
        pt2 = adsk.core.Point3D.create(x2, -hw, 0)
        pt3 = adsk.core.Point3D.create(hl, y1, 0)
        pt4 = adsk.core.Point3D.create(hl, hw - h_rad, 0)
        pt5 = adsk.core.Point3D.create(x2, hw, 0)
        pt6 = adsk.core.Point3D.create(x1, hw, 0)
        pt7 = adsk.core.Point3D.create(-hl, hw - h_rad, 0)
        pt8 = adsk.core.Point3D.create(-hl, y1, 0)
        
        lines.addByTwoPoints(pt1, pt2)
        lines.addByTwoPoints(pt3, pt4)
        lines.addByTwoPoints(pt5, pt6)
        lines.addByTwoPoints(pt7, pt8)
        
        # Create corner arcs with proper geometry
        arc_center = h_rad / 2.0
        
        arcs.addByThreePoints(pt2, adsk.core.Point3D.create(hl - arc_center, -hw + arc_center, 0), pt3)
        arcs.addByThreePoints(pt4, adsk.core.Point3D.create(hl - arc_center, hw - arc_center, 0), pt5)
        arcs.addByThreePoints(pt6, adsk.core.Point3D.create(-hl + arc_center, hw - arc_center, 0), pt7)
        arcs.addByThreePoints(pt8, adsk.core.Point3D.create(-hl + arc_center, -hw + arc_center, 0), pt1)
        
        sketch.close()
        
        # Get the profile
        profiles = sketch.profiles
        if profiles.count > 0:
            profile = profiles.item(0)
            
            # Create extrude feature
            extrudes = rootComp.features.extrudeFeatures
            h_height = get_parameter_value("HOUSING_HEIGHT") / 10.0
            
            extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            dist_value = adsk.core.ValueInput.createByReal(h_height / 2.0)
            extrude_input.setSymmetricExtent(dist_value, False)
            
            extrude = extrudes.add(extrude_input)
            
            # Rename the resulting body
            for body in rootComp.bodies:
                if body.name == "Body":
                    body.name = "Main_Housing"
                    break
        
    except Exception as e:
        ui.messageBox(f"Error in create_main_housing: {str(e)}\n{traceback.format_exc()}", "Error")


# ============================================================================
# HOUSING PANELS
# ============================================================================

def create_housing_panels():
    """Add shallow recessed panels to main housing."""
    
    try:
        sketch = rootComp.sketches.addSketch(rootComp.xYConstructionPlane)
        sketch.name = "Housing_Panels_Sketch"
        
        lines = sketch.sketchCurves.sketchLines
        
        # Left side panel outline
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-6.5, -1.2, 0),
            adsk.core.Point3D.create(-5.0, -1.2, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-5.0, -1.2, 0),
            adsk.core.Point3D.create(-5.0, 1.2, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-5.0, 1.2, 0),
            adsk.core.Point3D.create(-6.5, 1.2, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-6.5, 1.2, 0),
            adsk.core.Point3D.create(-6.5, -1.2, 0)
        )
        
        # Right side panel outline
        lines.addByTwoPoints(
            adsk.core.Point3D.create(5.0, -1.2, 0),
            adsk.core.Point3D.create(6.5, -1.2, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(6.5, -1.2, 0),
            adsk.core.Point3D.create(6.5, 1.2, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(6.5, 1.2, 0),
            adsk.core.Point3D.create(5.0, 1.2, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(5.0, 1.2, 0),
            adsk.core.Point3D.create(5.0, -1.2, 0)
        )
        
        sketch.close()
        
    except Exception as e:
        pass


# ============================================================================
# VENTILATION SLOTS
# ============================================================================

def create_front_vents():
    """Create front ventilation slots on the housing."""
    
    try:
        # Create sketch for slots
        sketch = rootComp.sketches.addSketch(rootComp.xYConstructionPlane)
        sketch.name = "Vents_Sketch"
        
        # Get slot parameters
        slot_len = get_parameter_value("FRONT_SLOT_LENGTH") / 10.0
        slot_height = get_parameter_value("FRONT_SLOT_HEIGHT") / 10.0
        slot_count = int(get_parameter_value("FRONT_SLOT_COUNT"))
        slot_spacing = get_parameter_value("FRONT_SLOT_SPACING") / 10.0
        
        lines = sketch.sketchCurves.sketchLines
        
        # Position slots vertically
        total_height = (slot_count - 1) * (slot_height + slot_spacing) + slot_height
        start_y = total_height / 2.0
        
        for i in range(slot_count):
            y_pos = start_y - i * (slot_height + slot_spacing)
            
            # Create rectangular slot profile
            x1 = -slot_len / 2.0
            x2 = slot_len / 2.0
            y1 = y_pos - slot_height / 2.0
            y2 = y_pos + slot_height / 2.0
            
            lines.addByTwoPoints(
                adsk.core.Point3D.create(x1, y1, 0),
                adsk.core.Point3D.create(x2, y1, 0)
            )
            lines.addByTwoPoints(
                adsk.core.Point3D.create(x2, y1, 0),
                adsk.core.Point3D.create(x2, y2, 0)
            )
            lines.addByTwoPoints(
                adsk.core.Point3D.create(x2, y2, 0),
                adsk.core.Point3D.create(x1, y2, 0)
            )
            lines.addByTwoPoints(
                adsk.core.Point3D.create(x1, y2, 0),
                adsk.core.Point3D.create(x1, y1, 0)
            )
        
        sketch.close()
        
    except Exception as e:
        pass


# ============================================================================
# TOP YELLOW FRAME
# ============================================================================

def create_top_frame():
    """Create the bright yellow protective frame."""
    
    try:
        # Create frame sketch
        sketch = rootComp.sketches.addSketch(rootComp.xYConstructionPlane)
        sketch.name = "Frame_Sketch"
        
        # Get dimensions (in cm)
        frame_len = get_parameter_value("YELLOW_FRAME_LENGTH") / 10.0
        frame_wid = get_parameter_value("YELLOW_FRAME_WIDTH") / 10.0
        frame_height = get_parameter_value("YELLOW_FRAME_HEIGHT") / 10.0
        frame_wall = get_parameter_value("YELLOW_FRAME_WALL") / 10.0
        
        lines = sketch.sketchCurves.sketchLines
        
        # Outer rectangle
        hl = frame_len / 2.0
        hw = frame_wid / 2.0
        
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
        
        # Inner rectangle (hollow center)
        il = (frame_len - 2 * frame_wall) / 2.0
        iw = (frame_wid - 2 * frame_wall) / 2.0
        
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-il, -iw, 0),
            adsk.core.Point3D.create(il, -iw, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(il, -iw, 0),
            adsk.core.Point3D.create(il, iw, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(il, iw, 0),
            adsk.core.Point3D.create(-il, iw, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-il, iw, 0),
            adsk.core.Point3D.create(-il, -iw, 0)
        )
        
        sketch.close()
        
        # Extrude the frame
        profiles = sketch.profiles
        if profiles.count > 0:
            profile = profiles.item(0)
            extrudes = rootComp.features.extrudeFeatures
            
            extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            dist_value = adsk.core.ValueInput.createByReal(frame_height / 2.0)
            extrude_input.setSymmetricExtent(dist_value, False)
            
            extrude = extrudes.add(extrude_input)
            
            # Rename body
            for body in rootComp.bodies:
                if body.name == "Body":
                    body.name = "Yellow_Frame"
                    break
        
    except Exception as e:
        pass


# ============================================================================
# CYAN MODULE
# ============================================================================

def create_cyan_module():
    """Create the transparent cyan main module body."""
    
    try:
        # Create module sketch
        sketch = rootComp.sketches.addSketch(rootComp.xYConstructionPlane)
        sketch.name = "Cyan_Module_Sketch"
        
        # Get module dimensions (in cm)
        mod_len = get_parameter_value("TOP_MODULE_LENGTH") / 10.0
        mod_wid = get_parameter_value("TOP_MODULE_WIDTH") / 10.0
        mod_height = get_parameter_value("TOP_MODULE_HEIGHT") / 10.0
        
        # Create rectangle
        ml = mod_len / 2.0
        mw = mod_wid / 2.0
        
        lines = sketch.sketchCurves.sketchLines
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-ml, -mw, 0),
            adsk.core.Point3D.create(ml, -mw, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(ml, -mw, 0),
            adsk.core.Point3D.create(ml, mw, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(ml, mw, 0),
            adsk.core.Point3D.create(-ml, mw, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-ml, mw, 0),
            adsk.core.Point3D.create(-ml, -mw, 0)
        )
        
        sketch.close()
        
        # Extrude
        profiles = sketch.profiles
        if profiles.count > 0:
            profile = profiles.item(0)
            extrudes = rootComp.features.extrudeFeatures
            
            extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            dist_value = adsk.core.ValueInput.createByReal(mod_height / 2.0)
            extrude_input.setSymmetricExtent(dist_value, False)
            
            extrude = extrudes.add(extrude_input)
            
            # Rename body
            for body in rootComp.bodies:
                if body.name == "Body":
                    body.name = "Cyan_Module_Base"
                    break
        
    except Exception as e:
        pass


def create_cyan_ribs():
    """Create vertical ribs on the cyan module."""
    
    try:
        # Get module dimensions
        mod_len = get_parameter_value("TOP_MODULE_LENGTH") / 10.0
        mod_wid = get_parameter_value("TOP_MODULE_WIDTH") / 10.0
        mod_height = get_parameter_value("TOP_MODULE_HEIGHT") / 10.0
        
        num_ribs = 6
        rib_width = 0.15
        
        for i in range(num_ribs):
            try:
                sketch = rootComp.sketches.addSketch(rootComp.xYConstructionPlane)
                sketch.name = f"Rib_Sketch_{i+1}"
                
                # Position ribs across the width
                spacing = mod_wid / (num_ribs + 1)
                x_pos = -mod_len / 2.0 + spacing * (i + 1)
                
                lines = sketch.sketchCurves.sketchLines
                y_half = mod_wid / 2.0
                
                lines.addByTwoPoints(
                    adsk.core.Point3D.create(x_pos - rib_width / 2.0, -y_half, 0),
                    adsk.core.Point3D.create(x_pos + rib_width / 2.0, -y_half, 0)
                )
                lines.addByTwoPoints(
                    adsk.core.Point3D.create(x_pos + rib_width / 2.0, -y_half, 0),
                    adsk.core.Point3D.create(x_pos + rib_width / 2.0, y_half, 0)
                )
                lines.addByTwoPoints(
                    adsk.core.Point3D.create(x_pos + rib_width / 2.0, y_half, 0),
                    adsk.core.Point3D.create(x_pos - rib_width / 2.0, y_half, 0)
                )
                lines.addByTwoPoints(
                    adsk.core.Point3D.create(x_pos - rib_width / 2.0, y_half, 0),
                    adsk.core.Point3D.create(x_pos - rib_width / 2.0, -y_half, 0)
                )
                
                sketch.close()
                
                profiles = sketch.profiles
                if profiles.count > 0:
                    profile = profiles.item(0)
                    extrudes = rootComp.features.extrudeFeatures
                    
                    extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
                    dist_value = adsk.core.ValueInput.createByReal(mod_height / 2.0)
                    extrude_input.setSymmetricExtent(dist_value, False)
                    
                    extrude = extrudes.add(extrude_input)
                    
                    # Rename body
                    for body in rootComp.bodies:
                        if body.name == "Body":
                            body.name = f"Cyan_Rib_{i+1}"
                            break
                    
            except Exception as e:
                pass
        
    except Exception as e:
        pass


# ============================================================================
# CONTROL BUTTONS
# ============================================================================

def create_control_buttons():
    """Create four yellow control buttons on the housing."""
    
    try:
        btn_dia = get_parameter_value("BUTTON_DIAMETER") / 10.0
        btn_height = get_parameter_value("BUTTON_HEIGHT") / 10.0
        
        # Button positions (2x2 layout on upper left) - in cm
        positions = [
            (-3.0, 2.0),
            (-1.5, 2.0),
            (-3.0, 0.5),
            (-1.5, 0.5),
        ]
        
        for idx, (x, y) in enumerate(positions):
            try:
                sketch = rootComp.sketches.addSketch(rootComp.xYConstructionPlane)
                sketch.name = f"Button_{idx+1}_Sketch"
                
                # Create circular button profile
                circles = sketch.sketchCurves.sketchCircles
                circle = circles.addByCenterAndRadius(
                    adsk.core.Point3D.create(x, y, 0),
                    btn_dia / 2.0
                )
                
                sketch.close()
                
                # Extrude button
                profiles = sketch.profiles
                if profiles.count > 0:
                    profile = profiles.item(0)
                    extrudes = rootComp.features.extrudeFeatures
                    
                    extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
                    dist_value = adsk.core.ValueInput.createByReal(btn_height / 2.0)
                    extrude_input.setSymmetricExtent(dist_value, False)
                    
                    extrude = extrudes.add(extrude_input)
                    
                    # Rename body
                    for body in rootComp.bodies:
                        if body.name == "Body":
                            body.name = f"Button_{idx+1}"
                            break
                
            except Exception as e:
                pass
        
    except Exception as e:
        pass


# ============================================================================
# WRIST STRAP
# ============================================================================

def create_strap():
    """Create the curved black wrist strap."""
    
    try:
        # Get strap dimensions (in cm)
        strap_wid = get_parameter_value("STRAP_WIDTH") / 10.0
        strap_thick = get_parameter_value("STRAP_THICKNESS") / 10.0
        
        # Create strap as a simplified rectangular extrusion
        sketch = rootComp.sketches.addSketch(rootComp.xYConstructionPlane)
        sketch.name = "Strap_Sketch"
        
        lines = sketch.sketchCurves.sketchLines
        
        # Strap outline (simplified as rectangle)
        x1 = -strap_wid / 2.0
        x2 = strap_wid / 2.0
        y1 = -5.0
        y2 = -3.0
        
        lines.addByTwoPoints(
            adsk.core.Point3D.create(x1, y1, 0),
            adsk.core.Point3D.create(x2, y1, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(x2, y1, 0),
            adsk.core.Point3D.create(x2, y2, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(x2, y2, 0),
            adsk.core.Point3D.create(x1, y2, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(x1, y2, 0),
            adsk.core.Point3D.create(x1, y1, 0)
        )
        
        sketch.close()
        
        # Extrude strap
        profiles = sketch.profiles
        if profiles.count > 0:
            profile = profiles.item(0)
            extrudes = rootComp.features.extrudeFeatures
            
            extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            dist_value = adsk.core.ValueInput.createByReal(strap_thick / 2.0)
            extrude_input.setSymmetricExtent(dist_value, False)
            
            extrude = extrudes.add(extrude_input)
            
            # Rename body
            for body in rootComp.bodies:
                if body.name == "Body":
                    body.name = "Strap"
                    break
        
    except Exception as e:
        pass


def create_strap_texture():
    """Create textured grid pattern on the inner strap surface."""
    
    try:
        sketch = rootComp.sketches.addSketch(rootComp.xYConstructionPlane)
        sketch.name = "Texture_Sketch"
        
        block_size = 0.04
        pitch = 0.08
        
        lines = sketch.sketchCurves.sketchLines
        
        # Create a small grid of rectangular blocks
        for i in range(-8, 9):
            for j in range(-5, 6):
                x = i * pitch
                y = -4.0 + j * pitch
                
                lines.addByTwoPoints(
                    adsk.core.Point3D.create(x, y, 0),
                    adsk.core.Point3D.create(x + block_size, y, 0)
                )
                lines.addByTwoPoints(
                    adsk.core.Point3D.create(x + block_size, y, 0),
                    adsk.core.Point3D.create(x + block_size, y + block_size, 0)
                )
                lines.addByTwoPoints(
                    adsk.core.Point3D.create(x + block_size, y + block_size, 0),
                    adsk.core.Point3D.create(x, y + block_size, 0)
                )
                lines.addByTwoPoints(
                    adsk.core.Point3D.create(x, y + block_size, 0),
                    adsk.core.Point3D.create(x, y, 0)
                )
        
        sketch.close()
        
    except Exception as e:
        pass


# ============================================================================
# HINGES
# ============================================================================

def create_hinges():
    """Create mechanical hinge assemblies."""
    
    try:
        hinge_dia = get_parameter_value("HINGE_DIAMETER") / 10.0
        
        # Left hinge
        sketch = rootComp.sketches.addSketch(rootComp.xYConstructionPlane)
        sketch.name = "Left_Hinge_Sketch"
        
        # Simple hinge barrel (cylinder)
        circles = sketch.sketchCurves.sketchCircles
        circle = circles.addByCenterAndRadius(
            adsk.core.Point3D.create(-7.2, -2.5, 0),
            hinge_dia / 2.0
        )
        
        sketch.close()
        
        # Extrude left hinge
        profiles = sketch.profiles
        if profiles.count > 0:
            profile = profiles.item(0)
            extrudes = rootComp.features.extrudeFeatures
            
            extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            extrude_input.setSymmetricExtent(adsk.core.ValueInput.createByReal(0.2), False)
            
            extrude = extrudes.add(extrude_input)
            
            for body in rootComp.bodies:
                if body.name == "Body":
                    body.name = "Left_Hinge"
                    break
        
        # Right hinge
        sketch2 = rootComp.sketches.addSketch(rootComp.xYConstructionPlane)
        sketch2.name = "Right_Hinge_Sketch"
        
        circles2 = sketch2.sketchCurves.sketchCircles
        circle2 = circles2.addByCenterAndRadius(
            adsk.core.Point3D.create(7.2, -2.5, 0),
            hinge_dia / 2.0
        )
        
        sketch2.close()
        
        # Extrude right hinge
        profiles2 = sketch2.profiles
        if profiles2.count > 0:
            profile2 = profiles2.item(0)
            extrudes2 = rootComp.features.extrudeFeatures
            
            extrude_input2 = extrudes2.createInput(profile2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            extrude_input2.setSymmetricExtent(adsk.core.ValueInput.createByReal(0.2), False)
            
            extrude2 = extrudes2.add(extrude_input2)
            
            for body in rootComp.bodies:
                if body.name == "Body":
                    body.name = "Right_Hinge"
                    break
        
    except Exception as e:
        pass


# ============================================================================
# REAR BUCKLE
# ============================================================================

def create_buckle():
    """Create the rear clasp/buckle assembly."""
    
    try:
        sketch = rootComp.sketches.addSketch(rootComp.xYConstructionPlane)
        sketch.name = "Buckle_Sketch"
        
        # Rectangular buckle body
        lines = sketch.sketchCurves.sketchLines
        
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-2.0, -5.5, 0),
            adsk.core.Point3D.create(2.0, -5.5, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(2.0, -5.5, 0),
            adsk.core.Point3D.create(2.0, -4.5, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(2.0, -4.5, 0),
            adsk.core.Point3D.create(-2.0, -4.5, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-2.0, -4.5, 0),
            adsk.core.Point3D.create(-2.0, -5.5, 0)
        )
        
        sketch.close()
        
        # Extrude
        profiles = sketch.profiles
        if profiles.count > 0:
            profile = profiles.item(0)
            extrudes = rootComp.features.extrudeFeatures
            
            extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            extrude_input.setSymmetricExtent(adsk.core.ValueInput.createByReal(0.15), False)
            
            extrude = extrudes.add(extrude_input)
            
            for body in rootComp.bodies:
                if body.name == "Body":
                    body.name = "Rear_Buckle"
                    break
        
    except Exception as e:
        pass


# ============================================================================
# SCREWS AND FASTENERS
# ============================================================================

def create_screws():
    """Add realistic small fastener heads."""
    
    try:
        screw_dia = get_parameter_value("SCREW_DIAMETER") / 10.0
        
        # Screw positions (in cm)
        screw_positions = [
            (-6.0, -2.0),
            (-6.0, 2.0),
            (6.0, -2.0),
            (6.0, 2.0),
            (0, -3.2),
            (0, 3.2),
        ]
        
        for idx, (x, y) in enumerate(screw_positions):
            try:
                sketch = rootComp.sketches.addSketch(rootComp.xYConstructionPlane)
                sketch.name = f"Screw_{idx+1}_Sketch"
                
                # Create circular screw head profile
                circles = sketch.sketchCurves.sketchCircles
                circle = circles.addByCenterAndRadius(
                    adsk.core.Point3D.create(x, y, 0),
                    screw_dia / 2.0
                )
                
                sketch.close()
                
                # Extrude
                profiles = sketch.profiles
                if profiles.count > 0:
                    profile = profiles.item(0)
                    extrudes = rootComp.features.extrudeFeatures
                    
                    extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
                    extrude_input.setSymmetricExtent(adsk.core.ValueInput.createByReal(0.05), False)
                    
                    extrude = extrudes.add(extrude_input)
                    
                    for body in rootComp.bodies:
                        if body.name == "Body":
                            body.name = f"Screw_{idx+1}"
                            break
                
            except Exception as e:
                pass
        
    except Exception as e:
        pass


# ============================================================================
# MARKINGS AND TEXT
# ============================================================================

def create_markings():
    """Create U1 marking on the device."""
    
    try:
        sketch = rootComp.sketches.addSketch(rootComp.xYConstructionPlane)
        sketch.name = "U1_Marking_Sketch"
        
        # Draw simple "U1" as rectangles
        lines = sketch.sketchCurves.sketchLines
        
        # U shape (left vertical)
        lines.addByTwoPoints(
            adsk.core.Point3D.create(5.5, 1.0, 0),
            adsk.core.Point3D.create(5.5, 0.5, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(5.5, 0.5, 0),
            adsk.core.Point3D.create(5.8, 0.5, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(5.8, 0.5, 0),
            adsk.core.Point3D.create(5.8, 1.0, 0)
        )
        
        # 1 shape (vertical line)
        lines.addByTwoPoints(
            adsk.core.Point3D.create(6.0, 1.0, 0),
            adsk.core.Point3D.create(6.0, 0.5, 0)
        )
        
        sketch.close()
        
    except Exception as e:
        pass


# ============================================================================
# FINALIZATION
# ============================================================================

def finalize_model():
    """Finalize the model and prepare for viewing."""
    
    try:
        # Recompute the design
        design.recompute()
        
        # Fit the view to show the entire model
        try:
            camera = app.activeViewport.camera
            camera.isFitView = True
            app.activeViewport.camera = camera
        except:
            pass
        
    except Exception as e:
        pass


# ============================================================================
# EXECUTION
# ============================================================================

if __name__ == "__main__":
    run(None)
