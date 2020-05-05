from flask import Flask, request, jsonify
from ViewsUtils import ViewsUtils

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
    return "<h1>The Flask application is running successfully! 👍</h1>"

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
        return_status = utils_obj.fetch_verified_tweets()

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


@application.route('/tweets_by_language', methods=['GET', 'POST'])
def fetch_tweets_by_language():
    return_status = {}
    result = []
    try:
        lang = request.args.get('lang')

        if (lang == None or lang == ""): 
            raise(Exception("Required parameter 'lang' was not specified"))
        
        formatted_lang = lang.strip().lower()
        # Roughly checking user input: language codes should be either 2 or 3 characters.
        # Either 2 characters for a language code or 3 characters for "und" (undefined).
        if (len(formatted_lang) != 2 and formatted_lang != "und"):
            raise Exception("Invalid language code passed: " + lang)

        return_status = utils_obj.fetch_tweets_by_language(formatted_lang)

        if return_status[STATUS_KEY] == STATUS_FAILED:
            raise Exception(return_status[ERROR_KEY])

        print("Tweets in language", formatted_lang, ":")
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

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8001)
