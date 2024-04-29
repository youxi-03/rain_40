import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

wd = webdriver.Chrome()
wd.get("http://www.weather.com.cn/weather40d/101210101.shtml")    # 打开Chrome浏览器

final = []
'''=========================final1========================================'''
final1 = []
# 要找的div的class是"W_left"
divs = wd.find_elements(By.CSS_SELECTOR, "div.W_left")   #寻找多节点
# 现在divs是一个包含所有class为"my-class"的div元素的列表
for div in divs:
    # print(div.text)  # 打印每个div的文本内容
    # tds = div.find_elements(By.CSS_SELECTOR,"td.history f  ")    #错的 #td.history.f\\20【引号里面的空格不能直接是空格】
    # #注意，在CSS选择器中，类名之间用点（.）分隔，而不是空格。
    # tds = div.find_elements(By.CSS_SELECTOR, "td.history.f\\20")   #错的

    # 在这个div容器内查找所有的tr标签
    tr_elements = div.find_elements(By.TAG_NAME, 'tr')
    # print(tr_elements)
    for tr in tr_elements[1:5]:     #本来写的是[1:],但是后面还有一个没用的tr，所以要[1:6]
        tds = tr.find_elements(By.TAG_NAME,'td')
        for td in tds:
            temp = []
            nongli = td.find_element(By.CSS_SELECTOR, "span.nongli")
            # yangli = td.find_element(By.CSS_SELECTOR, "span.nowday orange")         #如果类名中有空格，就不可以简单这样写。
            yangli = td.find_element(By.CSS_SELECTOR, "span.nowday")         #如果类名中有空格，就不可以简单这样写CSS选择器。
            temperature_highest = td.find_element(By.CSS_SELECTOR, "span.max")
            #replace方法要在字符串上调用，所以先把最低温度变成字符串
            temperature_lowest = td.find_element(By.CSS_SELECTOR, "span.min")
            text = temperature_lowest.text
            temperature_lowest = text.replace('/', '')  #replace方法要确保不是在WebElement对象上；而是字符串上调用rplace方法。
            temperature_lowest = temperature_lowest.replace('℃', '')  #replace方法要确保不是在WebElement对象上；而是字符串上调用rplace方法。
            rain_probability = td.find_element(By.CSS_SELECTOR, "span.tubiao")
            temp.append(yangli.text)
            temp.append(nongli.text)
            temp.append(temperature_highest.text)
            temp.append(temperature_lowest)
            temp.append(rain_probability.text)
            final1.append(temp)
final1 = final1[:23]        #final1到22为止

# final.append(temp)  # 将temp加到final中
# print(final)
'''=========================final2========================================'''
# 因为最后两行表格中的数据，它的html标签不同，所以这里重写最后两行表格的数据。
# 首先先重写倒数第二行数据,后面几个数据
final2 = []
divs = wd.find_elements(By.CSS_SELECTOR, "div.W_left")   #寻找多节点

for div in divs:
    tr_elements = div.find_elements(By.TAG_NAME, 'tr')
    for tr in tr_elements[4:5]:
        tds = tr.find_elements(By.XPATH,'//*[@id="table"]/tbody/tr[5]/td[3]|'
                                        '//*[@id="table"]/tbody/tr[5]/td[4]|//*[@id="table"]/tbody/tr[5]/td[5]|'
                                        '//*[@id="table"]/tbody/tr[5]/td[6]|//*[@id="table"]/tbody/tr[5]/td[7]')                        #xpath去控制台复制，右键复制，然后在这里用｜隔开
        for td in tds:
            temp = []
            nongli = td.find_element(By.CSS_SELECTOR, "span.nongli")
            yangli = td.find_element(By.CSS_SELECTOR, "span.nowday")
            temperature_highest = td.find_element(By.TAG_NAME, 'h6')
            txt = temperature_highest.text.split('/')[0]
            temperature_highest = txt
            temperature_lowest = td.find_element(By.TAG_NAME, 'b')
            text = temperature_lowest.text
            temperature_lowest = text.replace('/', '')  #replace方法要确保不是在WebElement对象上；而是字符串上调用rplace方法。
            temperature_lowest = temperature_lowest.replace('℃', '')  #replace方法要确保不是在WebElement对象上；而是字符串上调用rplace方法。
            rain_probability = td.find_element(By.TAG_NAME, 'h3')
            temp.append(yangli.text)
            temp.append(nongli.text)
            temp.append(temperature_highest)
            temp.append(temperature_lowest)
            temp.append(rain_probability.text)
            final2.append(temp)
            # print(temp)
    final2 = final2[:6]  # final2是从22～27


