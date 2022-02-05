def menu():
    print("--------------Seraph Financials-------------------")
    print("[1] 1,5,15,30 min Plotly Charts (with TwelveData) ")
    print("[2] Options Chain Data (with TwelveData)")
    print("[3] Daily Charts (with Finviz)")
    print("[4] Pull List of Stocks")
    print("[5] Pull Stock Quote (Yahoo)")
    print("[6] Pull Sec.gov Filings")
    print("--------------------------------------------------")
    print("------------Black Hole Indexing-------------------")
    print("[7] Spin up the search engine [OFF] ")
    print("[8] Re/Index data folders with Black Hole[OFF]")
    print("[9] Check Status: Black Hole [OFF]")
    print("--------------------------------------------------")
    print("---------------Automation-------------------------")
    print("[D] Spinup The Dockers [INACTIVE]")
    print("-------------Authentication-----------------------")
    print("[T] Select Authentication Tokens")
    print ("[0] Quit")
menu()
print()
print("all data located in /data/ folder")
options = int(input("Make a selection:"))

while options != 0:
    # 0 Quits App
    if options == 1:
    # selection 1
    
        print("")
    elif options == 2:
    # selection 2
    
        print("")
    elif options == 3:
        # selection 2
        
        print("")
    elif options == 4:
        # selection 2
        
        print("")
    elif options == 5:
        # selection 2
        
        print("")
    elif options == 6:
        # selection 2
        
        print("")
    else: print("Invalid Selection")
    menu()
    options = int(input("Make another Selection"))
print("Seraph has left this terminal.")