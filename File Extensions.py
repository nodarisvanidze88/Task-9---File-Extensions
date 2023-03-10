extensions = {                                                          # create extension dictionary
    "gif": "Image",
    "jpg": "Image",
    "jpeg": "Image",
    "png": "Image",
    "pdf": "Variable Document",
    "txt": "Text File",
    "zip": "Archive File"
    }

def extensionGen(txt):                                                  # function get from user file extension value
    text = list(txt.strip().lower())                                        # format text and splyt by characters
    for item in range(len(text),0,-1):                                      # initiate for loop with counting back
        if text[item-1] ==".":                                              # if from the end is "." character
            break                                                           # if true break the loop
    extens = text[item:]                                                    # get characters list from "." to end of the string
    return "".join(extens)                                                  # get from the list string without "."

def main():
    fileName = input("File Name: ")                                     # ask to user file name
    ext = extensionGen(fileName)                                        # get from string extension value
    if ext in extensions:                                               # check if extension value is in dictionary
        value = extensions[ext]                                         # if true get key value
        print(value+"/"+ext)                                            # print concatnated dictionary value and extension
    else:
        print("I do not know what type file extension is "+ext)         # say that whe do not have this kind of file
main()
