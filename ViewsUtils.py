from MongoDBUtility import MongoDBUtility

STATUS_SUCCESS = "SUCCESS"
STATUS_FAILED = "FAILED"
STATUS_KEY = "status"
ERROR_KEY = "error"
RESULT_KEY = "result"
COLLECTION_NAME = "tweets"
DATABASE_NAME = "tweet_analytics"

LANGUAGE_LIST = ['ar', 'bg', 'bn', 'ca', 'cs', 'cy', 'da', 
                'de', 'el', 'en', 'en-au', 'en-gb', 'es', 
                'es-mx', 'eu', 'fa', 'fi', 'fil', 'fr', 
                'ga', 'gl', 'gu', 'he', 'hi', 'hr', 'hu', 
                'id', 'it', 'ja', 'kn', 'ko', 'lv', 'mr', 
                'ms', 'msa', 'nb', 'nl', 'no', 'pl', 'pt', 
                'pt-pt', 'ro', 'ru', 'sk', 'sr', 'sv', 'ta', 
                'th', 'tr', 'uk', 'ur', 'vi', 'xx-lc', 'zh-cn', 
                'zh-hans', 'zh-hant', 'zh-hk']


class ViewsUtils:
    def __init__(self):
        pass

    def tweets_with_hashtags(self):
        utility_status = {}
        try:
            mongo_url = "mongodb://localhost:27023/"
            mongo_con = MongoDBUtility(mongo_url, DATABASE_NAME, COLLECTION_NAME)
            query = [{"entities.hashtags": {"$exists": True, "$ne": []}}, {"entities.hashtags.text": 1}]
            query_type = "select"
            result = mongo_con.execute_query(query, query_type)

            if result[STATUS_KEY] == STATUS_FAILED:
                raise Exception(result[ERROR_KEY])

            utility_status[RESULT_KEY] = []

            for record in result[RESULT_KEY]:
                if "_id" in record:
                    del record["_id"]
                utility_status[RESULT_KEY].append(record)

            utility_status[STATUS_KEY] = STATUS_SUCCESS
            return utility_status

        except Exception as exp:
            if ERROR_KEY in utility_status:
                error_msg = "Error while fetching tweets with hashtags in viewsutils " + str(utility_status[ERROR_KEY])
                print(error_msg)
            else:
                error_msg = "Error while fetching tweets with hashtags in viewsutils" + str(exp)
                print(error_msg)
            utility_status[STATUS_KEY] = STATUS_FAILED
            utility_status[ERROR_KEY] = error_msg
            return utility_status


    def deleted_tweets(self):
        utility_status = {}
        try:
            mongo_url = "mongodb://localhost:27023/"
            mongo_con = MongoDBUtility(mongo_url, DATABASE_NAME, COLLECTION_NAME)
            query = [{"delete" : {"$exists": True}}]
            query_type = "select"
            result = mongo_con.execute_query(query, query_type)

            if result[STATUS_KEY] == STATUS_FAILED:
                raise Exception(result[ERROR_KEY])

            utility_status[RESULT_KEY] = []

            for record in result[RESULT_KEY]:
                if "_id" in record:
                    del record["_id"]
                utility_status[RESULT_KEY].append(record)

            utility_status[STATUS_KEY] = STATUS_SUCCESS
            return utility_status

        except Exception as exp:
            if ERROR_KEY in utility_status:
                error_msg = "Error while fetching deleted tweets in viewsutils " + str(utility_status[ERROR_KEY])
                print(error_msg)
            else:
                error_msg = "Error while fetching deleted tweets in viewsutils" + str(exp)
                print(error_msg)
            utility_status[STATUS_KEY] = STATUS_FAILED
            utility_status[ERROR_KEY] = error_msg
            return utility_status


    def tweets_with_urls(self):
        utility_status = {}
        try:
            mongo_url = "mongodb://localhost:27023/"
            mongo_con = MongoDBUtility(mongo_url, DATABASE_NAME, COLLECTION_NAME)
            query = [{"entities.urls": {"$exists": True, "$ne": []}}]
            query_type = "select"
            result = mongo_con.execute_query(query, query_type)

            if result[STATUS_KEY] == STATUS_FAILED:
                raise Exception(result[ERROR_KEY])

            utility_status[RESULT_KEY] = []

            for record in result[RESULT_KEY]:
                if "_id" in record:
                    del record["_id"]
                utility_status[RESULT_KEY].append(record)

            utility_status[STATUS_KEY] = STATUS_SUCCESS
            return utility_status

        except Exception as exp:
            if ERROR_KEY in utility_status:
                error_msg = "Error while fetching tweets with urls in viewsutils " + str(utility_status[ERROR_KEY])
                print(error_msg)
            else:
                error_msg = "Error while fetching tweets with urls in viewsutils" + str(exp)
                print(error_msg)
            utility_status[STATUS_KEY] = STATUS_FAILED
            utility_status[ERROR_KEY] = error_msg
            return utility_status


    def fetch_verified_tweets(self):
        utility_status = {}
        try:
            mongo_url = "mongodb://localhost:27023/"
            mongo_con = MongoDBUtility(mongo_url, DATABASE_NAME, COLLECTION_NAME)
            query = [{"user.verified": True}, {"text":1, "user.name":1, "user.followers_count":1}]
            query_type = "select"
            result = mongo_con.execute_query(query, query_type)

            if result[STATUS_KEY] == STATUS_FAILED:
                raise Exception(result[ERROR_KEY])

            utility_status[RESULT_KEY] = []

            for record in result[RESULT_KEY]:
                if "_id" in record:
                    del record["_id"]
                utility_status[RESULT_KEY].append(record)

            utility_status[STATUS_KEY] = STATUS_SUCCESS
            return utility_status

        except Exception as exp:
            if ERROR_KEY in utility_status:
                error_msg = "Error while fetching verified tweets in viewsutils " + str(utility_status[ERROR_KEY])
                print(error_msg)
            else:
                error_msg = "Error while fetching verified tweets in viewsutils" + str(exp)
                print(error_msg)
            utility_status[STATUS_KEY] = STATUS_FAILED
            utility_status[ERROR_KEY] = error_msg
            return utility_status


    def fetch_tweets_by_language(self, lang):
        utility_status = {}
        try:
            formatted_lang = lang.strip().lower()
            if (formatted_lang not in LANGUAGE_LIST):
                raise Exception("Invalid language code passed: " + lang)
            
            mongo_url = "mongodb://localhost:27023/"
            mongo_con = MongoDBUtility(mongo_url, DATABASE_NAME, COLLECTION_NAME)
            query = [{"lang": formatted_lang}, {"text":1, "user.name":1, "lang":1}]
            query_type = "select"
            result = mongo_con.execute_query(query, query_type)

            if result[STATUS_KEY] == STATUS_FAILED:
                raise Exception(result[ERROR_KEY])

            utility_status[RESULT_KEY] = []

            for record in result[RESULT_KEY]:
                if "_id" in record:
                    del record["_id"]
                utility_status[RESULT_KEY].append(record)

            utility_status[STATUS_KEY] = STATUS_SUCCESS
            return utility_status

        except Exception as exp:
            if ERROR_KEY in utility_status:
                error_msg = "Error while fetching tweets by language in viewsutils: " + str(utility_status[ERROR_KEY])
                print(error_msg)
            else:
                error_msg = "Error while fetching tweets by language in viewsutils: " + str(exp)
                print(error_msg)
            utility_status[STATUS_KEY] = STATUS_FAILED
            utility_status[ERROR_KEY] = error_msg
            return utility_status
