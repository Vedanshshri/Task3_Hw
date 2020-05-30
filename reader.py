#This code have motive to read the file that will be provided by developer of code.
#we will do soe normal file handling in this code and we will try to extract main information needed from the code


dev_code = open('root/hw_ws1/dev_code.py')  #as normal file handling this code will open the file  and store in dev_code

code = dev_code.read()  #this have just a read function which will read tha whole code and store it in code

if  'sklearn' or 'pandas' and 'LinearRegression' in code :  
#we are using if function on the readed file and find some specific words like sklearn or pandas and LinearRegression if these words are found then them we will say if is LinearModel
	print('LinearModel')

elif 'KneighborsClassifier'  :

#similarly this will find the word KneighborsClassifier and if it found then it is KNN_MODEL
	print('KNN_CODE')

elif 'keras' or tensorflow in code :
#similar
	if 'Conv2D' in code :
		print('CNN_CODE')
	else :
		print('NOT_CNN')
else :
	print('NotRecognized')
