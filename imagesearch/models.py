"""
Exports ImageSearch app data models.
"""

from datetime import datetime

from mongoengine import DateTimeField, Document, StringField

class SearchEntry(Document):
    terms = StringField()
    when = DateTimeField(default=datetime.utcnow)

    meta = {"collection": "searches"}

    def to_json(self):
        return {
            "terms": self.terms,
            "when": self.when.isoformat()
        }
