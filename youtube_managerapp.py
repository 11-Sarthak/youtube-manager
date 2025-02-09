import json
def load_data():  
    try:    
        with open ('youtube.txt','r') as fp:  
            test= json.load(fp)
            return test  
    except FileNotFoundError:   
        return []

def save_data_helper(videos):  
    with open('youtube.txt','w') as fp: 
        return json.dump(videos,fp)  
        


def listallvideos(videos):  
    print("\n")
    print ("*" * 70)
    for index,video in enumerate(videos,start=1):   
        print(f"{index}.{video['name']},Duration:{video['time']}")
    print("\n")
    print ("*" * 70)
def addayoutubevideo(videos):   
            name=input("video name:")
            time=input("video time:")   
            videos.append({'name':name,'time':time})
            save_data_helper(videos)
def updateyoutubevideo(videos): 
    listallvideos(videos)
    index=int(input("Enter the video number to update "))
    if 1<=index<=len(videos):  
        name=input("enter the new video name")
        time=input("enter the new video time")
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
    else:   
        print('invalid index')



def deleteyoutubevideo(videos): 
    listallvideos(videos)
    index=int(input('enter the video number to be deleted'))
    if 1<=index<=len(videos):   
        del videos[index-1]
        save_data_helper(videos)
    else:   
        print('invalid video index')
def main():
    videos=load_data()

    while True: 
        print("\n youtube manager | choose an option")
        print("1.list a all youtube video")
        print("2.add a youtube video")
        print("3.update a youtube video with details")
        print("4. delete a youtube video")
        print("5. exit the app")
        choice=input("enter your choice ")
        

        match choice:   
            case '1':   
                listallvideos(videos)   
            case '2':   
                addayoutubevideo(videos)
            case '3':   
                updateyoutubevideo(videos)
            case '4':   
                deleteyoutubevideo(videos)
            case '5':
                break   
            case _: 
                print("invalid choice")


if __name__=="__main__":    
    main()