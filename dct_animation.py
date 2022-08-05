import numpy as np
from manim import *

# config.background_color = BLACK #DARK_BLUE
config.frame_height = 10
config.frame_widthe = 10

config.pixel_height = 500
config.pixel_width = 500

config.background_color = GREY#BLUE#GREY
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

        # self.show_axis()
        self.drift_field()
        # self.dashed_line()
        self.center_particle()
        # self.downgoing_particle()
        # self.electron()
        # self.positive_ion()
        # self.current_plot()
        self.graph()
        self.wait(10)

        
    def drift_field(self):
        color=BLACK
        drift_line = Arrow(0.9 * config.left_side, 0.9 * config.right_side, color=color).move_to(6.5 * DOWN) #, buff=0)        
        t=Text("Drift Field", color=color, font_size = 50).next_to(drift_line, UP)
        self.play(FadeIn(drift_line, t))

        dashed = DashedLine(2*config.top, 2*config.bottom, dash_length=0.5, dashed_ratio=0.5)
        self.play(FadeIn(dashed))

        sensor = Line(2*config.top, 2*config.bottom).shift(config.left_side * 0.9)
        cathode = Line(2*config.top, 2*config.bottom).shift(config.right_side * 0.9)

        self.play(FadeIn(sensor, cathode))

        
    def center_particle(self):
        center_particle = Circle(color=RED, radius=0.3, fill_opacity=0.75)#.move_to(2 * LEFT)
        t = Text("Ar", color=BLACK, font_size=30).move_to(center_particle.get_center())
        self.play(FadeIn(center_particle, t))
        self.wait(1)

    def downgoing_particle(self):
          
        d = Dot(point=np.array([0., 4.5, 0.]), radius=0.2, 
                stroke_width=0, fill_opacity=1.0, color=PURE_RED)
        t = Text("Be+", color=BLACK, font_size=20).move_to(d.get_center())
        moving_dot=VGroup(d,t)
        label = MathTex("x").add_updater(lambda m: m.next_to(d, LEFT))

        self.add(label)
        self.play(moving_dot.animate.move_to(DOWN*6), run_time=2)
        self.wait()
        
    def electron(self):
        self.wait()
    def positive_ion(self):
        self.wait()
    def current_plot(self):
        square = Square(color=BLACK, fill_opacity=0.75, 
                        side_length=7)
        # square.move_to(3.75*UR)
        
        plane = NumberPlane(
                    x_range = (0, 6),
                    y_range = (0, 6),
                    x_length = 6)# ,
            #        axis_config={"include_numbers": True},
            #   )
        plane.center()
        plane.move_to(0.3 * UR)
        ax = Axes(
            x_range = (0, 5),
            y_range = (0, 5),
            x_length = 5,
            tips=False)
        ax.center()
        square.center()
        
        t =Text("Time", font_size=40).next_to(plane, DOWN)
        t2 =Text("Current", font_size=40).rotate(PI/2).next_to(plane, LEFT)
        group = VGroup(square, plane, t, t2).move_to(UR)
        self.play(FadeIn(group), run_time=2)
        
                # create the axes and the curve
        curve = plane.plot(lambda x: (3*np.sin(8*(x-2))*np.exp(-0.5*x))+3, color=BLUE, x_range=[0, 6])
        # plane.plot()
        # create dots based on the graph
        moving_dot = Dot(plane.i2gp(curve.t_min, curve), color=ORANGE)
        dot_1 = Dot(plane.i2gp(curve.t_min, curve))
        dot_2 = Dot(plane.i2gp(curve.t_max, curve))
        # self.add(dot_1)
        self.add(dot_1, dot_2, moving_dot)

###
        self.play(FadeIn(curve))
       
        self.wait(4)
        
        ####
        dm = VMobject()
        dm.add_updater(lambda x: x.become(curve))
        self.play(MoveAlongPath(moving_dot, curve), rate_func=rate_functions.ease_in_quad, run_time=4)
        self.wait(2)


    #     square = Square(color=BLACK, fill_opacity=0.75,
    #                     side_length=6.25)
    #     square.move_to(3.75*UR)
        
    #     plane = NumberPlane(
    #         x_range = (0, 5),
    #         y_range = (0, 5),
    #         x_length = 5)# ,
    #         # axis_config={"include_numbers": True},
    #     # )
    #     # plane.center()
    #     ax = Axes(
    #         x_range = (0, 5),
    #         y_range = (0, 5),
    #         x_length = 5,
    #         tips=False)
    #     plane.move_to(3.75*UR)
    #     ax.move_to(3.75*UR)
    #     # ax.to_corner(3.75*UR)
    #     # line_graph = plane.plot_line_graph(
    #     #     x_values = [0, 1.5, 2, 2.8, 4, 6.25],
    #     #     y_values = [1, 3, 2.25, 4, 2.5, 1.75],
    #     #     line_color=GOLD_E,
    #     #     vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
    #     #     stroke_width = 4,
    #     # )
    #     # self.add(square, plane)#, line_graph)
    #     # self.add(square, ax)#, line_graph)
    #     #  self.play(FadeIn(square, ax))#, line_graph)
    #     self.play(FadeIn(square, plane))#, line_graph)


    # def graph(self): 
    #     square = Square(color=BLACK, fill_opacity=0.75, 
    #                     side_length=6)
    #     # square.move_to(3.75*UR)
        
    #     plane = NumberPlane(
    #         x_range = (0, 5, 0.5),
    #         y_range = (0, 5, 0.5),
    #         x_length = 5,
    #         faded_line_ratio=1)# ,
    #     #        axis_config={"include_numbers": True},
    #     #   )
    #     plane.center()
    #     plane.move_to(0.3 * UR)
    #     # ax = Axes(
    #     #     x_range = (0, 5),
    #     #     y_range = (0, 5),
    #     #     x_length = 5,
    #     #     tips=False)
    #     # ax.center()
    #     square.center()
    #     # plane.move_to(3.75*UR)
    #     # ax.move_to(3.75*UR)
    #     t =Text("Time", font_size=30).next_to(plane, DOWN)
    #     t2 =Text("Current", font_size=30).rotate(PI/2).next_to(plane, LEFT)
    #     graph = VGroup(square, plane, t, t2).move_to(4*UR)
    #     self.play(FadeIn(graph), run_time=2)
    #     self.wait(10)



    # self.add(square, plane, t, t2)
        # self.add(square, ax)


        
        #         ax = Axes(
#             x_range=[0, 8, 1],
#             y_range=[0, 4, 1],
#             tips=False,
#             axis_config={"include_numbers": True}).scale(0.5)#,
#          #    y_axis_config={"scaling": LogBase(custom_labels=True)},
#         # )
# #        ax.to_corner(UR).scale(0.5)
#         # x_min must be > 0 because log is undefined at 0.
#         # graph = ax.plot(lambda x: x ** 2, x_range=[0.001, 10], use_smoothing=True)
#         # self.add(ax, graph)
#         #self.add(ax.to_corner(UR))#.scale(0.5))
#         self.add(ax.shift(2,2))#.scale(0.5))
#         self.wait()
        
#     def show_axis(self):
# #        self.wait()
#         x_start = np.array([0,0,0])
#         x_end = np.array([6,0,0])
        
#         y_start = np.array([0,0,0])
#         y_end = np.array([0,3,0])
        
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
    
