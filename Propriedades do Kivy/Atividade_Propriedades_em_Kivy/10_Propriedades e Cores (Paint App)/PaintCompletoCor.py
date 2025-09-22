#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced Paint Application with ListProperty Color Management

This application demonstrates advanced Kivy Properties concepts:
- ListProperty for complex data types (RGBA color values)
- Property-driven color management for drawing applications
- Integration of Properties with Canvas graphics instructions
- Reactive color updates without manual UI refresh
- Professional color palette implementation

Advanced Concepts Demonstrated:
- ListProperty for storing and managing color arrays
- Property binding with lambda functions for dynamic updates
- Canvas graphics integration with property-driven colors
- Professional UI layout with color control buttons
- Real-time property updates affecting drawing behavior

Purpose: Advanced Properties usage in graphics applications
Complexity: Advanced
Concepts: ListProperty, Canvas integration, color management, reactive updates
"""

# Import Kivy framework components
from kivy.app import App                    # Base application class
from kivy.uix.widget import Widget         # Base widget for custom drawing
from kivy.graphics import Color, Line, Rectangle, Ellipse  # Graphics instructions
from kivy.uix.floatlayout import FloatLayout  # Free-positioning layout
from kivy.uix.button import Button          # Interactive button widget
from kivy.uix.slider import Slider          # Continuous value input widget
from kivy.uix.spinner import Spinner        # Dropdown selection widget
from kivy.properties import ListProperty    # Advanced property for lists/arrays
from kivy.core.window import Window         # Window management


class MyPaintWidget(Widget):
    """
    Advanced Paint Widget with Property-Driven Color Management
    
    This widget demonstrates sophisticated use of Kivy Properties:
    - ListProperty for managing RGBA color values
    - Property-driven graphics rendering
    - Reactive color updates across the entire application
    - Professional color management for drawing applications
    
    The ListProperty enables:
    - Type-safe storage of color arrays [R, G, B, A]
    - Automatic UI updates when colors change
    - Event-driven color management
    - Integration with Canvas graphics instructions
    
    Technical Implementation:
        - current_draw_color ListProperty stores RGBA values
        - Property changes automatically affect new drawing operations
        - Canvas Color instructions use the property value directly
        - UI buttons can modify the property to change drawing color
    
    Attributes:
        current_draw_color (ListProperty): RGBA color array for drawing
        line_width (int): Current line thickness
        shape (str): Current drawing tool selection
        start_pos (dict): Touch start positions for shape drawing
    """
    
    # ListProperty for RGBA Color Management
    # Stores color as [Red, Green, Blue, Alpha] with values 0.0-1.0
    current_draw_color = ListProperty([1, 0, 0, 1])  # Default: Red
    
    # Technical Note:
    # ListProperty automatically triggers events when the list contents change.
    # This enables reactive color updates throughout the application without
    # manual UI refresh code. The property supports list validation and
    # automatic type conversion.
    
    def __init__(self, **kwargs):
        """
        Initialize the advanced paint widget with property-driven configuration.
        
        Sets up drawing parameters and establishes the initial state
        for property-driven color management.
        """
        super().__init__(**kwargs)
        
        # Drawing configuration (non-property attributes)
        self.line_width = 2        # Line thickness in pixels
        self.shape = 'Line'        # Current drawing tool
        self.start_pos = {}        # Touch tracking for shapes

    def on_touch_down(self, touch):
        """
        Handle touch start with property-driven color application.
        
        This method demonstrates how Properties integrate with Canvas
        graphics instructions for dynamic, reactive drawing behavior.
        
        Args:
            touch (Touch): Kivy touch object with position data
        
        Property Integration:
            - Uses current_draw_color ListProperty for Color instruction
            - Property changes automatically affect subsequent drawing
            - No manual color management or UI updates required
        """
        with self.canvas:
            # Apply current color from ListProperty using unpacking operator
            # *self.current_draw_color expands [R, G, B, A] to Color(R, G, B, A)
            Color(*self.current_draw_color)
            
            # Create graphics instructions based on selected tool
            if self.shape == 'Line':
                # Freehand line drawing
                touch.ud['line'] = Line(
                    points=(touch.x, touch.y),  # Starting point
                    width=self.line_width       # Configurable thickness
                )
                
            elif self.shape == 'Rectangle':
                # Rectangle shape drawing
                self.start_pos[touch] = (touch.x, touch.y)
                touch.ud['rect'] = Rectangle(
                    pos=(touch.x, touch.y),     # Initial position
                    size=(1, 1)                 # Minimal initial size
                )
                
            elif self.shape == 'Ellipse':
                # Ellipse shape drawing
                self.start_pos[touch] = (touch.x, touch.y)
                touch.ud['ellipse'] = Ellipse(
                    pos=(touch.x, touch.y),     # Initial position
                    size=(1, 1)                 # Minimal initial size
                )

    def on_touch_move(self, touch):
        """
        Handle touch movement for continuous drawing operations.
        
        Updates graphics instructions as the user drags across the screen,
        maintaining the color set by the current_draw_color property.
        
        Args:
            touch (Touch): Kivy touch object with current position
        """
        if self.shape == 'Line' and 'line' in touch.ud:
            # Continue freehand drawing
            touch.ud['line'].points += [touch.x, touch.y]
            
        elif self.shape in ['Rectangle', 'Ellipse'] and touch in self.start_pos:
            # Update shape dimensions during drag
            x0, y0 = self.start_pos[touch]
            width = touch.x - x0
            height = touch.y - y0
            size = (abs(width), abs(height))
            pos = (min(x0, touch.x), min(y0, touch.y))
            
            if self.shape == 'Rectangle':
                touch.ud['rect'].pos = pos
                touch.ud['rect'].size = size
            elif self.shape == 'Ellipse':
                touch.ud['ellipse'].pos = pos
                touch.ud['ellipse'].size = size

    def clear_canvas(self, instance):
        """
        Clear all graphics from the drawing canvas.
        
        Args:
            instance (Button): Button that triggered the clear action
        """
        self.canvas.clear()

    def set_line_width(self, instance, value):
        """
        Update line width for drawing operations.
        
        Args:
            instance (Slider): Slider widget that changed
            value (float): New line width value
        """
        self.line_width = value

    def set_shape(self, spinner, text):
        """
        Change the active drawing tool.
        
        Args:
            spinner (Spinner): Dropdown widget that changed
            text (str): Selected tool name
        """
        self.shape = text

    def set_draw_color(self, color_list):
        """
        Update the drawing color using ListProperty.
        
        This method demonstrates proper ListProperty usage:
        - Direct assignment triggers property events
        - Automatic UI updates without manual refresh
        - Type-safe color management
        
        Args:
            color_list (list): RGBA color values as [R, G, B, A]
        
        Technical Note:
            Assigning to the ListProperty automatically triggers
            'on_current_draw_color' events and updates any bound
            UI elements or graphics instructions.
        """
        self.current_draw_color = color_list


class MyPaintApp(App):
    """
    Advanced Paint Application with Property-Driven Color Management
    
    This application demonstrates professional-level Kivy Properties usage:
    - ListProperty integration with complex graphics applications
    - Lambda function binding for dynamic property updates
    - Professional color palette implementation
    - Advanced UI layout with property-driven controls
    - Reactive programming patterns in graphics applications
    
    The app showcases how Properties enable clean, maintainable code
    for complex interactive applications with minimal boilerplate.
    
    Architecture Highlights:
        - Separation of drawing logic and color management
        - Property-driven reactive updates
        - Professional UI organization
        - Event-driven programming patterns
    """
    
    def build(self):
        """
        Construct the advanced paint application with property-driven color controls.
        
        This method demonstrates professional UI composition with:
        - Strategic placement of color control buttons
        - Lambda function binding for property updates
        - Professional spacing and sizing for optimal UX
        - Integration of Properties with UI event handling
        
        Returns:
            FloatLayout: Complete interface with property-driven color management
        
        UI Architecture:
            - Main drawing area (paint_widget) fills the screen
            - Color buttons positioned for easy access during drawing
            - Tool controls grouped logically in the top area
            - Clear button positioned to prevent accidental activation
        """
        # Create root layout for precise widget positioning
        root = FloatLayout()
        
        # Create main drawing widget with property-driven color management
        paint_widget = MyPaintWidget()
        root.add_widget(paint_widget)

        # Color Control Buttons with Property Integration
        # These buttons demonstrate lambda function binding for property updates
        
        # Red Color Button
        btn_red = Button(
            text='Vermelho',                    # Portuguese label
            size_hint=(0.15, 0.07),            # 15% width, 7% height
            pos_hint={'x': 0.02, 'y': 0.8}     # Top-left positioning
        )
        # Lambda binding: directly updates the ListProperty with red color
        btn_red.bind(
            on_release=lambda instance: paint_widget.set_draw_color([1, 0, 0, 1])
        )
        root.add_widget(btn_red)

        # Green Color Button
        btn_green = Button(
            text='Verde',                       # Portuguese label
            size_hint=(0.15, 0.07),            # Consistent sizing
            pos_hint={'x': 0.20, 'y': 0.8}     # Next to red button
        )
        # Lambda binding: updates ListProperty with green color
        btn_green.bind(
            on_release=lambda instance: paint_widget.set_draw_color([0, 1, 0, 1])
        )
        root.add_widget(btn_green)

        # Blue Color Button
        btn_blue = Button(
            text='Azul',                        # Portuguese label
            size_hint=(0.15, 0.07),            # Consistent sizing
            pos_hint={'x': 0.38, 'y': 0.8}     # Next to green button
        )
        # Lambda binding: updates ListProperty with blue color
        btn_blue.bind(
            on_release=lambda instance: paint_widget.set_draw_color([0, 0, 1, 1])
        )
        root.add_widget(btn_blue)

        # Clear Button - Positioned safely away from drawing area
        btn_clear = Button(
            text='Limpar',                      # Clear label
            size_hint=(0.15, 0.1),             # Slightly larger for importance
            pos_hint={'x': 0.82, 'y': 0.88}    # Top-right corner
        )
        # Direct method binding for canvas clearing
        btn_clear.bind(on_release=paint_widget.clear_canvas)
        root.add_widget(btn_clear)

        # Line Width Slider - Positioned for easy access
        slider = Slider(
            min=1,                             # Minimum line width
            max=10,                            # Maximum line width
            value=2,                           # Default line width
            size_hint=(0.5, 0.05),             # Half screen width
            pos_hint={'x': 0.02, 'y': 0.9}     # Top positioning
        )
        # Bind slider value changes to line width updates
        slider.bind(value=paint_widget.set_line_width)
        root.add_widget(slider)

        # Shape Selection Spinner - Tool selection dropdown
        spinner = Spinner(
            text='Line',                        # Default selection
            values=('Line', 'Rectangle', 'Ellipse'),  # Available tools
            size_hint=(0.2, 0.07),             # Compact size
            pos_hint={'x': 0.55, 'y': 0.88}    # Top-center positioning
        )
        # Bind selection changes to shape tool updates
        spinner.bind(text=paint_widget.set_shape)
        root.add_widget(spinner)

        return root


# Application Entry Point
if __name__ == '__main__':
    """
    Professional application entry point for advanced Properties demonstration.
    
    This application showcases advanced Kivy Properties concepts:
    - ListProperty for complex data management (RGBA colors)
    - Property-driven reactive programming patterns
    - Integration of Properties with Canvas graphics instructions
    - Professional UI design with property-based controls
    - Lambda function binding for dynamic property updates
    
    Key Educational Points:
        - ListProperty enables type-safe array/list management
        - Property changes automatically trigger UI updates
        - Canvas graphics can use Properties directly for reactive rendering
        - Lambda functions provide clean, inline property update callbacks
        - Professional color management in graphics applications
    
    Advanced Concepts Demonstrated:
        - Reactive programming with automatic UI synchronization
        - Property-driven application architecture
        - Professional graphics application development
        - Clean separation of data management and UI logic
        - Type-safe property management with validation
    """
    MyPaintApp().run()
