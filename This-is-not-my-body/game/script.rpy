# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define g = Character("Gnina")
define n = ("  ")

image hand = "hand.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    n "C’est mon anniversaire."

    n "Un mauvais pressentiment me donne mal au ventre"

    call screen plush
    ##la main ne s'affiche pas et la transition n'apparaît pas
    ##il faut que je la répare plus tard

    show hand 
    show hand with moveintop
    show hand with moveinbottom

label plush_click:

    scene bg room plush

    g "Mes yeux commencent à se remplir de larmes; mes amis ne sont pas venus.
"

    g "Et maintenant mes mains tremble car maman me lance des regards noir."

    call screen cigarette

label cigarette_click:

    scene bg room cigarette

    g "Mes yeux commencent à se remplir de larmes; mes amis ne sont pas venus."
    call screen mirror

label mirror_click:

    scene bg room mirror

    g "Mes yeux commencent à se remplir de larmes; mes amis ne sont pas venus."

    # These display lines of dialogue.

   
    # This ends the game.

return
