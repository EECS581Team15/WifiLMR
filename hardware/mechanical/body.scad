$fn=20;
SPEAKER_WIDTH = 27;
SPEAKER_HEIGHT= 20;
BODY_HEIGHT = 120;
BODY_WIDTH = 55;
BODY_DEPTH = 30;
BODY_THICKNESS = 2.5;
BODY_CURVE = 5;
BODY_CENTER_X = (BODY_WIDTH + 2*BODY_CURVE)/2;

BACK_COVER_THICKNESS = 2;
BACK_COVER_OVERHANG = 2;
SCREEN_WIDTH = 46.6;
SCREEN_HEIGHT = 34.2;
PTT_CURVE = 3;
PTT_LENGTH = 25;
PTT_WIDTH = 10;
PTT_SKIRT_H = 2;
PTT_SKIRT_D = 3;
PTT_HEIGHT = 4 + BODY_THICKNESS;
BUTTON_CENTER_Z = BODY_CURVE+(BODY_HEIGHT*0.28);
BUTTON_THICKNESS = 2;

module regular_polygon(order, r=1)
{
 	angles=[ for (i = [0:order-1]) i*(360/order) ];
 	coords=[ for (th=angles) [r*cos(th), r*sin(th)] ];
 	polygon(coords);
 }

module Button(sides = 4, radius=5, height= 4, hollow=true, thick=BUTTON_THICKNESS)
{
    module _outline(r=radius)
    {
        difference()
        {
            minkowski()
            {
                linear_extrude(height)
                {
                    regular_polygon(sides, r);
                }
                sphere(thick);
            }
            translate([0, 0, -thick])
            {
                cylinder(r=r+thick, h=thick);
            }
        }
    }
    module _hollowOutline(r=radius)
    {
        if (hollow)
        {
            difference()
            {
                _outline(r);
                scalingFactor = (r * 2) / (thick * 2 + r * 2);
                translate([0, 0, -0.01])
                {
                    scale(scalingFactor)
                    {
                        _outline(r);
                    }
                }
            }
        } else {
            _outline(r);
        }
    }
    module _skirt()
    {
        intersection()
        {
            cylinder(r=radius+2*thick, h=thick);
            _hollowOutline(r=radius+thick-0.3);
        }
    }
    union()
    {
        _hollowOutline();
        cylinder(r=2, h=height-0.2);
        _skirt();
    }
}
module BackCover()
{
    color("Red")
    {
        cube([BODY_WIDTH + (BACK_COVER_OVERHANG*2),
              BACK_COVER_THICKNESS,
              BODY_HEIGHT+ (BACK_COVER_OVERHANG*2)]);
    }
}
module Screen()
{
    color("Pink")
    {
        linear_extrude(BODY_THICKNESS*1.4)
            square([SCREEN_WIDTH, SCREEN_HEIGHT]);
    }
}
module BodyOutline()
{
    translate([BODY_CURVE, BODY_CURVE, BODY_CURVE])
    {
        minkowski()
        {
            sphere(r=BODY_CURVE);
            cube([BODY_WIDTH, BODY_DEPTH, BODY_HEIGHT]);
        }
    }
}
module Body()
{
    difference()
    {
        color("Lime")
        {
            BodyOutline();
        }
        union()
        {
            // Hollow out body
            color("Green")
            {
                // Inside
                scalingFactorW = BODY_WIDTH/(BODY_WIDTH+BODY_THICKNESS * 2);
                scalingFactorD = BODY_DEPTH/(BODY_DEPTH+BODY_THICKNESS * 2);
                scalingFactorH = BODY_HEIGHT/(BODY_HEIGHT+BODY_THICKNESS * 2);
                translate([BODY_THICKNESS, BODY_THICKNESS, BODY_THICKNESS])
                scale([scalingFactorW, scalingFactorD*1.06, scalingFactorH])
                {
                    BodyOutline();
                }
            }
            color("Yellow")
            {
                // Rear cover
                translate([BODY_CURVE/2, BODY_DEPTH + (BODY_CURVE*1.6), BODY_CURVE/2])
                {
                    cube([BODY_WIDTH + (BACK_COVER_OVERHANG*2),
                              BACK_COVER_THICKNESS,
                              BODY_HEIGHT+ (BACK_COVER_OVERHANG*2)]);
                }
            }
            // Screen
            translate([(BODY_CURVE * 2 + BODY_WIDTH) / 2 - (SCREEN_WIDTH/2),
                             BODY_THICKNESS*1.1,
                             BUTTON_CENTER_Z+19.0])
            {
                rotate([90, 0, 0])
                {
                    Screen();
                }
            }
            // Microphone
            translate([BODY_CENTER_X - 13.3,
                            BODY_THICKNESS+ 0.5,
                             BUTTON_CENTER_Z + 10])
            {
                rotate([90, 0, 0])
                {
                    cylinder(r=1, h=BODY_THICKNESS+1);
                }
            }
            // PTT
            translate([BODY_THICKNESS + BUTTON_THICKNESS * 1.03,
                             BODY_DEPTH * 0.8,
                             BODY_HEIGHT * 0.7])
            {
                rotate([90,90,-90])
                {
                    scale([2.04, 1.02, 1])
                    {
                        rotate([0, 0, 45])
                        {
                            Button(height = 6, hollow=false);
                        }
                    }
                }
            }
            // D-pad
            translate([(BODY_WIDTH+(BODY_CURVE*2))/2,
                          BODY_THICKNESS+BUTTON_THICKNESS+0.3,
                          BODY_CURVE+(BODY_HEIGHT*0.25)])
            {
                rotate([90, 0, 0])
                {
                   Buttons(hollow=false, scaling=1.05);
                }
            }
            // Speaker Fins
            translate([(BODY_WIDTH+(BODY_CURVE * 2)-SPEAKER_WIDTH) / 2,
                              6,
                              BODY_HEIGHT * 1.0])
            {
                rotate([90, 90, 0])
                {
                    linear_extrude(12)
                        SpeakerFins();
                }
            }
        }
    }
}
module SpeakerOutline()
{
    CURVE = 5;
    translate([CURVE, CURVE, 0.5])
    {
        minkowski()
        {
            square([SPEAKER_HEIGHT - (2*CURVE),
                         SPEAKER_WIDTH - (2*CURVE)]);
            circle(CURVE);
        }
    }
}
module SpeakerFins()
{
    intersection()
    {
        SpeakerOutline();
        for(n= [0:6])
        {
            translate([n*3, 0, 0.5])
            {
                square([1.5, 27]);
            }
        }
    }
}

