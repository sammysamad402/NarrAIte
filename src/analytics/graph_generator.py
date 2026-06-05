
import networkx as nx
import matplotlib.pyplot as plt

class StoryGraph:
    def build(self):
        g=nx.DiGraph()
        g.add_edge('Start','Forest')
        g.add_edge('Forest','Dragon Ending')
        return g

    def save_graph(self,path='story_graph.png'):
        g=self.build()
        nx.draw(g,with_labels=True)
        plt.savefig(path)
