def headers(cookies):
    jwt = cookies['connect.sid']
    return {
        'Cookie': f'connect.sid={jwt}'
    }

