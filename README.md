#**Cryptography **
Cryptography is the study of secure communications techniques that allow only the sender and intended recipient of a message to view its contents. The term is derived from the Greek word Kryptos, which means hidden. It is closely associated to encryption, which is the act of scrambling ordinary text into what's known as ciphertext and then back again upon arrival. In addition, cryptography also covers the obfuscation of information in images using techniques such as microdots or merging. Ancient Egyptians were known to use these methods in complex hieroglyphics, and Roman Emperor Julius Caesar is credited with using one of the first modern ciphers.
 
Fig. 1.1 – Cryptography block diagram

When transmitting electronic data, the most common use of cryptography is to encrypt and decrypt email and other plain-text messages. The simplest method uses the symmetric or "secret key" system. Here, data is encrypted using a secret key, and then both the encoded message and secret key are sent to the recipient for decryption. The problem? If the message is intercepted, a third party has everything they need to decrypt and read the message. To address this issue, cryptologists devised the asymmetric or "public key" system. In this case, every user has two keys: one public and one private. Senders request the public key of their intended recipient, encrypt the message and send it along. When the message arrives, only the recipient's private key will decode it — meaning theft is of no use without the corresponding private key.
Proposed method: Flowchart
Encryption:

 
Fig. 1.2 – Encryption using shift cipher and steganography



Decryption:

 

Fig. 1.3 – Decryption using steganography and shift cipher 


Used Cryptography Techniques:

1.	Shift Ciphers 
	Shift Ciphers work by using the modulo operator to encrypt and decrypt messages. The Shift Cipher has a key K, which is an integer. We will only share this key with people that we want to see our message.

How to Encrypt:
For every letter in the message M:

1. Convert the letter into the number that matches its order in the alphabet starting from 0, and call this number X.
(A=0, B=1, C=2, ..., Y=24, Z=25)
2. Calculate: Y = (X + K) mod 26
3. Convert the number Y into a letter that matches its order in the alphabet starting from 0.
(A=0, B=1, C=2, ..., Y=24, Z=25)

For Example: We agree with our friend to use the Shift Cipher with key K=5 for our message. 
We encrypt the message "SARVESH", as follows:
So, after applying the Shift Cipher with key K=5 our message text "SARVESH" gave us cipher text "XFWAJXM".
We give the message "XFWAJXM" to our friend.

How to decrypt:
For every letter in the cipher text C:

1. Convert the letter into the number that matches its order in the alphabet starting from 0, and call this number Y.
(A=0, B=1, C=2, ..., Y=24, Z=25)
2. Calculate: X= (Y - K) mod 26
3. Convert the number X into a letter that matches its order in the alphabet starting from 0.
(A=0, B=1, C=2, ..., Y=24, Z=25)
Our friend now decodes the message using our agreed upon key K=5. As follows:

So, after decrypting the Shift Cipher with key K=5 our friend deciphers the cipher text "XFWAJXM" into the message text "SARVESH".








2.	Image Based Steganography
	Steganography is the method of hiding secret data in any image/audio/video. In a nutshell, the main motive of steganography is to hide the intended information within any image/audio/video that doesn’t appear to be secret just by looking at it.
	The idea behind image-based Steganography is very simple. Images are composed of digital data (pixels), which describes what’s inside the picture, usually the colors of all the pixels. Since we know every image is made up of pixels and every pixel contains 3-values (red, green, blue).

Encode the data:
Every byte of data is converted to its 8-bit binary code using ASCII values. Now pixels are read from left to right in a group of 3 containing a total of 9 values. The first 8-values are used to store binary data. The value is made odd if 1 occurs and even if 0 occurs. 

For example: 
Suppose the message to be hidden is ‘ Hii ‘. Since the message is of 3-bytes, therefore, pixels required to encode the data is 3 x 3 = 9. Consider a 4 x 3 image with a total 12-pixels, which are sufficient to encode the given data.

[(27, 64, 164), (248, 244, 194), (174, 246, 250), (149, 95, 232),
(188, 156, 169), (71, 167, 127), (132, 173, 97), (113, 69, 206),
(255, 29, 213), (53, 153, 220), (246, 225, 229), (142, 82, 175)]

ASCII value of ‘H‘ is 72 whose binary equivalent is 01001000.

Taking first 3-pixels (27, 64, 164), (248, 244, 194), (174, 246, 250) to encode. Now change the pixel to odd for 1 and even for 0. So, the modifies pixels are (26, 63, 164), (248, 243, 194), (174, 246, 250). Since we have to encode more data, therefore, the last value should be even. Similarly, ‘i‘ can be encoded in this image.
The new image will look like:
 
[(26, 63, 164), (248, 243, 194), (174, 246, 250), (148, 95, 231),
(188, 155, 168), (70, 167, 126), (132, 173, 97), (112, 69, 206),
(254, 29, 213), (53, 153, 220), (246, 225, 229), (142, 82, 175)]


Decode the data:
To decode, three pixels are read at a time, till the last value is odd, which means the message is over. Every 3-pixels contain a binary data, which can be extracted by the same encoding logic. If the value if odd the binary bit is 1 else 0. 

 
Workflow:
1.	Encryption
Step 01: Run the python program. User will land on main page. Click on <ENCRYPT> button
       

Step 02: The user will land on Encrypt page. 
 

Step 03: User can select text file which he wants to encrypt by clicking <BROWSE> button
 
Step 04: Enter Key 1 and Loop Value both should be numeric values and click <ENCRYPT> button. The ciphertext will be displayed in the preview window.
 

Step 05: Click <BROWSE> button to select an input image in which the user wants to embed the ciphertext 

 

Selected image will be displayed in preview window. 
Step 06: Enter output image name and file extension and click <ENCRYPT> Button

 

The ciphertext will be embedded inside the image and the image is saved in Output folder
 



1.	Decryption
Step 01: Run the python program. User will land on main page. Click on <DECRYPT> button
       

Step 02: The user will land on Decryption page.
 

Step 03: User can select input image from which he wants to extract the Cipher Text by clicking <BROWSE> button
 
Step 04: Click on <DECRYPT> button to extract Cipher Text from the input image 
 

Step 05: Enter output file name, Key 1 and Loop value to decrypt the Cipher Text. The Decrypted file will be saved in output folder.
 
The user can verify the decrypted message in Preview window.

Conclusion:
	The Application to Encrypt and Decrypt text files using two cryptography methods was implemented successfully. We studied shift cipher in detail and implemented it using python language and the second technique we used is Image Based Steganography in which we embedded ciphertext inside the pixel values of the image. The UI was developed in Python and we tried to make it user friendly so that users with limited knowledge of programming can also use the application seamlessly.
