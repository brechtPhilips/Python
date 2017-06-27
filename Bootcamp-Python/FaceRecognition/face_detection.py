# coding=utf-8
import glob

import kairos_face

kairos_face.settings.app_id = "79a716fe"
kairos_face.settings.app_key = "4ecebdf074dd075766b066b49a5c49a4"

# List all galleries that have been created.
# gallerie_list = kairos_face.get_galleries_names_list()
# remove_gallery = kairos_face.remove_gallery('a-gallery')

# Verify from a file
# recognized_faces = kairos_face.verify_face(subject_id="brecht",gallery_name="a-gallery",file="test.jpg")

for file in glob.glob("/Volumes/SD-Kaart/Privé/fotosgsm/Snapfun/*.PNG"):
    count = 0
    recognized_face = kairos_face.detect_face(file=file)
    if recognized_face:
        if kairos_face.recognize_face(file="test.jpg", gallery_name="snapfun-gallery"):
            print ("face is recognised!")
            print(recognized_face)
        else:
            # Enrolling from a file
            print("starting")
            kairos_face.enroll_face(file=file, subject_id=count, gallery_name='snapfun-gallery')
            print("next one")
            count += 1

    else:
        print("No face found!")

galleries_object = kairos_face.get_galleries_names_object()
for gallery_name in galleries_object:
    gallery = kairos_face.get_gallery_object(gallery_name)
    print('Gallery name: {}'.format(gallery.name))
    print('Gallery subjects: {}'.format(gallery.subjects))
