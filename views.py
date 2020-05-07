from flask import Flask, request, jsonify, render_template
from ViewsUtils import ViewsUtils
from urllib.parse import unquote

application = Flask(__name__)
application.debug = True

STATUS_SUCCESS = "SUCCESS"
STATUS_FAILED = "FAILED"
STATUS_KEY = "status"
ERROR_KEY = "error"
RESULT_KEY = "result"
utils_obj = ViewsUtils()

# Default route. For testing if the client can connect to the application.
@application.route('/')
def default_route():
    return render_template("index.html")

@application.route('/tweets_with_hashtags', methods=['GET', 'POST'])
def fetch_tweets_with_hashtags():
    return_status = {}
    result = []
    try:
        return_status = utils_obj.tweets_with_hashtags()

        if return_status[STATUS_KEY] == STATUS_FAILED:
            raise Exception(return_status[ERROR_KEY])

        print("Tweets with hashtags are as follows:")

        print(return_status[RESULT_KEY])


        # return_status[RESULT_KEY] = result

        # print(return_status)
        return jsonify(return_status)

    except Exception as exp:
        if ERROR_KEY in return_status:
            error_msg = "Error while fetching tweets with hashtags in views", str(return_status[ERROR_KEY])
            print(error_msg)
        else:
            error_msg = "Error while fetching tweets with hashtags in views" + str(exp)
            print(error_msg)
            return_status[STATUS_KEY] = STATUS_FAILED
            return_status[ERROR_KEY] = error_msg
        return jsonify(return_status)


@application.route('/deleted_tweets', methods=['GET', 'POST'])
def fetch_deleted_tweets():
    return_status = {}
    result = []
    try:
        return_status = utils_obj.deleted_tweets()

        if return_status[STATUS_KEY] == STATUS_FAILED:
            raise Exception(return_status[ERROR_KEY])

        print("Deleted tweets are as follows:")

        print(return_status[RESULT_KEY])


        # return_status[RESULT_KEY] = result

        # print(return_status)
        return jsonify(return_status)

    except Exception as exp:
        if ERROR_KEY in return_status:
            error_msg = "Error while fetching deleted tweets in views", str(return_status[ERROR_KEY])
            print(error_msg)
        else:
            error_msg = "Error while fetching deleted tweets in views" + str(exp)
            print(error_msg)
            return_status[STATUS_KEY] = STATUS_FAILED
            return_status[ERROR_KEY] = error_msg
        return jsonify(return_status)


@application.route('/tweets_with_urls', methods=['GET', 'POST'])
def fetch_tweets_with_urls():
    return_status = {}
    result = []
    try:
        return_status = utils_obj.tweets_with_urls()

        if return_status[STATUS_KEY] == STATUS_FAILED:
            raise Exception(return_status[ERROR_KEY])

        print("Tweets with urls are as follows:")

        print(return_status[RESULT_KEY])


        # return_status[RESULT_KEY] = result

        # print(return_status)
        return jsonify(return_status)

    except Exception as exp:
        if ERROR_KEY in return_status:
            error_msg = "Error while fetching Tweets with urls in views", str(return_status[ERROR_KEY])
            print(error_msg)
        else:
            error_msg = "Error while fetching Tweets with urls in views" + str(exp)
            print(error_msg)
            return_status[STATUS_KEY] = STATUS_FAILED
            return_status[ERROR_KEY] = error_msg
        return jsonify(return_status)


@application.route('/verified_tweets', methods=['GET', 'POST'])
def fetch_verified_tweets():
    return_status = {}
    result = []
    try:
        date = request.args.get('date')

        if (date == None or date == ""): 
            return_status = utils_obj.fetch_verified_tweets()
        else:
            # Undoing escape characters from URL
            date = unquote(date)
            return_status = utils_obj.fetch_verified_tweets(date=date)
        

        if return_status[STATUS_KEY] == STATUS_FAILED:
            raise Exception(return_status[ERROR_KEY])

        print("Verified tweets:")

        print(return_status[RESULT_KEY])
        return jsonify(return_status)

    except Exception as exp:
        if ERROR_KEY in return_status:
            error_msg = "Error while fetching verified tweets in views: ", str(return_status[ERROR_KEY])
            print(error_msg)
        else:
            error_msg = "Error while fetching verified tweets in views: " + str(exp)
            print(error_msg)
            return_status[STATUS_KEY] = STATUS_FAILED
            return_status[ERROR_KEY] = error_msg
        return jsonify(return_status)


