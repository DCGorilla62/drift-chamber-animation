import numpy as np
from manim import *

# config.background_color = BLACK #DARK_BLUE
config.frame_height = 10
config.frame_widthe = 10

config.pixel_height = 500
config.pixel_width = 500

config.background_color = GREY
# config.frame_width = 9
# config.frame_height = 16

# config.pixel_width = 1080
# config.pixel_height = 1920

'''
What I want to do first is create all the objects that I need
Drift field line
sensor wire
cathode plane
dashed line down middle
argon molegule in center
Be nuclueus coming down
argon molecule ionized
positive goes toward right
electron goes towards sensor wire
Be nucleus contines
plot on upper right
dot on current pulse curves moves as elecotron hits sensor wire
huge spike
contines when postive argon hits wire
tapers off but still there
fundamental physics showing change in acceleration
fancy text
'''

class dct_animation(Scene):
    def construct(self):
        # self.current_plot()
        # self.show_axis()
        self.drift_field()
        # self.dashed_line()
        self.center_particle()
        # self.downgoing_particle()
        # self.electron()
        # self.positive_ion()
        self.wait(10)

        
    def drift_field(self):
        # pixel_height = config["pixel_height"] # 1080 is default
        # pixel_width = config["pixel_width"] # 1920 is default
        # frame_width = config["frame_width"]
        # frame_height = config["frame_height"]

        # drift_line = Arrow(start=RIGHT, end=LEFT, color=GOLD)
        # drift_line = Arrow(start=config.top + DOWN, end=config.top, color=GOLD)
        color=BLACK
        drift_line = Arrow(config.left_side, config.right_side, color=color).move_to(6.5 * DOWN) #, buff=0)        
        t=Text("Drift Field", color=color, font_size = 50).next_to(drift_line, UP)
        # self.add(drift_line, t)
        self.play(FadeIn(drift_line, t))

        # self.add(Dot())
        # d = Arrow(config.left_side, config.right_side).shift(DOWN*2)
        # dashed = DashedLine(config.left_side, config.right_side, dashed_ratio=0.1).shift(UP*2)
        # dashed = DashedLine(config.top, config.bottom, dashed_ratio=0.1)
        dashed = DashedLine(2*config.top, 2*config.bottom, dash_length=0.5, dashed_ratio=0.5)
        # self.add(d,dashed)
        # self.add(dashed)
        self.play(FadeIn(dashed))

#        self.play(FadeOut(drift_line, t))
        
        # d1 = Line(0.9 * frame_width * LEFT / 2, 0.9 * frame_width * RIGHT/ 2).to_edge(DOWN)
        # self.add(d1)
        # self.add(Text(str(pixel_width)).next_to(d1, UP))
        # d2 = Line(frame_height * UP / 2, frame_height * DOWN / 2).to_edge(LEFT)
        # self.add(d2)
        # self.add(Text(str('Drift Field')).next_to(d2, RIGHT))


    # def dashed_line(self):
    #     self.wait()
    def center_particle(self):
        center_particle = Circle(color=RED, radius=0.25, fill_opacity=0.75)#.move_to(2 * LEFT)
        self.play(FadeIn(center_particle))
        self.wait(1)
    def downgoing_particle(self):
        self.wait()
    def electron(self):
        self.wait()
    def positive_ion(self):
        self.wait()
    def current_plot(self):
        ax = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 4, 1],
            tips=False,
            axis_config={"include_numbers": True}).scale(0.5)#,
         #    y_axis_config={"scaling": LogBase(custom_labels=True)},
        # )
#        ax.to_corner(UR).scale(0.5)
        # x_min must be > 0 because log is undefined at 0.
        # graph = ax.plot(lambda x: x ** 2, x_range=[0.001, 10], use_smoothing=True)
        # self.add(ax, graph)
        #self.add(ax.to_corner(UR))#.scale(0.5))
        self.add(ax.shift(2,2))#.scale(0.5))
        self.wait()
        
    def show_axis(self):
#        self.wait()
        x_start = np.array([0,0,0])
        x_end = np.array([6,0,0])
        
        y_start = np.array([0,0,0])
        y_end = np.array([0,3,0])
        
        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)
        
        self.add(x_axis, y_axis)
        self.add_x_labels()
        
        self.origin_point = np.array([-4,0,0])
        self.curve_start = np.array([-3,0,0])
        
    def add_x_labels(self):
        x_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])



                
# class SineCurveUnitCircle(Scene):
#     # contributed by heejin_park, https://infograph.tistory.com/230
#     def construct(self):
#         self.show_axis()
#         self.show_circle()
#         self.move_dot_and_draw_curve()
#         self.wait()

#     def show_axis(self):
#         x_start = np.array([-6,0,0])
#         x_end = np.array([6,0,0])

#         y_start = np.array([-4,-2,0])
#         y_end = np.array([-4,2,0])

#         x_axis = Line(x_start, x_end)
#         y_axis = Line(y_start, y_end)

#         self.add(x_axis, y_axis)
#         self.add_x_labels()

#         self.origin_point = np.array([-4,0,0])
#         self.curve_start = np.array([-3,0,0])

#     def add_x_labels(self):
#         x_labels = [
#             MathTex("\pi"), MathTex("2 \pi"),
#             MathTex("3 \pi"), MathTex("4 \pi"),
#         ]

#         for i in range(len(x_labels)):
#             x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
#             self.add(x_labels[i])

#     def show_circle(self):
#         circle = Circle(radius=1)
#         circle.move_to(self.origin_point)
#         self.add(circle)
#         self.circle = circle

#     def move_dot_and_draw_curve(self):
#         orbit = self.circle
#         origin_point = self.origin_point

#         dot = Dot(radius=0.08, color=YELLOW)
#         dot.move_to(orbit.point_from_proportion(0))
#         self.t_offset = 0
#         rate = 0.25

#         def go_around_circle(mob, dt):
#             self.t_offset += (dt * rate)
#             # print(self.t_offset)
#             mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

#         def get_line_to_circle():
#             return Line(origin_point, dot.get_center(), color=BLUE)

#         def get_line_to_curve():
#             x = self.curve_start[0] + self.t_offset * 4
#             y = dot.get_center()[1]
#             return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )


#         self.curve = VGroup()
#         self.curve.add(Line(self.curve_start,self.curve_start))
#         def get_curve():
#             last_line = self.curve[-1]
#             x = self.curve_start[0] + self.t_offset * 4
#             y = dot.get_center()[1]
#             new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
#             self.curve.add(new_line)

#             return self.curve

#         dot.add_updater(go_around_circle)

#         origin_to_circle_line = always_redraw(get_line_to_circle)
#         dot_to_curve_line = always_redraw(get_line_to_curve)
#         sine_curve_line = always_redraw(get_curve)

#         self.add(dot)
#         self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
#         self.wait(8.5)

#         dot.remove_updater(go_around_circle)
    
