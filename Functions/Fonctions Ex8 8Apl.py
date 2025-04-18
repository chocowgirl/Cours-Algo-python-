## QUESTION: ARE WE APPENDING THE LIST OR REPLACING THE LAST CHAR WITH THE SUPPLIED CHAR?

list = [".", ".", ".", ".", ".", ".",]


def list_appender(list, char):
    list.append(char)
    print(list)
    return list

list_appender(list, "B")