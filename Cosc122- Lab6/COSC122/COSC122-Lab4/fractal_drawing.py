from Tkinter import *
from fractals import FractalCanvas
global count 

class SierpinskiTriangle(FractalCanvas):

    def draw(self, width, height):
        """Sets up various bits for the initial draw."""
        # Keep the triangle bounded inside a square
        t_size = min(width, height)
        global count
        count = 0
        # And keep it centred
        outer_triangle = [((width/2)-(t_size/2),-(height/2)-(t_size/2)),
                          (width/2, (-height/2)+(t_size/2)),
                          ((width/2)+(t_size/2),-(height/2)-(t_size/2))]

        # Setup colour gradient from dark orange-brown to light
        step = 255.0 / max(1, self.levels)
        colour_vals = [1*step*k for k in xrange(self.levels+1)]
        self.colours = [(k, k/2, k/4) for k in colour_vals]
        # Start recursively drawing the triangle
        self.turtle.reset()
        self.turtle.tracer(0)
        self.turtle.penup()
        self.draw_triangle(outer_triangle, self.levels)
        print count
        
    def draw_triangle(self, points, level):
        """
        Recursively draws the Sierpinski triangle.
        'points' is a list of (x,y) tuples containing the co-ordinates of where
        to draw the triangle.
        'level' is which level of the triangle we're up to (where 0 is the
        innermost level).
        """
        global count
        count+=1
        # Set the fill colour
        self.turtle.fillcolor(self.colours[level])
        
        # Draw the triangle
        self.turtle.begin_fill()
        
        self.turtle.goto(*points[0])   # Move to the first point
       
        self.turtle.pendown()          # Put the turtle pen down
        
        self.turtle.goto(*points[1])   # Draw move to the three points of the triangle
        
        self.turtle.goto(*points[2])
        
        self.turtle.goto(*points[0])
        
        self.turtle.penup()            # Lift the pen up
        
        self.turtle.end_fill()         # Finish the colour fill
        
        self.update_screen()           
        
        # If we still have more levels to draw...
        if level > 0:
            # Calculate the position of the three inner triangles and recursively
            # draw them and their inner triangles
            inner_points = [points[0], self.midpoint(points[0], points[1]), self.midpoint(points[0], points[2])]
            self.draw_triangle(inner_points, level-1)
            inner_points = [points[1], self.midpoint(points[0], points[1]), self.midpoint(points[1], points[2])]
            self.draw_triangle(inner_points, level-1)
            inner_points = [points[2], self.midpoint(points[2], points[1]), self.midpoint(points[0], points[2])]
            self.draw_triangle(inner_points, level-1)
        
    def midpoint(self, p1, p2):
        """Returns a tuple of the midpoint between two (x,y) point tuples."""
        return ((p1[0] + p2[0])/2.0, (p1[1] + p2[1])/2.0)


class KochCurve(FractalCanvas):

    def draw(self, width, height):
        # Reset the turtle
        self.turtle.reset()
        self.turtle.tracer(0)
        
        # Position the turtle at the centre-left of the screen
        self.turtle.penup()
        self.turtle.goto(0, -height/2)
        self.turtle.pendown()
        
        self.draw_koch(self.levels, width)
        self.turtleScreen.update()
        
    
    def draw_koch(self, level, length):
        if (level == 0):
            self.turtle.forward(length)
            self.turtleScreen.update()
        else:
            length/=3
            self.draw(level, length)
            self.turtle.left(60)
            self.draw(level,length)
            self.turtle.right(120)
            self.draw(level,length)
            self.turtle.left(60)
            self.draw(level,length)
            draw_koch(level-1,length)
            
    
class KochSnowflake(KochCurve):
    
    def draw(self, width, height):
        # Reset the turtle
        self.turtle.reset()
        self.turtle.tracer(0)
        
        # Position the turtle at the centre-top of the screen
        self.turtle.penup()
        self.turtle.goto(width/2, 0)
        self.turtle.pendown()
        
        self.turtle.right(60)
        
        import math
        length = math.sqrt(math.pow(width/2, 2) + math.pow(height/1.5, 2))

        
        #need to draw three Koch curves here to get a snowflake
        pass 
    


class DragonCurve(FractalCanvas):
    
    def draw(self, width, height):
        # Reset the turtle
        self.turtle.reset()
        self.turtle.tracer(0)
        
        # Position the turtle
        self.turtle.penup()
        self.turtle.goto(width/4, -height/3)
        self.turtle.pendown()
        
        self.draw_dragon(self.levels, width/2, 45)
        self.turtleScreen.update()
        
    def draw_dragon(self, level, length, angle):
        pass
    


class HilbertCurve(FractalCanvas):

    def draw(self, width, height):
        # Reset the turtle
        self.turtle.reset()
        self.turtle.tracer(0)
        
        # Scale the line length such that the entire curve fits on the screen
        length = 2**self.levels - (1.0 / 2**self.levels)
        self.line_length = width / length
        self.draw_hilbert(self.levels, 90)
        self.turtleScreen.update()        
        
    def draw_hilbert(self, level, angle):
        pass
        
   
if __name__ == '__main__':
    root = Tk()
    frame = Frame(root)
    frame.pack(fill=BOTH,expand=YES)

    # Draw a SierpinskiTriangle to 5 levels
    #f = KochCurve(frame,4)
    f = SierpinskiTriangle(frame, 5)
    
    root.mainloop()