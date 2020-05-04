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


#fetch_tweets_with_hashtags()

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8002)
