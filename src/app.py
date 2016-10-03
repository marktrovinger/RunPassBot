import train_model
import tpot_generation

cmdargs = sys.argv

def main():	
	# load the dataset, if it is clean
	train_X, test_X, train_y, test_y = train_model()

	if 'generate' in cmdargs:
		generate_model(10, train_X, train_y)
	pass

if __name__ == '__main__':
	main()