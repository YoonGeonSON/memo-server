from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from config import Config
from resources.memo import DeleteListResource, MemoListResource

from resources.user import LoginRegisterResource, UserLogoutResource, UserRegisterResource

app = Flask(__name__)

# 환경변수 셋팅
app.config.from_object(Config)
# jwt 매니저 초기화
jwt = JWTManager(app)

api = Api(app)

# 경로와 리소르를 연결한다
api.add_resource( UserRegisterResource, '/user/register' )
api.add_resource( LoginRegisterResource,'/user/login')
api.add_resource( MemoListResource, '/memo')
api.add_resource( DeleteListResource,'/memo/<int:memo_id>')
api.add_resource( UserLogoutResource,'/memo/logout')


if __name__ == '__main__' :
    app.run()