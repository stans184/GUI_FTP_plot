import os

from GUI import GUI
from LoadInfo import LoadInfo

infoData = "lineInfo.xml"

if __name__ == "__main__":
    GUI.open(data=LoadInfo.loadFromXml(infoData))