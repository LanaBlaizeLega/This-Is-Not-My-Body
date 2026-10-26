screen plush:
    imagebutton:
        xpos 1
        ypos 0.5
        idle "plush.png"
        at custom_zoom1
        action Jump("plush_click")

transform custom_zoom1:
    zoom 0.65

screen cigarette:
    imagebutton:
        xpos 800
        ypos 10
        idle "cigarette.png"
        at custom_zoom2
        action Jump("cigarette_click")
    
transform custom_zoom2:
    zoom 0.5

screen mirror:
    imagebutton:
        xpos 1500
        ypos 100
        idle "mirror.png"
        at custom_zoom3
        action Jump("mirror_click")
    
transform custom_zoom3:
    zoom 0.45