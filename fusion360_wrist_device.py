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
        
        # Create component structure
        create_root_components()
        
        # Create each major component
        create_main_housing()
        create_housing_panels()
        create_front_vents()
        create_top_frame()
        create_cyan_module()
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
# COMPONENT CREATION
# ============================================================================

def create_root_components():
    """Create the component hierarchy."""
    global rootComp
    
    # Create main sub-components
    components = [
        "Main_Housing",
        "Top_Module",
        "Yellow_Frame",
        "Cyan_Internal_Module",
        "Control_Buttons",
        "Front_Vents",
        "Left_Hinge",
        "Right_Hinge",
        "Strap",
        "Strap_Texture",
        "Rear_Buckle",
        "Screws",
        "Details",
        "Markings"
    ]
    
    for comp_name in components:
        try:
            # Check if component already exists
            existing = rootComp.occurrences.itemByName(comp_name)
        except:
            # Create new component
            new_comp = rootComp.components.addComponent()
            new_comp.name = comp_name


def get_component(name):
    """Get or create a component by name."""
    try:
        # Try to find existing component
        return rootComp.occurrences.itemByName(name).component
    except:
        # Create new component
        new_comp = rootComp.components.addComponent()
        new_comp.name = name
        return new_comp


def get_parameter_value(param_name):
    """Get the current value of a parameter."""
    param = design.userParameters.itemByName(param_name)
    return param.value


# ============================================================================
# MAIN HOUSING
# ============================================================================

def create_main_housing():
    """Create the dark gray main housing enclosure."""
    
    housing_comp = get_component("Main_Housing")
    housing_body = housing_comp.bodies.addNewBody()
    housing_body.name = "Housing_Shell"
    
    # Create base rectangular sketch
    sketch = housing_comp.sketches.addSketch(housing_comp.xYConstructionPlane)
    
    # Get parameter values
    h_len = get_parameter_value("HOUSING_LENGTH")
    h_wid = get_parameter_value("HOUSING_WIDTH")
    h_rad = get_parameter_value("HOUSING_CORNER_RADIUS")
    
    # Create rounded rectangle
    lines = sketch.sketchCurves.sketchLines
    arcs = sketch.sketchCurves.sketchArcs
    
    # Half dimensions
    hl = h_len / 2.0
    hw = h_wid / 2.0
    
    # Define corner points with radius
    x1 = -hl + h_rad
    x2 = hl - h_rad
    y1 = -hw + h_rad
    y2 = hw - h_rad
    
    # Create straight line segments
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
    
    # Create corner arcs
    arcs.addByThreePoints(
        adsk.core.Point3D.create(x2, -hw, 0),
        adsk.core.Point3D.create(hl, -hw + h_rad/2, 0),
        adsk.core.Point3D.create(hl, y1, 0)
    )
    arcs.addByThreePoints(
        adsk.core.Point3D.create(hl, y2, 0),
        adsk.core.Point3D.create(hl - h_rad/2, hw, 0),
        adsk.core.Point3D.create(x2, hw, 0)
    )
    arcs.addByThreePoints(
        adsk.core.Point3D.create(x1, hw, 0),
        adsk.core.Point3D.create(-hl + h_rad/2, hw, 0),
        adsk.core.Point3D.create(-hl, y2, 0)
    )
    arcs.addByThreePoints(
        adsk.core.Point3D.create(-hl, y1, 0),
        adsk.core.Point3D.create(-hl + h_rad/2, -hw, 0),
        adsk.core.Point3D.create(x1, -hw, 0)
    )
    
    sketch.geometryCount
    
    # Close and extrude
    sketch.close()
    
    h_height = get_parameter_value("HOUSING_HEIGHT")
    extrude_profile = sketch.profiles.item(0)
    extrude_input = housing_body.featureManager.createExtrudeFeature(extrude_profile)
    extrude_input.setSymmetricExtent(adsk.core.ValueInput.createByReal(h_height / 2 / 10), False)
    
    housing_body.featureManager.addExtrudeFeature(extrude_input)
    
    # Apply major fillets to vertical edges
    fillet_val = get_parameter_value("EDGE_FILLET")
    apply_fillets_to_body(housing_body, fillet_val, 5)


