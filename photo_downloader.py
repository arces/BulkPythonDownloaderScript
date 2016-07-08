import urllib.request

file_type = ".jpg"
base_url = ""
num_of_times = input("Enter loop amount: ")

num_of_times = int(num_of_times) + 0
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent': user_agent, }
print(" ")

while num_of_times > 0:
    if (num_of_times>=10):
        url = base_url + str(num_of_times) + file_type
    else:
        url = base_url + "0"+ str(num_of_times) + file_type
    file_name = str(num_of_times)+file_type
    print("Downloading: " + url)
    print("Photo will be saved as: " + file_name)

    try:
        request = urllib.request.Request(url, None, headers)
        response = urllib.request.urlopen(request)
        data = response.read()
        f = open(file_name, 'wb')
        f.write(data)
        f.close()
        print("Download complete")
        print(" ")

    except:
        print("Download failed... moving to next photo")

    num_of_times -= 1