'''=========================final3========================================'''
final3 = []
divs = wd.find_elements(By.CSS_SELECTOR, "div.W_left")   #寻找多节点
# #因为最后一行表格中的数据，它的html标签不同，所以这里重写最后一行表格的数据。
for div in divs:
    # 在这个div容器内查找所有的tr标签
    tr_elements = div.find_elements(By.TAG_NAME, 'tr')
    for tr in tr_elements[6:7]:
        tds = tr.find_elements(By.XPATH, '//*[@id="table"]/tbody/tr[6]/td[1]|//*[@id="table"]/tbody/tr[6]/td[2]|'
                                         '//*[@id="table"]/tbody/tr[6]/td[3]|//*[@id="table"]/tbody/tr[6]/td[4]|'
                                         '//*[@id="table"]/tbody/tr[6]/td[5]|//*[@id="table"]/tbody/tr[6]/td[6]|//*[@id="table"]/tbody/tr[6]/td[7]')
        #储存降雨量的xpath
        rain_index = ['//*[@id="table"]/tbody/tr[6]/td[1]/div[3]/dl/dd/p[4]/i','//*[@id="table"]/tbody/tr[6]/td[2]/div[3]/dl/dd/p[4]/i',
                      '//*[@id="table"]/tbody/tr[6]/td[3]/div[3]/dl/dd/p[4]/i','//*[@id="table"]/tbody/tr[6]/td[4]/div[3]/dl/dd/p[4]/i',
                      '//*[@id="table"]/tbody/tr[6]/td[5]/div[3]/dl/dd/p[4]/i','//*[@id="table"]/tbody/tr[6]/td[6]/div[3]/dl/dd/p[4]/i',
                      '//*[@id="table"]/tbody/tr[6]/td[7]/div[3]/dl/dd/p[4]/i']
        #储存叉叉的xpath
        close_index = ['//*[@id="table"]/tbody/tr[6]/td[1]/div[3]/h1','//*[@id="table"]/tbody/tr[6]/td[2]/div[3]/h1',
                       '//*[@id="table"]/tbody/tr[6]/td[3]/div[3]/h1','//*[@id="table"]/tbody/tr[6]/td[4]/div[3]/h1',
                       '//*[@id="table"]/tbody/tr[6]/td[5]/div[3]/h1','//*[@id="table"]/tbody/tr[6]/td[6]/div[3]/h1',
                       '//*[@id="table"]/tbody/tr[6]/td[7]/div[3]/h1']
        i = 0
        for td in tds:
            temp = []
            # 农历 阳历
            nongli = td.find_element(By.CSS_SELECTOR, "span.nongli")
            yangli = td.find_element(By.CSS_SELECTOR, "span.nowday")    #这句话也会把class=“nowday orange”的选上
            temp.append(yangli.text)
            temp.append(nongli.text)
            #最高温
            temper_div= td.find_element(By.CSS_SELECTOR, "div.ks")
            temperature_highest = temper_div.find_element(By.TAG_NAME, 'i')
            txt = temperature_highest.text
            temperature_highest = txt.replace('°', '')
            temp.append(temperature_highest)
            #最低温
            low_span = temper_div.find_element(By.CSS_SELECTOR, "span.w_night")
            temperature_lowest = low_span.find_element(By.TAG_NAME, 'i')
            txt = temperature_lowest.text
            temperature_lowest = txt.replace('℃', '')
            temp.append(temperature_lowest)

            #降水——————点击一下temper_div【"div.ks"】
            temper_div.click()
            rain_i = temper_div.find_element(By.XPATH,rain_index[i])
            rain_probability = rain_i.text
            # print(rain_probability)
            temp.append(rain_probability)
            final3.append(temp)
            close = rain_i.find_element(By.XPATH,close_index[i]).click()
            i+=1

