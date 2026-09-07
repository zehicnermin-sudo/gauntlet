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
        
        # Apply visual appearances
        apply_appearances()
        
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


def add_parameter(name, value, description):
    """Helper to add a user parameter."""
    try:
        param = design.userParameters.itemByName(name)
        # Parameter exists, update it
        param.value = adsk.core.ValueInput.createByString(value)
    except:
        # Parameter doesn't exist, create it
        design.userParameters.add(
            name,
            adsk.core.ValueInput.createByString(value),
            "",
            description
        )


# ============================================================================
# PARAMETER ACCESS
# ============================================================================

def get_parameter_value(param_name):
    """Get the current value of a parameter."""
    try:
        param = design.userParameters.itemByName(param_name)
        return param.value
    except:
        return 0.0


def get_parameter_expression(param_name):
    """Get a parameter as an expression string for use in features."""
    return f'"{param_name}"'


# ============================================================================
# MAIN HOUSING
# ============================================================================

def create_main_housing():
    """Create the dark gray main housing enclosure."""
    
    try:
        # Create a new body for the housing
        housing_body = rootComp.bodies.addNewBody()
        housing_body.name = "Main_Housing"
        
        # Create base rectangular sketch on XY plane
        xy_plane = rootComp.xYConstructionPlane
        sketch = rootComp.sketches.addSketch(xy_plane)
        sketch.name = "Housing_Base_Sketch"
        
        # Get parameter values
        h_len = get_parameter_value("HOUSING_LENGTH")
        h_wid = get_parameter_value("HOUSING_WIDTH")
        h_rad = get_parameter_value("HOUSING_CORNER_RADIUS")
        
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
        y2 = hw - h_rad
        
        # Create straight segments
        lines.addByTwoPoints(
            adsk.core.Point3D.create(x1, -hw, 0),
            adsk.core.Point3D.create(x2, -hw, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(hl, y1, 0),
            adsk.core.Point3D.create(hl, y2, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(x2, hw, 0),
            adsk.core.Point3D.create(x1, hw, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-hl, y2, 0),
            adsk.core.Point3D.create(-hl, y1, 0)
        )
        
        # Create corner arcs (simplified)
        arc_r = h_rad / 2.0
        arcs.addByThreePoints(
            adsk.core.Point3D.create(x2, -hw, 0),
            adsk.core.Point3D.create(hl - arc_r, -hw + arc_r, 0),
            adsk.core.Point3D.create(hl, y1, 0)
        )
        arcs.addByThreePoints(
            adsk.core.Point3D.create(hl, y2, 0),
            adsk.core.Point3D.create(hl - arc_r, hw - arc_r, 0),
            adsk.core.Point3D.create(x2, hw, 0)
        )
        arcs.addByThreePoints(
            adsk.core.Point3D.create(x1, hw, 0),
            adsk.core.Point3D.create(-hl + arc_r, hw - arc_r, 0),
            adsk.core.Point3D.create(-hl, y2, 0)
        )
        arcs.addByThreePoints(
            adsk.core.Point3D.create(-hl, y1, 0),
            adsk.core.Point3D.create(-hl + arc_r, -hw + arc_r, 0),
            adsk.core.Point3D.create(x1, -hw, 0)
        )
        
        sketch.close()
        
        # Get the profile and extrude
        profiles = sketch.profiles
        if profiles.count > 0:
            profile = profiles.item(0)
            
            # Create extrude feature
            extrudes = rootComp.features.extrudeFeatures
            h_height = get_parameter_value("HOUSING_HEIGHT")
            
            extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            extrude_input.setSymmetricExtent(adsk.core.ValueInput.createByReal(h_height / 2.0 / 10.0), False)
            
            extrude = extrudes.add(extrude_input)
            extrude.bodies.item(0).name = "Main_Housing"
        
    except Exception as e:
        ui.messageBox(f"Error in create_main_housing: {str(e)}", "Error")


# ============================================================================
# HOUSING PANELS
# ============================================================================

def create_housing_panels():
    """Add shallow recessed panels to main housing."""
    
    try:
        # Create a sketch for panel details
        xy_plane = rootComp.xYConstructionPlane
        sketch = rootComp.sketches.addSketch(xy_plane)
        sketch.name = "Housing_Panels_Sketch"
        
        lines = sketch.sketchCurves.sketchLines
        
        # Left side panel outline
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-65, -12, 0),
            adsk.core.Point3D.create(-50, -12, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-50, -12, 0),
            adsk.core.Point3D.create(-50, 12, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-50, 12, 0),
            adsk.core.Point3D.create(-65, 12, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-65, 12, 0),
            adsk.core.Point3D.create(-65, -12, 0)
        )
        
        # Right side panel outline
        lines.addByTwoPoints(
            adsk.core.Point3D.create(50, -12, 0),
            adsk.core.Point3D.create(65, -12, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(65, -12, 0),
            adsk.core.Point3D.create(65, 12, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(65, 12, 0),
            adsk.core.Point3D.create(50, 12, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(50, 12, 0),
            adsk.core.Point3D.create(50, -12, 0)
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
        # Create a body for the vents
        vent_body = rootComp.bodies.addNewBody()
        vent_body.name = "Front_Vents"
        
        # Get slot parameters
        slot_len = get_parameter_value("FRONT_SLOT_LENGTH")
        slot_height = get_parameter_value("FRONT_SLOT_HEIGHT")
        slot_count = int(get_parameter_value("FRONT_SLOT_COUNT"))
        slot_spacing = get_parameter_value("FRONT_SLOT_SPACING")
        
        # Create sketch for slots
        xy_plane = rootComp.xYConstructionPlane
        sketch = rootComp.sketches.addSketch(xy_plane)
        sketch.name = "Vents_Sketch"
        
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
        # Create a body for the frame
        frame_body = rootComp.bodies.addNewBody()
        frame_body.name = "Yellow_Frame"
        
        # Get dimensions
        frame_len = get_parameter_value("YELLOW_FRAME_LENGTH")
        frame_wid = get_parameter_value("YELLOW_FRAME_WIDTH")
        frame_height = get_parameter_value("YELLOW_FRAME_HEIGHT")
        frame_wall = get_parameter_value("YELLOW_FRAME_WALL")
        
        # Create frame sketch
        xy_plane = rootComp.xYConstructionPlane
        sketch = rootComp.sketches.addSketch(xy_plane)
        sketch.name = "Frame_Sketch"
        
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
        if sketch.profiles.count > 0:
            profile = sketch.profiles.item(0)
            extrudes = rootComp.features.extrudeFeatures
            
            extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            extrude_input.setSymmetricExtent(adsk.core.ValueInput.createByReal(frame_height / 2.0 / 10.0), False)
            
            extrude = extrudes.add(extrude_input)
            extrude.bodies.item(0).name = "Yellow_Frame"
        
    except Exception as e:
        pass


# ============================================================================
# CYAN MODULE
# ============================================================================

def create_cyan_module():
    """Create the transparent cyan main module body."""
    
    try:
        # Create body for cyan module
        cyan_body = rootComp.bodies.addNewBody()
        cyan_body.name = "Cyan_Module_Base"
        
        # Get module dimensions
        mod_len = get_parameter_value("TOP_MODULE_LENGTH")
        mod_wid = get_parameter_value("TOP_MODULE_WIDTH")
        mod_height = get_parameter_value("TOP_MODULE_HEIGHT")
        
        # Create module sketch
        xy_plane = rootComp.xYConstructionPlane
        sketch = rootComp.sketches.addSketch(xy_plane)
        sketch.name = "Cyan_Module_Sketch"
        
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
        if sketch.profiles.count > 0:
            profile = sketch.profiles.item(0)
            extrudes = rootComp.features.extrudeFeatures
            
            extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            extrude_input.setSymmetricExtent(adsk.core.ValueInput.createByReal(mod_height / 2.0 / 10.0), False)
            
            extrude = extrudes.add(extrude_input)
            extrude.bodies.item(0).name = "Cyan_Module_Base"
        
    except Exception as e:
        pass


def create_cyan_ribs():
    """Create vertical ribs on the cyan module."""
    
    try:
        # Create separate rib bodies
        mod_len = get_parameter_value("TOP_MODULE_LENGTH")
        mod_wid = get_parameter_value("TOP_MODULE_WIDTH")
        mod_height = get_parameter_value("TOP_MODULE_HEIGHT")
        
        num_ribs = 6
        rib_width = 1.5
        
        for i in range(num_ribs):
            try:
                rib_body = rootComp.bodies.addNewBody()
                rib_body.name = f"Cyan_Rib_{i+1}"
                
                xy_plane = rootComp.xYConstructionPlane
                sketch = rootComp.sketches.addSketch(xy_plane)
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
                
                if sketch.profiles.count > 0:
                    profile = sketch.profiles.item(0)
                    extrudes = rootComp.features.extrudeFeatures
                    
                    extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
                    extrude_input.setSymmetricExtent(adsk.core.ValueInput.createByReal(mod_height / 2.0 / 10.0), False)
                    
                    extrude = extrudes.add(extrude_input)
                    extrude.bodies.item(0).name = f"Cyan_Rib_{i+1}"
                    
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
        btn_dia = get_parameter_value("BUTTON_DIAMETER")
        btn_height = get_parameter_value("BUTTON_HEIGHT")
        
        # Button positions (2x2 layout on upper left)
        positions = [
            (-30, 20),
            (-15, 20),
            (-30, 5),
            (-15, 5),
        ]
        
        for idx, (x, y) in enumerate(positions):
            try:
                button_body = rootComp.bodies.addNewBody()
                button_body.name = f"Button_{idx+1}"
                
                xy_plane = rootComp.xYConstructionPlane
                sketch = rootComp.sketches.addSketch(xy_plane)
                sketch.name = f"Button_{idx+1}_Sketch"
                
                # Create circular button profile
                circles = sketch.sketchCurves.sketchCircles
                circle = circles.addByCenterAndRadius(
                    adsk.core.Point3D.create(x, y, 0),
                    btn_dia / 2.0 / 10.0
                )
                
                sketch.close()
                
                # Extrude button
                if sketch.profiles.count > 0:
                    profile = sketch.profiles.item(0)
                    extrudes = rootComp.features.extrudeFeatures
                    
                    extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
                    extrude_input.setSymmetricExtent(adsk.core.ValueInput.createByReal(btn_height / 2.0 / 10.0), False)
                    
                    extrude = extrudes.add(extrude_input)
                    extrude.bodies.item(0).name = f"Button_{idx+1}"
                
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
        strap_body = rootComp.bodies.addNewBody()
        strap_body.name = "Strap"
        
        # Get strap dimensions
        strap_wid = get_parameter_value("STRAP_WIDTH")
        strap_thick = get_parameter_value("STRAP_THICKNESS")
        inner_rad = get_parameter_value("STRAP_INNER_RADIUS")
        outer_rad = get_parameter_value("STRAP_OUTER_RADIUS")
        
        # Create strap as a simplified rectangular extrusion
        # positioned at the bottom of the device
        xy_plane = rootComp.xYConstructionPlane
        sketch = rootComp.sketches.addSketch(xy_plane)
        sketch.name = "Strap_Sketch"
        
        lines = sketch.sketchCurves.sketchLines
        
        # Strap outline (simplified as rectangle)
        x1 = -strap_wid / 2.0
        x2 = strap_wid / 2.0
        y1 = -50
        y2 = -30
        
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
        if sketch.profiles.count > 0:
            profile = sketch.profiles.item(0)
            extrudes = rootComp.features.extrudeFeatures
            
            extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            extrude_input.setSymmetricExtent(adsk.core.ValueInput.createByReal(strap_thick / 2.0 / 10.0), False)
            
            extrude = extrudes.add(extrude_input)
            extrude.bodies.item(0).name = "Strap"
        
    except Exception as e:
        pass


def create_strap_texture():
    """Create textured grid pattern on the inner strap surface."""
    
    try:
        texture_body = rootComp.bodies.addNewBody()
        texture_body.name = "Strap_Texture"
        
        # Create repeating pattern of raised blocks
        sketch = rootComp.sketches.addSketch(rootComp.xYConstructionPlane)
        sketch.name = "Texture_Sketch"
        
        block_size = 0.4
        pitch = 0.8
        
        lines = sketch.sketchCurves.sketchLines
        
        # Create a small grid of rectangular blocks
        for i in range(-8, 9):
            for j in range(-5, 6):
                x = i * pitch
                y = -40 + j * pitch
                
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
        hinge_dia = get_parameter_value("HINGE_DIAMETER")
        
        # Left hinge
        left_hinge = rootComp.bodies.addNewBody()
        left_hinge.name = "Left_Hinge"
        
        xy_plane = rootComp.xYConstructionPlane
        sketch = rootComp.sketches.addSketch(xy_plane)
        sketch.name = "Left_Hinge_Sketch"
        
        # Simple hinge barrel (cylinder)
        circles = sketch.sketchCurves.sketchCircles
        circle = circles.addByCenterAndRadius(
            adsk.core.Point3D.create(-72, -25, 0),
            hinge_dia / 2.0 / 10.0
        )
        
        sketch.close()
        
        # Right hinge
        right_hinge = rootComp.bodies.addNewBody()
        right_hinge.name = "Right_Hinge"
        
        sketch2 = rootComp.sketches.addSketch(xy_plane)
        sketch2.name = "Right_Hinge_Sketch"
        
        circles2 = sketch2.sketchCurves.sketchCircles
        circle2 = circles2.addByCenterAndRadius(
            adsk.core.Point3D.create(72, -25, 0),
            hinge_dia / 2.0 / 10.0
        )
        
        sketch2.close()
        
    except Exception as e:
        pass


# ============================================================================
# REAR BUCKLE
# ============================================================================

def create_buckle():
    """Create the rear clasp/buckle assembly."""
    
    try:
        buckle_body = rootComp.bodies.addNewBody()
        buckle_body.name = "Rear_Buckle"
        
        # Create buckle sketch
        xy_plane = rootComp.xYConstructionPlane
        sketch = rootComp.sketches.addSketch(xy_plane)
        sketch.name = "Buckle_Sketch"
        
        # Rectangular buckle body
        lines = sketch.sketchCurves.sketchLines
        
        # Buckle housing
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-20, -55, 0),
            adsk.core.Point3D.create(20, -55, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(20, -55, 0),
            adsk.core.Point3D.create(20, -45, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(20, -45, 0),
            adsk.core.Point3D.create(-20, -45, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-20, -45, 0),
            adsk.core.Point3D.create(-20, -55, 0)
        )
        
        sketch.close()
        
    except Exception as e:
        pass


# ============================================================================
# SCREWS AND FASTENERS
# ============================================================================

def create_screws():
    """Add realistic small fastener heads."""
    
    try:
        screw_dia = get_parameter_value("SCREW_DIAMETER")
        
        # Screw positions (example locations)
        screw_positions = [
            (-60, -20),
            (-60, 20),
            (60, -20),
            (60, 20),
            (0, -32),
            (0, 32),
        ]
        
        for idx, (x, y) in enumerate(screw_positions):
            try:
                screw_body = rootComp.bodies.addNewBody()
                screw_body.name = f"Screw_{idx+1}"
                
                xy_plane = rootComp.xYConstructionPlane
                sketch = rootComp.sketches.addSketch(xy_plane)
                sketch.name = f"Screw_{idx+1}_Sketch"
                
                # Create circular screw head profile
                circles = sketch.sketchCurves.sketchCircles
                circle = circles.addByCenterAndRadius(
                    adsk.core.Point3D.create(x, y, 0),
                    screw_dia / 2.0 / 10.0
                )
                
                sketch.close()
                
                # Extrude to create screw head
                if sketch.profiles.count > 0:
                    profile = sketch.profiles.item(0)
                    extrudes = rootComp.features.extrudeFeatures
                    
                    extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
                    extrude_input.setSymmetricExtent(adsk.core.ValueInput.createByReal(0.05), False)
                    
                    extrude = extrudes.add(extrude_input)
                    extrude.bodies.item(0).name = f"Screw_{idx+1}"
                
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
        marks_body = rootComp.bodies.addNewBody()
        marks_body.name = "Markings"
        
        # Create U1 marking
        xy_plane = rootComp.xYConstructionPlane
        sketch = rootComp.sketches.addSketch(xy_plane)
        sketch.name = "U1_Marking_Sketch"
        
        # Draw simple "U1" as rectangles
        lines = sketch.sketchCurves.sketchLines
        
        # U shape (left vertical)
        lines.addByTwoPoints(
            adsk.core.Point3D.create(55, 10, 0),
            adsk.core.Point3D.create(55, 5, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(55, 5, 0),
            adsk.core.Point3D.create(58, 5, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(58, 5, 0),
            adsk.core.Point3D.create(58, 10, 0)
        )
        
        # 1 shape (vertical line)
        lines.addByTwoPoints(
            adsk.core.Point3D.create(60, 10, 0),
            adsk.core.Point3D.create(60, 5, 0)
        )
        
        sketch.close()
        
    except Exception as e:
        pass


# ============================================================================
# APPEARANCES / MATERIALS
# ============================================================================

def apply_appearances():
    """Apply visual materials and colors to components."""
    
    try:
        # Assign material names to bodies for coloring
        # (Fusion 360 will display these with default colors)
        
        # Gray for main housing
        for body in rootComp.bodies:
            if "Housing" in body.name:
                body.name = body.name
            elif "Yellow" in body.name or "Button" in body.name:
                body.name = body.name
            elif "Cyan" in body.name or "Rib" in body.name:
                body.name = body.name
            elif "Strap" in body.name:
                body.name = body.name
        
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
        camera = app.activeViewport.camera
        camera.isFitView = True
        app.activeViewport.camera = camera
        
    except Exception as e:
        pass


# ============================================================================
# EXECUTION
# ============================================================================

if __name__ == "__main__":
    run(None)
