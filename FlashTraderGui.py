from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class FlashTraderMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Flash Executor')
        self.setGeometry(100, 100, 1200, 700)
        #self.setStyleSheet("""
        #    QToolBar {
        #        background-color: #DFDFDF;
        #    }
        #    QMainWindow {
        #        background-color: #2b2b2b;
        #    }
        #""")

        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setSpacing(5)

        # Top toolbar
        self.create_toolbar(main_layout)

        # Trading panels layout
        trading_layout = QHBoxLayout()
        main_layout.addLayout(trading_layout)

        # Create trading panels
        self.create_long_panel(trading_layout)
        self.create_center_panel(trading_layout)
        self.create_short_panel(trading_layout)

        # Status bars at bottom
        self.create_status_bars(main_layout)

    def create_toolbar(self, parent_layout):
        toolbar_layout = QHBoxLayout()
        
        # Toolbar buttons
        left_buttons = [
            ("Connect User API", "#7c7c7c"),
            ("API tester", "#7c7c7c"),
            ("API strings tester", "#7c7c7c"),
        ]

        right_button = ("Disconnect User and System API", "#7c7c7c")
        
        # Add left buttons
        for text, color in left_buttons:
            if text == "Disconnect User and System API":
                spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
                toolbar_layout.addItem(spacer)

            btn = QPushButton(text)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    color: black;
                    border: 1px solid #666;
                    padding: 8px 40px;
                    font-size: 12px;
                    font-weight: bold;
                    border-top-left-radius: 6px;
                    border-top-right-radius: 6px;
                }}
                QPushButton:hover {{
                    background-color: {self.lighten_color(color)};
                }}
            """)
            toolbar_layout.addWidget(btn)
        # Add a stretch to push following items to the right
        toolbar_layout.addStretch()
         # Add the right-side button
        text, color = right_button
        btn = QPushButton(text)
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: red;
                border: 1px solid #666;
                padding: 8px 30px;
                font-size: 12px;
                font-weight: bold;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
            }}
            QPushButton:hover {{
                background-color: {self.lighten_color(color)};
            }}
        """)
        toolbar_layout.addWidget(btn)
        toolbar_layout.setContentsMargins(0, 10, 0, 0)
        parent_layout.addLayout(toolbar_layout)

    def lighten_color(self, color):
        """Lighten a hex color"""
        if color.startswith('#'):
            color = color[1:]
        
        # Convert to RGB
        r = min(255, int(color[0:2], 16) + 30)
        g = min(255, int(color[2:4], 16) + 30)
        b = min(255, int(color[4:6], 16) + 30)
        
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def darken_color(self, color):
        """Darken a hex color"""
        if color.startswith('#'):
            color = color[1:]
        
        # Convert to RGB
        r = max(0, int(color[0:2], 16) - 30)
        g = max(0, int(color[2:4], 16) - 30)
        b = max(0, int(color[4:6], 16) - 30)
        
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def create_long_panel(self, parent_layout):
        # Long panel (green)
        long_frame = QFrame()
        long_frame.setStyleSheet("""
            QFrame {
                background-color: #2d5a3d;
                border: 2px solid #4CAF50;
                border-radius: 5px;
            }
        """)
        
        long_layout = QVBoxLayout(long_frame)
        
        # Title
        title = QLabel("OPEN LONG")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                font-size: 14px;
                padding: 8px;
                margin-bottom: 10px;
            }
        """)
        long_layout.addWidget(title)
        
        # ETH trading info
        self.create_trading_info(long_layout, "green")
        
        # Lot size buttons
        self.create_lot_buttons(long_layout, "long", "#4CAF50")
        
        # Risk management section
        self.create_risk_section(long_layout, "long", "#4CAF50")
        
        # Auto trading strategy
        self.create_auto_trading(long_layout, "#4CAF50")
        
        parent_layout.addWidget(long_frame, 1)

    def create_short_panel(self, parent_layout):
        # Short panel (red)
        short_frame = QFrame()
        short_frame.setStyleSheet("""
            QFrame {
                background-color: #5a2d2d;
                border: 2px solid #f44336;
                border-radius: 5px;
            }
        """)
        
        short_layout = QVBoxLayout(short_frame)
        
        # Title
        title = QLabel("OPEN SHORT")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                background-color: #f44336;
                color: white;
                font-weight: bold;
                font-size: 14px;
                padding: 8px;
                margin-bottom: 10px;
            }
        """)
        short_layout.addWidget(title)
        
        # ETH trading info
        self.create_trading_info(short_layout, "red")
        
        # Lot size buttons
        self.create_lot_buttons(short_layout, "short", "#f44336")
        
        # Risk management section
        self.create_risk_section(short_layout, "short", "#f44336")
        
        # Auto trading strategy
        self.create_auto_trading(short_layout, "#f44336")
        
        parent_layout.addWidget(short_frame, 1)
        
    def create_center_panel(self, parent_layout):
        # Center panel with symbol selector
        center_frame = QFrame()
        center_frame.setStyleSheet("""
            QFrame {
                background-color: #3a3a3a;
                border: 1px solid #666;
                border-radius: 5px;
            }
        """)
        center_frame.setFixedWidth(150)
        
        center_layout = QVBoxLayout(center_frame)
        
        # Symbol selector
        symbol_label = QLabel("ETH/USDT")
        symbol_label.setAlignment(Qt.AlignCenter)
        symbol_label.setStyleSheet("""
            QLabel {
                background-color: #666;
                color: white;
                font-weight: bold;
                font-size: 16px;
                padding: 15px;
                border-radius: 5px;
            }
        """)
        center_layout.addWidget(symbol_label)
        
        # Current price (example)
        price_label = QLabel("$3,245.67")
        price_label.setAlignment(Qt.AlignCenter)
        price_label.setStyleSheet("""
            QLabel {
                color: #4CAF50;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
            }
        """)
        center_layout.addWidget(price_label)
        
        center_layout.addStretch()
        parent_layout.addWidget(center_frame)  

    def create_status_bars(self, parent_layout):
        # Bottom status bars
        status_layout = QHBoxLayout()
        
        # Long position status
        long_status = QLabel("FLASH Close of Long POSITION")
        long_status.setStyleSheet("""
            QLabel {
                background-color: #2d5a3d;
                color: #4CAF50;
                padding: 8px;
                border: 1px solid #4CAF50;
                font-weight: bold;
                font-size: 11px;
            }
        """)
        
        # Short position status
        short_status = QLabel("FLASH Close of Short POSITION")
        short_status.setStyleSheet("""
            QLabel {
                background-color: #5a2d2d;
                color: #f44336;
                padding: 8px;
                border: 1px solid #f44336;
                font-weight: bold;
                font-size: 11px;
            }
        """)
        
        status_layout.addWidget(long_status)
        status_layout.addWidget(short_status)
        
        parent_layout.addLayout(status_layout)

    def create_trading_info(self, parent_layout, color_theme):
        info_layout = QHBoxLayout()
        
        # Balance info
        balance_label = QLabel("Available Balance:")
        balance_value = QLabel("$50,000.00")
        
        color = "#4CAF50" if color_theme == "green" else "#f44336"
        
        for label in [balance_label, balance_value]:
            label.setStyleSheet(f"""
                QLabel {{
                    color: white;
                    font-size: 11px;
                    padding: 2px;
                }}
            """)
        
        balance_value.setStyleSheet(f"""
            QLabel {{
                color: {color};
                font-weight: bold;
                font-size: 11px;
            }}
        """)
        
        info_layout.addWidget(balance_label)
        info_layout.addWidget(balance_value)
        info_layout.addStretch()
        
        parent_layout.addLayout(info_layout)
        
    def create_lot_buttons(self, parent_layout, side, color):
        # Lot size section
        lot_label = QLabel("Buy with auto take profit" if side == "long" else "Sell with auto take profit")
        lot_label.setStyleSheet("color: white; font-size: 12px; margin: 5px 0;")
        parent_layout.addWidget(lot_label)
        
        # First row of lot buttons (0.1, 0.2, 0.3, 0.5)
        lot_row1 = QHBoxLayout()
        lot_values1 = ["0.1", "0.2", "0.3", "0.5"]
        
        for value in lot_values1:
            btn = self.create_lot_button(value, color)
            lot_row1.addWidget(btn)
        
        parent_layout.addLayout(lot_row1)
        
        # Second row of lot buttons (1, 2, 3, 5)
        lot_row2 = QHBoxLayout()
        lot_values2 = ["1", "2", "3", "5"]
        
        for value in lot_values2:
            btn = self.create_lot_button(value, color)
            lot_row2.addWidget(btn)
        
        parent_layout.addLayout(lot_row2)
        
        # Third row of lot buttons (10, 20, 30, 50)
        lot_row3 = QHBoxLayout()
        lot_values3 = ["10", "20", "30", "50"]
        
        for value in lot_values3:
            btn = self.create_lot_button(value, color)
            lot_row3.addWidget(btn)
        
        parent_layout.addLayout(lot_row3)
        
    def create_lot_button(self, value, color):
        btn = QPushButton(f"{value}\nETH")
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: 1px solid #666;
                border-radius: 3px;
                padding: 8px;
                font-size: 10px;
                font-weight: bold;
                min-height: 40px;
            }}
            QPushButton:hover {{
                background-color: {self.lighten_color(color)};
            }}
            QPushButton:pressed {{
                background-color: {self.darken_color(color)};
            }}
        """)
        btn.clicked.connect(lambda checked, v=value: self.on_lot_clicked(v))
        return btn
        
    def create_risk_section(self, parent_layout, side, color):
        # Risk management section
        risk_frame = QFrame()
        risk_frame.setStyleSheet(f"""
            QFrame {{
                border: 1px solid {color};
                border-radius: 3px;
                margin: 5px 0;
            }}
        """)
        risk_layout = QVBoxLayout(risk_frame)
        
        # Stop loss and take profit row
        sl_tp_layout = QHBoxLayout()
        
        # Stop loss buttons
        sl_values = ["5", "10", "12", "15", "17", "20"]
        for value in sl_values:
            btn = QPushButton(value)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {self.darken_color(color)};
                    color: white;
                    border: 1px solid #666;
                    border-radius: 2px;
                    padding: 5px;
                    font-size: 10px;
                    min-width: 25px;
                    min-height: 25px;
                }}
                QPushButton:hover {{
                    background-color: {color};
                }}
            """)
            sl_tp_layout.addWidget(btn)
        
        risk_layout.addLayout(sl_tp_layout)
        
        # Second row
        sl_tp_layout2 = QHBoxLayout()
        sl_values2 = ["25", "30", "35", "40", "45", "50"]
        for value in sl_values2:
            btn = QPushButton(value)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {self.darken_color(color)};
                    color: white;
                    border: 1px solid #666;
                    border-radius: 2px;
                    padding: 5px;
                    font-size: 10px;
                    min-width: 25px;
                    min-height: 25px;
                }}
                QPushButton:hover {{
                    background-color: {color};
                }}
            """)
            sl_tp_layout2.addWidget(btn)
        
        risk_layout.addLayout(sl_tp_layout2)
        parent_layout.addWidget(risk_frame)
        
    def create_auto_trading(self, parent_layout, color):
        # Auto trading strategy section
        auto_frame = QFrame()
        auto_frame.setStyleSheet(f"""
            QFrame {{
                border: 1px solid {color};
                border-radius: 3px;
                margin: 5px 0;
                padding: 10px;
            }}
        """)
        auto_layout = QVBoxLayout(auto_frame)
        
        # Title
        auto_title = QLabel("Auto trading strategy")
        auto_title.setStyleSheet("color: white; font-size: 11px; font-weight: bold;")
        auto_layout.addWidget(auto_title)
        
        # Settings row
        settings_layout = QHBoxLayout()
        
        # Input field
        amount_input = QLineEdit("20")
        amount_input.setStyleSheet("""
            QLineEdit {
                background-color: #4a4a4a;
                color: white;
                border: 1px solid #666;
                padding: 5px;
                border-radius: 3px;
            }
        """)
        
        # ETH label
        eth_label = QLabel("ETH")
        eth_label.setStyleSheet("color: white; font-size: 11px;")
        
        # Price label
        price_label = QLabel("94,560.00")
        price_label.setStyleSheet("color: white; font-size: 11px;")
        
        # USDT label
        usdt_label = QLabel("USDT")
        usdt_label.setStyleSheet("color: white; font-size: 11px;")
        
        settings_layout.addWidget(amount_input)
        settings_layout.addWidget(eth_label)
        settings_layout.addStretch()
        settings_layout.addWidget(price_label)
        settings_layout.addWidget(usdt_label)
        
        auto_layout.addLayout(settings_layout)
        
        # Slider and percentage buttons
        slider_layout = QHBoxLayout()
        
        # Slider
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(50)
        slider.setStyleSheet(f"""
            QSlider::groove:horizontal {{
                height: 6px;
                background: #4a4a4a;
                border-radius: 3px;
            }}
            QSlider::handle:horizontal {{
                background: {color};
                border: 1px solid #666;
                width: 15px;
                height: 15px;
                border-radius: 7px;
                margin: -5px 0;
            }}
            QSlider::sub-page:horizontal {{
                background: {color};
                border-radius: 3px;
            }}
        """)
        
        slider_layout.addWidget(slider)
        auto_layout.addLayout(slider_layout)
        
        # Percentage buttons
        percent_layout = QHBoxLayout()
        percentages = ["5", "7", "10", "15", "20", "30"]
        
        for perc in percentages:
            btn = QPushButton(perc)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {self.darken_color(color)};
                    color: white;
                    border: 1px solid #666;
                    border-radius: 2px;
                    padding: 3px 8px;
                    font-size: 10px;
                    min-height: 20px;
                }}
                QPushButton:hover {{
                    background-color: {color};
                }}
            """)
            percent_layout.addWidget(btn)
        
        auto_layout.addLayout(percent_layout)
        parent_layout.addWidget(auto_frame)    