label nameselection:
    $ povname = renpy.input("Input Name:")
    $ povname = povname.strip()

    if not povname:
        $povname = "Emcee"

    return