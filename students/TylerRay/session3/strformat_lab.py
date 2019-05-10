tpl1 = ( 2, 123.4567, 10000, 12345.67)

def printTuple(tpl1):
    v1 = "file_{0:03}: ".format(tpl1[0])
    v2 = "{0:.2f}".format(tpl1[1])
    v3 = "{:.2e}".format(tpl1[2])
    v4 = "{0:.2e}".format(tpl1[3])
    return f"{v1} {v2} {v3} {v4}"

    # fileName = 'file_{0:03}:  '.format(tpl1[0])
    #
    # fileData = "{0:.2f}".format(tpl1[1]),  	"{:.2e}".format(tpl1[2]), "{0:.2e}".format(tpl1[3])
    #
    # return fileName, fileData

print(printTuple(tpl1))

