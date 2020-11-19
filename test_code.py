def triangulito2(char,space_char,n_rows):
    
    """
    Draw an acute triangle, aligned on the center. Each `char` separated by `space_char`.\n

    char: character to draw the figure.\n
    space_char: character to mark spaces.\n
    n_rows: triangle size, the number of rows.\n

    returns: print the figure.
    """

    rows = list(range(1,n_rows+1))
    for row in rows:
        # spaces at start
        spaces = (n_rows - row) * space_char
        
        # Total chars in row (char to draw + spaces)
        length = 2*row-1
        characters = char

        for i in list(range(1,length)):

            if i%2==0:
                append_char = char
            else:
                append_char = space_char

            characters = characters + append_char

        # Final row
        result = spaces + characters

        print(result)