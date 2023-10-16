from useCases.SearchTask import SearchTask
from useCases.MapTask import MapTask
from useCases.DeleteTask import DeleteTask

"""
The ROUTES dictionary defines the routes and links them to their respective controllers.
"""
ROUTES = {
    "POST search": lambda request: SearchTask().handle(request),
    "POST map": lambda request: MapTask().handle(request),
    "POST delete": lambda request: DeleteTask().handle(request),
}
