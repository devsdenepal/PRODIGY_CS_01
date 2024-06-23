def slowType(text):
    """
    Prints the text slowly.

    Parameters:
    text (str): The string to be printed.
    
    Returns:
    str: The printed text.
    """
    import time
    typing_speed = 50
    for char in text:
        print(char, end='', flush=True)
        time.sleep(10.0/typing_speed)
    print("\n")
# slowType("=============")