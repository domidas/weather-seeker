from os.path import exists

key = input("Please enter your API key: ")

c = open(".api_key","a")

c.write(key)

c.close()

file_exists = exists("./.api_key")

if file_exists == True:

    print("Success!")

else:

    print("ERROR: Failed to create API key file.")
