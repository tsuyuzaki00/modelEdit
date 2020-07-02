import maya.cmds as cmds

def main():
    camImageOffsetConnection()

def camImageOffsetConnection():
    cam = cmds.ls(sl=1,dag=1,typ = 'camera')
    connections = cmds.listConnections(cam,t = 'imagePlane')
    imagePs =  []
    for connection in connections:
        imagePs.append(connection.replace(cam[0]+'->',''))
    
    for imageP in imagePs:
        cmds.connectAttr(cam[0]+'.filmOffset',imageP+'.offset')