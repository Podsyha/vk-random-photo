import vk_api

access_token = ""
group_id = ""

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
