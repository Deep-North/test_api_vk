import vk
import setup as S

def auth():
    session = vk.Session(access_token=S.access_token)
    if not session:
        raise Exception('Can not establish connection')
    api = vk.API(session, scope='wall, messages', v='5.130', lang='ru', timeout=10)
    return api

def getUserNameFromId(user_id):
    api = auth()
    if user_id < 1:
        raise ValueError('user_id can not be smaller than "1"')
    fullname = api.users.get(user_id=user_id)
    print(fullname[0]['first_name'] + ' ' + fullname[0]['last_name'])

def getFollowers(count): #вывожу имена подписчиков (10 шт) Павла Дурова (id=1)
    api = auth()
    folowers = api.users.getFollowers(user_id=1, count=count)
    for item in folowers.get('items'):
        fullname = api.users.get(user_id=item)
        print(fullname[0]['first_name'] + ' ' + fullname[0]['last_name'])

def getWallMessages():
    api = auth()
    wallPost=api.wall.get(domain='merkuloff16', count=10)
    #print(wallPost.get('items')[0].get('text'))
    for item in wallPost.get('items'):
        print(item.get('text'))

def postMessageToWall():
    api = auth()
    api.wall.post(message = 'test')

def deleteMessageFromWall():
    api = auth()
    api.wall.delete(post_id=2800)

if __name__ == '__main__':
    postMessageToWall()