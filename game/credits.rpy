screen credits():
    $ quick_menu = False
    
    imagemap:
        ground "credits1.png"
        idle "credits1.png"
        hover "credits2.png"
        hotspot(565, 228, 206, 44) action OpenURL("https://twitter.com/SoftDutch")
        hotspot(787, 228, 244, 45) action OpenURL("https://studiopeaches.itch.io/")
        hotspot(577, 530, 188, 53) action OpenURL("https://www.instagram.com/dela.png/")
        hotspot(336, 776, 358, 53) action OpenURL("https://lemmasoft.renai.us/forums/viewtopic.php?t=22098")
        hotspot(336, 861, 136, 50) action OpenURL("https://www.pexels.com/")
        hotspot(519, 859, 156, 53) action OpenURL("https://pixabay.com/")
        hotspot(1163, 107, 231, 55) action OpenURL("https://npckc.itch.io/pronoun-tool")
        hotspot(1170, 286, 227, 58) action OpenURL("https://www.kenney.nl/")
        hotspot(1167, 348, 340, 49) action OpenURL("https://freesound.org/")
        hotspot(1169, 399, 486, 53) action OpenURL("https://incompetech.com/")
        hotspot(1170, 483, 371, 49) action OpenURL("https://www.youtube.com/watch?v=-UDlsf0RfuI")
        hotspot(1167, 567, 456, 46) action OpenURL("https://www.youtube.com/watch?v=kGf9_EuAswc")
        hotspot(1166, 648, 403, 47) action OpenURL("https://www.youtube.com/watch?v=jX-0Wb_wQsY")
        hotspot(1154, 735, 318, 318) action OpenURL("http://www.lostdutchmansoftware.com")
        hotspot(1582, 981, 324, 59) action ShowTransient("main_menu")    

return
