
def safe_input(question = " "):
    """
    function to return answer or None for the safe input
    """
    try:
        answer = input(question)
        return answer

    except (EOFError, KeyboardInterrupt):# I don't know how to account for EOFError.  I could not raise the error
        # print("ctrl z was pressed")
        return None

    

def main():

    answer = safe_input("Who is Yoda? ")

    if answer is None:
        print("There was an error or you pressed ^Z, ^C, ^D!!")
    else:
        print("Yoda is...", answer)
   

if __name__ == "__main__": 
    # safe_input("who is yoda ")
    main()
    
    