import wifi_qrcode_generator.generator
qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
    ssid=input("SSID: "),
    hidden=bool(input("Hidden (true or false): ")),
    authentication_type=input("Authentication Type: "),
    password=input("Password: ")
)
qr_code.make_image().save('wifi_qr.png')
