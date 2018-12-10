# Short example: What can I do with Owlready?

# Load an ontology from a local repository, or from Internet:
from owlready2 import *
owl_output_path = os.path.join(os.path.abspath(''),'test', 'ontology')
onto_path.append(owl_output_path)
onto = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl")
onto.load()

# Create new classes in the ontology, possibly mixing OWL constructs and Python methods:
#class NonVegetarianPizza(onto.Pizza):
    #equivalent_to = [ onto.Pizza & ( onto.has_topping.some(onto.MeatTopping) | onto.has_topping.some(onto.FishTopping)) ]

   # def eat(self): print("Beurk! I'm vegetarian!")

# Access the classes of the ontology, and create new instances / individuals:
test_pizza = onto.Pizza("test_pizza_owl_identifier")
test_pizza.has_topping = [ onto.CheeseTopping(), onto.TomatoTopping() ]

# In Owlready2, almost any lists can be modified in place, for example by appending/removing items from lists. Owlready2 automatically 
# updates the RDF quadstore.
#test_pizza.has_topping.append(onto.MeatTopping())

#print(onto.MeatTopping())

# Perform reasoning, and classify instances and classes:
print(test_pizza.__class__) #Output: 'onto.Pizza'

# sync_reasoner() # Execute HermiT and reparent instances and classes

# print(test_pizza.__class__) # Output: 'onto.NonVegetarianPizza'

# test_pizza.eat() 

list(onto.classes())

# Export to OWL file:
onto.save()
