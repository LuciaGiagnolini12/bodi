# Generates RDF/XML and documentation from ontology/bodi.ttl
import subprocess
import rdflib

SRC = "ontology/bodi.ttl"
g = rdflib.Graph().parse(SRC, format="turtle")
print(f"{SRC}: {len(g)} triples, syntax OK")
g.serialize("ontology/bodi.rdf", format="pretty-xml")
g.serialize("ontology/bodi.owl", format="pretty-xml")
print("Generated bodi.rdf and bodi.owl")
subprocess.run(["pylode", SRC, "-o", "ontology/index.html"], check=True)
print("Generated ontology/index.html")
