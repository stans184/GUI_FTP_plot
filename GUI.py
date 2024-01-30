import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.uic import loadUi

from FTPClient import FTPClient

class GUI(QMainWindow):
    
    @staticmethod
    def open(data):
        app = QApplication(sys.argv)
        window = GUI(data)
        window.show()
        sys.exit(app.exec_())
        
    # 종료 감지
    def closeEvent(self, event):
        print("program quit")
        event.accept()
    
    def __init__(self, data):
        self.data = data
        self.line = None
        self.machine_type = None
        self.machine_name = None
        
        super(GUI, self).__init__()
        
        # UI 파일 로드
        loadUi('Scanner Analyzer.ui', self)
        
        # Line type 초기화
        self.lineViewModel = QStandardItemModel(self)
        self.LineView.setModel(self.lineViewModel)
        
        # Machine Type 초기화
        self.machineTypeViewModel = QStandardItemModel(self)
        self.MachineTypeView.setModel(self.machineTypeViewModel)
        
        # Machine 초기화
        self.machineListViewModel = QStandardItemModel(self)
        self.MachineListView.setModel(self.machineListViewModel)
        
        # update line info
        self.updateLineView()
        
        # click event
        self.LineView.selectionModel().selectionChanged.connect(self.onLineSelected)
        self.MachineTypeView.selectionModel().selectionChanged.connect(self.onMachineTypeSelected)
        self.MachineListView.selectionModel().selectionChanged.connect(self.connectMachine)
    
    # update line info
    def updateLineView(self):
        self.lineViewModel.clear()
        for lineName in self.data.keys():
            self.lineViewModel.appendRow(QStandardItem(lineName))
            
    # select function
    def onLineSelected(self, selected):
        self.machine_type = None
        self.machineListViewModel.clear()
        self.machineTypeViewModel.clear()
        
        if selected.indexes():
            lineName = selected.indexes()[0].data()
            self.updateMachineTypeView(lineName)
            self.line = lineName
            
    # update machine type
    def updateMachineTypeView(self, lineName):
        self.machineTypeViewModel.clear()
        machineTypes = self.data[lineName].keys()
        for machineTypeName in machineTypes:
            self.machineTypeViewModel.appendRow(QStandardItem(machineTypeName))
    
    # select machine type
    def onMachineTypeSelected(self, selected):
        if selected.indexes():
            machineTypeName = selected.indexes()[0].data()
            lineIndex = self.LineView.currentIndex().row()
            lineName = self.lineViewModel.item(lineIndex).text()
            self.updateMachineView(lineName, machineTypeName)
            self.machine_type = machineTypeName
    
    # update machine list
    def updateMachineView(self, lineName, machineTypeName):
        self.machineListViewModel.clear()
        machines = self.data[lineName][machineTypeName]
        for machineName in machines:
            self.machineListViewModel.appendRow(QStandardItem(machineName))
            
    # machine connect
    # 정보 잘 빼옴
    # FTP 연결 테스트 해야함
    def connectMachine(self, selected):
        if selected.indexes():
            index = selected.indexes()[0]
            machine_name = self.machineListViewModel.itemFromIndex(index).text()
            # print(self.line, self.machine_type, machine_name)
            print(self.data[self.line][self.machine_type][machine_name])