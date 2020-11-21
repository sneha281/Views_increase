from pytube import YouTube
from tkinter.filedialog import  *
from tkinter.messagebox import *
from tkinter import *
from threading import *
font = ('verdana', 20)
file_size= 0
def completeDownload (stream = None, file_path =None):
    print("download completed")
    showinfo("Message", "File has been downloaded...")
    db['text']= "Download Video"
    db['state'] = "active"
    urlfield.delete(0,END)
def progressDownload(stream = None, chunck= None,bytes_remaining = None):
    per = (100*(file_size-bytes_remaining)/file_size)
    db['text']= "{:00.0f}% downloaded " .format(per)
def btnclick():
    try :
        db['text']= 'Please Wait....'
        db['state']= 'disable'
        url =urlfield.get()
        if url=='':
            return
        print(url)
        thread =Thread(target=down, args=(url,))

        thread.start()
    except EXCEPTION as e:
        print(e)
def down(url):
    global file_size
    path = askdirectory()
    if path is None:
        return
    try:
        yt =YouTube(url)
        st =yt.streams.first()
        yt.register_on_complete_callback(completeDownload)
        yt.register_on_progress_callback(progressDownload)
        file_size = st.filesize
        st.download(output_path=path)
        showinfo("Message", "File has been downloaded...")
    except Exception as e:
        print(e)
root = Tk()
root.title("Sneha's Youtube Downloader")
root.geometry("500x600")
photo = PhotoImage(file = "yotube.png")
headingIcon = Label(root, image = photo)
headingIcon.pack(side = TOP ,pady = 3)
urlfield = Entry(root,font= font,justify = CENTER)
urlfield.pack(side = TOP,fill = X,padx = 10)
urlfield.focus()
db = Button(root,text = "start download", font= font,relief = 'ridge', command = btnclick)
db.pack(side = TOP, pady = 20)

root.mainloop()
