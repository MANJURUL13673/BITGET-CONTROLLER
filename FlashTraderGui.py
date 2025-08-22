from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import AngledButton

class FlashTraderMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Flash Executor')
        self.setGeometry(100, 100, 1200, 700)

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
        stacked = QStackedLayout()
        stacked.setStackingMode(QStackedLayout.StackingMode.StackAll)

        # Overlay layout
        overlay_widget = QWidget()
        overlay_layout = QVBoxLayout(overlay_widget)
        overlay_layout.setContentsMargins(0, 0, 0, 0)
        overlay_layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.create_center_panel(overlay_layout)

        # left and right panel layout
        widget = QWidget()
        trading_layout = QHBoxLayout(widget)
        trading_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addLayout(stacked)

        # Create trading panels
        self.create_long_panel(trading_layout)
        self.create_short_panel(trading_layout)

        # setup the stacked to visualize
        stacked.addWidget(overlay_widget)
        stacked.addWidget(widget)
        # Status bars at bottom
        #self.create_status_bars(main_layout)

    def create_toolbar(self, parent_layout):
        toolbar_layout = QHBoxLayout()
        
         # Add image at the beginning of toolbar
        image_label = QLabel()
        pixmap = QPixmap("FlashExecutor.jpg")  # Replace with your actual image path
    
        # Scale the image to fit toolbar height (adjust size as needed)
        scaled_pixmap = pixmap.scaled(60, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignCenter)
    
        # Optional: Add some margin around the image
        image_label.setContentsMargins(10, 0, 0, 0)
    
        toolbar_layout.addWidget(image_label)

        # Toolbar buttons
        left_buttons = [
            ("Connect User API", "#7c7c7c"),
            ("API tester", "#7c7c7c"),
            ("API strings tester", "#7c7c7c"),
        ]

        buttons_sub_text = ("Test OK\nNext test in 59 sec")


        right_button = ("Disconnect User and System API", "#7c7c7c")
        
        # Add left buttons
        for text, color in left_buttons:
            if text == "Disconnect User and System API":
                spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
                toolbar_layout.addItem(spacer)

            btn = QPushButton()
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    border: 1px solid #666;
                    padding: 8px 40px;
                    min-width: 180px;
                    min-height: 20px;
                    border-top-left-radius: 6px;
                    border-top-right-radius: 6px;
                }}
                QPushButton:hover {{
                    background-color: {self.lighten_color(color)};
                }}
            """)
             # Create a layout for the button content
            button_layout = QHBoxLayout(btn)
            button_layout.setContentsMargins(10, 5, 10, 5)
            button_layout.setSpacing(4)
    
            # First text line
            label1 = QLabel(text)
            label1.setAlignment(Qt.AlignCenter)
            label1.setStyleSheet("font-weight: bold; font-size: 12px; color: black;")

            if text != "Connect User API":
                # Second text line
                label2 = QLabel(buttons_sub_text)
                label2.setAlignment(Qt.AlignLeft)
                label2.setStyleSheet("font-weight: normal; font-size: 10px; color: #00FF00;")
    
            button_layout.addWidget(label1)
            if text != "Connect User API":
                button_layout.addWidget(label2)
            toolbar_layout.addWidget(btn, 0, Qt.AlignBottom)
            #btn.setFixedSize(container.sizeHint())

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
                padding: 8px 40px;
                min-width: 180px;
                min-height: 20px;
                font-size: 12px;
                font-weight: bold;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
            }}
            QPushButton:hover {{
                background-color: {self.lighten_color(color)};
            }}
        """)
        toolbar_layout.addWidget(btn, 0, Qt.AlignBottom)
        #toolbar_layout.setContentsMargins(0, 10, 0, 0)
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
                background-color: #006634;
                border: 2px solid #E6E6E6;
                border-radius: 5px;
            }
        """)
        
        long_layout = QVBoxLayout(long_frame)
        long_layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title = QLabel("OPEN LONG")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                color: #FEFFFF;
                font-size: 20px;
                padding: 8px 8px 0px 8px;
                border: none;
            }
        """)
        long_layout.addWidget(title)
        
        # Add a white line under the title
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("QFrame { border: 4px solid #FEFFFF; }")
        line.setFixedHeight(4) 
        line.setFixedWidth(title.sizeHint().width() * 2)  # Adjust width to match title
        long_layout.addWidget(line, alignment=Qt.AlignHCenter)

        # sub layout
        long_sub_frame = QFrame()
        long_sub_frame.setStyleSheet("""
              QFrame {
                background-color: #029834;
                border: none;
                border-radius: 0px;
            }             
        """)
        long_sub_layout = QVBoxLayout(long_sub_frame)
        long_sub_layout.setContentsMargins(40, 20, 40, 20)
        long_layout.addWidget(long_sub_frame)
        
        # bLot size buttons
        self.create_lot_buttons(long_sub_layout, "long", "#E6E6E6")
        
        # auto take profit
        self.create_profit_buttons(long_sub_layout, "long", "#E6E6E6")

        # Risk management section
        #self.create_risk_section(long_layout, "long", "#4CAF50")
        
        # Auto trading strategy
        #self.create_auto_trading(long_layout, "#4CAF50")
        long_layout.addStretch()
        parent_layout.addWidget(long_frame, 1)

    def create_short_panel(self, parent_layout):
        # Short panel (red)
        short_frame = QFrame()
        short_frame.setStyleSheet("""
            QFrame {
                background-color: #9c0403;
                border: 2px solid #E6E6E6;
                border-radius: 5px;
            }
        """)
        
        short_layout = QVBoxLayout(short_frame)
        short_layout.setContentsMargins(20, 20, 20, 20)
        
        # Title
        title = QLabel("OPEN SHORT")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                color: #FEFFFF;
                font-size: 20px;
                padding: 8px 8px 0px 8px;
                border: none;
            }
        """)
        short_layout.addWidget(title)

        # Add a white line under the title
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("QFrame { border: 4px solid #FEFFFF; }")
        line.setFixedHeight(4) 
        line.setFixedWidth(title.sizeHint().width() * 2.25)  # Adjust width to match title
        short_layout.addWidget(line, alignment=Qt.AlignHCenter) 

        short_sub_frame = QFrame()
        short_sub_frame.setStyleSheet("""
              QFrame {
                background-color: #FE0000;
                border: none;
                border-radius: 0px;
            }             
        """)
        short_sub_layout = QVBoxLayout(short_sub_frame)
        short_sub_layout.setContentsMargins(40, 20, 40, 20)
        short_layout.addWidget(short_sub_frame)

        # ETH trading info
        # self.create_trading_info(short_sub_layout, "red")
        
        # Lot size buttons
        self.create_lot_buttons(short_sub_layout, "short", "#E6E6E6")

        # auto take profit buttons
        self.create_profit_buttons(short_sub_layout, "short", "#E6E6E6")

        # Risk management section
        #self.create_risk_section(short_layout, "short", "#f44336")
        
        # Auto trading strategy
        #self.create_auto_trading(short_layout, "#f44336")
        
        short_layout.addStretch()
        parent_layout.addWidget(short_frame, 1)
        
    def create_center_panel(self, parent_layout):
        # Center panel with symbol selector
        center_frame = QFrame()
        center_frame.setStyleSheet("""
            QFrame {
                background-color: #808080;
                border: 4px solid #E6E6E6;
            }
        """)
        center_frame.setFixedWidth(250)
        center_frame.setFixedHeight(150)
        
        center_layout = QVBoxLayout(center_frame)
        
        # Symbol selector
        #symbol_label = QLabel("ETH/USDT")
        #symbol_label.setAlignment(Qt.AlignCenter)
        #symbol_label.setStyleSheet("""
        #    QLabel {
        #        background-color: #666;
        #        color: white;
        #        font-weight: bold;
        #        font-size: 16px;
        #        padding: 15px;
        #        border-radius: 5px;
        #    }
        #""")
        #center_layout.addWidget(symbol_label)
        
        # Current price (example)
        #price_label = QLabel("$3,245.67")
        #price_label.setAlignment(Qt.AlignCenter)
        #price_label.setStyleSheet("""
        #    QLabel {
        #        color: #4CAF50;
        #        font-size: 14px;
        #        font-weight: bold;
        #        padding: 10px;
        #    }
        #""")
        #center_layout.addWidget(price_label)
        
        #center_layout.addStretch()
        parent_layout.addWidget(center_frame, 1)  

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

    def create_profit_buttons(self, parent_layout, side, color):
        # Profit buttons section
        profit_label = QLabel("Buy with auto take profit" if side == "long" else "Sell with auto take profit")
        if side == "long":
            profit_label.setStyleSheet("color: #07FA07; font-size: 16px; margin: 20px 0;")
        else :
            profit_label.setStyleSheet("color: #07FA07; font-size: 16px; margin: 20px 0px;")
        parent_layout.addWidget(profit_label)

        # Add a white line under the title
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("QFrame { border: 2px solid #C1DACA; }")
        line.setFixedHeight(2) 
        line.setFixedWidth(480)  # Adjust width to match title
        parent_layout.addWidget(line)

        description = QLabel("auto take profit is set automatically of figure bellow on top of order price if this function\nhas been connected together with flash order:")
        description.setStyleSheet(f"color: {color}; font-size: 10px; margin: 20px 0;")
        parent_layout.addWidget(description)


    def create_lot_buttons(self, parent_layout, side, color):
        # Lot size section
        lot_label = QLabel("Buy Market Price" if side == "long" else "Sell Market Price")
        if side == "long":
            lot_label.setStyleSheet("color: #07FA07; font-size: 16px; margin: 20px 0;")
        else:
            lot_label.setStyleSheet("color: #07FA07; font-size: 16px; margin: 20px 65px;")

        parent_layout.addWidget(lot_label)
        
        # Add a white line under the title
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("QFrame { border: 2px solid #C1DACA; }")
        line.setFixedHeight(2) 

        # First row of lot buttons (0.1, 0.2, 0.3, 0.5)
        lot_row1 = QHBoxLayout()
        lot_values1 = ["0.1", "0.2", "0.3", "0.5"]
        line.setFixedWidth(480)  # Adjust width to match title
        parent_layout.addWidget(line)
        
        for value in lot_values1:
            if side == "long":
                btn = AngledButton.AngledTextButton(f"{value}\nETH", "BUY", color)
            else:
                btn = AngledButton.AngledTextButton(f"{value}\nETH", "SELL", color)
            #btn = self.create_lot_button(value, color)
            lot_row1.addWidget(btn)

        lot_row1.addStretch()
        parent_layout.addLayout(lot_row1)
        
        # Second row of lot buttons (1, 2, 3, 5)
        lot_row2 = QHBoxLayout()
        lot_values2 = ["1", "2", "3", "5"]
        
        for value in lot_values2:
            if side == "long":
                btn = AngledButton.AngledTextButton(f"{value}\nETH", "BUY", color)
            else:
                btn = AngledButton.AngledTextButton(f"{value}\nETH", "SELL", color)
            #btn = self.create_lot_button(value, color)
            lot_row2.addWidget(btn)
        
        lot_row2.addStretch()
        parent_layout.addLayout(lot_row2)
        
        # Third row of lot buttons (10, 20, 30, 50)
        lot_row3 = QHBoxLayout()
        lot_values3 = ["10", "20", "30", "50"]
        
        for value in lot_values3:
            if side == "long":
                btn = AngledButton.AngledTextButton(f"{value}\nETH", "BUY", color)
            else:
                btn = AngledButton.AngledTextButton(f"{value}\nETH", "SELL", color)
            #btn = self.create_lot_button(value, color)
            lot_row3.addWidget(btn)
        
        lot_row3.addStretch()
        parent_layout.addLayout(lot_row3)
        
    def create_lot_button(self, value, color):
        btn = AngledButton.AngledTextButton(f"{value}\nETH", "BUY", color)
        return btn
        btn.setMinimumWidth(100)
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: #333333;
                border-radius: 3px;
                padding: 10px;
                margin: 20px 20px 0px 0px;
                font-size: 15px;
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