from web_app import db

class LanguageRegionMap(db.Model):
	__tablename__ = 'LanguageRegionMap'
	#__table_args__ = (
        #db.PrimaryKeyConstraint('id'),
    #)
	language_id = db.Column(db.Integer, primary_key=True)
	language  = db.Column(db.String, nullable=False)
	region = db.Column(db.String, nullable=False)

class Character(db.Model):
	__tablename__ = 'CharacterPhonologyMap'
	decimal = db.Column(db.Integer, primary_key=True)
	character = db.Column(db.String, nullable=False)
	charset = db.Column(db.String)
	language = db.Column(db.String)
	dialect = db.Column(db.String)
	is_punctuation = db.Column(db.Boolean, nullable=False)
	is_printable = db.Column(db.Boolean, nullable=False)
	phonology_engb = db.Column(db.String)
	
class Word(db.Model):
	__tablename__ = 'WordsList'
	word_id = db.Column(db.Integer, primary_key = True)
	word = db.Column(db.String, nullable=False)
	phonology_engb = db.Column(db.String)
	is_plural = db.Column(db.Boolean)
	root = db.Column(db.String)
	dictionary_tags = db.Column(db.String)
	upenn_tag1 = db.Column(db.String)
	upenn_tag2 = db.Column(db.String)
	definition = db.Column(db.String)

