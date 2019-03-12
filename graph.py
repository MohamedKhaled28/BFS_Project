import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as Tk
import networkx as nx
from tkinter import ttk

class Graph (Frame):

    def __init__(self,master):
       self.G=nx.Graph()
       self.graph = {"A": set(["B", "C", "D"]),
         "B": set(["A", "E", "F"]),
         "C": set(["A", "G", "H"]),
         "D": set(["A", "I", "J"]),
         "E": set(["B", "K", "L"]),
         "F": set(["B", "M", "N"]),
         "G": set(["C", "O", "P"]),
         "H": set(["C", "Q", "R"]),
         "I": set(["D", "S", "T"]),
         "J": set(["D", "U", "V"]),
         "K": set(["E", "W", "X"]),
         "L": set(["E","Y", "Z"]),
         "M": set(["F", "a", "b"]),
         "N": set(["F", "c", "d", "e"]),
         "O": set(["G", "e"]),
         "P": set(["G", "f", "g"]),
         "Q": set(["H", "g", "h"]),
         "R": set(["H", "S", "i", "j"]),
         "S": set(["I", "R", "k", "l"]),
         "T": set(["I", "l"]),
         "U": set(["J", "m"]),
         "V": set(["J", "m", "n"]),
         "W": set(["K"]),
         "X": set(["K"]),
         "Y": set(["L"]),
         "Z": set(["L"]),
         "a": set(["M"]),
         "b": set(["M"]),
         "c": set(["N"]),
         "d": set(["N"]),
         "e": set(["N", "O"]),
         "f": set(["P"]),
         "g": set(["P", "Q"]),
         "h": set(["Q"]),
         "i": set(["R"]),
         "j": set(["R"]),
         "k": set(["S"]),
         "l": set(["S", "T"]) ,
         "m": set(["U", "V"]),
         "n": set(["V"])}
       self.edges = self.generate_edges(self.graph)
       self.G.add_edges_from(self.edges)
       self.G.add_nodes_from(self.graph)
       self.f = plt.figure(figsize=(5, 4))
       nx.draw_networkx(self.G, node_size=500)
       canvas = FigureCanvasTkAgg(self.f, master=master)
       canvas.get_tk_widget().pack(side='right', fill='both', expand=True)
       master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
       self.frame_form = ttk.Frame(master)
       self.frame_form.pack(fill='both', expand=True)
       self.start_node = ttk.Label(self.frame_form, text=" Enter start node :")
       self.start_node.grid(row=100, column=50)
       self.startnode_value = ttk.Entry(self.frame_form, width=24)
       self.startnode_value.grid(row=100, column=51)
       self.goal = ttk.Label(self.frame_form, text="Goal :")
       self.goal.grid(row=101, column=50)
       self.goal_value = ttk.Entry(self.frame_form, width=24)
       self.goal_value.grid(row=101, column=51)
       self.submit = ttk.Button(self.frame_form, text="submit", command=self.shortest_path)
       self.submit.grid(row=102, column=50, columnspan=2)
       self.entry = ttk.Label(self.frame_form, text="the shortest path is : ").grid(row=103, column=50)
       self.logout = ttk.Button(self.frame_form , text="LOGOUT" , command = self.Logout)
       self.logout.grid(row = 105 , column =50 , columnspan = 2)
    def generate_edges(self,graph):
        edges = []
        for parent in (graph):
            for child in graph[parent]:
                edges.append((parent, child))
        return edges
    def bfs_paths(self , graph, start, goal):
        queue = [(start, [start])]
        while queue:
            (x, path) = queue.pop(0)
            for next in graph[x] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))
    def shortest_path(self ):
        start = self.startnode_value.get()
        goal = self.goal_value.get()
        graph = self.graph
        if (start == "" or goal ==""):
            self.out = ttk.Label(self.frame_form, text="Enter start&goal").grid(row=103, column=51)
        elif(start == goal):
                self.out = ttk.Label(self.frame_form, text="there is no path").grid(row=103, column=51)
        else :
            self.result = next(self.bfs_paths(graph, start, goal))
            self.out = ttk.Label(self.frame_form, text=self.result).grid(row=103, column=51)
            #mn awl hna w ana brsm l path k graph
            self.G.clear()
            self.G.add_nodes_from(self.result)
            self.G.add_path(self.result)
            self.f = plt.figure(figsize=(5, 4))
            nx.draw_networkx(self.G, node_size=900)
            canvas = FigureCanvasTkAgg(self.f,root)
            canvas.get_tk_widget().pack(side='right', fill='both', expand=True)
    def Logout(self):
        root.destroy()
        exec(open("loginn.py").read(), globals())
root = Tk.Tk()
root.wm_title("Animated Graph embedded in TK  ")
root.wm_protocol('WM_DELETE_WINDOW', root.quit())
app = Graph(root)
root.mainloop()


