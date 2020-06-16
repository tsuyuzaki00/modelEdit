import pymel.core as pm

def main():
    sceneName = pm.sceneName().basename()
    part = sceneName.split("_")
    if part[0].endswith('.ma') or part[0].endswith('.mb'):
        scene = part[0][:-3]
    elif part[0] == '':
        scene = 'scene'
    else:
        scene = part[0]
    
    num = '1'.zfill(3)
    selFace = pm.selected()
    shape = pm.listRelatives(selFace, p = True)
    obj = pm.listRelatives(shape, p = True) 
    pm.polyChipOff(selFace, dup=False )
    pm.polySeparate(obj)
    pm.delete(ch = True)
    childs = pm.listRelatives( obj, c = True )
    for child in childs:
        pm.rename(child , '_'.join(['geo','model',scene,num]) )
        if pm.objExists( '_'.join(['grp','geo',scene]) ):
            pm.parent(child, '_'.join(['grp','geo',scene]) )
        else :
            pm.parent(child, w = True)
    pm.delete(obj)