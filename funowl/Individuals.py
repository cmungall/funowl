"""
Individual := NamedIndividual | AnonymousIndividual

NamedIndividual := IRI

AnonymousIndividual := nodeID
"""
from dataclasses import dataclass
from typing import Union, ClassVar

from rdflib import OWL, URIRef

from funowl.GeneralDefinitions import NodeID
from funowl.Identifiers import IRI
from funowl.base.fun_owl_choice import FunOwlChoice


@dataclass
class NamedIndividual(IRI):
    rdf_type: ClassVar[URIRef] = OWL.NamedIndividual


class AnonymousIndividual(NodeID):
    pass


@dataclass
class Individual(FunOwlChoice):
    v: Union[NamedIndividual, AnonymousIndividual]

