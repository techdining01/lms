import qrcode


def generate_qr(verification_url):

    qr = qrcode.make(verification_url)

    return qr