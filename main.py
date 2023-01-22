import tkinter as tk  # Gui Library
import tkinter.font as tkFont
import cv2  # openCV for face Detection
from deepface import DeepFace  # Emotion Identification Library
res = ""
class App:
    def __init__(self, root):
        #setting title
        root.title("Emotion Identification")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_128=tk.Label(root)
        ft = tkFont.Font(family='Times',size=15)
        GLabel_128["font"] = ft
        GLabel_128["fg"] = "#333333"
        GLabel_128["justify"] = "center"
        GLabel_128["text"] = ""
        GLabel_128.place(x=350,y=240,width=386,height=82)

        GLabel_450 = tk.Label(root)
        GLabel_450["bg"]="#999c9f"
        ft = tkFont.Font(family='Times', size=15)
        GLabel_450["font"] = ft
        GLabel_450["fg"] = "#333333"
        GLabel_450["justify"] = "center"
        GLabel_450["text"] = ""
        GLabel_450.place(x=0, y=0, width=603, height=506)

        GButton_167=tk.Button(root)
        GButton_167["bg"] = "#c1bbbb"
        ft = tkFont.Font(family='Times',size=23)
        GButton_167["font"] = ft
        GButton_167["fg"] = "#000000"
        GButton_167["justify"] = "center"
        GButton_167["text"] = "OPEN CAMERA"
        GButton_167["borderwidth"]="8px"
        GButton_167.place(x=180,y=280,width=248,height=85)
        GButton_167["command"] = self.GButton_167_command

        GLabel_316=tk.Label(root)
        GLabel_316["bg"] = "#191a1a"
        ft = tkFont.Font(family='Times',size=30)
        GLabel_316["font"] = ft
        GLabel_316["fg"] = "#ffffff"
        GLabel_316["justify"] = "center"
        GLabel_316["text"] = "EmotionChecker"
        GLabel_316.place(x=0,y=50,width=603,height=77)

        GLabel_730=tk.Label(root)
        ft = tkFont.Font(family='Times',size=21)
        GLabel_730["font"] = ft
        GLabel_730["fg"] = "#333333"
        GLabel_730["justify"] = "center"
        GLabel_730["text"] = "Emotion Detection Using Face Recognition"
        GLabel_730.place(x=0,y=155,width=603,height=77)

    def GButton_167_command(self):
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("Mood Detection")
        img_counter = 0
        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("test", frame)

            k = cv2.waitKey(1)
            if k % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k % 256 == 32:
                # SPACE pressed
                img_name = "opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1
                img1 = cv2.imread(img_name)
                result = DeepFace.analyze(img1, actions=['emotion'])
                res = result['dominant_emotion']
                print(result)
                GLabel_128 = tk.Label(root)
                ft = tkFont.Font(family='Times', size=15)
                GLabel_128["font"] = ft
                GLabel_128["fg"] = "#333333"
                GLabel_128["justify"] = "center"
                GLabel_128["text"] = "Detected Emotion: "+ res
                GLabel_128.place(x=180, y=390, width=248, height=53)
                #res = result['dominant_emotion']
                print(res)

                cam.release()
                cv2.destroyAllWindows()
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
