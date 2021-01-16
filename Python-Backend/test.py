import requests
rootDomain = "https://pickafriend.gulk.dev"

def test1(img='test images/im0.jpg'):
    # just uploads an image with no password
    r = requests.post(f"{rootDomain}/upload/", files={'image.jpg': open(img, 'rb')})
    return r.text

def test2():
    # runs test 1, then pulls image back
    code = test1("test images/im1.jpg")

    r = requests.get(f'{rootDomain}/images/{code}')
    if r.status_code == 200:
        with open('test2.jpg', 'wb') as f:
            f.write(r.content)
        return 200

    else:
        return r.status_code

def test3(img='test images/im2.jpg'):
    # like test 1, but with a password
    r = requests.post(f"{rootDomain}/upload/", files={'image.jpg': open(img, 'rb')}, headers={"psswd":"test3"})
    return r.text

def test4():
    # test 2 with a password
    code = test3("test images/im3.jpg")

    r = requests.get(f'{rootDomain}/images/{code}', headers={"psswd":"test3"})
    if r.status_code == 200:
        with open('test4.jpg', 'wb') as f:
            f.write(r.content)
        return 200

    else:
        return r.status_code

def test5():
    # test 4 using the wrong password
    code = test3("test images/im4.jpg")

    r = requests.get(f'{rootDomain}/images/{code}', headers={"psswd":"incorrect password"})
    if r.status_code == 200:
        with open('test5.jpg', 'wb') as f:
            f.write(r.content)
        return 200

    else:
        return r.status_code

def test6():
    # try to get a non existant image
    r = requests.get(f'{rootDomain}/images/not_a_real_image')
    return r.status_code


if __name__ == "__main__":
    print("test 1")
    print(test1())
    print()
    print('test 2')
    print(test2())
    print()
    print("test3")
    print(test3())
    print()
    print("test4")
    print(test4())
    print()
    print("test 5")
    print(test5())
    print()
    print('test 6')
    print(test6())