module Buttons(hollow=true, scaling=1)
{
    BUTTON_RADIUS = 3;
    offset = 13;
    // Down button
    translate([0, -offset, 0])
    {
        rotate([0, 0, -90])
        {
            scale([scaling, scaling, 1])
                Button(3, hollow=hollow);
        }
    }
    // Up button
    translate([0, offset, 0])
    {
        rotate(a=[0, 0, 90])
        {
            scale([scaling, scaling, 1])
                Button(3, hollow=hollow);
        }
    }
    // Left button
    translate([-offset, 0, 0])
    {
        rotate([0, 0, 60])
        {
            scale([scaling, scaling, 1])
                Button(3, hollow=hollow);
        }
    }
    // Right button
    translate([offset, 0, 0])
   {
       scale([scaling, scaling, 1])
            Button(3, hollow=hollow);
   }
   // Select button
   rotate([0, 0, 45])
   {
       scale([scaling, scaling, 1])
            Button(4, hollow=hollow);
   }
}
module Standoff(length=10)
{
    RADIUS = 3.175;
    FILLET_SIZE = 2;
    union()
    {
        translate([0, 0, length-FILLET_SIZE])
        {
            rotate_extrude(convexity = 10)
            {
                translate([-(FILLET_SIZE+6), 0, 0])
                {
                    difference()
                    {
                        square(FILLET_SIZE);
                        circle(FILLET_SIZE);
                    }
                }
            }
        }
        difference()
        {
           cylinder(r=6, h=length);
            translate([0, 0, -0.01])
                cylinder(r=3.175, h=3.2);
        }
    }
}
module WifiLMR()
{
    STANDOFFX1 = BODY_CENTER_X - 15; // taken from pcb
    STANDOFFX2 = BODY_CENTER_X + 3.8; // taken from pcb
    STANDOFFX3 = BODY_CENTER_X + 27;
    STANDOFFZ1 = BUTTON_CENTER_Z - 20.3; // taken from pcb
    STANDOFFZ3 = BUTTON_CENTER_Z + 61;
    PUSH_BUTTON_HEIGHT = 5;
    MAIN_STANDOFF_HEIGHT= PUSH_BUTTON_HEIGHT;
    intersection()
    {
        cube([BODY_WIDTH+BODY_CURVE*2,
                  BODY_THICKNESS+MAIN_STANDOFF_HEIGHT,
                  BODY_HEIGHT+BODY_CURVE*2]);
        union()
        {
            Body();
            
            /*
              * Main PCB Standoffs 
              */
            // Bottom left
            translate([STANDOFFX1, 
                            MAIN_STANDOFF_HEIGHT+BODY_THICKNESS, 
                            STANDOFFZ1])
                rotate([90, 0, 0])
                    Standoff(MAIN_STANDOFF_HEIGHT);

            // Bottom right
            translate([STANDOFFX3,
                             MAIN_STANDOFF_HEIGHT+BODY_THICKNESS, 
                             STANDOFFZ1])
                rotate([90, 0, 0])
                    Standoff(MAIN_STANDOFF_HEIGHT);
            // Top left
            translate([STANDOFFX1 - 5, 
                             MAIN_STANDOFF_HEIGHT+BODY_THICKNESS,
                             STANDOFFZ3])
                rotate([90, 0, 0])
                    Standoff(MAIN_STANDOFF_HEIGHT);
            // Top right
            translate([STANDOFFX3, 
                             MAIN_STANDOFF_HEIGHT+BODY_THICKNESS,
                             STANDOFFZ3])
                rotate([90, 0, 0])
                    Standoff(MAIN_STANDOFF_HEIGHT);
        }
    }
}
WifiLMR();
