#字典
def dictReverse(): 
#输入
    d={}
    while True:
        x=(input("你要输入键值对的个数:"))
        if not x.isdigit():
            print("输入错误，请重新输入")
            continue
        else:
            n=int(x)
            break
    n=int(x)

    i=0
    while i<n:
        s=input('请输入第'+str(i+1)+'个值(键和值用空格分开)')
        con = s.split()
        if len(con) != 2:
            print('你输入的数据有误，刚刚输入的',s,'未加入字典！')
            continue
        d[con[0]] = con[1]
        i=i+1
    
    import json
    json_str1=json.dumps(d)
    print("JOSN转化后:"+json_str1)
    kind1=type(json_str1)
    print("您所得的字符串类型为：",kind1)

    nd={}
    for item in d.items():
        if item[1] in nd:
            if(isinstance(nd[item[1]],list)):
                list1=nd[item[1]]
                list1.append(item[0])
            else:
                list2=[]
                list2.append(nd[item[1]])
                list2.append(item[0])
                nd[item[1]]=list2
        else:
            nd[item[1]]=item[0]
    json_str2=json.dumps(nd)
    print("反转后:"+json_str2)
    kind2=type(json_str2)
    print("反转所得的字符串类型为:",kind2)
    print("感谢你的使用。")

# base64编码
def b64Encode():
    import base64
    s=input("请输入要编码的字符串：")
    s1=base64.b64encode(bytes(s, 'utf-8'))
    print("编码后为:",str(s1,'utf-8'))
    print("感谢你的使用。")
    

# base64解码
def b64Decode():
    import base64
    while True:
        s=input("请输入要解码的base64字符串：")
        try:
            s1=base64.b64decode(s.encode('utf-8'))
            print("解码后为:",str(s1,'utf-8')) 
            break 
        except:
            print("你输入的字符串有误")
            continue
    print("感谢你的使用。")

# 二维码生成
def qrGenerator():
    from qrcode import make
    import os
    while True:
        filePath = input('请输入文件路径：')
        if not os.path.exists(filePath):
            print('你输入的路径不正确！')
            continue
        else:
            break

    saveFile = os.path.splitext(filePath)[0] + '.jpg'
    while True:
        if os.path.splitext(filePath)[1]!='.txt':
            print('你选择的文件不是txt文件！')
            qrGenerator()
        else:
            break

    while True:
        try:
            ioText=open(filePath)
            s = ioText.read()
            break
        except:
            print('无法读取文件，请检查文件是否被占用及拥有读取权限，文件编码是否正确等等')
            qrGenerator()
        ioText.close()
    while True:
        try:
            r=make(s)
            break
        except:
            print('二维码制作失败，请检查你的源文件')
            qrGenerator()
            
    while True:
        try:
            if os.path.exists(saveFile):
                os.remove(saveFile)

            r.save(saveFile,'JPEG')
            print('已将二维码保存为',saveFile)
            break
        except:
            print('无法保存二维码，请确认源文件目录下的同名.jpg文件是否被占用')
            qrGenerator()
    print("感谢你的使用。")
    
    


print('这是Phyton小工具箱')
print('功能如下：')
print('1.Base64编码')
print('2.Base64解码')
print('3.字符串生成字典并反转')
print('4.二维码生成')

select = input('请选择你要使用的功能：')

if select=='1':
    b64Encode()
elif select=='2':
    b64Decode()
elif select=='3':
    dictReverse()
elif select=='4':
    qrGenerator()
else:
    print('你选择的选项有误。')