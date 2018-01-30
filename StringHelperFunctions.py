
#Remove unaccetable characters frmo a string - basic sanitization
def clean_string(cleaning_string):
    cleaning_string = cleaning_string.replace("'","")
    cleaning_string = cleaning_string.replace("(","")
    cleaning_string = cleaning_string.replace(")","")
    cleaning_string = cleaning_string.replace("[","")
    cleaning_string = cleaning_string.replace("]","")
    cleaning_string = cleaning_string.replace("~","")
    cleaning_string = cleaning_string.replace("!","")
    cleaning_string = cleaning_string.replace("%","")
    cleaning_string = cleaning_string.replace("^","")
    cleaning_string = cleaning_string.replace("*","")
    cleaning_string = cleaning_string.replace("/","")
    cleaning_string = cleaning_string.replace(".","_")
    cleaning_string = cleaning_string.replace(" ","_")
    return cleaning_string

