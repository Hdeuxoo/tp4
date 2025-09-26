import numpy as np
import matplotlib.pyplot as plt 

from utils import display_graph_from_dict  

def main():
    # Définition du graphe sous forme de dictionnaire
    graph = {
        "A": ["B"],     # A pointe vers B
        "B": [],        # B n'a pas de successeurs
        "C": ["A", "B"],# C pointe vers A et B
        "D": ["C"],     # D pointe vers C
        "E": ["D", "C"] # E pointe vers D et C
    }

    # Afficher le graphe
    display_graph_from_dict(graph)
    
main()