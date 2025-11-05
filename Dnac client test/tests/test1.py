# tests/test_ap_client_join.py
# Author: Manjunath Sai
# Project: Cisco DNAC - AP & Client Join Test Automation
# Description: Automates verification of AP and Client join on WLC using PyATS

import logging
from datetime import datetime
from pyats import aetest
from genie.testbed import load
from utils import log_result, validate_output

# Setup logging
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
logging.basicConfig(
    filename=f'logs/test_run_{timestamp}.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

logger = logging.getLogger(__name__)

class CommonSetup(aetest.CommonSetup):
    """Connect to devices in the testbed"""

    @aetest.subsection
    def connect_to_devices(self, testbed):
        self.parent.parameters['devices'] = {}
        logger.info("Connecting to all devices in testbed...")
        for device in testbed.devices.values():
            try:
                device.connect(log_stdout=False)
                self.parent.parameters['devices'][device.name] = device
                logger.info(f"Connected to {device.name}")
            except Exception as e:
                logger.error(f"Failed to connect to {device.name}: {e}")
                self.failed(f"Connection failed for {device.name}")

# ---------------- Main Test Case ---------------- #

class VerifyAPClientJoin(aetest.Testcase):

    @aetest.test
    def check_ap_join(self, devices):
        """Check if AP is registered on WLC"""
        logger.info("Checking AP registration on WLC...")
        wlc = devices['WLC']
        output = wlc.execute('show ap summary')
        if validate_output(output, 'Registered'):
            log_result("AP Registration", "PASS")
        else:
            log_result("AP Registration", "FAIL")
            self.failed("No APs registered to WLC")

    @aetest.test
    def check_client_join(self, devices):
        """Check if client device has joined"""
        logger.info("Checking client connection...")
        wlc = devices['WLC']
        output = wlc.execute('show client summary')
        if validate_output(output, 'Connected'):
            log_result("Client Join", "PASS")
        else:
            log_result("Client Join", "FAIL")
            self.failed("Client not connected")

    @aetest.test
    def verify_client_ping(self, devices):
        """Verify client connectivity"""
        logger.info("Verifying client connectivity with ping...")
        client = devices['Client']
        output = client.execute('ping 192.168.1.1')
        if validate_output(output, 'Success rate is 100 percent'):
            log_result("Client Ping", "PASS")
        else:
            log_result("Client Ping", "FAIL")
            self.failed("Ping test failed")

class CommonCleanup(aetest.CommonCleanup):
    """Disconnect all devices after test"""

    @aetest.subsection
    def disconnect(self, steps, devices):
        for device in devices.values():
            device.disconnect()
            logger.info(f"Disconnected from {device.name}")
        log_result("Cleanup", "Completed")

if __name__ == '__main__':
    testbed = load('testbed.yaml')
    aetest.main(testbed=testbed)
