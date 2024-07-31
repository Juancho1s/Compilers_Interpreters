symbolicTable = {
    """
    I have tought to implement the corresponding name of each identifier without repetition
    """
    "name": [],
    
    """
    As you would have tought, I will add the corresponding type of each variable (both; 'name' and 'type' are equally indexed)
    """
    "type": [],
    
    """
    The value field represents a space on memory to hold the corresponding value of each variable. It is redundant to say 'type', and
    'name' are equally indexed than this field
    """
    "value": [],
    
    """
    This is the most abstract list on the 'symbolicTable' data structure, since here I will storage a path
    where the previous element is higher priority than the following one; I mean, it is like groups which represent the scopes
    there can be in the source. 
    Because I define 'scope' as a dynamic structure there will exist multiple lists with each corresponding structure, consider; 
    FOR STAT, WHILE STAT, IF STAT, and MAIN as first set; [[FOR STAT(identifiers)], [WHILE STAT(identifiers)],
    [IF STAT(identifiers)], [MAIN(identifiers)]] so there I can control which is greater scope than another
    """
    "scope": []
}