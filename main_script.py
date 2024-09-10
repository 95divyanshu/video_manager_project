# importing the json file
import json

# this function will load data from our json file into a python object
def loadData():
    try:
        with open("data.json",'r') as file:
            data = json.load(file) # type of data is list
            return data
    except FileNotFoundError:
        return [] # return an empty list if the file isn't found

# this function will be called when the user selects "list all videos" option
def listAllVideos(videos):
    print("Output : ")
    print("____________________________________________________________________________________________________________")
    print(" ")
    for index, video in enumerate(videos,start=1):
        print(f"{index}. name : {video['name']} time : {video['time']} min")
    print(" ")
    print("____________________________________________________________________________________________________________")

# this function will be called when the user selects "add a video" option
def addAVideo(videos):
    print("____________________________________________________________________________________________________________")
    print(" ")

    name = input("Enter video name : ")
    time = input("Enter video time : ")
    videos.append({"name":name, "time":time})
    print(" ")
    print("new video added successfully!")
    print(" ")
    print("____________________________________________________________________________________________________________")
    helperMethod(videos)

# this function will be called when the user select "delete a video" option
def deleteAVideo(videos):
    print("____________________________________________________________________________________________________________")
    print(" ")
    index = int(input("Enter the index you want to update : "))
    if 1<=index<=len(videos):
        del videos[index-1]
        helperMethod(videos)
        print(" ")
        print("video deleted successfully")
        print(" ")
    else:
        print("invalid index selected!")
    print("____________________________________________________________________________________________________________")
    print(" ")

# this function will be called when the user selects "update a video" option
def updateAVideo(videos):
    print("____________________________________________________________________________________________________________")
    print(" ")
    index = int(input("Enter the index you want to update : "))
    if 1<=index<=len(videos):
        name = input("Enter the new name : ")
        time = input("Enter the new video time : ")
        videos[index-1] = {'name':name,"time":time}
        helperMethod(videos)
        print(" ")
        print("video updates successfully!")
        print(" ")
    else:
        print("invalid index selected!")

# this function saves the changes to the json file (which contains the data)
def helperMethod(videos):
    with open("data.json",'w') as file:
        json.dump(videos,file)

# the main function
def main():
    # first, we'll load the data from the json file 
    videos = loadData()
    # we will keep asking the user if he/she wants do something more, until he/she wants to exit the video manager assitant 
    while True:
        # welcome message 
        print(" ")
        print("WELCOME TO THE VIDEO MANGER ASSISTANT")
        print("")
        # asking user to select an option from the lists options
        print("Please select an option : ")
        print("1. list all videos")
        print("2. add a video")
        print("3. update a video")
        print("4. delete a video")
        print("5. exit youtube manager application")
        print("")
        choice = input("Enter your choice: ")
        print(" ")
        # calling the respective function, according the user's input
        match choice:
            case '1':
                listAllVideos(videos)
            case '2':
                addAVideo(videos)
            case '3':
                updateAVideo(videos)
            case '4':
                deleteAVideo(videos)
            case '5':
                break
            case _:
                print("invalid check")

# run this main_script only when it's being run directly
if __name__ == "__main__":
    main()