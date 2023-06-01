########################################################################
# IMPORT GUI FILE
from ui_interface_pfe_project import *
########################################################################
# IMPORTS
import sys
import os
########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
########################################################################
import cv2
import numpy as np
import face_recognition
import json

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################

        self.show()
        
        # EXPAND CENTER MENU WIDGET SIZE
        # self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        # self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())

        
        # CLOSE NOTIFICATION MENU WIDGET SIZE
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())
        
        # Create a timer for updating the video stream
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame_reco_video)
        
        self.timer_2 = QTimer(self)
        self.timer_2.timeout.connect(self.update_frame_screenshot_video)
        
        # Start the video stream
        self.ui.cameraActiveBtn.clicked.connect(self.start_webcam)
        # Connect the button's clicked signal to a function
        self.ui.cameraDesactiveBtn.clicked.connect(self.closeEvent)
        self.ui.cameraActiveBtn_3.clicked.connect(self.start_webcam_2)
        self.ui.cameraDesactiveBtn_3.clicked.connect(self.closeEvent_2)
        self.ui.recognizeBtn.clicked.connect(self.recognize)
        self.ui.addBtn.clicked.connect(self.insert_user)
        self.ui.clearDataBtn.clicked.connect(self.clearData)
        self.ui.cancelBtn.clicked.connect(self.clearInsertData)
        self.ui.screenshotBtn.clicked.connect(self.screenshot)
        self.ui.changeScreenshotBtn.clicked.connect(self.changeScreenshot)
        
        self.ui.database.setColumnWidth(0,50)
        self.ui.database.setColumnWidth(1,180)
        self.ui.database.setColumnWidth(2,180)
        self.ui.database.setColumnWidth(3,120)
        self.ui.database.setColumnWidth(4,200)
        self.ui.database.setColumnWidth(5,502)
        
        self.load_data()
################################################################################################################################################
    def start_webcam(self):
        # Open the webcam
        self.cap = cv2.VideoCapture(0)
        self.ui.label_8.setText("La webcam a démarré.")
        # Start the timer to update the frame
        self.timer.start()  # Update the frame every 30 milliseconds
        
################################################################################################################################################        
    def start_webcam_2(self):
        # Open the webcam
        self.cap_2 = cv2.VideoCapture(0)
        self.ui.label_8.setText("La webcam a démarré.")
        # Start the timer to update the frame
        self.timer_2.start()  # Update the frame every 30 milliseconds
################################################################################################################################################    
    def recognize(self):
        
        with open('data.json') as json_file:
            data = json.load(json_file)

        images = []
        classNames = []

        for user_data in data['users']:
            curPersonn = cv2.imread(user_data["img_path"])
            images.append(curPersonn)
            classNames.append(user_data['firstname'])

        def findEncodeings(image):
            encodeList = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encodeList.append(encode)
            return encodeList
        
        print('Encoding start...')
        
        encodeListKnown = findEncodeings(images)
        print('Encoding Complete.')
        img_screenshot = cv2.imread('screenshot/screenshot.png')
        imgS = cv2.resize(img_screenshot, (0,0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        faceCurentScreenshot = face_recognition.face_locations(imgS)
        encodeCurentScreenshot = face_recognition.face_encodings(imgS, faceCurentScreenshot)
        
        for encodeface, faceLoc in zip(encodeCurentScreenshot, faceCurentScreenshot):
            matches = face_recognition.compare_faces(encodeListKnown, encodeface)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeface)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                for user_data in data['users']:
                    if user_data['id'] == matchIndex:
                        self.ui.fnameData.setText(f"{user_data['firstname']}")
                        self.ui.lnameData.setText(f"{user_data['lastname']}")
                        self.ui.ageData.setText(f"{user_data['age']}")
                        self.ui.phonenumData.setText(f"{user_data['phonenum']}")
                        self.ui.emailData.setText(f"{user_data['email']}")
                        print(user_data['firstname'])
                        
        self.ui.label_8.setText("Reconnaissance faciale réussie avec succès.")
 
################################################################################################################################################  
    def update_frame_reco_video(self):
        # Read the current frame from the webcam
        ret, frame = self.cap.read()

        if ret:
            frame_2 = frame
            # Convert the frame to RGB format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # # Resize the frame to fit the label/widget size
            frame = cv2.resize(frame, (self.ui.videoLive.width(), self.ui.videoLive.height()))
            
            imgS = cv2.resize(frame, (0,0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            faceCurentFrame = face_recognition.face_locations(imgS)

            for faceLoc in faceCurentFrame:
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0,0,255), 2)
                    
            cv2.imwrite('screenshot/screenshot.png', frame_2)

            # Convert the frame to QImage
            image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)

            # Display the image in the label/widget
            self.ui.videoLive.setPixmap(QPixmap.fromImage(image))
            
        else:
            pixmap = QPixmap('backgrounds/face_reco.jpg')
            pixmap = pixmap.scaled(self.ui.videoLive.width(), self.ui.videoLive.height(), aspectRatioMode=True)  # Scale the QPixmap to fit the label size
            self.ui.videoLive.setPixmap(pixmap)
        
