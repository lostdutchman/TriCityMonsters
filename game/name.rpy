label nameselection:
    $ povname = renpy.input("Please sign in:")
    $ povname = povname.strip()

    if not povname:
        $povname = "Bababooie"

    return