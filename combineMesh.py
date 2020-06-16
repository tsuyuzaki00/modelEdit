import pymel.core as pm

def main():
    sels = pm.selected()
    sel = tuple(sels)
    pm.polyUnite( sel, n = sels[0])
    pm.delete(ch = True)