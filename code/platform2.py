#sys.path.append("code\classes\energy_controlling.py")
#import energy_controlling as energy

from classes.energy_controlling import EnergyControlling

ec = EnergyControlling( 'name1', 'type1', 'age1', 'description1', 'system_type1', 'counter1', 'task1')

print(ec.name)