for i in final1:
    print(i)
    final.append(i)
print('final1列表打印完毕！')
for j in final2:
    print(j)
    final.append(j)
print('final2列表打印完毕！')
for z in final3:
    print(z)
    final.append(z)
print('final3列表打印完毕！')


def write_data(data, name):
    file_name = name
    with open(file_name, 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)

write_data(final, '/Users/weixinqiang/Desktop/rain.csv')
time.sleep(30000)
wd.quit()   #关闭浏览器










        # #因为倒数第二行少了一个27，所以在这里给他补上
        # #这些代码是一个序号为27的框，它有点击事件，它的数据获取。——xpath依赖网页源码。所以一觉醒来，27格子变成了非点击事件。不过它的代码可以保留，用于最后一行。
        # index_27 = []
        # #阳历
        # temp_span = tr.find_elements(By.XPATH, '//*[@id="table"]/tbody/tr[5]/td[7]/h2/span[2]')   #找到最高温的span
        # for i in temp_span:
        #     yangli = i.text
        #     print(yangli)
        #     index_27.append(yangli)
        # #农历
        # temp_span = tr.find_elements(By.XPATH, '//*[@id="table"]/tbody/tr[5]/td[7]/h2/span[1]')   #找到最高温的span
        # for i in temp_span:
        #     nongli = i.text
        #     print(nongli)
        #     index_27.append(nongli)
        # # 最高温
        # temp_span = tr.find_elements(By.XPATH, '//*[@id="table"]/tbody/tr[5]/td[7]/div[4]/dl/dt/span[1]')   #找到最高温的span
        # #根据xpath返回的是一个列表，虽然里面只有一个元素，但是还是要用循环去读取。
        # for i in temp_span:
        #     temperature_highest_hou = i.find_element(By.TAG_NAME, 'i')
        #     txt = temperature_highest_hou.text
        #     temperature_highest_hou = txt.replace('°', '')  # replace方法要确保不是在WebElement对象上；而是字符串上调用rplace方法。
        #     print(temperature_highest_hou)
        #     index_27.append(temperature_highest_hou)
        # #最低温
        # temp_span = tr.find_elements(By.XPATH,'//*[@id="table"]/tbody/tr[5]/td[7]/div[4]/dl/dt/span[2]')  # 找到最高温的span
        # for i in temp_span:
        #     temperature_lowest_hou = i.find_element(By.TAG_NAME, 'i')
        #     text = temperature_lowest_hou.text
        #     temperature_lowest_hou = text.replace('℃', '')  # replace方法要确保不是在WebElement对象上；而是字符串上调用rplace方法。
        #     print(temperature_lowest_hou)
        #     index_27.append(temperature_lowest_hou)
        # #下雨概率——————注意这里又click的点击事件,要先点击这个小框
        # temp_span = tr.find_elements(By.XPATH,'//*[@id="table"]/tbody/tr[5]/td[7]') # 找到最高温的span
        # # temp_span = tr.find_elements(By.XPATH,'//*[@id="table"]/tbody/tr[5]/td[7]/div[3]/dl/dd/p[4]/i')  # 找到最高温的span
        # for i in temp_span:
        #     i.click()
        #     a = tr.find_elements(By.XPATH, '//*[@id="table"]/tbody/tr[5]/td[7]/div[3]/dl/dd/p[4]/i')  # 点击之后进入下一个框
        #     for j in a:
        #         rain_probability = j.text
        #         print(rain_probability)
        #         index_27.append(rain_probability)


        # date = td.find_element(By.TAG_NAME, "h2")
        # yangli = date.find_elements(By.XPATH, "//span[contains(@class, 'nowday') and contains(@class, 'orange')]")
        # # 如果类名中有空格，就不可以简单这样写CSS选择器。 (By.CSS_SELECTOR,"td.history f  ")    #错的 #td.history.f\\20【引号里面的空格不能直接是空格】    最好使用xpath加正则表达式来进行选择