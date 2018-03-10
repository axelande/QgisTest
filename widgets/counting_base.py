# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Qgis3TestDialog
                                 A QGIS plugin
 Port of builder to python3
                             -------------------
        begin                : 2018-02-27
        git sha              : $Format:%H$
        copyright            : (C) 2018 by GeoApt LLC
        email                : gsherman@geoapt.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
from time import sleep, time

from PyQt5 import uic, QtWidgets, QtCore

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'counting_base.ui'))


class CountingTest(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(CountingTest, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.my_timer = None
        self.task = None
        self.counting = None
        self.t0 = None

    def _update_text(self):
        tid = int(time() - self.t0)
        self.LSeconds.setText(str(tid))
        self.update()
        if tid == self.counting:
            self.done(0)
            return self.counting
        if self.task.isCanceled():
            self.done(0)
            return

    def run_count(self, task, counting):
        self.counting = int(counting)
        self.t0 = time()
        self.task = task
        self.show()
        self.my_timer = QtCore.QTimer(self)
        self.my_timer.timeout.connect(self._update_text)
        self.my_timer.start(1000)  # 1 sec intervall
        self.exec_()
        self.done(0)
        return counting