################################################################################################################################################       
    def update_frame_screenshot_video(self):
        
        # Read the current frame from the webcam
        ret, frame = self.cap_2.read()

        if ret:
            frame_2 = frame
            # Convert the frame to RGB format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # # Resize the frame to fit the label/widget size
            frame = cv2.resize(frame, (self.ui.videoLive_3.width(), self.ui.videoLive_3.height()))
            
            imgS = cv2.resize(frame, (0,0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            faceCurentFrame = face_recognition.face_locations(imgS)
            
            

            for faceLoc in faceCurentFrame:
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0,0,255), 2)
                    

            # Convert the frame to QImage
            image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)

            # Display the image in the label/widget
            self.ui.videoLive_3.setPixmap(QPixmap.fromImage(image))
              
        else:
            pixmap = QPixmap('backgrounds/face_reco.jpg')
            pixmap = pixmap.scaled(self.ui.videoLive_3.width(), self.ui.videoLive_3.height(), aspectRatioMode=True)  # Scale the QPixmap to fit the label size
            self.ui.videoLive_3.setPixmap(pixmap)
            
################################################################################################################################################           
    def screenshot(self):
        # Read the current frame from the webcam
        ret, frame = self.cap_2.read()

        if ret:

            # # Resize the frame to fit the label/widget size
            frame = cv2.resize(frame, (self.ui.videoLive_3.width(), self.ui.videoLive_3.height()))
            cv2.imwrite('screenshot/screenshot.png', frame)
            self.timer_2.stop()
            self.cap_2.release()
            self.ui.label_8.setText("Capture de photo effectuée avec succès.")
################################################################################################################################################    
    def closeEvent(self , event):
        # Stop the timer and release the webcam
        self.timer.stop()
        self.cap.release()
        pixmap = QPixmap('backgrounds/face_reco.jpg')
        pixmap = pixmap.scaled(self.ui.videoLive.width(), self.ui.videoLive.height(), aspectRatioMode=True)  # Scale the QPixmap to fit the label size
        self.ui.videoLive.setPixmap(pixmap)
        # self.ui.videoLive.setScaledContents(True)
        # event.accept()
        self.ui.label_8.setText("La webcam s'est arrêtée avec succès.")
################################################################################################################################################       
    def closeEvent_2(self , event):
        # Stop the timer and release the webcam
        self.timer_2.stop()
        self.cap_2.release()
        pixmap = QPixmap('backgrounds/face_reco.jpg')
        pixmap = pixmap.scaled(self.ui.videoLive_3.width(), self.ui.videoLive_3.height(), aspectRatioMode=True)  # Scale the QPixmap to fit the label size
        self.ui.videoLive_3.setPixmap(pixmap)
        # self.ui.videoLive.setScaledContents(True)
        # event.accept()
        self.ui.label_8.setText("La webcam s'est arrêtée avec succès.")
