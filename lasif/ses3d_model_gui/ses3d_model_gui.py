# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/lion/workspace/code/LASIF/lasif/ses3d_model_gui/ses3d_model_gui.ui'
#
# Created: Sat Feb 14 00:06:39 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(1463, 813)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mapView = Qt4MplCanvas(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapView.sizePolicy().hasHeightForWidth())
        self.mapView.setSizePolicy(sizePolicy)
        self.mapView.setMinimumSize(QtCore.QSize(500, 0))
        self.mapView.setObjectName(_fromUtf8("mapView"))
        self.verticalLayout.addWidget(self.mapView)
        self.histogram = Qt4MplCanvas(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.histogram.sizePolicy().hasHeightForWidth())
        self.histogram.setSizePolicy(sizePolicy)
        self.histogram.setMinimumSize(QtCore.QSize(500, 150))
        self.histogram.setMaximumSize(QtCore.QSize(16777215, 150))
        self.histogram.setObjectName(_fromUtf8("histogram"))
        self.verticalLayout.addWidget(self.histogram)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.colorbar = Qt4MplCanvas(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorbar.sizePolicy().hasHeightForWidth())
        self.colorbar.setSizePolicy(sizePolicy)
        self.colorbar.setMinimumSize(QtCore.QSize(100, 0))
        self.colorbar.setMaximumSize(QtCore.QSize(100, 16777215))
        self.colorbar.setObjectName(_fromUtf8("colorbar"))
        self.horizontalLayout_2.addWidget(self.colorbar)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_2.addWidget(self.line_2)
        self.depth_slider = QtGui.QSlider(self.centralwidget)
        self.depth_slider.setOrientation(QtCore.Qt.Vertical)
        self.depth_slider.setInvertedAppearance(True)
        self.depth_slider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.depth_slider.setObjectName(_fromUtf8("depth_slider"))
        self.horizontalLayout_2.addWidget(self.depth_slider)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_2.addWidget(self.line)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.model_selection_comboBox = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_selection_comboBox.sizePolicy().hasHeightForWidth())
        self.model_selection_comboBox.setSizePolicy(sizePolicy)
        self.model_selection_comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.model_selection_comboBox.setEditable(False)
        self.model_selection_comboBox.setProperty("currentText", _fromUtf8(""))
        self.model_selection_comboBox.setObjectName(_fromUtf8("model_selection_comboBox"))
        self.gridLayout.addWidget(self.model_selection_comboBox, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.variable_selection_comboBox = QtGui.QComboBox(self.centralwidget)
        self.variable_selection_comboBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.variable_selection_comboBox.sizePolicy().hasHeightForWidth())
        self.variable_selection_comboBox.setSizePolicy(sizePolicy)
        self.variable_selection_comboBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.variable_selection_comboBox.setEditable(False)
        self.variable_selection_comboBox.setProperty("currentText", _fromUtf8(""))
        self.variable_selection_comboBox.setObjectName(_fromUtf8("variable_selection_comboBox"))
        self.gridLayout.addWidget(self.variable_selection_comboBox, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.plotted_depth_label = QtGui.QLabel(self.centralwidget)
        self.plotted_depth_label.setObjectName(_fromUtf8("plotted_depth_label"))
        self.verticalLayout_2.addWidget(self.plotted_depth_label)
        self.depth_label = QtGui.QLabel(self.centralwidget)
        self.depth_label.setObjectName(_fromUtf8("depth_label"))
        self.verticalLayout_2.addWidget(self.depth_label)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_2.addWidget(self.line_4)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radio_button_absolute = QtGui.QRadioButton(self.groupBox)
        self.radio_button_absolute.setEnabled(True)
        self.radio_button_absolute.setChecked(True)
        self.radio_button_absolute.setObjectName(_fromUtf8("radio_button_absolute"))
        self.horizontalLayout.addWidget(self.radio_button_absolute)
        self.radio_button_relative = QtGui.QRadioButton(self.groupBox)
        self.radio_button_relative.setObjectName(_fromUtf8("radio_button_relative"))
        self.horizontalLayout.addWidget(self.radio_button_relative)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_2.addWidget(self.line_3)
        self.clear_profiles_button = QtGui.QPushButton(self.centralwidget)
        self.clear_profiles_button.setObjectName(_fromUtf8("clear_profiles_button"))
        self.verticalLayout_2.addWidget(self.clear_profiles_button)
        self.depth_profile = Qt4MplCanvas(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.depth_profile.sizePolicy().hasHeightForWidth())
        self.depth_profile.setSizePolicy(sizePolicy)
        self.depth_profile.setMinimumSize(QtCore.QSize(300, 0))
        self.depth_profile.setObjectName(_fromUtf8("depth_profile"))
        self.verticalLayout_2.addWidget(self.depth_profile)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(0, 12)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)
        self.horizontalLayout_2.setStretch(4, 1)
        self.horizontalLayout_2.setStretch(5, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SES3D Model GUI", None))
        self.label.setText(_translate("MainWindow", "Model", None))
        self.label_2.setText(_translate("MainWindow", "Variable", None))
        self.plotted_depth_label.setText(_translate("MainWindow", "Plotted Depth", None))
        self.depth_label.setText(_translate("MainWindow", "Desired Depth", None))
        self.groupBox.setTitle(_translate("MainWindow", "Style", None))
        self.radio_button_absolute.setText(_translate("MainWindow", "Absolute", None))
        self.radio_button_relative.setText(_translate("MainWindow", "Relative", None))
        self.clear_profiles_button.setText(_translate("MainWindow", "Clear all Profiles", None))

from lasif.misfit_gui.qt4mplcanvas import Qt4MplCanvas
