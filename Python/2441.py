def star():
	num=int(input())
	
	for i in range(num,0,-1):
		print(" "*(num-i)+"*"*i)

def main():
	star()

if __name__ == "__main__" :
	main()