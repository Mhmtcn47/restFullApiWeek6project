from flask import request, jsonify

from . import bp
from app.models import User

#  Verify User
# @bp.post('/verify-user', methods=['POST']) same as below @bp...
@bp.post('/verify-user')
def verify_user():
    content = request.json
    print(content)
    username= content['username']
    password= content['password']
    user = User.query.filter_by(user_name=username).first()
    if user and user.check_password(password):
        return jsonify([{'user id': user.user_id}])
    return jsonify({'message':'Invalid User Info'})


# Register user
@bp.post('/register-user')
def register_user():
    content = request.json
    username= content['username']
    email= content['email']
    password= content['password']
    user = User.query.filter_by(user_name=username).filter()
    if user:
        return jsonify([{'message': 'Username Taken, Try again'}])
    user = User.query.filter_by(email=email).filter()
    if user:
        return jsonify([{'message': 'Email Taken, Try again'}])
    user = User(email=email, user_name=username)
    # user.password = user.hash_password(password)
    setattr(user,'password', user.hash_password(password))
    user.add_token()
    user.commit()
    print(user)
    return jsonify([{'message': f"{user.username} Registered"}])