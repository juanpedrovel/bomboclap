from ants import *
hive, layout = Hive(AssaultPlan()), dry_layout
colony = AntColony(None, hive, ant_types(), layout, (1, 9))

# Testing bodyguard performs thrower's action
bodyguard = BodyguardAnt()
thrower = ThrowerAnt()
bee = Bee(2)
# Place thrower before bodyguard
colony.places["tunnel_0_0"].add_insect(thrower)
colony.places["tunnel_0_0"].add_insect(bodyguard)
colony.places["tunnel_0_3"].add_insect(bee)
bodyguard.action(colony)