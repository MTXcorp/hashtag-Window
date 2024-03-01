import hash_DevSpray as DSpray

__version__ = "V2.1"
con = ""
currfilename = ""
workvarcurrfilename = ""
DSpray.cleanscr()
DSpray.menu("Create A File", "Open A File", "Configuration", "Show A Files Contents", "Hash Editor V " + __version__ + "P1/2")
DSpray.cursor("Hash Editor - No Option.")
if DSpray.DevSprayInput == 1:
    DSpray.Say("Name:")
    DSpray.cursor("Enter A Name. (With . Extension)")