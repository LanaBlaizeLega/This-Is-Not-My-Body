# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define g = Character("Gnina")
define n = ("  ")
define m = ("mom")

image hand = "hand.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene background

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    n "C’est mon anniversaire."

    n "Un mauvais pressentiment me donne mal au ventre"

    call screen plush
    ##la main ne s'affiche pas et la transition n'apparaît pas
    ##il faut que je la répare plus tard

 
label plush_click:

    scene bg room plush

    g "Lorem ipsum dolor sit amet consectetur adipiscing elit."

    g "Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas."

    scene bg bday

    show gnina_afraid_night

    m "Lorem ipsum dolor sit amet consectetur adipiscing elit."

    show mom_night

    m "Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas."

    hide mom_night

    m "Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas."

    g "Lorem ipsum dolor sit amet consectetur adipiscing elit."

    g "Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas."

    m "Lorem ipsum dolor sit amet consectetur adipiscing elit."

    scene bg room plush

    call screen cigarette

label cigarette_click:

    scene bg room cigarette

    g "Lorem ipsum dolor sit amet consectetur adipiscing elit."

    scene bg kitchen

    call screen mirror

label mirror_click:

    scene bg room mirror

    g "Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas."

    # These display lines of dialogue.

   
    # This ends the game.

return
