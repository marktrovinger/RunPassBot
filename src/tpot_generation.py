##
# tpot_generation - Adds functionality for generating models using TPOT
#
##

from tpot import TPOTClassifier

##
# generate_model - Uses TPOT to generate a probable model for usage, exports the
#					model as a .py file
##
def generate_model(generations, train_X, train_y):
	tpot_generator = TPOTClassifier(generations=generations, verbosity=2)
	tpot_generator.fit(train_X, train_y)
	tpot_generator.export('tpot_model' + generations + '.py')