################################################################################################################################################        
    def load_data(self):
        with open('data.json', 'r') as file:
            json_data = json.load(file)

        self.ui.database.setRowCount(len(json_data['users']))
        self.ui.database.setColumnCount(6)  # Assuming 4 columns for id, name, age, email

        for row, user in enumerate(json_data['users']):
            id_item = QTableWidgetItem(str(user["id"]))
            firstname_item = QTableWidgetItem(user['firstname'])
            lastname_item = QTableWidgetItem(user['lastname'])
            age_item = QTableWidgetItem(str(user["age"]))
            phonenum_item = QTableWidgetItem(str(user["phonenum"]))
            email_item = QTableWidgetItem(user['email'])
            
            self.ui.database.setItem(row, 0, id_item)
            self.ui.database.setItem(row, 1, firstname_item)
            self.ui.database.setItem(row, 2, lastname_item)
            self.ui.database.setItem(row, 3, age_item)
            self.ui.database.setItem(row, 4, phonenum_item)
            self.ui.database.setItem(row, 5, email_item)
################################################################################################################################################
    def insert_user(self):
        # Read the existing JSON data, if any
        try:
            with open("data.json", "r") as file:
                json_data = json.load(file)
        except FileNotFoundError:
            json_data = []

        # Retrieve the data from the QLineEdit widgets
        id = len(json_data['users'])+1
        firstname = self.ui.fnameInsertData.text()
        lastname = self.ui.lnameInsertData.text()
        age = self.ui.ageInsertData.text()
        phonenum = self.ui.phonenumInsertData.text()
        email = self.ui.emailInsertData.text()
        img_path = "screenshot/screenshot.png"

        # Create a dictionary object with the user's data
        new_user = { "id": int(id), "firstname": firstname, "lastname": lastname, "age": int(age), "phonenum": phonenum, "email": email, "img_path": img_path }

        # Add the new user to the existing JSON data
        json_data["users"].append(new_user)

        # Write the updated JSON data back to the file
        with open("data.json", "w") as file:
            json.dump(json_data, file)

        # Clear the QLineEdit widgets after inserting the user
        self.ui.fnameInsertData.clear()
        self.ui.lnameInsertData.clear()
        self.ui.ageInsertData.clear()
        self.ui.phonenumInsertData.clear()
        self.ui.emailInsertData.clear()
        self.ui.label_8.setText("Les données ont été insérées avec succès.")
        self.start_webcam_2
        
################################################################################################################################################
    def clearData(self):
        self.ui.fnameData.clear()
        self.ui.lnameData.clear()
        self.ui.ageData.clear()
        self.ui.phonenumData.clear()
        self.ui.emailData.clear()
        self.ui.label_8.setText("Les données ont été effacées avec succès.")
################################################################################################################################################
    def clearInsertData(self):
        self.start_webcam_2()
        self.ui.fnameInsertData.clear()
        self.ui.lnameInsertData.clear()
        self.ui.ageInsertData.clear()
        self.ui.phonenumInsertData.clear()
        self.ui.emailInsertData.clear()
        file_path = "/media/ismail_charai/PROGRAMS/PROJECT/FACE-RECOGNITION-PFE-PROJECT/screenshot/screenshot.png"
        self.delete_photo(file_path)
        self.ui.label_8.setText("L'insertion de données a été annulée.")
################################################################################################################################################
    def changeScreenshot(self):
        self.start_webcam_2()
        file_path = "/media/ismail_charai/PROGRAMS/PROJECT/FACE-RECOGNITION-PFE-PROJECT/screenshot/screenshot.png"
        self.delete_photo(file_path)
        self.ui.label_8.setText("La capture d'écran a été supprimée avec succès.")
################################################################################################################################################        
    def delete_photo(self, file_path):
        try:
            os.remove(file_path)
            print(f"Deleted photo: {file_path}")
        except FileNotFoundError:
            print(f"Photo not found: {file_path}")
        except Exception as e:
            print(f"Error deleting photo: {e}")
        # self.ui.label_8.setText("screenshot deleted")
        
################################################################################################################################################
## EXECUTE APP
################################################################################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
################################################################################################################################################
## END===>
################################################################################################################################################