from django.db import models
from .utils import load_data, save_data, load_admins


# Create your models here.

class Article:
    @staticmethod
    def all():
        return load_data()

    @staticmethod
    def get(p_id):
        data = load_data()
        post = data[f"{p_id}"]
        if post:
            return post
        return None

    @staticmethod
    def create(article_data):
        data = load_data()
        data[f"{len(data) + 1}"] = article_data
        save_data(data)
        return article_data

    @staticmethod
    def update(article_id, new_data):
        data = Article.all()
        if data[article_id]:
            data[article_id]=new_data
            save_data(data=data)


    @staticmethod
    def delete(post_id):
        data = load_data()
        print(post_id)
        new_data = {id_:post for id_,post in data.items() if id_ != str(post_id)}
        i = 1
        new_ = {}
        for id_,p in new_data.items():
            new_[i] = p
            i += 1

        new_data = new_
        if len(new_data) != len(data):
            save_data(new_data)
            return True
        return False


class Admins:
    @staticmethod
    def load_admins():
        return load_admins()

    @staticmethod
    def verify_ad(ad_name, ad_password):
        data = load_admins()
        try:
            if data[ad_name] == ad_password:
                print(ad_name,ad_password)
                return True
        except KeyError:
            return False
