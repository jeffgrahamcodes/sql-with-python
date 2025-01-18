import hashlib
import secrets
from flask import Blueprint, jsonify, abort, request
from ..models import Tweet, User, db

def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

bp = Blueprint('users', __name__, url_prefix='/users')

# TASK 2
@bp.route('', methods=['GET'])
def index():
  users = User.query.all()
  result = []
  for user in users:
    result.append(user.serialize())
  return jsonify(result)

# TASK 3
@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
  user = User.query.get_or_404(id)
  return jsonify(user.serialize())

# TASK 4
@bp.route('', methods=['POST'])
def create():
  if 'username' not in request.json or 'password' not in request.json:
    return abort(400)

  if len(request.json['username']) < 3 or len(request.json['password']) < 8:
    return abort(400)

  user = User(
    username=request.json['username'],
    password=scramble(request.json['password'])
  )

  db.session.add(user)
  db.session.commit()
  return jsonify(user.serialize())

# TASK 5
@bp.route('<int:id>', methods=['DELETE'])
def delete(id: int):
  user = User.query.get_or_404(id)
  try:
    db.session.delete(user)
    db.session.commit()
    return jsonify(True)
  except:
    return jsonify(False)

# TASK 6
@bp.route('<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
  user = User.query.get_or_404(id)

  if 'username' not in request.json and 'password' not in request.json:
    return abort(400, '1')

  if 'username' in request.json:
    if len(request.json['username']) < 3:
      return abort(400,'2')
    else:
      user.username = request.json['username']

  if 'password' in request.json:
    if len(request.json['password']) < 8:
      return abort(400, '3')
    else:
      user.password = scramble(request.json['password'])

  try:
    db.session.commit()
    return jsonify(user.serialize())
  except:
    return jsonify(False)

# TASK 8
@bp.route('/<int:id>/liked_tweets', methods=['GET'])
def liked_tweets(id: int):
    user = User.query.get_or_404(id)
    result = []
    for tweet in user.liked_tweets:
        result.append(tweet.serialize())
    return jsonify(result)

# BONUS TASK 1

