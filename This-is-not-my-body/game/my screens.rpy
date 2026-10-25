screen plush:
    imagebutton:
        xpos 800
        ypos 20
        idle "plush.png"
        at custom_zoom
        action Jump("plush_click")

transform custom_zoom:
    zoom 0.5

screen cigarette:
    imagebutton:
        xpos 800
        ypos 20
        idle "cigarette.png"
        at custom_zoom
        action Jump("cigarette_click")
    
transform custom_zoom:
    zoom 0.7

screen mirror:
    imagebutton:
        xpos 800
        ypos 20
        idle "mirror.png"
        at custom_zoom
        action Jump("mirror_click")
    
transform custom_zoom:
    zoom 0.7