from flask import Blueprint, jsonify, abort, request
from ..models import Tweet, User, db

bp = Blueprint('tweets', __name__, url_prefix='/tweets')

@bp.route('', methods=['GET'])
def index():
  tweets = Tweet.query.all()
  result = []
  for tweet in tweets:
    result.append(tweet.serialize())
  return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
  tweet = Tweet.query.get_or_404(id)
  return jsonify(tweet.serialize())

@bp.route('', methods=['POST'])
def create():
  if 'user_id' not in request.json or 'content' not in request.json:
    return abort(400)

  User.query.get_or_404(request.json['user_id'])

  tweet = Tweet(
    user_id=request.json['user_id'],
    content=request.json['content']
  )

  db.session.add(tweet)
  db.session.commit()
  return jsonify(tweet.serialize())

@bp.route('<int:id>', methods=['DELETE'])
def delete(id: int):
  tweet = Tweet.query.get_or_404(id)
  try:
    db.session.delete(tweet)
    db.session.commit()
    return jsonify(True)
  except:
    return jsonify(False)


# TASK 7
@bp.route('/<int:id>/liking_users', methods=['GET'])
def liking_users(id: int):
    tweet = Tweet.query.get_or_404(id)
    result = []
    for user in tweet.liking_users:
        result.append(user.serialize())
    return jsonify(result)