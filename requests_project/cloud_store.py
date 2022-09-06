from requests_project.utils import MongoConnectionManager


def store_data(data, target_collection):
    with MongoConnectionManager(target_collection) as session:
        session.insert_many(data)
