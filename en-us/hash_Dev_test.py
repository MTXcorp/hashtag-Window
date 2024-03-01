import hash_DevSpray as DSpray

DSpray.Say("this is a test of the DevSpray Dev Platform For hash Window.")
DSpray.menu("test1", 
            "this is a test", 
            "", 
            "", 
            "DSpray Menu Test")
DSpray.cursor("Press 9 For Another Menu, Press 8 To Go Back.")
if DSpray.DevSprayInput == "9":
    DSpray.menu("Test 2",
                "this is a test",
                "123",
                "456",
                "test")
    DSpray.cursor("Press 9 to go an another menu. Press 8 To Return to")