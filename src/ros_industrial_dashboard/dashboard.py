"""
   Copyright 2017 Austin Deric

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import os
import rospy
import rospkg

from threading import Thread
from qt_gui.plugin import Plugin
from python_qt_binding import loadUi
from python_qt_binding.QtCore import Qt, QThread
from python_qt_binding.QtWidgets import QWidget
from python_qt_binding.QtGui import QPalette
from std_srvs.srv import Trigger
from packml_msgs.srv import Transition
from packml_msgs.srv import TransitionRequest
from packml_msgs.msg import Status
from packml_msgs.msg import State
from packml_msgs.msg import Mode

class Dashboard(Plugin):

    def __init__(self, context):
        super(Dashboard, self).__init__(context)
        self.setObjectName('Dashboard')

        from argparse import ArgumentParser
        parser = ArgumentParser()

        parser.add_argument("-q", "--quiet", action="store_true",
                      dest="quiet",
                      help="Put plugin in silent mode")
        args, unknowns = parser.parse_known_args(context.argv())
        if not args.quiet:
            print 'arguments: ', args
            print 'unknowns: ', unknowns

        # Create QWidget
        self._widget = QWidget()
        ui_file = os.path.join(rospkg.RosPack().get_path('ros_industrial_dashboard'), 'resource', 'dashboard.ui')
        loadUi(ui_file, self._widget)
        self._widget.setObjectName('Dashboard')

        if context.serial_number() > 1:
            self._widget.setWindowTitle(self._widget.windowTitle() + (' (%d)' % context.serial_number()))

        context.add_widget(self._widget)

    @staticmethod
    def add_arguments(parser):
        rospy.loginfo("Add arguments callback")
        group = parser.add_argument_group('Options for PackML plugin')
        group.add_argument('--arg1', action='store_true', help='arg1 help')