@application.route('/top_favorited_tweets', methods=['GET', 'POST'])
def fetch_top_favorited_tweets():
    return_status = {}
    result = []
    try:
        date = request.args.get('date')

        if (date == None or date == ""): 
            return_status = utils_obj.fetch_top_favorited_tweets()
        else:
            return_status = utils_obj.fetch_top_favorited_tweets(date=date)
        

        if return_status[STATUS_KEY] == STATUS_FAILED:
            raise Exception(return_status[ERROR_KEY])

        print("Verified tweets:")

        print(return_status[RESULT_KEY])
        return jsonify(return_status)

    except Exception as exp:
        if ERROR_KEY in return_status:
            error_msg = "Error while fetching verified tweets in views: ", str(return_status[ERROR_KEY])
            print(error_msg)
        else:
            error_msg = "Error while fetching verified tweets in views: " + str(exp)
            print(error_msg)
            return_status[STATUS_KEY] = STATUS_FAILED
            return_status[ERROR_KEY] = error_msg
        return jsonify(return_status)


@application.route('/tweets_by_min_followers', methods=['GET', 'POST'])
def fetch_tweets_by_min_followers():
    return_status = {}
    result = []
    try:
        # variable name "minimum" to avoid conflict with min() function
        minimum = request.args.get('min')

        if (minimum == None or minimum == ""):
            raise(Exception("Required parameter 'min' was not specified"))

        return_status = utils_obj.fetch_tweets_by_min_followers(minimum)

        if return_status[STATUS_KEY] == STATUS_FAILED:
            raise Exception(return_status[ERROR_KEY])

        print("Tweets from users with more than", minimum, "followers:")
        print(return_status[RESULT_KEY])

        return jsonify(return_status)

    except Exception as exp:
        if ERROR_KEY in return_status:
            error_msg = "Error while fetching tweets by language in views: ", str(return_status[ERROR_KEY])
            print(error_msg)
        else:
            error_msg = "Error while fetching tweets by language in views: " + str(exp)
            print(error_msg)
            return_status[STATUS_KEY] = STATUS_FAILED
            return_status[ERROR_KEY] = error_msg
        return jsonify(return_status)


@application.route('/tweets_with_mentions', methods=['GET', 'POST'])
def fetch_tweets_with_mentions():
    return_status = {}
    result = []
    try:
        # variable name "minimum" to avoid conflict with min() function
        username = request.args.get('username')

        if (username == None or username == ""):
            raise(Exception("Required parameter 'username' was not specified"))

        return_status = utils_obj.fetch_tweets_with_mentions(username)

        if return_status[STATUS_KEY] == STATUS_FAILED:
            raise Exception(return_status[ERROR_KEY])

        print("Tweets that mention @" + username + ":")
        print(return_status[RESULT_KEY])

        return jsonify(return_status)

    except Exception as exp:
        if ERROR_KEY in return_status:
            error_msg = "Error while fetching tweets by language in views: ", str(return_status[ERROR_KEY])
            print(error_msg)
        else:
            error_msg = "Error while fetching tweets by language in views: " + str(exp)
            print(error_msg)
            return_status[STATUS_KEY] = STATUS_FAILED
            return_status[ERROR_KEY] = error_msg
        return jsonify(return_status)


@application.route('/tweets_by_language', methods=['GET', 'POST'])
def fetch_tweets_by_language():
    return_status = {}
    result = []
    try:
        lang = request.args.get('lang')

        if (lang == None or lang == ""):
            raise(Exception("Required parameter 'lang' was not specified"))

        return_status = utils_obj.fetch_tweets_by_language(lang)

        if return_status[STATUS_KEY] == STATUS_FAILED:
            raise Exception(return_status[ERROR_KEY])

        print("Tweets in language", lang, ":")
        print(return_status[RESULT_KEY])

        return jsonify(return_status)

    except Exception as exp:
        if ERROR_KEY in return_status:
            error_msg = "Error while fetching tweets by language in views: ", str(return_status[ERROR_KEY])
            print(error_msg)
        else:
            error_msg = "Error while fetching tweets by language in views: " + str(exp)
            print(error_msg)
            return_status[STATUS_KEY] = STATUS_FAILED
            return_status[ERROR_KEY] = error_msg
        return jsonify(return_status)


