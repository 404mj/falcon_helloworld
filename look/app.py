import falcon
from .images import ImageResource
# https://falcon.readthedocs.io/en/stable/user/tutorial.html
 
api = application = falcon.API()

# an instance of the resource class
images = ImageResource()
api.add_route('/images', images)

