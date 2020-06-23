# a function that takes multiple arguements use ** n/b uses dictinaries    
def fav_elder(**facilitator):
    for elder,course in facilitator.items():
        print(f"{elder} is the best facilitator for {course}")
fav_elder(Nonso = "java",Christian = "python",Tobi ="Spring",Seyi ="database")