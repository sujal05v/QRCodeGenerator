import qrcode

# Taking UPI ID as a input
upi_id = input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&apn=NAME7am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining the payment URL based on the UPI ID and the payemnt app
#You can modify these URLs based on the payment apps you want to support

phonepe_url =f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url =f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
googlepay_url =f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create QR codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
googlepay_qr = qrcode.make(googlepay_url)

#save the QR code to image file(optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
googlepay_qr.save('googlepay_qr.png')

#Display the QR codes ((You may need to install PIL/Pillow library))

phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()