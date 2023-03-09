## 说明
宜小说下载程序，因点“立即下载”需要下载APP并付费，因此写了一个程序，只需要粘贴目录地址就可以将整部小说下载

## 声明
软件仅供学习交流使用，禁止商业使用，禁止用来做危害网络安全的事情，因错误使用造成的危害由使用者负责。

### 核心代码

    `    res = requests.get(url).text
    html = etree.HTML(res)
    title = html.xpath('//h1/text()')[0]
    hrefs = html.xpath(
        f'//h2[text()="《{title}》正文"]/following-sibling::div[@class="section-box"]/ul/li/a/@href')
    for h in hrefs:
        i += 1
        section_list.append({"num": i, "u": base_url+h})
        i += 1
        _h = h.rsplit("/", 1)[0] + '/' + h.rsplit("/", 1)[-1][:-5] + "_2.html"
        section_list.append({"num": i, "u": base_url+_h})`

    `html = etree.HTML(res)
    _title = html.xpath('//h1[@class="title"]/text()')
    content = html.xpath('//div[@class="content"]/text()')
    content = [i.replace('\u3000', ' ') for i in content]`
