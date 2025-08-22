from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QFont, QFontMetrics
import math

class AngledTextButton(QPushButton):
    def __init__(self, main_text, angled_text, color, parent=None):
        super().__init__(parent)
        self.main_text = main_text
        self.angled_text = angled_text
        self.color = color
        
        # Set button size and basic style
        self.setMinimumWidth(120)
        self.setMinimumHeight(80)
        
        # Basic button styling (the angled text will be drawn in paintEvent)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: #333333;
                border-radius: 3px;
                padding: 0px;
                margin: 20px 20px 0px 0px;
                border: none;
            }}
            QPushButton:hover {{
                background-color: {self.lighten_color(color)};
            }}
            QPushButton:pressed {{
                background-color: {self.darken_color(color)};
            }}
        """)
        
        # Don't show any text in the button itself - we'll draw everything custom
        self.setText("")
    
    def paintEvent(self, event):
        """Custom paint method to draw both texts"""
        # First call the parent to draw the background and border
        super().paintEvent(event)
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        
        # Get button dimensions
        rect = self.rect()
        
        # === Draw Main Text (0.1\nETH) ===
        main_font = QFont()
        main_font.setPointSize(10)
        main_font.setBold(True)
        painter.setFont(main_font)
        painter.setPen(Qt.black)
        
        # Draw main text in upper center area
        #main_rect = rect.adjusted(10, 5, -10, -25)  # Leave space at bottom for angled text
        main_rect = rect.adjusted(0, 20, -20, 0)  # Adjusted to fit main text
        painter.drawText(main_rect, Qt.AlignCenter, self.main_text)
        
        # === Draw Angled Text (BUY) ===
        angled_font = QFont()
        angled_font.setPointSize(6)
        painter.setFont(angled_font)
        
        # Calculate text dimensions for proper positioning
        fm = QFontMetrics(angled_font)
        text_width = fm.width(self.angled_text)
        text_height = fm.height()
        
        # Calculate the diagonal space needed for rotated text
        # When text is rotated 45°, it needs space = (width + height) / sqrt(2)
        diagonal_space = int((text_width + text_height) / 1.4)
        
        # Position for angled text (bottom-right corner, INSIDE button)
        # Use diagonal space calculation to ensure text fits inside
        margin = 20  # Small margin from edges
        x_pos = rect.width() - diagonal_space//2 - margin
        y_pos = rect.height() - diagonal_space//2
        
        # Save painter state
        painter.save()
        
        # Move to position and rotate 45 degrees
        painter.translate(x_pos, y_pos)
        painter.rotate(-45)  # Negative for clockwise rotation
        
        # Draw the angled text centered at the rotation point
        painter.drawText(-text_width//2, text_height//4, self.angled_text)
        
        # Restore painter state
        painter.restore()
    
    def lighten_color(self, color):
        """Lighten the color for hover effect"""
        if color.startswith('#'):
            hex_color = color.lstrip('#')
            if len(hex_color) == 6:
                rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
                lightened = tuple(min(255, int(c * 1.15)) for c in rgb)
                return f"#{lightened[0]:02x}{lightened[1]:02x}{lightened[2]:02x}"
        # Fallback for non-hex colors
        color_map = {
            'green': '#98fb98', 'lightgreen': '#90EE90',
            'blue': '#add8e6', 'lightblue': '#87CEEB',
            'red': '#ffb6c1', 'pink': '#ffc0cb'
        }
        return color_map.get(color.lower(), color)
    
    def darken_color(self, color):
        """Darken the color for pressed effect"""
        if color.startswith('#'):
            hex_color = color.lstrip('#')
            if len(hex_color) == 6:
                rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
                darkened = tuple(max(0, int(c * 0.85)) for c in rgb)
                return f"#{darkened[0]:02x}{darkened[1]:02x}{darkened[2]:02x}"
        # Fallback for non-hex colors
        color_map = {
            'lightgreen': '#7fb97f', 'green': '#006400',
            'lightblue': '#6bb6e6', 'blue': '#0000cd',
            'pink': '#e6a6b1', 'red': '#8b0000'
        }
        return color_map.get(color.lower(), color)

# Your create_lot_button method
def create_lot_button(self, value, color):
    btn = AngledTextButton(f"{value}\nETH", "BUY", color)
    btn.clicked.connect(lambda checked, v=value: self.on_lot_clicked(v))
    return btn
