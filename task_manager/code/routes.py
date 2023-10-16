from useCases.SearchTask import SearchTask

"""
The ROUTES dictionary defines the routes and link them to their respective controllers.
"""
ROUTES = {
    "POST search": lambda request: SearchTask().handle(request)
}
