from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle() # create a circle
        circle.set_fill(PINK, opacity = 0.5) # set the color and the transparency
        self.play(Create(circle)) # show the circle on the screen

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle() # create a circle
        circle.set_fill(PINK, opacity = 0.5) # set the color and the transparency

        square = Square() # create a square
        square.rotate(PI/4) # rotate a certain amount

        self.play(Create(square)) # animate the creation of the square
        self.play(Transform(square, circle)) # interpolate the square inot a circle
        self.play(FadeOut(square)) # fade out animation

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle() # create a circle
        circle.set_fill(PINK, opacity=0.5) # set the color and the transparency

        square = Square() # create a square
        square.set_fill(BLUE, opacity=0.5) # set the color and the transparency

        square.next_to(circle, RIGHT, buff=0.5) # set the position
        self.play(Create(circle), Create(square)) # show the shapes


class SquaresAndCircles(Scene):
    def construct(self):
        circle = Circle() # create a circle
        circle.set_fill(PINK, opacity=0.5) # set the color and the transparency
        circle2 = Circle() # create a circle
        circle2.set_fill(RED, opacity=0.75) # set the color and the transparency
        
        square = Square() # create a square
        square.set_fill(BLUE, opacity=0.5) # set the color and the transparency
        square2 = Square() # create a square
        square.set_fill(RED, opacity=0.75) # set the color and the transparency


        square.next_to(circle, RIGHT, buff=0.5) # set the position
        square2.next_to(circle, DOWN, buff=0.5) # set the position
        circle2.next_to(square, UP, buff=0.5) # set the position
        self.play(Create(circle), Create(square),
                  Create(circle2), Create(square2)) # show the shapes

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle() # create a circle
        square = Square() # create a square

        self.play(Create(square)) # show the square on screen
        self.play(square.animate.rotate(PI / 4)) # rotate the square
        self.play(
            ReplacementTransform(square, circle)
        ) # transform the square into a cirlce
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
            ) # color the circle on screen

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2*RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=3
            )
        self.wait()

class Disorder(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait(1)
        self.remove(circle)
        self.wait(1)
        # play the first animations...
        # you don't need a section in the very beginning as it gets created automatically
        self.next_section()
        circle = Circle()
        self.add(circle)
        self.wait(1)
        self.remove(circle)
        self.wait(1)
        self.add(Square())
        self.wait()
        # play more animations...
        self.next_section("This is a section")
        circle = Circle()
        self.add(circle)
        self.wait(1)
        self.remove(circle)
        self.wait(1)

class ShowScreenResolution(Scene):
    def construct(self):
        pixel_height = config["pixel_height"] # 1080 is default
        pixel_width = config["pixel_width"] # 1920 is default
        frame_width = config["frame_width"]
        frame_height = config["frame_height"]

        self.add(Dot())
        d1 = Line(frame_width * LEFT / 2, frame_width * RIGHT/ 2).to_edge(DOWN)
        self.add(d1)
        self.add(Text(str(pixel_width)).next_to(d1, UP))
        d2 = Line(frame_height * UP / 2, frame_height * DOWN / 2).to_edge(LEFT)
        self.add(d2)
        self.add(Text(str(pixel_height)).next_to(d2, RIGHT))
