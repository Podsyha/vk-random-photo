import vk_api

access_token = "38e04726fa931d27226c09408652ae84d7e64afda378e2aa289972a17b5a064360f504ce3e7f22ff56035"
group_id = "196735921"

lat = "57.175961"
long = "65.552962"
radius = 50000

session = vk_api.VkApi(token=access_token)
api = session.get_api()

last_photo = api.photos.search(
    lat=lat,
    long=long,
    sort=0,
    count=1,
    radius=radius
)['items'][0]

api.wall.repost(
    object="photo{}_{}".format(last_photo['owner_id'], last_photo['id']),
    group_id=group_id
)
