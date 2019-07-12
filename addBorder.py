def addBorder(picture):
    output = []
    border = ""
    for i in range(0,len(picture[0])+2):
        border += "*"
    output.append(border)
    for i in range(0,len(picture)):
        output.append("*"+picture[i]+"*")
    
    output.append(border)
    
    return output