@application.route('/tweets_with_certain_text', methods=['GET', 'POST'])
def fetch_tweets_with_certain_text():
    return_status = {}
    try:

        lang = request.args.get('lang')
        text = request.args.get('text')

        if lang is None or lang == "":
            raise(Exception("Required parameter 'lang' was not specified"))

        if text is None or text == "":
            raise(Exception("Required parameter 'text' was not specified"))

        formatted_lang = lang.strip().lower().capitalize()

        return_status = utils_obj.fetch_tweets_with_certain_text(formatted_lang, text)

        if return_status[STATUS_KEY] == STATUS_FAILED:
            raise Exception(return_status[ERROR_KEY])

        print("Tweets in language", formatted_lang, ":")
        print(return_status[RESULT_KEY])

        return jsonify(return_status)

    except Exception as exp:
        if ERROR_KEY in return_status:
            error_msg = "Error while fetching tweets with certain text in views: ", str(return_status[ERROR_KEY])
            print(error_msg)
        else:
            error_msg = "Error while fetching tweets with certain text in views: " + str(exp)
            print(error_msg)
            return_status[STATUS_KEY] = STATUS_FAILED
            return_status[ERROR_KEY] = error_msg
        return jsonify(return_status)


@application.route('/add_new_tweet', methods=['GET', 'POST'])
def insert_tweet():
    return_status = {}
    try:
        input_parameters = {}
        input_parameters['id_str'] = request.args.get('id_str')

        if input_parameters is None or input_parameters == "":
            raise (Exception("Input needs to be provided inorder to add tweet"))

        return_status = utils_obj.insert_tweet(input_parameters)

        if return_status[STATUS_KEY] == STATUS_FAILED:
            raise Exception(return_status[ERROR_KEY])

        print(return_status[RESULT_KEY])

        return jsonify(return_status)

    except Exception as exp:
        if ERROR_KEY in return_status:
            error_msg = "Error while inserting tweet in views", str(return_status[ERROR_KEY])
            print(error_msg)
        else:
            error_msg = "Error while inserting tweet in views" + str(exp)
            print(error_msg)
            return_status[STATUS_KEY] = STATUS_FAILED
            return_status[ERROR_KEY] = error_msg
        return jsonify(return_status)


@application.route('/delete_tweet', methods=['GET', 'POST'])
def remove_tweet():
    return_status = {}
    try:
        input_parameters = {}
        input_parameters['_id'] = request.args.get('_id')

        if "_id" not in input_parameters or input_parameters["_id"] is None or input_parameters["_id"] == "":
            raise (Exception("Input needs to be provided inorder to delete tweet"))

        return_status = utils_obj.remove_tweet(input_parameters)

        if return_status[STATUS_KEY] == STATUS_FAILED:
            raise Exception(return_status[ERROR_KEY])

        print(return_status[RESULT_KEY])

        return jsonify(return_status)

    except Exception as exp:
        if ERROR_KEY in return_status:
            error_msg = "Error while deleting tweet in views", str(return_status[ERROR_KEY])
            print(error_msg)
        else:
            error_msg = "Error while deleting tweet in views" + str(exp)
            print(error_msg)
            return_status[STATUS_KEY] = STATUS_FAILED
            return_status[ERROR_KEY] = error_msg
        return jsonify(return_status)


@application.route('/tweets_for_user_ordered', methods=['GET', 'POST'])
def find_tweets_for_user_ordered():
    return_status = {}
    try:
        input_parameters = {}
        input_parameters['user_id'] = request.args.get('user_id')

        if input_parameters is None or input_parameters == "" or input_parameters["user_id"] is None \
                or input_parameters["user_id"] == "":
            raise (Exception("User id needs to be provided inorder to fetch tweets"))

        return_status = utils_obj.find_tweets_for_user_ordered(input_parameters["user_id"])

        if return_status[STATUS_KEY] == STATUS_FAILED:
            raise Exception(return_status[ERROR_KEY])

        # print(return_status[RESULT_KEY])

        return jsonify(return_status)

    except Exception as exp:
        if ERROR_KEY in return_status:
            error_msg = "Error while deleting tweet in views", str(return_status[ERROR_KEY])
            print(error_msg)
        else:
            error_msg = "Error while deleting tweet in views" + str(exp)
            print(error_msg)
            return_status[STATUS_KEY] = STATUS_FAILED
            return_status[ERROR_KEY] = error_msg
        return jsonify(return_status)


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8005)
