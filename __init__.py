# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Qgis3Test
                                 A QGIS plugin
 Port of builder to python3
                             -------------------
        begin                : 2018-02-27
        copyright            : (C) 2018 by GeoApt LLC
        email                : gsherman@geoapt.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Qgis3Test class from file Qgis3Test.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Qgis3Test import Qgis3Test
    from .widgets import waiting_msg
    from .widgets.counting_base import CountingTest

    return Qgis3Test(iface)
