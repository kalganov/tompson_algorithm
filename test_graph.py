from graphviz import Graph

graph = Graph('FSM2', filename='fsm2.gv', engine='sfdp')

graph.node("A", shape="circle", start="true")
graph.node("B", shape="doublecircle")

graph.edge("A", "A", label='a,b')
graph.edge("A", "B", label="a")
graph.edge("B", "A", label="b")
graph.edge("B", "B", label="b")

graph.render("test_graph3.gv")