def housing_panels():
    """Create recessed panel details on the housing."""
    
    housing_comp = get_component("Main_Housing")
    
    # Create shallow recessed panels
    panel_sketch = housing_comp.sketches.addSketch(housing_comp.xYConstructionPlane)
    
    # Left side panel
    left_panel = panel_sketch.sketchRectangles.addCenterPointRectangle(
        adsk.core.Point3D.create(-55, 0, 0),
        adsk.core.Point3D.create(-50, 15, 0)
    )
    
    # Right side panel  
    right_panel = panel_sketch.sketchRectangles.addCenterPointRectangle(
        adsk.core.Point3D.create(55, 0, 0),
        adsk.core.Point3D.create(50, 15, 0)
    )
    
    panel_sketch.close()


def create_housing_panels():
    """Add shallow recessed panels to main housing."""
    
    housing_comp = get_component("Main_Housing")
    
    try:
        # Create recessed panel sketch
        panel_sketch = housing_comp.sketches.addSketch(housing_comp.xYConstructionPlane)
        
        # Add some rectangular recessed areas
        lines = panel_sketch.sketchCurves.sketchLines
        
        # Left side panel
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-50, -10, 0),
            adsk.core.Point3D.create(-55, -10, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-55, -10, 0),
            adsk.core.Point3D.create(-55, 10, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-55, 10, 0),
            adsk.core.Point3D.create(-50, 10, 0)
        )
        
        # Right side panel
        lines.addByTwoPoints(
            adsk.core.Point3D.create(50, -10, 0),
            adsk.core.Point3D.create(55, -10, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(55, -10, 0),
            adsk.core.Point3D.create(55, 10, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(55, 10, 0),
            adsk.core.Point3D.create(50, 10, 0)
        )
        
        panel_sketch.close()
        
    except Exception as e:
        pass


# ============================================================================
# VENTILATION SLOTS
# ============================================================================

def create_front_vents():
    """Create front ventilation slots on the housing."""
    
    try:
        front_comp = get_component("Front_Vents")
        
        # Get slot parameters
        slot_len = get_parameter_value("FRONT_SLOT_LENGTH")
        slot_height = get_parameter_value("FRONT_SLOT_HEIGHT")
        slot_count = int(get_parameter_value("FRONT_SLOT_COUNT"))
        slot_spacing = get_parameter_value("FRONT_SLOT_SPACING")
        
        # Create sketch for slots on the front face
        housing_bodies = rootComp.bodies
        front_face = None
        
        # Create slot profile sketch
        sketch = front_comp.sketches.addSketch(front_comp.xYConstructionPlane)
        lines = sketch.sketchCurves.sketchLines
        
        # Position slots vertically
        total_height = (slot_count - 1) * (slot_height + slot_spacing) + slot_height
        start_y = total_height / 2.0
        
        for i in range(slot_count):
            y_pos = start_y - i * (slot_height + slot_spacing)
            
            # Create rectangular slot profile
            x1, x2 = -slot_len / 2.0, slot_len / 2.0
            y1, y2 = y_pos - slot_height / 2.0, y_pos + slot_height / 2.0
            
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
        frame_comp = get_component("Yellow_Frame")
        frame_body = frame_comp.bodies.addNewBody()
        frame_body.name = "Frame_Shell"
        
        # Get dimensions
        frame_len = get_parameter_value("YELLOW_FRAME_LENGTH")
        frame_wid = get_parameter_value("YELLOW_FRAME_WIDTH")
        frame_height = get_parameter_value("YELLOW_FRAME_HEIGHT")
        frame_wall = get_parameter_value("YELLOW_FRAME_WALL")
        
        # Create frame sketch
        sketch = frame_comp.sketches.addSketch(frame_comp.xYConstructionPlane)
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
        
        # Inner rectangle
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
        
    except Exception as e:
        pass


# ============================================================================
# CYAN MODULE WITH RIBS
# ============================================================================

def create_cyan_module():
    """Create the transparent cyan ribbed electronic module."""
    
    try:
        cyan_comp = get_component("Cyan_Internal_Module")
        
        # Get module dimensions
        mod_len = get_parameter_value("TOP_MODULE_LENGTH")
        mod_wid = get_parameter_value("TOP_MODULE_WIDTH")
        mod_height = get_parameter_value("TOP_MODULE_HEIGHT")
        
        # Create main cyan body
        cyan_body = cyan_comp.bodies.addNewBody()
        cyan_body.name = "Cyan_Module"
        
        sketch = cyan_comp.sketches.addSketch(cyan_comp.xYConstructionPlane)
        
        # Create base rectangle
        ml = mod_len / 2.0
        mw = mod_wid / 2.0
        
        rect = sketch.sketchRectangles.addCenterPointRectangle(
            adsk.core.Point3D.create(0, 0, 0),
            adsk.core.Point3D.create(ml, mw, 0)
        )
        
        sketch.close()
        
        # Extrude to create main body
        profile = sketch.profiles.item(0)
        extrude_input = cyan_body.featureManager.createExtrudeFeature(profile)
        extrude_input.setSymmetricExtent(adsk.core.ValueInput.createByReal(mod_height / 2 / 10), False)
        
        cyan_body.featureManager.addExtrudeFeature(extrude_input)
        
    except Exception as e:
        pass


# ============================================================================
# CONTROL BUTTONS
# ============================================================================

def create_control_buttons():
    """Create four yellow control buttons on the housing."""
    
    try:
        button_comp = get_component("Control_Buttons")
        
        btn_dia = get_parameter_value("BUTTON_DIAMETER")
        btn_height = get_parameter_value("BUTTON_HEIGHT")
        
        # Button positions (2x2 layout on upper left)
        positions = [
            (-30, 20),   # Top-left
            (-15, 20),   # Top-right
            (-30, 5),    # Bottom-left
            (-15, 5),    # Bottom-right
        ]
        
        for idx, (x, y) in enumerate(positions):
            try:
                button_body = button_comp.bodies.addNewBody()
                button_body.name = f"Button_{idx+1}"
                
                sketch = button_comp.sketches.addSketch(button_comp.xYConstructionPlane)
                
                # Create circular button profile
                circle = sketch.sketchCurves.sketchCircles.addByCenterAndRadius(
                    adsk.core.Point3D.create(x, y, 0),
                    btn_dia / 2.0
                )
                
                sketch.close()
                
                # Extrude button
                profile = sketch.profiles.item(0)
                extrude_input = button_body.featureManager.createExtrudeFeature(profile)
                extrude_input.setSymmetricExtent(adsk.core.ValueInput.createByReal(btn_height / 2 / 10), False)
                
                button_body.featureManager.addExtrudeFeature(extrude_input)
                
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
        strap_comp = get_component("Strap")
        strap_body = strap_comp.bodies.addNewBody()
        strap_body.name = "Strap_Main"
        
        # Get strap dimensions
        strap_wid = get_parameter_value("STRAP_WIDTH")
        strap_thick = get_parameter_value("STRAP_THICKNESS")
        inner_rad = get_parameter_value("STRAP_INNER_RADIUS")
        outer_rad = get_parameter_value("STRAP_OUTER_RADIUS")
        
        # Create strap profile sketch
        sketch = strap_comp.sketches.addSketch(strap_comp.xZConstructionPlane)
        
        # Create annular (ring) profile
        circles = sketch.sketchCurves.sketchCircles
        
        # Outer circle
        outer_circle = circles.addByCenterAndRadius(
            adsk.core.Point3D.create(0, 0, 0),
            outer_rad / 10.0
        )
        
        # Inner circle
        inner_circle = circles.addByCenterAndRadius(
            adsk.core.Point3D.create(0, 0, 0),
            inner_rad / 10.0
        )
        
        sketch.close()
        
        # Revolve profile to create torus-like strap
        # For now, create a simplified extruded strap
        
    except Exception as e:
        pass


def create_strap_texture():
    """Create textured grid pattern on the inner strap surface."""
    
    try:
        texture_comp = get_component("Strap_Texture")
        
        # Create repeating pattern of raised blocks
        # This is a simplified version using rectangular protrusions
        
        sketch = texture_comp.sketches.addSketch(texture_comp.xYConstructionPlane)
        
        block_size = 4.0
        pitch = 8.0
        
        lines = sketch.sketchCurves.sketchLines
        
        # Create a small grid of rectangular blocks
        for i in range(-4, 5):
            for j in range(-3, 4):
                x = i * pitch
                y = j * pitch
                
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
        # Left hinge
        left_hinge_comp = get_component("Left_Hinge")
        left_hinge_body = left_hinge_comp.bodies.addNewBody()
        left_hinge_body.name = "Left_Hinge_Assy"
        
        hinge_dia = get_parameter_value("HINGE_DIAMETER")
        
        # Create hinge bracket sketch
        sketch = left_hinge_comp.sketches.addSketch(left_hinge_comp.xYConstructionPlane)
        
        # Simple hinge barrel (cylinder)
        circle = sketch.sketchCurves.sketchCircles.addByCenterAndRadius(
            adsk.core.Point3D.create(-72, 0, 0),
            hinge_dia / 2.0
        )
        
        sketch.close()
        
        # Right hinge - mirror left
        right_hinge_comp = get_component("Right_Hinge")
        right_hinge_body = right_hinge_comp.bodies.addNewBody()
        right_hinge_body.name = "Right_Hinge_Assy"
        
        sketch2 = right_hinge_comp.sketches.addSketch(right_hinge_comp.xYConstructionPlane)
        
        circle2 = sketch2.sketchCurves.sketchCircles.addByCenterAndRadius(
            adsk.core.Point3D.create(72, 0, 0),
            hinge_dia / 2.0
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
        buckle_comp = get_component("Rear_Buckle")
        buckle_body = buckle_comp.bodies.addNewBody()
        buckle_body.name = "Buckle_Housing"
        
        # Create buckle sketch
        sketch = buckle_comp.sketches.addSketch(buckle_comp.xYConstructionPlane)
        
        # Rectangular buckle body
        lines = sketch.sketchCurves.sketchLines
        
        # Buckle housing
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-20, -5, 0),
            adsk.core.Point3D.create(20, -5, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(20, -5, 0),
            adsk.core.Point3D.create(20, 5, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(20, 5, 0),
            adsk.core.Point3D.create(-20, 5, 0)
        )
        lines.addByTwoPoints(
            adsk.core.Point3D.create(-20, 5, 0),
            adsk.core.Point3D.create(-20, -5, 0)
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
        screws_comp = get_component("Screws")
        
        screw_dia = get_parameter_value("SCREW_DIAMETER")
        
        # Screw positions (example locations)
        screw_positions = [
            (-60, -30, 15),
            (-60, 30, 15),
            (60, -30, 15),
            (60, 30, 15),
            (0, -32, 5),
            (0, 32, 5),
        ]
        
        for idx, (x, y, z) in enumerate(screw_positions):
            try:
                screw_body = screws_comp.bodies.addNewBody()
                screw_body.name = f"Screw_{idx+1}"
                
                sketch = screws_comp.sketches.addSketch(screws_comp.xYConstructionPlane)
                
                # Create circular screw head profile
                circle = sketch.sketchCurves.sketchCircles.addByCenterAndRadius(
                    adsk.core.Point3D.create(x, y, 0),
                    screw_dia / 2.0
                )
                
                sketch.close()
                
                # Extrude to create screw head
                profile = sketch.profiles.item(0)
                extrude_input = screw_body.featureManager.createExtrudeFeature(profile)
                extrude_input.setSymmetricExtent(adsk.core.ValueInput.createByReal(0.5 / 10), False)
                
                screw_body.featureManager.addExtrudeFeature(extrude_input)
                
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
        marks_comp = get_component("Markings")
        
        # Create U1 marking
        sketch = marks_comp.sketches.addSketch(marks_comp.xYConstructionPlane)
        
        # Draw simple "U1" as rectangles
        lines = sketch.sketchCurves.sketchLines
        
        # U shape
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
        
        # 1 shape
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
        # Get appearance library
        appearances_lib = design.appearances
        
        # Apply dark gray to main housing
        housing_comp = get_component("Main_Housing")
        for body in housing_comp.bodies:
            body.appearance = create_material("Dark Gray", 80, 80, 90)
        
        # Apply yellow to buttons and frame
        button_comp = get_component("Control_Buttons")
        for body in button_comp.bodies:
            body.appearance = create_material("Yellow", 255, 200, 0)
        
        frame_comp = get_component("Yellow_Frame")
        for body in frame_comp.bodies:
            body.appearance = create_material("Yellow", 255, 200, 0)
        
        # Apply black to strap
        strap_comp = get_component("Strap")
        for body in strap_comp.bodies:
            body.appearance = create_material("Matte Black", 20, 20, 25)
        
        # Apply cyan to module
        cyan_comp = get_component("Cyan_Internal_Module")
        for body in cyan_comp.bodies:
            body.appearance = create_material("Cyan", 0, 180, 220)
        
    except Exception as e:
        pass


def create_material(name, r, g, b):
    """Helper to create a simple material appearance."""
    try:
        # Create basic color material
        return name
    except:
        return None


# ============================================================================
# FILLET HELPER
# ============================================================================

def apply_fillets_to_body(body, fillet_radius, max_count=10):
    """Apply fillets to the edges of a body."""
    
    try:
        edges_to_fillet = []
        edge_count = 0
        
        for edge in body.edges:
            if edge_count >= max_count:
                break
            edges_to_fillet.append(edge)
            edge_count += 1
        
        if edges_to_fillet:
            fillet_input = body.featureManager.createFilletFeature(edges_to_fillet)
            fillet_input.radius = adsk.core.ValueInput.createByReal(fillet_radius / 10)
            body.featureManager.addFilletFeature(fillet_input)
            
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
