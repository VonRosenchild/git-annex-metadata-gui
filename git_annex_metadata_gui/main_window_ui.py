# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtdesigner-ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.widget_tabs.setObjectName("widget_tabs")
        self.tab_keys = QtWidgets.QWidget()
        self.tab_keys.setObjectName("tab_keys")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_keys)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.view_keys = QtWidgets.QTableView(self.tab_keys)
        self.view_keys.setAlternatingRowColors(True)
        self.view_keys.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.view_keys.setShowGrid(False)
        self.view_keys.setSortingEnabled(True)
        self.view_keys.setWordWrap(False)
        self.view_keys.setCornerButtonEnabled(False)
        self.view_keys.setObjectName("view_keys")
        self.view_keys.horizontalHeader().setDefaultSectionSize(150)
        self.view_keys.verticalHeader().setDefaultSectionSize(20)
        self.view_keys.verticalHeader().setMinimumSectionSize(20)
        self.verticalLayout.addWidget(self.view_keys)
        self.widget_tabs.addTab(self.tab_keys, "")
        self.tab_head = QtWidgets.QWidget()
        self.tab_head.setObjectName("tab_head")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_head)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.view_head = QtWidgets.QTreeView(self.tab_head)
        self.view_head.setUniformRowHeights(True)
        self.view_head.setSortingEnabled(True)
        self.view_head.setObjectName("view_head")
        self.view_head.header().setDefaultSectionSize(150)
        self.view_head.header().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.view_head)
        self.widget_tabs.addTab(self.tab_head, "")
        self.horizontalLayout.addWidget(self.widget_tabs)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_headers = QtWidgets.QMenu(self.menubar)
        self.menu_headers.setEnabled(False)
        self.menu_headers.setObjectName("menu_headers")
        self.menu_docks = QtWidgets.QMenu(self.menubar)
        self.menu_docks.setObjectName("menu_docks")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dock_preview = QtWidgets.QDockWidget(MainWindow)
        self.dock_preview.setObjectName("dock_preview")
        self.dock_preview_contents = QtWidgets.QWidget()
        self.dock_preview_contents.setObjectName("dock_preview_contents")
        self.gridLayout = QtWidgets.QGridLayout(self.dock_preview_contents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.stack_preview = QtWidgets.QStackedWidget(self.dock_preview_contents)
        self.stack_preview.setObjectName("stack_preview")
        self.page_text_preview = QtWidgets.QWidget()
        self.page_text_preview.setObjectName("page_text_preview")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_text_preview)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.text_preview = QtWidgets.QPlainTextEdit(self.page_text_preview)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.text_preview.setFont(font)
        self.text_preview.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.text_preview.setReadOnly(True)
        self.text_preview.setObjectName("text_preview")
        self.gridLayout_2.addWidget(self.text_preview, 0, 0, 1, 1)
        self.stack_preview.addWidget(self.page_text_preview)
        self.page_graphics_preview = QtWidgets.QWidget()
        self.page_graphics_preview.setObjectName("page_graphics_preview")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_graphics_preview)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.graphics_preview = QtWidgets.QGraphicsView(self.page_graphics_preview)
        self.graphics_preview.setObjectName("graphics_preview")
        self.gridLayout_3.addWidget(self.graphics_preview, 0, 0, 1, 1)
        self.stack_preview.addWidget(self.page_graphics_preview)
        self.gridLayout.addWidget(self.stack_preview, 0, 0, 1, 1)
        self.dock_preview.setWidget(self.dock_preview_contents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dock_preview)
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_refresh = QtWidgets.QAction(MainWindow)
        self.action_refresh.setObjectName("action_refresh")
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_refresh)
        self.menu_file.addAction(self.action_exit)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_headers.menuAction())
        self.menubar.addAction(self.menu_docks.menuAction())

        self.retranslateUi(MainWindow)
        self.widget_tabs.setCurrentIndex(0)
        self.action_exit.triggered.connect(MainWindow.close)
        self.action_refresh.triggered.connect(MainWindow.refresh_repo)
        self.action_open.triggered.connect(MainWindow.open_repo)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Git-Annex Metadata Gui"))
        self.widget_tabs.setTabText(self.widget_tabs.indexOf(self.tab_keys), _translate("MainWindow", "All Keys"))
        self.widget_tabs.setTabText(self.widget_tabs.indexOf(self.tab_head), _translate("MainWindow", "Work Tree"))
        self.menu_file.setTitle(_translate("MainWindow", "&File"))
        self.menu_headers.setTitle(_translate("MainWindow", "Headers"))
        self.menu_docks.setTitle(_translate("MainWindow", "Docks"))
        self.dock_preview.setWindowTitle(_translate("MainWindow", "File Preview"))
        self.action_open.setText(_translate("MainWindow", "&Open"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_exit.setText(_translate("MainWindow", "E&xit"))
        self.action_exit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action_refresh.setText(_translate("MainWindow", "&Refresh"))
        self.action_refresh.setShortcut(_translate("MainWindow", "F5"))

