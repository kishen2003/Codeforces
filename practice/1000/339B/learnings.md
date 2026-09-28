Modulo arithmetic for circular problems no need to check three conditions and three equations 
one modulo equation is enough (target - current) % n

since the tasks are present in m variable time and space should have been O(m) but space can be improved by not converting the map into list and using the lazy evaulation of the map function then space becomes O(1)

map object is single use only and can't be used again once exhausted so convert to list or another data structure if needed to be used multiple times