from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from config import Config
from resources.follow import FollowMemoResource, FollowResource
from resources.memo import DeleteListResource, MemoListResource
from resources.user import jwt_blocklist
from resources.user import LoginRegisterResource, UserLogoutResource, UserRegisterResource

app = Flask(__name__)

# 환경변수 셋팅
app.config.from_object(Config)
# jwt 매니저 초기화
jwt = JWTManager(app)
# 로그아웃된 토큰으로 요청하는 경우,
# 실행되지 않도록 처리하는 코드.
@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in jwt_blocklist
api = Api(app)

# 경로와 리소르를 연결한다
api.add_resource( UserRegisterResource, '/user/register' )
api.add_resource( LoginRegisterResource,'/user/login')
api.add_resource( MemoListResource, '/memo')
api.add_resource( DeleteListResource,'/memo/<int:memo_id>')
api.add_resource( UserLogoutResource,'/memo/logout')
api.add_resource( FollowResource,'/follow/<int:followee_id>')
api.add_resource( FollowMemoResource,'/follow/memo')


if __name__ == '__main__' :
    app.run()