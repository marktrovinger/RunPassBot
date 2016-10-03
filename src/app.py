from train_model import train_model, load_dataset
from tpot_generation import generate_model
import sys

cmdargs = sys.argv

def main():	
	# load the dataset, if it is clean
	print('Loading dataset...')
	train_X, test_X, train_y, test_y = load_dataset()

	if 'generate' in cmdargs:
		print('Generating new model...')
		generate_model(10, train_X, train_y)
	pass

if __name__ == '__main__':
	main()