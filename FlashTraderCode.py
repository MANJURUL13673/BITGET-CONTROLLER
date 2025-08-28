import threading
import time
from PyQt5.QtCore import QTimer, pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication
from BitgetConn import BitgetConn

class FlashTraderCode:
    BitgetHwnd = None

    # intialize of Flash Trader code
    def __init__(self, gui):
        self.gui = gui
        self.BitgetHwnd = BitgetConn()
        self.timer = QTimer()
        self.timer.timeout.connect(self._perform_api_test)  # Thread for running API tests
        self.is_testing = False
        self.last_status = None
        self.test_count = 0
        self.usdt_value = 0
        self.selectedLongBtn = None
        self.selectedShortBtn = None
        self.param = {"symbol": "ETHUSDT_UMCBL"}

    # Event for connect button
    def connectBitget(self):
        success = self.BitgetHwnd.Connect()
        if success:
            print("Bitget API connected successfully.")
            self.last_status = True
            self.start_testing()
        else:
            self.last_status = False
            print("Bitget API connection failed.")

    # Event for disconnect button
    def disconnectBitget(self):
        self.stop_testing()
        self.last_status = False
        print("Bitget API disconnected.")

        # Change the label
        self.gui.labels["API tester"].setStyleSheet("font-weight: normal; font-size: 10px; color: #00FF00;")
        self.gui.labels["API tester"].setText(f"No\nConnection")
        

    # Start the API Testing
    def start_testing(self):
        """Start the API connection testing."""
        self.is_testing = True
        self.timer.start(1000)
        print("Started API connection testing.")

    # Stop the API Testing
    def stop_testing(self):
        """Stop the API connection testing."""
        self.is_testing = False
        self.test_count = 0
        self.timer.stop()
        print("Stopped API connection testing.")
    
    # API Testing thread
    def APIThreadTest(self):
        """Test API connection - runs in main thread but non-blocking"""
        try:
            # Run the actual API call in a separate thread to avoid blocking UI
            thread = threading.Thread(target=self._perform_api_test, daemon=True)
            thread.start()
        except Exception as e:
            print(f"Error starting API test thread: {e}")

    # API Testing perform function
    def _perform_api_test(self):
        """Actual API test - runs in background thread"""
        self.test_count += 1
        remaining_time = 30 - (self.test_count * 1)

        self.last_status, self.usdt_value = self.BitgetHwnd.APITest(self.param)
        if self.last_status:
            self.gui.labels["Current Price"].setStyleSheet("color: #11F011; font-size: 20px; border: none;")
            self.gui.labels["API tester"].setStyleSheet("font-weight: normal; font-size: 10px; color: #00FF00;")
        else:
            self.gui.labels["Current Price"].setStyleSheet("color: #11F011; font-size: 20px; border: none;")
            self.gui.labels["API tester"].setStyleSheet("font-weight: normal; font-size: 10px; color: #FF0000;")
            self.connectBitget()

        if self.last_status:
            self.gui.labels["Current Price"].setText(f"{self.usdt_value}")
            self.gui.labels["API tester"].setText(f"Test OK\nNext test in {remaining_time} sec")
        else:
            self.gui.labels["Current Price"].setText(f"0")
            self.gui.labels["API tester"].setText(f"Test Failed\nNext test in {remaining_time} sec")

        if self.test_count >= 30:
            self.test_count = 0

    def onCoinChanged(self, text):
        self.gui.labels["Symbol"].setText(f"{text}")
        self.param["symbol"] = text.replace(" / ", "") + "_UMCBL"
        print(self.param["symbol"])

    def changeBtnStyleSelected(self, buttonName, side):
        if side == "long":
            self.selectedLongBtn = buttonName
        else:
            self.selectedShortBtn = buttonName

        self.gui.buttons[buttonName].setStyleSheet(f"""
            QPushButton {{
                background-color: #003334;
                color: #04F806;
                border-radius: 3px;
                padding: 10px;
                margin: 2px 2px 0px 0px;
                font-size: 15px;
                font-weight: bold;
            }}

        """)

    def changeBtnStyleDeselected(self, buttonName, side):
        if(buttonName is None):
            return

        if side == "long":
            self.selectedLongBtn = None
        else:
            self.selectedShortBtn = None

        self.gui.buttons[buttonName].setStyleSheet(f"""
            QPushButton {{
                background-color: #E6E6E6;
                color: #333333;
                border-radius: 3px;
                padding: 10px;
                margin: 2px 2px 0px 0px;
                font-size: 15px;
                font-weight: bold;
            }}

        """)

    # profit button event
    def onProfitLong5(self):
        selected = self.selectedLongBtn
        self.changeBtnStyleDeselected(self.selectedLongBtn, "long")

        if selected == "5long":
            return

        self.changeBtnStyleSelected("5long", "long")

    def onProfitLong10(self):
        selected = self.selectedLongBtn
        self.changeBtnStyleDeselected(self.selectedLongBtn, "long")

        if selected == "10long":
            return

        self.changeBtnStyleSelected("10long", "long")

    def onProfitLong12(self):
        selected = self.selectedLongBtn
        self.changeBtnStyleDeselected(self.selectedLongBtn, "long")

        if selected == "12long":
            return

        self.changeBtnStyleSelected("12long", "long")

    def onProfitLong15(self):
        selected = self.selectedLongBtn
        self.changeBtnStyleDeselected(self.selectedLongBtn, "long")

        if selected == "15long":
            return

        self.changeBtnStyleSelected("15long", "long")

    def onProfitLong17(self):
        selected = self.selectedLongBtn
        self.changeBtnStyleDeselected(self.selectedLongBtn, "long")

        if selected == "17long":
            return

        self.changeBtnStyleSelected("17long", "long")

    def onProfitLong20(self):
        selected = self.selectedLongBtn
        self.changeBtnStyleDeselected(self.selectedLongBtn, "long")

        if selected == "20long":
            return

        self.changeBtnStyleSelected("20long", "long")

    def onProfitLong25(self):
        selected = self.selectedLongBtn
        self.changeBtnStyleDeselected(self.selectedLongBtn, "long")

        if selected == "25long":
            return

        self.changeBtnStyleSelected("25long", "long")

    def onProfitLong30(self):
        selected = self.selectedLongBtn
        self.changeBtnStyleDeselected(self.selectedLongBtn, "long")

        if selected == "30long":
            return

        self.changeBtnStyleSelected("30long", "long")

    def onProfitLong35(self):
        selected = self.selectedLongBtn
        self.changeBtnStyleDeselected(self.selectedLongBtn, "long")

        if selected == "35long":
            return

        self.changeBtnStyleSelected("35long", "long")

    def onProfitLong40(self):
        selected = self.selectedLongBtn
        self.changeBtnStyleDeselected(self.selectedLongBtn, "long")

        if selected == "40long":
            return

        self.changeBtnStyleSelected("40long", "long")

    def onProfitLong45(self):
        selected = self.selectedLongBtn
        self.changeBtnStyleDeselected(self.selectedLongBtn, "long")

        if selected == "45long":
            return

        self.changeBtnStyleSelected("45long", "long")

    def onProfitLong50(self):
        selected = self.selectedLongBtn
        self.changeBtnStyleDeselected(self.selectedLongBtn, "long")

        if selected == "50long":
            return

        self.changeBtnStyleSelected("50long", "long")
    
    # short profit
    def onProfitShort5(self):
        selected = self.selectedShortBtn
        self.changeBtnStyleDeselected(self.selectedShortBtn, "short")

        if selected == "5short":
            return

        self.changeBtnStyleSelected("5short", "short")

    def onProfitShort10(self):
        selected = self.selectedShortBtn
        self.changeBtnStyleDeselected(self.selectedShortBtn, "short")

        if selected == "10short":
            return

        self.changeBtnStyleSelected("10short", "short")

    def onProfitShort12(self):
        selected = self.selectedShortBtn
        self.changeBtnStyleDeselected(self.selectedShortBtn, "short")

        if selected == "12short":
            return

        self.changeBtnStyleSelected("12short", "short")

    def onProfitShort15(self):
        selected = self.selectedShortBtn
        self.changeBtnStyleDeselected(self.selectedShortBtn, "short")

        if selected == "15short":
            return

        self.changeBtnStyleSelected("15short", "short")

    def onProfitShort17(self):
        selected = self.selectedShortBtn
        self.changeBtnStyleDeselected(self.selectedShortBtn, "short")

        if selected == "17short":
            return

        self.changeBtnStyleSelected("17short", "short")

    def onProfitShort20(self):
        selected = self.selectedShortBtn
        self.changeBtnStyleDeselected(self.selectedShortBtn, "short")

        if selected == "20short":
            return

        self.changeBtnStyleSelected("20short", "short")

    def onProfitShort25(self):
        selected = self.selectedShortBtn
        self.changeBtnStyleDeselected(self.selectedShortBtn, "short")

        if selected == "25short":
            return

        self.changeBtnStyleSelected("25short", "short")

    def onProfitShort30(self):
        selected = self.selectedShortBtn
        self.changeBtnStyleDeselected(self.selectedShortBtn, "short")

        if selected == "30short":
            return

        self.changeBtnStyleSelected("30short", "short")

    def onProfitShort35(self):
        selected = self.selectedShortBtn
        self.changeBtnStyleDeselected(self.selectedShortBtn, "short")

        if selected == "35short":
            return

        self.changeBtnStyleSelected("35short", "short")

    def onProfitShort40(self):
        selected = self.selectedShortBtn
        self.changeBtnStyleDeselected(self.selectedShortBtn, "short")

        if selected == "40short":
            return

        self.changeBtnStyleSelected("40short", "short")

    def onProfitShort45(self):
        selected = self.selectedShortBtn
        self.changeBtnStyleDeselected(self.selectedShortBtn, "short")

        if selected == "45short":
            return

        self.changeBtnStyleSelected("45short", "short")

    def onProfitShort50(self):
        selected = self.selectedShortBtn
        self.changeBtnStyleDeselected(self.selectedShortBtn, "short")

        if selected == "50short":
            return

        self.changeBtnStyleSelected("50short", "short")