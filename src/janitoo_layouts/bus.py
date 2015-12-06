# -*- coding: utf-8 -*-
"""The Raspberry hardware worker

Define a node for the cpu with 3 values : temperature, frequency and voltage

http://www.maketecheasier.com/finding-raspberry-pi-system-information/

"""

__license__ = """
    This file is part of Janitoo.

    Janitoo is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Janitoo is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Janitoo. If not, see <http://www.gnu.org/licenses/>.

"""
__author__ = 'Sébastien GALLET aka bibi21000'
__email__ = 'bibi21000@gmail.com'
__copyright__ = "Copyright © 2013-2014-2015 Sébastien GALLET aka bibi21000"

# Set default logging handler to avoid "No handler found" warnings.
import logging
logger = logging.getLogger(__name__)
import os, sys
import threading
import pickle
import datetime
from pkg_resources import get_distribution, DistributionNotFound
from janitoo.thread import JNTBusThread, BaseThread
from janitoo.options import get_option_autostart
from janitoo.utils import HADD, HADD_SEP
from janitoo.utils import TOPIC_VALUES_USERS, TOPIC_VALUES
from janitoo.utils import json_dumps, json_loads
from janitoo.component import JNTComponent
from janitoo.node import JNTNode
from janitoo.value import JNTValue
from janitoo.classes import COMMAND_DESC
from janitoo.bus import JNTBus
from janitoo.mqtt import MQTTClient
from janitoo.threads.http import HttpResourceComponent

##############################################################
#Check that we are in sync with the official command classes
#Must be implemented for non-regression
from janitoo.classes import COMMAND_DESC

COMMAND_CONTROLLER = 0x1050

assert(COMMAND_DESC[COMMAND_CONTROLLER] == 'COMMAND_CONTROLLER')
##############################################################

class LayoutsBus(JNTBus):
    """A pseudo-bus to manage layouts
    """
    def __init__(self, **kwargs):
        """
        """
        JNTBus.__init__(self, **kwargs)

    def check_heartbeat(self):
        """Check that the component is 'available'

        """
        #~ print "it's me %s : %s" % (self.values['upsname'].data, self._ups_stats_last)
        return False


    def start(self, mqttc, trigger_thread_reload_cb=None):
        JNTBus.start(self, mqttc, trigger_thread_reload_cb)

    def stop(self):
        JNTBus.stop(self)

