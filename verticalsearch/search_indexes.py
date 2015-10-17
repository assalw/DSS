from haystack import indexes
from verticalsearch.models import RedditUser


class RedditUserIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    username = indexes.CharField(model_attr='username')

    def get_model(self):
        return RedditUser

