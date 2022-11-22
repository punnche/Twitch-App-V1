import wx

def screensize():
    size = str(wx.GetDisplaySize())
    size = size.replace("(","")
    new_size = size.replace(",","")
    n_size = new_size.replace(")","")
    n_size = n_size.strip()
    for char in n_size:
        if char == " ":
            n_size = n_size.replace(" ","x")
            return n_size


