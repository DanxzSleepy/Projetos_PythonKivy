#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete Paint Application - Advanced Graphics and Touch Interaction

This application demonstrates advanced Kivy concepts:
- Custom canvas drawing with graphics instructions
- Touch event handling for interactive drawing
- Dynamic line creation and shape drawing
- Real-time graphics manipulation
- UI controls for drawing parameters
- Multiple drawing tools (Line, Rectangle, Ellipse)
- Interactive sliders and spinners for tool configuration

Features:
- Free-hand drawing with variable line width
- Geometric shape drawing (rectangles and ellipses)
- Random color generation for artistic variety
- Clear canvas functionality
- Adjustable line thickness
- Shape selection via dropdown spinner

Purpose: Advanced graphics programming and touch interaction
Complexity: Advanced
Concepts: Canvas graphics, touch events, drawing tools, UI controls
"""

# Import Python standard library
import random  # For random color generation

# Import Kivy framework components
from kivy.app import App                    # Base application class
from kivy.uix.widget import Widget         # Base widget for custom drawing
from kivy.graphics import Color, Line, Rectangle, Ellipse  # Graphics instructions
from kivy.uix.floatlayout import FloatLayout  # Free-positioning layout
from kivy.uix.button import Button          # Interactive button widget
from kivy.uix.slider import Slider          # Continuous value input widget
from kivy.uix.spinner import Spinner        # Dropdown selection widget
from kivy.core.window import Window         # Window management


class MyPaintWidget(Widget):
    """
    Custom Paint Widget with Advanced Drawing Capabilities
    
    This widget implements a complete drawing surface with:
    - Multi-touch support for simultaneous drawing
    - Multiple drawing tools (lines, rectangles, ellipses)
    - Dynamic color generation
    - Configurable line width
    - Real-time shape preview and manipulation
    
    The widget handles touch events to create interactive graphics
    that persist on the canvas until cleared by the user.
    
    Technical Implementation:
        - Uses Kivy's Canvas for persistent graphics
        - Tracks touch events for interactive drawing
        - Maintains drawing state (tool, width, colors)
        - Implements different drawing modes with unified interface
    
    Attributes:
        line_width (int): Current line thickness for drawing
        shape (str): Current drawing tool ('Line', 'Rectangle', 'Ellipse')
        start_pos (dict): Tracks starting positions for shape drawing
    """
    
    def __init__(self, **kwargs):
        """
        Initialize the paint widget with default drawing settings.
        
        Sets up the initial state for drawing operations and
        configures default tool parameters.
        """
        super().__init__(**kwargs)
        
        # Drawing configuration
        self.line_width = 2        # Default line thickness (2 pixels)
        self.shape = 'Line'        # Default drawing tool
        self.start_pos = {}        # Dictionary to track shape start positions
                                  # Key: touch object, Value: (x, y) position

    def on_touch_down(self, touch):
        """
        Handle touch start events to initiate drawing operations.
        
        This method is called when the user first touches the screen.
        It sets up the initial drawing state and creates the appropriate
        graphics instruction based on the selected drawing tool.
        
        Args:
            touch (Touch): Kivy touch object containing position and other data
        
        Drawing Process:
            1. Generate random color for visual variety
            2. Create appropriate graphics instruction based on selected tool
            3. Store initial state for tools that require end position
        
        Technical Notes:
            - Each touch gets its own graphics instruction
            - Random colors provide artistic variety
            - Shape tools store start position for later completion
            - Line tool begins immediate point tracking
        """
        # Generate random RGB color values (0.0 to 1.0)
        r, g, b = [random.random() for _ in range(3)]
        
        # Apply color to canvas for subsequent graphics instructions
        with self.canvas:
            Color(r, g, b)  # Set random color for this drawing operation
            
            if self.shape == 'Line':
                # Create line graphics instruction for freehand drawing
                # Store reference in touch's user data for later updates
                touch.ud['line'] = Line(
                    points=(touch.x, touch.y),  # Start with single point
                    width=self.line_width       # Use configured line width
                )
                
            elif self.shape == 'Rectangle':
                # Initialize rectangle for shape drawing
                # Store start position for calculating final dimensions
                self.start_pos[touch] = (touch.x, touch.y)
                
                # Create rectangle with minimal initial size
                touch.ud['rect'] = Rectangle(
                    pos=(touch.x, touch.y),     # Start position
                    size=(1, 1)                 # Minimal initial size
                )
                
            elif self.shape == 'Ellipse':
                # Initialize ellipse for shape drawing
                # Store start position for calculating final dimensions
                self.start_pos[touch] = (touch.x, touch.y)
                
                # Create ellipse with minimal initial size
                touch.ud['ellipse'] = Ellipse(
                    pos=(touch.x, touch.y),     # Start position
                    size=(1, 1)                 # Minimal initial size
                )

    def on_touch_move(self, touch):
        """
        Handle touch movement events to update drawing operations.
        
        This method is called continuously while the user drags their
        finger/mouse across the screen. It updates the graphics based
        on the current drawing tool and touch position.
        
        Args:
            touch (Touch): Kivy touch object with current position
        
        Drawing Updates:
            - Line: Add new points to create continuous path
            - Rectangle/Ellipse: Update size and position based on drag
        
        Technical Implementation:
            - Line tool appends points for smooth curves
            - Shape tools calculate dimensions from start to current position
            - Handles negative dimensions for shapes drawn in any direction
        """
        if self.shape == 'Line' and 'line' in touch.ud:
            # Continue freehand line drawing
            # Append current position to create smooth line
            touch.ud['line'].points += [touch.x, touch.y]
            
        elif self.shape in ['Rectangle', 'Ellipse'] and touch in self.start_pos:
            # Update shape dimensions during drag operation
            
            # Get original start position
            x0, y0 = self.start_pos[touch]
            
            # Calculate dimensions from start to current position
            width = touch.x - x0
            height = touch.y - y0
            
            # Handle negative dimensions (drawing in reverse direction)
            size = (abs(width), abs(height))  # Always positive dimensions
            pos = (min(x0, touch.x), min(y0, touch.y))  # Top-left corner
            
            # Update the appropriate shape graphics instruction
            if self.shape == 'Rectangle':
                touch.ud['rect'].pos = pos
                touch.ud['rect'].size = size
            elif self.shape == 'Ellipse':
                touch.ud['ellipse'].pos = pos
                touch.ud['ellipse'].size = size

    def clear_canvas(self, instance):
        """
        Clear all graphics from the drawing canvas.
        
        This method removes all drawn content, returning the canvas
        to a blank state. Useful for starting fresh or correcting mistakes.
        
        Args:
            instance (Button): The clear button that triggered this action
                              (required by Kivy's event binding system)
        
        Technical Note:
            canvas.clear() removes all graphics instructions,
            effectively erasing everything drawn on the widget.
        """
        self.canvas.clear()

    def set_line_width(self, instance, value):
        """
        Update the line width for drawing operations.
        
        This method is called when the user adjusts the line width slider,
        updating the thickness for all subsequent drawing operations.
        
        Args:
            instance (Slider): The slider widget that triggered this update
            value (float): New line width value from the slider
        
        Technical Note:
            This affects only new drawing operations; existing graphics
            maintain their original line width.
        """
        self.line_width = value

    def set_shape(self, spinner, text):
        """
        Change the active drawing tool.
        
        This method is called when the user selects a different tool
        from the shape selection spinner, switching between line drawing
        and shape creation modes.
        
        Args:
            spinner (Spinner): The dropdown widget that triggered this change
            text (str): The selected tool name ('Line', 'Rectangle', 'Ellipse')
        
        Drawing Modes:
            - 'Line': Freehand drawing with continuous paths
            - 'Rectangle': Click and drag to create rectangles
            - 'Ellipse': Click and drag to create ellipses/circles
        """
        self.shape = text


class MyPaintApp(App):
    """
    Complete Paint Application with Professional UI Controls
    
    This application demonstrates advanced Kivy development techniques:
    - Custom widget integration (MyPaintWidget)
    - Multiple UI control types (Button, Slider, Spinner)
    - Precise widget positioning with FloatLayout
    - Professional graphics application architecture
    - User interface design for creative applications
    
    The app provides a complete digital painting experience with:
    - Multiple drawing tools for different artistic needs
    - Adjustable parameters for creative control
    - Intuitive user interface with logical control placement
    - Professional graphics performance
    
    Architecture:
        - Separation of drawing logic (MyPaintWidget) and UI (MyPaintApp)
        - Event-driven programming with widget callbacks
        - Modular design allowing easy feature extension
        - Professional positioning and sizing for optimal UX
    """
    
    def build(self):
        """
        Construct the complete paint application interface.
        
        This method demonstrates professional UI composition with:
        - Strategic widget positioning for optimal workflow
        - Logical grouping of related controls
        - Proper sizing for both functionality and aesthetics
        - Event binding for interactive functionality
        
        Returns:
            FloatLayout: Root widget containing the complete interface
        
        UI Layout Strategy:
            - Main drawing area takes most of the screen space
            - Controls positioned around edges for easy access
            - Clear button prominently placed for safety
            - Tool controls grouped logically for workflow efficiency
        """
        # Create root layout allowing precise positioning
        root = FloatLayout()
        
        # Create main drawing widget (fills entire screen)
        paint_widget = MyPaintWidget()
        root.add_widget(paint_widget)

        # Clear Button - Positioned prominently in top-right corner
        # Strategic placement prevents accidental activation while drawing
        btn_clear = Button(
            text='Limpar',                    # Clear label in Portuguese
            size_hint=(0.15, 0.1),           # 15% width, 10% height
            pos_hint={'x': 0.82, 'y': 0.88}  # Top-right corner positioning
        )
        # Bind click event to the paint widget's clear method
        btn_clear.bind(on_release=paint_widget.clear_canvas)
        root.add_widget(btn_clear)

        # Line Width Slider - Positioned at top for easy access
        # Horizontal placement maximizes adjustment precision
        slider = Slider(
            min=1,                          # Minimum line width (1 pixel)
            max=10,                         # Maximum line width (10 pixels)
            value=2,                        # Default line width
            size_hint=(0.5, 0.05),          # 50% width, 5% height
            pos_hint={'x': 0.02, 'y': 0.9}  # Top-left area positioning
        )
        # Bind value changes to the paint widget's line width setter
        slider.bind(value=paint_widget.set_line_width)
        root.add_widget(slider)

        # Shape Selection Spinner - Positioned near clear button
        # Dropdown design saves space while providing clear options
        spinner = Spinner(
            text='Line',                        # Default selection
            values=('Line', 'Rectangle', 'Ellipse'),  # Available drawing tools
            size_hint=(0.2, 0.07),              # 20% width, 7% height
            pos_hint={'x': 0.55, 'y': 0.88}     # Top-center positioning
        )
        # Bind selection changes to the paint widget's shape setter
        spinner.bind(text=paint_widget.set_shape)
        root.add_widget(spinner)

        return root


# Application Entry Point
if __name__ == '__main__':
    """
    Professional application entry point for the Paint application.
    
    This demonstrates a complete, production-ready graphics application with:
    - Advanced touch interaction for natural drawing experience
    - Multiple drawing tools for creative flexibility
    - Professional UI design with intuitive control placement
    - Efficient graphics rendering with Kivy's Canvas system
    - Extensible architecture for future feature additions
    
    Key Technical Achievements:
        - Real-time graphics manipulation with smooth performance
        - Multi-touch support for advanced drawing techniques
        - Dynamic shape creation with live preview
        - Random color generation for artistic variety
        - Professional widget positioning and sizing
        - Event-driven architecture with clean separation of concerns
    
    Educational Value:
        - Demonstrates advanced Canvas programming
        - Shows professional UI/UX design principles
        - Illustrates touch event handling best practices
        - Exemplifies modular application architecture
    """
    MyPaintApp().run()
