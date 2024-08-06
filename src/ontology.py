# src/ontology.py
from rdflib import RDF, Graph


def load_ontology(ontology_path):
    g = Graph()
    g.parse(ontology_path, format='xml')
    return g

def get_classes(ontology_graph):
    classes = set()
    for cls in ontology_graph.subjects(predicate=RDF.type, object=None):
        if str(cls).startswith("http://www.example.com/ontology/machine_learning#"):
            classes.add(cls.split("#")[-1])
    return classes
