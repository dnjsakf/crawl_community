class AuthException(Exception):
  def __init__(self):
    super(AuthException, self).__init__('유저 인증 오류')

class PasswordNotMatchedException(Exception):
  def __init__(self):
    super(PasswordNotMatchedException, self).__init__('비밀번호가 일치하지 않습니다')

class NotFoundUserException(Exception):
  def __init__(self):
    super(NotFoundUserException, self).__init__('유저를 찾을 수 없습니다.')
  
class AlreadyExistUserException(Exception):
  def __init__(self):
    super(AlreadyExistUserException, self).__init__('이미 가입된 이메일입니다.')
  