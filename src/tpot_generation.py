##
# tpot_generation - Adds functionality for generating models using TPOT
#
##

from tpot import TPOT

##
# generate_model - Uses TPOT to generate a probable model for usage, exports the
#					model as a .py file
##
def generate_model(generations, verbosity, train_X, train_y):
	tpot_generator = TPOT(generations=generations, verbosity=verbosity)
	tpot_generator.fit(train_X, train_y)
	tpot_generator.export('tpot_model' + generations + verbosity + '.py')

