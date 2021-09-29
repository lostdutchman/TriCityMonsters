label nameselection:
    $ povname = renpy.input("Input Name")
    $ povname = povname.strip()

    if not povname:
        $ povname = "Emcee"

    python:
        if povname.lower() == "mori":
            same_name_flag = True
        else: 
            same_name_flag = False

    return