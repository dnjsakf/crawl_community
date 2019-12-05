from app import createApp

if __name__ == '__main__':
    server = createApp('dev')
    server.run(host='0.0.0.0', port='3000')