from flask import request, jsonify

from . import bp

from app.blueprints.api.helpers import token_required
from app.models import Post, User


# recieve all post
@bp.get('/posts/<post_id>')
@token_required
def get_post(user,post_id):
    try:
        posts = Post.query.get(post_id)
        return jsonify([{
                'id':posts.id,
                'body' :posts.body,
                'timestamp': posts.timestamp,
                'author':posts.user_id
                }])
    except:
        return jsonify([{'message': 'Invalid Id'}]), 404

# recieve posts from single User
@bp.get('/posts/<username>')
def user_post(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify([{
                'id': username,
                'body' :post.body,
                'timestamp': post.timestamp,
                'author':post.user_id
                }for post in user.posts]), 200
    return jsonify({'messages':'Invalid Username'}), 404


# send a single post
@bp.get('/post/<id>')
def get_post(id):
    try:
        post = Post.query.get(id)
        if post:
            return jsonify([{
                    'id': id,
                    'body' :post.body,
                    'timestamp': post.timestamp,
                    'author':post.user_id
                    }])
    except:
        return jsonify([{'message':'Invalid Post'}]), 404
