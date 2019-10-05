import requests
import re
import os

url_list=[
    'https://sina.com-h-sina.com/20180906/18215_c0fc8873/' ,
    'https://sina.com-h-sina.com/20180906/18216_80a7de01/' ,
    'https://sina.com-h-sina.com/20180906/18217_365c8b79/' ,
    'https://sina.com-h-sina.com/20180906/18218_f02026af/' ,
    'https://sina.com-h-sina.com/20180906/18219_7aca4012/' ,
    'https://sina.com-h-sina.com/20180906/18220_ed8429ba/' ,
    'https://cdn.youku-letv.net/20181130/11218_5aec4df0/' ,
    'https://cdn.youku-letv.net/20181130/11217_64a3d965/' ,
    'https://sina.com-h-sina.com/20180906/18223_5f07955a/' ,
    'https://sina.com-h-sina.com/20180906/18224_0f7d62f7/' ,
    'https://sina.com-h-sina.com/20180906/18225_70b7a36b/' ,
    'https://sina.com-h-sina.com/20180906/18226_e51fc698/' ,
    'https://sina.com-h-sina.com/20180906/18227_66271ec7/' ,
    'https://sina.com-h-sina.com/20180906/18228_026dee76/' ,
    'https://sina.com-h-sina.com/20180906/18229_371750e8/' ,
    'https://sina.com-h-sina.com/20180906/18230_997b5e5f/' ,
    'https://sina.com-h-sina.com/20180906/18231_88b8a296/' ,
    'https://sina.com-h-sina.com/20180906/18232_f20b2ca2/' ,
    'https://sina.com-h-sina.com/20180906/18233_3352578d/' ,
    'https://sina.com-h-sina.com/20180906/18234_347f6882/' ,
    'https://sina.com-h-sina.com/20180906/18235_44565aa7/' ,
    'https://cdn.youku-letv.net/20181130/11203_138f5930/' ,
    'https://sina.com-h-sina.com/20180906/18237_09096b18/' ,
    'https://sina.com-h-sina.com/20180906/18238_154e2c99/' ,
    'https://sina.com-h-sina.com/20180906/18239_e9fe736e/' ,
    'https://cdn.youku-letv.net/20181130/11199_aaf119a6/' ,
    'https://sina.com-h-sina.com/20180906/18241_e8d0a446/' ,
    'https://sina.com-h-sina.com/20180906/18242_ccfe1975/' ,
    'https://sina.com-h-sina.com/20180906/18243_316cafde/' ,
    'https://sina.com-h-sina.com/20180906/18244_c67bb56b/' ,
    'https://sina.com-h-sina.com/20180906/18245_f7707700/' ,
    'https://sina.com-h-sina.com/20180906/18246_01688d4e/' ,
    'https://sina.com-h-sina.com/20180906/18247_8bfc042c/' ,
    'https://sina.com-h-sina.com/20180906/18248_e85bfdc0/' ,
    'https://sina.com-h-sina.com/20180906/18249_b750a51f/' ,
    'https://cdn.youku-letv.net/20181130/11189_acdfba0e/'
]
## [注意]正阳门下的视频的第一个m3u8是指向另一个m3u8，并不是直接指向ts媒体分片
index='index.m3u8'
savefile_path='E://Downloads//ZhengYangMenXia//'

for i in range(0,len(url_list)):
    # os.mkdir(savefile_path+str(i)+'//')   ## 创建文件夹。如果手动创建了文件夹，那就注释掉这一句
    data=requests.get(url_list[i]+index)

    lines=str.split(data.text, '\n')        ## 字符串处理。从第一层m3u8里面取得真正的m3u8地址
    m3u8=lines[2]
    pattern="index.m3u8"
    m3u8_directory=re.sub(pattern,"", m3u8) ## 取文件夹路径，后面会用到

    data = requests.get(url_list[i] + m3u8)
    '''
    # 保存m3u8文件。注释掉，就不存了。
    file=open(savefile_path+str(i)+'//'+index, 'w')
    file.write(data.text)
    file.close()
    '''
    lines=str.split(data.text,'\n')
    pattern=r".*ts"
    # 保存ts文件(注意，是二进制的)
    video = open(savefile_path + str(i) + '//' + '正阳门下-' + str(i).zfill(3) + '.mp4', 'wb')
    for j in range(0,len(lines)):
        if re.match(pattern,lines[j]):
            print("Downloading %s..." % lines[j])
            data = requests.get(url_list[i]+m3u8_directory+lines[j])
            video.write(data.content)
    video.close()