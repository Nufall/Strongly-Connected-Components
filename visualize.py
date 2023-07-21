import sys
import json
import graphviz as viz
import tempfile
import random

from graph import Graph

colors = ["aliceblue",
"antiquewhite",
"antiquewhite1",
"antiquewhite2",
"antiquewhite3",
"antiquewhite4",
"aqua",
"aquamarine",
"aquamarine1",
"aquamarine2",
"aquamarine3",
"aquamarine4",
"azure",
"azure1",
"azure2",
"azure3",
"azure4",
"beige",
"bisque",
"bisque1",
"bisque2",
"bisque3",
"bisque4",
"black",
"blanchedalmond",
"blue",
"blue1",
"blue2",
"blue3",
"blue4",
"blueviolet",
"brown",
"brown1",
"brown2",
"brown3",
"brown4",
"burlywood",
"burlywood1",
"burlywood2",
"burlywood3",
"burlywood4",
"cadetblue",
"cadetblue1",
"cadetblue2",
"cadetblue3",
"cadetblue4",
"chartreuse",
"chartreuse1",
"chartreuse2",
"chartreuse3",
"chartreuse4",
"chocolate",
"chocolate1",
"chocolate2",
"chocolate3",
"chocolate4",
"coral",
"coral1",
"coral2",
"coral3",
"coral4",
"cornflowerblue",
"cornsilk",
"cornsilk1",
"cornsilk2",
"cornsilk3",
"cornsilk4",
"crimson",
"cyan",
"cyan1",
"cyan2",
"cyan3",
"cyan4",
"darkblue",
"darkcyan",
"darkgoldenrod",
"darkgoldenrod1",
"darkgoldenrod2",
"darkgoldenrod3",
"darkgoldenrod4",
"darkgray",
"darkgreen",
"darkgrey",
"darkkhaki",
"darkmagenta",
"darkolivegreen",
"darkolivegreen1",
"darkolivegreen2",
"darkolivegreen3",
"darkolivegreen4",
"darkorange",
"darkorange1",
"darkorange2",
"darkorange3",
"darkorange4",
"darkorchid",
"darkorchid1",
"darkorchid2",
"darkorchid3",
"darkorchid4",
"darkred",
"darksalmon",
"darkseagreen",
"darkseagreen1",
"darkseagreen2",
"darkseagreen3",
"darkseagreen4",
"darkslateblue",
"darkslategray",
"darkslategray1",
"darkslategray2",
"darkslategray3",
"darkslategray4",
"darkslategrey",
"darkturquoise",
"darkviolet",
"deeppink",
"deeppink1",
"deeppink2",
"deeppink3",
"deeppink4",
"deepskyblue",
"deepskyblue1",
"deepskyblue2",
"deepskyblue3",
"deepskyblue4",
"dimgray",
"dimgrey",
"dodgerblue",
"dodgerblue1",
"dodgerblue2",
"dodgerblue3",
"dodgerblue4",
"firebrick",
"firebrick1",
"firebrick2",
"firebrick3",
"firebrick4",
"floralwhite",
"forestgreen",
"fuchsia",
"gainsboro",
"ghostwhite",
"gold",
"gold1",
"gold2",
"gold3",
"gold4",
"goldenrod",
"goldenrod1",
"goldenrod2",
"goldenrod3",
"goldenrod4",]

def visualize(graph, components: list[list[int]] = []):
    if isinstance(graph, Graph):
        graph = graph.json()

    random.shuffle(colors)

    edges = graph["edges"]
    vertices = graph["vertices"]

    graph = viz.Digraph()
    graph.attr(rankdir='LR')
    graph.attr(overlap='scale')
    graph.attr('node', shape='doublecircle')

    for i, component in enumerate(components):
        color = colors[i % len(colors)]
        if len(component) > 1:
            for vertex in component:
                graph.node(str(vertex), style='filled', fillcolor=color)

    for vertex in range(vertices + 1):
        graph.node(str(vertex))

    for [src, dst] in edges:
        graph.edge(str(src), str(dst))
        
    graph.view(tempfile.mktemp('.gv'))

if __name__ == "__main__":
    for filename in sys.argv[1:]:
        with open(filename, 'r') as file:
            graph = json.load(file)
            visualize(graph)